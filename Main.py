from Example_Programs import *
from Tokenizer import *
from Parser.Parser_LR1 import LR1Parser
from Grammar import *
from cmp.evaluation import evaluate_reverse_parse
import AST.AST_Print as print_ast
from SemanticChecker.Type_Collector import TypeCollector
from SemanticChecker.Type_Builder import TypeBuilder
from SemanticChecker.Type_Checker import TypeChecker
from SemanticChecker.Type_Inferer import TypeInferer


tokens, errors = tokenize_text(program0)
pprint_tokens(tokens)

parser = LR1Parser(G)
parse, operations = parser([t.token_type for t in tokens], get_shift_reduce=True)
# print('PARSE')
# print('\n'.join(repr(x) for x in parse))
# print('OPERATIONS')
# print('\n'.join(repr(x) for x in operations))

ast = evaluate_reverse_parse(parse, operations, tokens)
# print(print_ast.FormatVisitor().visit(ast))

errors = []
collector = TypeCollector(errors)
collector.visit(ast)
context = collector.context
print('Errors:')
for error in errors: print(error)
print('Context:')
print(context)

if not errors:
   builder = TypeBuilder(context, errors)
   builder.visit(ast)
   print('Errors:')
   for error in errors: print(error)
   print('Context:')
   print(context)


   if not errors:
      checker = TypeChecker(context, errors)
      scope = checker.visit(ast)
      print('Errors:')
      for error in errors: print(error)

      if not errors:
         auto = []
         checker = TypeInferer(context, errors, auto)
         scope = checker.visit(ast)
         print('Errors:')
         for error in errors: print(error)
         print('Inferers:')
         for error in errors: print(auto)
