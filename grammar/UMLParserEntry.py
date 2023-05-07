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

    def __init__(self):  # this method creates the class object.
        pass

    # function used to parse an input file
    def parse(self, argv):
        if len(sys.argv) > 1:
            # read the first argument as a filestream
            input = FileStream(argv[1])
            lexer = UMLLexer(input)  # call your lexer
            stream = CommonTokenStream(lexer)
            parser = UMLParser(stream)
            # start from the parser rule, however should be changed to your entry rule for your specific grammar.
            tree = parser.s()
            printer = UMLListener()
            walker = ParseTreeWalker()
            walker.walk(printer, tree)
        else:
            print('Error : Expected a valid file')
