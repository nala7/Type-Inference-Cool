from altair.vegalite.v4.schema.core import Parse
from cmp.semantic import Scope
import AST.AST_Print as print_ast
import streamlit as st 
import pickle
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
from Serializer import Serializer

st.sidebar.header("About")
st.sidebar.subheader("Segundo Proyecto de Compilacion: Cool Type Inferer")
st.sidebar.text("Nadia González Fernández")
st.sidebar.text("Jose Alejandro Labourdette-Lartigue Soto")
st.sidebar.text("Grupo: C-312")


""" # Cool Intrepreter """

data = st.text_area("Enter code", "")
run_analysis = st.button("Run", "")

def run_pipeline(G, text):
   st.write('=================== TEXT ======================')
   st.write(text)
   st.write('================== TOKENS =====================')
   tokens = tokenize_text(text)
   st.write('=================== PARSE =====================')
   # parser = Serializer.load(os.getcwd() + '/parser')
   parser = LR1Parser(G)
   parse, operations = parser([t.token_type for t in tokens], get_shift_reduce=True)

   st.write('==================== AST ======================')
   ast = evaluate_reverse_parse(parse, operations, tokens)
   formatter = print_ast.FormatVisitor()
   tree = formatter.visit(ast)
   st.write(tree)
   st.write('============== COLLECTING TYPES ===============')
   errors = []
   collector = TypeCollector(errors)
   collector.visit(ast)
   context = collector.context
   st.write('Errors:', errors)
   st.write('Context:')
   st.write(context)
   st.write('=============== BUILDING TYPES ================')
   builder = TypeBuilder(context, errors)
   builder.visit(ast)
   st.write('Errors: [')
   for error in errors:
      print('\t', error)
   st.write(']')
   st.write('Context:')
   st.write(context)
   st.write('=============== CHECKING TYPES ================')
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

   st.write('Scope:')
   scope_tree = Scope_Print().visit(scope)
   st.write(scope_tree)
   st.write('Errors: [')
   for error in errors:
       st.write('\t', error)
   st.write(']')
   st.write('Auto Types\n', auto_types)
   for key in infered_types:
      st.write('{\n\t' + '\n\t'.join(f'{key}: {infered_types[key]}' for key in infered_types))

   # st.write('Infered Types\n', infered_types)

if (run_analysis):
   run_pipeline(G, data)