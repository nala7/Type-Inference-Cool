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


def run_pipeline(G, text):
   # st.write('=================== TEXT ======================')
   # st.write(text)
   # st.write('================== TOKENS =====================')
   tokens = tokenize_text(text)
   # st.write('=================== PARSE =====================')
   parser = Serializer.load(os.getcwd() + '/parser')

   parse, operations = parser([t.token_type for t in tokens], get_shift_reduce=True)

   # st.write('==================== AST ======================')
   ast = evaluate_reverse_parse(parse, operations, tokens)
   formatter = print_ast.FormatVisitor()
   tree = formatter.visit(ast)
   # print (tree)
   # st.text(tree)
   # st.write('============== COLLECTING TYPES ===============')
   errors = []
   collector = TypeCollector(errors)
   collector.visit(ast)
   context = collector.context
   # st.write('Errors:', errors)
   # st.write('Context:')
   # st.text(str(context))
   # st.write('=============== BUILDING TYPES ================')
   builder = TypeBuilder(context, errors)
   builder.visit(ast)
   # st.write('Errors:', errors)
   # st.write('Context:',)
   # st.text(str(context))
   # st.write(context)
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
   st.text(scope_tree)
   st.write('Errors:', errors)
   st.write('Auto Types\n', auto_types)
   st.write('Infered Types')
   st.text('\n'.join(f'{key}: {infered_types[key].name}' for key in infered_types))
   # st.write('{\n\t' + '\n\t'.join(f'{key}: {infered_types[key]}' for key in infered_types))

data = st.text_area("Enter code", "", 500)
run_analysis = st.button("Run", "")

if (run_analysis):
   run_pipeline(G, data)
   # st.write('Infered Types\n', infered_types)

