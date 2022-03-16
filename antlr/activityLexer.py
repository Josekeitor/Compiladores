# Generated from /Users/jc/Documents/Compiladores/antlr/activity.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write("J\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\7\6\7\65\n\7")
        buf.write("\r\7\16\7\66\3\b\6\b:\n\b\r\b\16\b;\3\t\3\t\3\n\3\n\3")
        buf.write("\13\3\13\3\f\6\fE\n\f\r\f\16\fF\3\f\3\f\2\2\r\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\3\2\5\3\2")
        buf.write("\62;\4\2C\\c|\5\2\13\f\17\17\"\"\2L\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\3\31\3\2\2\2\5\36\3\2\2\2\7%\3\2\2\2\t*")
        buf.write("\3\2\2\2\13\61\3\2\2\2\r\64\3\2\2\2\179\3\2\2\2\21=\3")
        buf.write("\2\2\2\23?\3\2\2\2\25A\3\2\2\2\27D\3\2\2\2\31\32\7k\2")
        buf.write("\2\32\33\7h\2\2\33\34\7\"\2\2\34\35\7*\2\2\35\4\3\2\2")
        buf.write("\2\36\37\7+\2\2\37 \7\"\2\2 !\7v\2\2!\"\7j\2\2\"#\7g\2")
        buf.write("\2#$\7p\2\2$\6\3\2\2\2%&\7g\2\2&\'\7n\2\2\'(\7u\2\2()")
        buf.write("\7g\2\2)\b\3\2\2\2*+\7r\2\2+,\7t\2\2,-\7k\2\2-.\7p\2\2")
        buf.write("./\7v\2\2/\60\7*\2\2\60\n\3\2\2\2\61\62\7+\2\2\62\f\3")
        buf.write("\2\2\2\63\65\t\2\2\2\64\63\3\2\2\2\65\66\3\2\2\2\66\64")
        buf.write("\3\2\2\2\66\67\3\2\2\2\67\16\3\2\2\28:\t\3\2\298\3\2\2")
        buf.write("\2:;\3\2\2\2;9\3\2\2\2;<\3\2\2\2<\20\3\2\2\2=>\7-\2\2")
        buf.write(">\22\3\2\2\2?@\7?\2\2@\24\3\2\2\2AB\7@\2\2B\26\3\2\2\2")
        buf.write("CE\t\4\2\2DC\3\2\2\2EF\3\2\2\2FD\3\2\2\2FG\3\2\2\2GH\3")
        buf.write("\2\2\2HI\b\f\2\2I\30\3\2\2\2\6\2\66;F\3\b\2\2")
        return buf.getvalue()


class activityLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    Number = 6
    Letter = 7
    ADD = 8
    EQUAL = 9
    GREATER_THAN = 10
    WS = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if ('", "') then'", "'else'", "'print('", "')'", "'+'", "'='", 
            "'>'" ]

    symbolicNames = [ "<INVALID>",
            "Number", "Letter", "ADD", "EQUAL", "GREATER_THAN", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "Number", "Letter", 
                  "ADD", "EQUAL", "GREATER_THAN", "WS" ]

    grammarFileName = "activity.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


