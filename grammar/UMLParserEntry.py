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
            input_ = FileStream(argv[1])
            lexer = UMLLexer(input_)
            stream = CommonTokenStream(lexer)
            parser = UMLParser(stream)
            tree = parser.program()
            printer = UMLListener()
            walker = ParseTreeWalker()
            try:
                walker.walk(printer, tree)
            except Exception as e:
                print('\033[91m' + '\033[1m' + 'Error : ' + str(e))
        else:
            print('\033[91m' + '\033[1m' + 'Error : Expected a valid file')
