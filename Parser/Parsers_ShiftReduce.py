from cmp.pycompiler import *
from cmp.automata import *
from PIL import Image
import streamlit as st
import numpy as np
import pandas as pd
from pandas import DataFrame

class ShiftReduceParser:
    SHIFT = 'SHIFT'
    REDUCE = 'REDUCE'
    OK = 'OK'
    
    def __init__(self, G, verbose=False):
        self.G = G
        self.verbose = verbose
        self.action = {}
        self.goto = {}
        self.conflict = False
        self._build_parsing_table()
    
    def _build_parsing_table(self):
        raise NotImplementedError()

    def __call__(self, w, get_shift_reduce = False):
        #print("Entre a parsear la cadena")
        if self.conflict:
            print('La gramatica presenta conflictos.')
            return None
        #print("No tenia conflictos el parser")
        #print("Esta es la cadena a parsear", w)
        #print("la tabla action tiene", self.action)
        #print("la tabla goto tiene", self.goto)
        stack = [ 0 ]
        cursor = 0
        output = []
        operations = []

        while True:
            state = stack[-1]
            lookahead = w[cursor]
            if self.verbose: print(stack, '<---||--->', w[cursor:])
                
            #print(lookahead)
            # Your code here!!! (Detect error)
            if not (state, lookahead) in self.action:
                #print("Falle pq no supe que accion realizar en el estado", state)
                return None
                
            action, tag = self.action[state, lookahead]
            # Your code here!!! (Shift case)
            if action == self.SHIFT:
                operations.append('SHIFT')
                stack.append(tag)
                cursor += 1
            # Your code here!!! (Reduce case)
            elif action == self.REDUCE:
                operations.append('REDUCE')
                length=len(tag.Right)
                while(length>0):
                    stack.pop()
                    length-=1
                output.append(tag)
                last=stack[-1]
                stack.append(self.goto[last,tag.Left])
            # Your code here!!! (OK case)
            elif action==self.OK:
                if get_shift_reduce:
                    return output, operations
                return output
            # Your code here!!! (Invalid case)
            else:
                assert False,'Error'
                break

def encode_value(value):
    try:
        action, tag = value
        if action == ShiftReduceParser.SHIFT:
            return 'S' + str(tag)
        elif action == ShiftReduceParser.REDUCE:
            return repr(tag)
        elif action ==  ShiftReduceParser.OK:
            return action
        else:
            return value
    except TypeError:
        return value

def table_to_dataframe(table):
    d = {}
    for (state, symbol), value in table.items():
        value = encode_value(value)
        try:
            d[state][symbol] = value
        except KeyError:
            d[state] = { symbol: value }

    return DataFrame.from_dict(d, orient='index', dtype=str)