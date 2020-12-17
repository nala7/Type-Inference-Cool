import AST.AST_Print as AST_Print
import os

from cmp.evaluation import evaluate_reverse_parse
from Example_Programs import examples
from Tokenizer import *
from SemanticChecker.Type_Builder import TypeBuilder
from SemanticChecker.Type_Checker import TypeChecker
from SemanticChecker.Type_Collector import TypeCollector
from SemanticChecker.ScopePrint import ScopePrint
from Serializer import Serializer

""" # Cool Interpreter """


def run_pipeline(text):
    tokens = tokenize_text(text)
    parser = Serializer.load(os.getcwd() + "/compiled_parser")

    try:
        parse, operations = parser([t.token_type for t in tokens], get_shift_reduce=True)
    except:
        return "Input could not be parsed. Please check your code"

    ret_text = ""
    ret_text += "==================== AST ====================== \n"
    ast = evaluate_reverse_parse(parse, operations, tokens)
    formatter = AST_Print.FormatVisitor()
    tree = formatter.visit(ast)
    ret_text += str(tree) + "\n"
    errors = []
    collector = TypeCollector(errors)
    collector.visit(ast)
    context = collector.context
    ret_text += "=============== BUILDING TYPES ================" + "\n"
    builder = TypeBuilder(context, errors)
    builder.visit(ast)
    ret_text += "Context:" + "\n"
    ret_text += str(context) + "\n"
    ret_text += "=============== CHECKING TYPES ================" + "\n"
    old_errors = errors.copy()
    inferred_types = {}
    checker = TypeChecker(context, old_errors, inferred_types)
    scope, inferred_types, auto_types = checker.visit(ast)
    while True:
        old_errors = errors.copy()
        old_len = len(auto_types)
        checker = TypeChecker(context, old_errors, inferred_types)
        scope, inferred_types, auto_types = checker.visit(ast)
        if len(auto_types) == old_len:
            errors = old_errors
            break
    del checker

    ret_text += "Scope:" + "\n"
    scope_tree = ScopePrint().visit(scope)
    ret_text += str(scope_tree) + "\n"
    str_errors = "\n\t".join(error for error in errors)
    ret_text += "Errors:\n\t" + str_errors + "\n"
    str_auto_types = "\n\t".join(str(at) for at in auto_types)
    ret_text += "Auto Types:\n\t" + str_auto_types + "\n"
    ret_text += "Inferred Types:" + "\n\t"
    ret_text += (
        "\n\t".join(f"{key}: {inferred_types[key].name}" for key in inferred_types)
        + "\n"
    )

    return ret_text


def run_example_files():
    fail = []
    for example_name, example_text in examples:
        print(example_name)
        try:
            print(run_pipeline(example_text))
        except:
            fail.append(example_name)

    print(f"FAILING EXAMPLES: {fail}")
    print(f"SUCCEDED EXAMPLES: {len(examples) - len(fail)}/{len(examples)}")


if __name__ == "__main__":
    run_example_files()
