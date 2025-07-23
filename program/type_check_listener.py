from SimpleLangListener import SimpleLangListener
from SimpleLangParser import SimpleLangParser
from custom_types import IntType, FloatType, StringType, BoolType

class TypeCheckListener(SimpleLangListener):
  def enterAnd(self, ctx: SimpleLangParser.AndContext):
    pass

  def exitAnd(self, ctx: SimpleLangParser.AndContext):
    left_type = self.types[ctx.expr(0)]
    right_type = self.types[ctx.expr(1)]
    op = ctx.op.text
    # Solo se permite AND entre booleanos
    if not (isinstance(left_type, BoolType) and isinstance(right_type, BoolType)):
      self.errors.append(f"Unsupported operand types for {op}: {left_type} and {right_type}")
    self.types[ctx] = BoolType()

  def __init__(self):
    self.errors = []
    self.types = {}

  def enterCompare(self, ctx: SimpleLangParser.CompareContext):
    pass

  def exitCompare(self, ctx: SimpleLangParser.CompareContext):
    left_type = self.types[ctx.expr(0)]
    right_type = self.types[ctx.expr(1)]
    op = ctx.op.text
    # Solo se permite comparar int y float
    if not (isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType))):
      self.errors.append(f"Unsupported operand types for {op}: {left_type} and {right_type}")
    self.types[ctx] = BoolType()

class TypeCheckListener(SimpleLangListener):

  def __init__(self):
    self.errors = []
    self.types = {}

  def enterMulDivModPow(self, ctx: SimpleLangParser.MulDivModPowContext):
    pass

  def exitMulDivModPow(self, ctx: SimpleLangParser.MulDivModPowContext):
    left_type = self.types[ctx.expr(0)]
    right_type = self.types[ctx.expr(1)]
    op = ctx.op.text
    # 1. Tipos incompatibles
    if not self.is_valid_arithmetic_operation(left_type, right_type):
      self.errors.append(f"Unsupported operand types for {op}: {left_type} and {right_type}")
    # 2. División por cero
    if op == '/' and hasattr(ctx.expr(1), 'getText') and ctx.expr(1).getText() == '0':
      self.errors.append("Error: División por cero detectada")
    # 3. Módulo con float
    if op == '%' and (isinstance(left_type, FloatType) or isinstance(right_type, FloatType)):
      self.errors.append("Error: El operador % no acepta floats")
    # 4. Potencia con string o bool
    if op == '^' and (isinstance(left_type, StringType) or isinstance(right_type, StringType) or isinstance(left_type, BoolType) or isinstance(right_type, BoolType)):
      self.errors.append("Error: El operador ^ no acepta string ni bool")
    self.types[ctx] = FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()

  def enterAddSub(self, ctx: SimpleLangParser.AddSubContext):
    pass

  def exitAddSub(self, ctx: SimpleLangParser.AddSubContext):
    left_type = self.types[ctx.expr(0)]
    right_type = self.types[ctx.expr(1)]
    if not self.is_valid_arithmetic_operation(left_type, right_type):
      self.errors.append(f"Unsupported operand types for + or -: {left_type} and {right_type}")
    self.types[ctx] = FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()

  def enterInt(self, ctx: SimpleLangParser.IntContext):
    self.types[ctx] = IntType()

  def enterFloat(self, ctx: SimpleLangParser.FloatContext):
    self.types[ctx] = FloatType()

  def enterString(self, ctx: SimpleLangParser.StringContext):
    self.types[ctx] = StringType()

  def enterBool(self, ctx: SimpleLangParser.BoolContext):
    self.types[ctx] = BoolType()

  def enterParens(self, ctx: SimpleLangParser.ParensContext):
    pass

  def exitParens(self, ctx: SimpleLangParser.ParensContext):
    self.types[ctx] = self.types[ctx.expr()]

  def is_valid_arithmetic_operation(self, left_type, right_type):
    if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
      return True
    return False
