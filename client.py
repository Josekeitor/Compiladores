import imp
from antlr4 import *
from antlr.activityParser import activityParser
from antlr.activityLexer import activityLexer
from listeners.codegen import CodeGen

import sys


def main():
    parser = activityParser(CommonTokenStream(activityLexer(FileStream("input.txt"))))
    tree = parser.program()
    codegen = CodeGen()
    walker = ParseTreeWalker()
    walker.walk(codegen, tree)

if __name__ == '__main__':
    main()