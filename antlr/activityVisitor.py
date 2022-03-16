# Generated from /Users/jc/Documents/Compiladores/antlr/activity.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .activityParser import activityParser
else:
    from activityParser import activityParser

# This class defines a complete generic visitor for a parse tree produced by activityParser.

class activityVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by activityParser#program.
    def visitProgram(self, ctx:activityParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by activityParser#suma.
    def visitSuma(self, ctx:activityParser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by activityParser#asignacion.
    def visitAsignacion(self, ctx:activityParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by activityParser#numero.
    def visitNumero(self, ctx:activityParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by activityParser#letra.
    def visitLetra(self, ctx:activityParser.LetraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by activityParser#comparacion.
    def visitComparacion(self, ctx:activityParser.ComparacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by activityParser#if.
    def visitIf(self, ctx:activityParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by activityParser#print.
    def visitPrint(self, ctx:activityParser.PrintContext):
        return self.visitChildren(ctx)



del activityParser