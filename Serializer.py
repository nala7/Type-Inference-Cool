import os
import dill
import sys
from typing import Any
from Grammar import G
from Parser.Parser_LR1 import LR1Parser


class Serializer:
    @staticmethod
    def save(target: Any, path: str) -> bool:
        try:
            with open(path, "wb") as p:

                dill.dump(target, p)
            return True
        except Exception as e:
            print("Exception")
            print(e)
            return False

    @staticmethod
    def load(path: str) -> Any:
        try:
            with open(path, "rb") as p:
                return dill.load(p)
        except:
            return None


if __name__ == "__main__":
    sys.setrecursionlimit(5000)
    parser = LR1Parser(G)
    Serializer.save(parser, os.getcwd() + "/compiled_parser")
