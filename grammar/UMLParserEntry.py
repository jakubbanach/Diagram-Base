from UMLLexer import UMLLexer
from UMLListener import UMLListener
from UMLParser import UMLParser
from antlr4 import *
import sys


class UMLParserEntry(object):
    """
    Debugger class - accepts a single input script and processes
    all subsequent requirements
    """
    
    # function used to parse an input file
    def parse(self, argv):
        if len(sys.argv) > 1:
            input = FileStream(argv[1])
            lexer = UMLLexer(input)
            stream = CommonTokenStream(lexer)
            parser = UMLParser(stream)
            tree = parser.program()
            printer = UMLListener()
            walker = ParseTreeWalker()
            walker.walk(printer, tree)
        else:
            print('Error : Expected a valid file')
