from cmp.semantic import Scope
import AST.AST_Print as print_ast
import streamlit as st 
import pickle
from Serializer import Serializer
import os

from Example_Programs import *
from Tokenizer import *
from Parser.Parser_LR1 import LR1Parser
from Grammar import *
from cmp.evaluation import evaluate_reverse_parse
from SemanticChecker.Scope_Print import Scope_Print
from SemanticChecker.Type_Collector import TypeCollector
from SemanticChecker.Type_Builder import TypeBuilder
from SemanticChecker.Type_Checker import TypeChecker
from SemanticChecker.Type_Inferer import TypeInferer

from altair.vegalite.v4.schema.core import Parse
from cmp.semantic import Scope
import AST.AST_Print as print_ast
import streamlit as st 
import pickle
import os
import gc

from Example_Programs import *
from Tokenizer import *
from Parser.Parser_LR1 import LR1Parser
from Grammar import *
from cmp.evaluation import evaluate_reverse_parse
from SemanticChecker.Scope_Print import Scope_Print
from SemanticChecker.Type_Collector import TypeCollector
from SemanticChecker.Type_Builder import TypeBuilder
from SemanticChecker.Type_Checker import TypeChecker
from SemanticChecker.Type_Inferer import TypeInferer
from Serializer import Serializer
from flask import Flask,render_template,request,redirect


""" # Cool Intrepreter """
#run_analysis = st.button("Run", "")

def run_pipeline(G, text):
   print(text)
   tokens = tokenize_text(text)
   parser = Serializer.load(os.getcwd() + '/parser')

   parse, operations = parser([t.token_type for t in tokens], get_shift_reduce=True)

   ret_text = ''
   ret_text += '==================== AST ====================== \n'
   ast = evaluate_reverse_parse(parse, operations, tokens)
   formatter = print_ast.FormatVisitor()
   tree = formatter.visit(ast)
   ret_text += str(tree) + '\n'
   ret_text += '============== COLLECTING TYPES ==============='  + '\n'
   errors = []
   collector = TypeCollector(errors)
   collector.visit(ast)
   context = collector.context
   ret_text += 'Errors:' + str(errors)  + '\n'
   ret_text += 'Context:'  + '\n'
   ret_text += str(context)  + '\n'
   ret_text += '=============== BUILDING TYPES ================' + '\n'
   builder = TypeBuilder(context, errors)
   builder.visit(ast)
   ret_text += 'Errors:' + str(errors) + '\n'
   ret_text += 'Context:' + '\n'
   ret_text += str(context) + '\n'
   ret_text += '=============== CHECKING TYPES ================'  + '\n'
   old_errors = errors.copy()
   checker = TypeChecker(context, old_errors)
   checker.FirstCall(context)
   scope, infered_types, auto_types = checker.visit(ast)
   print('\n\t'.join(f'{key}: {infered_types[key]}' for key in infered_types))
   while True:
      old_errors = errors.copy()
      old_len = len(auto_types)
      checker = TypeChecker(context, old_errors, infered_types)
      scope, infered_types, auto_types = checker.visit(ast)
      if len(auto_types) == old_len:
         errors = old_errors
         break
   del checker

   ret_text += 'Scope:' + '\n'
   scope_tree = Scope_Print().visit(scope)
   ret_text += str(scope_tree) + '\n'
   ret_text += 'Errors:' + str(errors) + '\n'
   ret_text += 'Auto Types\n' + str(auto_types) + '\n'
   ret_text += 'Infered Types' + '\n'
   ret_text += '\n\t'.join(f'{key}: {infered_types[key]}' for key in infered_types) + '\n'

   return ret_text


