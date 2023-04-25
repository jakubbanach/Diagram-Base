# Generated from UML.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,19,5,2,0,7,0,1,0,1,0,1,0,0,0,1,0,0,0,3,0,2,1,0,0,0,2,3,5,1,0,
        0,3,1,1,0,0,0,0
    ]

class UMLParser ( Parser ):

    grammarFileName = "UML.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "DiagramKlas", "Klasa", "Interface", 
                      "Enum", "Abstract", "Nazwa", "Inside", "Pole", "Zasi\u0004g", 
                      "Typ", "Metoda", "Argumenty", "InsideEnum", "PoleEnum", 
                      "Zwi\u0003zek", "ZKrotno\u0007ci\u000A", "Dziedziczenie", 
                      "Krotno\u0006\u0007", "Liczba" ]

    RULE_diagramUML = 0

    ruleNames =  [ "diagramUML" ]

    EOF = Token.EOF
    DiagramKlas=1
    Klasa=2
    Interface=3
    Enum=4
    Abstract=5
    Nazwa=6
    Inside=7
    Pole=8
    Zasięg=9
    Typ=10
    Metoda=11
    Argumenty=12
    InsideEnum=13
    PoleEnum=14
    Związek=15
    ZKrotnością=16
    Dziedziczenie=17
    Krotność=18
    Liczba=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class DiagramUMLContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DiagramKlas(self):
            return self.getToken(UMLParser.DiagramKlas, 0)

        def getRuleIndex(self):
            return UMLParser.RULE_diagramUML

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiagramUML" ):
                listener.enterDiagramUML(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiagramUML" ):
                listener.exitDiagramUML(self)




    def diagramUML(self):

        localctx = UMLParser.DiagramUMLContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_diagramUML)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(UMLParser.DiagramKlas)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





