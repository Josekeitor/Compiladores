# Generated from /Users/jc/Documents/Compiladores/antlr/activity.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .activityParser import activityParser
else:
    from activityParser import activityParser

# This class defines a complete listener for a parse tree produced by activityParser.
class activityListener(ParseTreeListener):

    # Enter a parse tree produced by activityParser#program.
    def enterProgram(self, ctx:activityParser.ProgramContext):
        pass

    # Exit a parse tree produced by activityParser#program.
    def exitProgram(self, ctx:activityParser.ProgramContext):
        pass


    # Enter a parse tree produced by activityParser#suma.
    def enterSuma(self, ctx:activityParser.SumaContext):
        pass

    # Exit a parse tree produced by activityParser#suma.
    def exitSuma(self, ctx:activityParser.SumaContext):
        pass


    # Enter a parse tree produced by activityParser#asignacion.
    def enterAsignacion(self, ctx:activityParser.AsignacionContext):
        pass

    # Exit a parse tree produced by activityParser#asignacion.
    def exitAsignacion(self, ctx:activityParser.AsignacionContext):
        pass


    # Enter a parse tree produced by activityParser#numero.
    def enterNumero(self, ctx:activityParser.NumeroContext):
        pass

    # Exit a parse tree produced by activityParser#numero.
    def exitNumero(self, ctx:activityParser.NumeroContext):
        pass


    # Enter a parse tree produced by activityParser#letra.
    def enterLetra(self, ctx:activityParser.LetraContext):
        pass

    # Exit a parse tree produced by activityParser#letra.
    def exitLetra(self, ctx:activityParser.LetraContext):
        pass


    # Enter a parse tree produced by activityParser#comparacion.
    def enterComparacion(self, ctx:activityParser.ComparacionContext):
        pass

    # Exit a parse tree produced by activityParser#comparacion.
    def exitComparacion(self, ctx:activityParser.ComparacionContext):
        pass


    # Enter a parse tree produced by activityParser#if.
    def enterIf(self, ctx:activityParser.IfContext):
        pass

    # Exit a parse tree produced by activityParser#if.
    def exitIf(self, ctx:activityParser.IfContext):
        pass


    # Enter a parse tree produced by activityParser#print.
    def enterPrint(self, ctx:activityParser.PrintContext):
        pass

    # Exit a parse tree produced by activityParser#print.
    def exitPrint(self, ctx:activityParser.PrintContext):
        pass



del activityParser