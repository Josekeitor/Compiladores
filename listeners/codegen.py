from ast import Expression
from operator import le
from antlr.activityListener import activityListener
from antlr.activityParser import activityParser

class CodeGen(activityListener):
    stack = []
    assignQ = []
    printQ = []

    def enterProgram(self, ctx:activityParser.ProgramContext):
        print('.text')

    def exitNumero(self, ctx:activityParser.NumeroContext):
        self.stack.append(ctx.Number().getText())

    def enterSuma(self, ctx:activityParser.SumaContext):
        pass

    def exitSuma(self, ctx:activityParser.SumaContext):
        right = self.stack.pop()
        left = self.stack.pop()
        print('add ', left, ',', right)

    def exitLetra(self, ctx: activityParser.LetraContext):
        self.stack.append(ctx.Letter().getText())

    def exitAsignacion(self, ctx:activityParser.AsignacionContext):
        value = self.stack.pop()
        variable = self.stack.pop()
        print('sw $t0,', variable)
        print('lw $t0,', value)

    def exitPrint(self, ctx:activityParser.PrintContext):
        print('li $v0 4')
        print('la $a0,', ctx.expression().getText())
        print('syscall')

    def exitComparacion(self, ctx: activityParser.ComparacionContext):
        right = self.stack.pop()
        left = self.stack.pop()
        print('bgt', left, ',', right, ', 1')

    def enterIf(self, ctx: activityParser.IfContext):
        print('IF ', ctx.expression().getText(), 'THEN')

    
        