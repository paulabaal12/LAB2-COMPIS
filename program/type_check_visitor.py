from SimpleLangParser import SimpleLangParser
from SimpleLangVisitor import SimpleLangVisitor
from custom_types import IntType, FloatType, StringType, BoolType


def visitAnd(self, ctx: SimpleLangParser.AndContext):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))
    op = ctx.op.text
    # Solo se permite AND entre booleanos
    if not (isinstance(left_type, BoolType) and isinstance(right_type, BoolType)):
        raise TypeError(f"Unsupported operand types for {op}: {left_type} and {right_type}")
    return BoolType()


def visitCompare(self, ctx: SimpleLangParser.CompareContext):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))
    op = ctx.op.text
    # Solo se permite comparar int y float
    if not (isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType))):
        raise TypeError(f"Unsupported operand types for {op}: {left_type} and {right_type}")
    return BoolType()


class TypeCheckVisitor(SimpleLangVisitor):

  def visitMulDivModPow(self, ctx: SimpleLangParser.MulDivModPowContext):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))
    op = ctx.op.text
    # 1. Tipos incompatibles
    if not (isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType))):
        raise TypeError(f"Unsupported operand types for {op}: {left_type} and {right_type}")
    # 2. División por cero
    if op == '/' and hasattr(ctx.expr(1), 'getText') and ctx.expr(1).getText() == '0':
        raise ZeroDivisionError("Error: División por cero detectada")
    # 3. Módulo con float
    if op == '%' and (isinstance(left_type, FloatType) or isinstance(right_type, FloatType)):
        raise TypeError("Error: El operador % no acepta floats")
    # 4. Potencia con string o bool
    if op == '^' and (isinstance(left_type, StringType) or isinstance(right_type, StringType) or isinstance(left_type, BoolType) or isinstance(right_type, BoolType)):
        raise TypeError("Error: El operador ^ no acepta string ni bool")
    return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()

  def visitAddSub(self, ctx: SimpleLangParser.AddSubContext):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))
    
    if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
        return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()
    else:
        raise TypeError("Unsupported operand types for + or -: {} and {}".format(left_type, right_type))
  
  def visitInt(self, ctx: SimpleLangParser.IntContext):
    return IntType()

  def visitFloat(self, ctx: SimpleLangParser.FloatContext):
    return FloatType()

  def visitString(self, ctx: SimpleLangParser.StringContext):
    return StringType()

  def visitBool(self, ctx: SimpleLangParser.BoolContext):
    return BoolType()

  def visitParens(self, ctx: SimpleLangParser.ParensContext):
    return self.visit(ctx.expr())
