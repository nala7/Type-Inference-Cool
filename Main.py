from cmp.semantic import Scope
import AST.AST_Print as print_ast
import streamlit as st 
import pickle

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
   # print(text)
   print('================== TOKENS =====================')
   tokens = tokenize_text(text)
   # pprint_tokens(tokens)
   print('=================== PARSE =====================')
   parser = LR1Parser(G)
   # with open('action.p','wb') as fp:
   #    pickle.dump(parser.action, fp, protocol = pickle.HIGHEST_PROTOCOL)
   # with open('goto.p', 'wb') as fp:
   #    pickle.dump(parser.goto, fp, protocol = pickle.HIGHEST_PROTOCOL)
   # parser = LR1Parser(G, False, False)
   # with open('action.p','rb') as fp:
   #    parser.action = pickle.load(fp)
   # with open('goto.p', 'rb') as fp:
   #    parser.goto = pickle.load(fp)
   parse, operations = parser([t.token_type for t in tokens], get_shift_reduce=True)

   # print('\n'.join(repr(x) for x in parse))
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


run_pipeline(G, inference)

# # nti = st.text_area('Ingrese el programa', '')

# tokens, errors = tokenize_text(program01)
# pprint_tokens(tokens)

# parser = LR1Parser(G)
# parse, operations = parser([t.token_type for t in tokens], get_shift_reduce=True)
# # st.text("Parser")   
# #print('PARSE')
# # # print('\n'.join(repr(x) for x in parse))
# # # print('OPERATIONS')
# # # print('\n'.join(repr(x) for x in operations))

# ast = evaluate_reverse_parse(parse, operations, tokens)
# print(print_ast.FormatVisitor().visit(ast))
# # st.text(print_ast.FormatVisitor().visit(ast))

# errors = []
# collector = TypeCollector(errors)
# collector.visit(ast)
# context = collector.context
# # st.text('Type Collector')
# # st.text('Errors')
# # st.text(errors)
# # st.text('Context')
# # st.text(context)
# # print('Errors:')
# # s = ''
# # for error in errors: s+= error
# # print('Context:')
# # print(context)

# if not errors:
#    builder = TypeBuilder(context, errors)
#    builder.visit(ast)
#    # print('Errors:')
#    # for error in errors: print(error)
#    # print('Context:')
#    # print(context)
#    # st.text('Type Builder')
#    # st.text('Errors')
#    # st.text(errors)
#    # st.text('Context')
#    # st.text(context)


#    if not errors:
#       checker = TypeChecker(context, errors)
#       scope = checker.visit(ast)
#       print('Errors:')
#       for error in errors: print(error)
#       # st.text('Type Checker')
#       # st.text('Errors')
#       # st.text(errors)

#       if not errors:
#          var_with_autotype = []
#          attr_infered = {}
#          method_infered = {}

#          while True:
#             initial_len = len(var_with_autotype)
#             checker = TypeInferer(context, errors, var_with_autotype,attr_infered, method_infered)
#             scope = checker.visit(ast)
#             current_len = len(var_with_autotype)

#             if initial_len == current_len:
#                break

#          print('Errors:')
#          for error in errors: print(error)
#          print('not Inferers:')
#          for error in errors: print(error)

#          print('attr')
#          for at in attr_infered: print(at)
#          print('metj=h')
#          # st.text('Type Inferer')
#          # st.text('Metodos inferidos')
#          # s = ''
#          # for at in method_infered: s+= 'metodo '+ at[0] + ' en clase ' + at[1]
#          # st.text(s)

#          # st.text('Atributos inferidos')
#          # s = ''
#          # for at in attr_infered: s+= 'atributo '+ at[0] + ' en clase ' + at[1]
#          # st.text(s)