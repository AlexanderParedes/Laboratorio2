class Calculadora:
  #Restricción de valores negativos
  #Operación Suma
      def suma(self, val1, val2):
        if (val1 < 0 or val2 < 0):
            raise ArithmeticError("No se aceptan valores negativos")
        return val1 + val2
      
  #Operación Resta
    def resta(self, val1, val2):
        if (val1 < 0 or val2 < 0):
            raise ArithmeticError("No se aceptan valores negativos")
        return val1 - val2
  
  #Operación Multiplicar
    def multiplicar(self, val1, val2):
        if (val1 < 0 or val2 < 0):
            raise ArithmeticError("No se aceptan valores negativos")
        resultado = 0
        for i in range(val2):
            resultado = self.suma(resultado,val1)
        return resultado
