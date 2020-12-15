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
    
    def __init__(self, G, verbose=False, build_parsing_table=True):
        self.G = G
        self.verbose = verbose
        self.action = {}
        self.goto = {}
        self.conflict = False
        if build_parsing_table:
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
            #print('1')
            state = stack[-1]
            #print('2')
            lookahead = w[cursor]
            #print('3')
            #print(lookahead)
            if self.verbose: print(stack, '<---||--->', w[cursor:])
                
            #print(lookahead)
            # Your code here!!! (Detect error)
            #print('4')
            
            # action, tag = self.action[state, lookahead]
            # print(action, tag)
            if not (state, lookahead.Name) in self.action:
                # print("Falle pq no supe que accion realizar en el estado", state)
                # for t in self.G.terminals:
                    # if (state, t.Name) in self.action:
                        # print(t.Name, self.action[state, t.Name])
                return None
            #print('5')
                
            action, tag = self.action[state, lookahead.Name]
            #print('6')
            # Your code here!!! (Shift case)
            if action == self.SHIFT:
                # print(lookahead)
                operations.append('SHIFT')
                stack.append(tag)
                cursor += 1
                #print('Shift done')
            # Your code here!!! (Reduce case)
            elif action == self.REDUCE:
                # print(tag)
                operations.append('REDUCE')
                length=len(tag.Right)
                while(length>0):
                    stack.pop()
                    length-=1
                output.append(tag)
                last=stack[-1]
                stack.append(self.goto[last,tag.Left.Name])
                #print('Reduce done')
            # Your code here!!! (OK case)
            elif action==self.OK:
                #print('casi q devuelvo la cadena')
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