# Generated from /Users/jc/Documents/Compiladores/antlr/activity.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write("\66\4\2\t\2\4\3\t\3\4\4\t\4\3\2\6\2\n\n\2\r\2\16\2\13")
        buf.write("\3\2\6\2\17\n\2\r\2\16\2\20\5\2\23\n\2\3\3\3\3\3\3\5\3")
        buf.write("\30\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3#\n\3\f")
        buf.write("\3\16\3&\13\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4.\n\4\3\4\3\4")
        buf.write("\3\4\3\4\5\4\64\n\4\3\4\2\3\4\5\2\4\6\2\2\2;\2\22\3\2")
        buf.write("\2\2\4\27\3\2\2\2\6\63\3\2\2\2\b\n\5\4\3\2\t\b\3\2\2\2")
        buf.write("\n\13\3\2\2\2\13\t\3\2\2\2\13\f\3\2\2\2\f\23\3\2\2\2\r")
        buf.write("\17\5\6\4\2\16\r\3\2\2\2\17\20\3\2\2\2\20\16\3\2\2\2\20")
        buf.write("\21\3\2\2\2\21\23\3\2\2\2\22\t\3\2\2\2\22\16\3\2\2\2\23")
        buf.write("\3\3\2\2\2\24\25\b\3\1\2\25\30\7\b\2\2\26\30\7\t\2\2\27")
        buf.write("\24\3\2\2\2\27\26\3\2\2\2\30$\3\2\2\2\31\32\f\7\2\2\32")
        buf.write("\33\7\n\2\2\33#\5\4\3\b\34\35\f\6\2\2\35\36\7\13\2\2\36")
        buf.write("#\5\4\3\7\37 \f\5\2\2 !\7\f\2\2!#\5\4\3\6\"\31\3\2\2\2")
        buf.write("\"\34\3\2\2\2\"\37\3\2\2\2#&\3\2\2\2$\"\3\2\2\2$%\3\2")
        buf.write("\2\2%\5\3\2\2\2&$\3\2\2\2\'(\7\3\2\2()\5\4\3\2)*\7\4\2")
        buf.write("\2*-\5\6\4\2+,\7\5\2\2,.\5\6\4\2-+\3\2\2\2-.\3\2\2\2.")
        buf.write("\64\3\2\2\2/\60\7\6\2\2\60\61\5\4\3\2\61\62\7\7\2\2\62")
        buf.write("\64\3\2\2\2\63\'\3\2\2\2\63/\3\2\2\2\64\7\3\2\2\2\n\13")
        buf.write("\20\22\27\"$-\63")
        return buf.getvalue()


class activityParser ( Parser ):

    grammarFileName = "activity.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if ('", "') then'", "'else'", "'print('", 
                     "')'", "<INVALID>", "<INVALID>", "'+'", "'='", "'>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "Number", "Letter", "ADD", 
                      "EQUAL", "GREATER_THAN", "WS" ]

    RULE_program = 0
    RULE_expression = 1
    RULE_statement = 2

    ruleNames =  [ "program", "expression", "statement" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    Number=6
    Letter=7
    ADD=8
    EQUAL=9
    GREATER_THAN=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(activityParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(activityParser.ExpressionContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(activityParser.StatementContext)
            else:
                return self.getTypedRuleContext(activityParser.StatementContext,i)


        def getRuleIndex(self):
            return activityParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = activityParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.state = 16
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [activityParser.Number, activityParser.Letter]:
                self.enterOuterAlt(localctx, 1)
                self.state = 7 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 6
                    self.expression(0)
                    self.state = 9 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==activityParser.Number or _la==activityParser.Letter):
                        break

                pass
            elif token in [activityParser.T__0, activityParser.T__3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 12 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 11
                    self.statement()
                    self.state = 14 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==activityParser.T__0 or _la==activityParser.T__3):
                        break

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return activityParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SumaContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a activityParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(activityParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(activityParser.ExpressionContext,i)

        def ADD(self):
            return self.getToken(activityParser.ADD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuma" ):
                listener.enterSuma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuma" ):
                listener.exitSuma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuma" ):
                return visitor.visitSuma(self)
            else:
                return visitor.visitChildren(self)


    class AsignacionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a activityParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(activityParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(activityParser.ExpressionContext,i)

        def EQUAL(self):
            return self.getToken(activityParser.EQUAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)


    class NumeroContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a activityParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Number(self):
            return self.getToken(activityParser.Number, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumero" ):
                listener.enterNumero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumero" ):
                listener.exitNumero(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumero" ):
                return visitor.visitNumero(self)
            else:
                return visitor.visitChildren(self)


    class LetraContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a activityParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Letter(self):
            return self.getToken(activityParser.Letter, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLetra" ):
                listener.enterLetra(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLetra" ):
                listener.exitLetra(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLetra" ):
                return visitor.visitLetra(self)
            else:
                return visitor.visitChildren(self)


    class ComparacionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a activityParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(activityParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(activityParser.ExpressionContext,i)

        def GREATER_THAN(self):
            return self.getToken(activityParser.GREATER_THAN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparacion" ):
                listener.enterComparacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparacion" ):
                listener.exitComparacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparacion" ):
                return visitor.visitComparacion(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = activityParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [activityParser.Number]:
                localctx = activityParser.NumeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 19
                self.match(activityParser.Number)
                pass
            elif token in [activityParser.Letter]:
                localctx = activityParser.LetraContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 20
                self.match(activityParser.Letter)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 34
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 32
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = activityParser.SumaContext(self, activityParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 23
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 24
                        localctx.op = self.match(activityParser.ADD)
                        self.state = 25
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = activityParser.AsignacionContext(self, activityParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 26
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 27
                        localctx.op = self.match(activityParser.EQUAL)
                        self.state = 28
                        self.expression(5)
                        pass

                    elif la_ == 3:
                        localctx = activityParser.ComparacionContext(self, activityParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 29
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 30
                        localctx.op = self.match(activityParser.GREATER_THAN)
                        self.state = 31
                        self.expression(4)
                        pass

             
                self.state = 36
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return activityParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrintContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a activityParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(activityParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)


    class IfContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a activityParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(activityParser.ExpressionContext,0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(activityParser.StatementContext)
            else:
                return self.getTypedRuleContext(activityParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = activityParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [activityParser.T__0]:
                localctx = activityParser.IfContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.match(activityParser.T__0)
                self.state = 38
                self.expression(0)
                self.state = 39
                self.match(activityParser.T__1)
                self.state = 40
                self.statement()
                self.state = 43
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 41
                    self.match(activityParser.T__2)
                    self.state = 42
                    self.statement()


                pass
            elif token in [activityParser.T__3]:
                localctx = activityParser.PrintContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.match(activityParser.T__3)
                self.state = 46
                self.expression(0)
                self.state = 47
                self.match(activityParser.T__4)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         




