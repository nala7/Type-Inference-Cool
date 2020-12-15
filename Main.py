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

def run_pipeline(G, text):
   print('=================== TEXT ======================')
   print('================== TOKENS =====================')
   tokens = tokenize_text(text)
   print('=================== PARSE =====================')
   parser = Serializer.load(os.getcwd() + '/parser')

   parse, operations = parser([t.token_type for t in tokens], get_shift_reduce=True)

   print('==================== AST ======================')
   ast = evaluate_reverse_parse(parse, operations, tokens)
   formatter = print_ast.FormatVisitor()
   tree = formatter.visit(ast)
   print(tree)
   print('============== COLLECTING TYPES ===============')
   errors = []
   collector = TypeCollector(errors)
   collector.visit(ast)
   context = collector.context
   print('Errors:', errors)
   print('Context:')
   print(context)
   print('=============== BUILDING TYPES ================')
   builder = TypeBuilder(context, errors)
   builder.visit(ast)
   print('Errors: [')
   for error in errors:
      print('\t', error)
   print(']')
   print('Context:')
   print(context)
   print('=============== CHECKING TYPES ================')
   old_errors = errors.copy()
   checker = TypeChecker(context, old_errors)
   scope, infered_types, auto_types = checker.visit(ast)
   while True:
      old_errors = errors.copy()
      old_len = len(auto_types)
      checker = TypeChecker(context, old_errors, infered_types)
      scope, infered_types, auto_types = checker.visit(ast)
      if len(auto_types) == old_len:
         errors = old_errors
         break

   print('Scope:')
   scope_tree = Scope_Print().visit(scope)
   print(scope_tree)
   print('Errors: [')
   for error in errors:
       print('\t', error)
   print(']')
   print('Auto Types\n', auto_types)
   print('Infered Types\n', infered_types)
   
run_pipeline(G, ejemplo9)


