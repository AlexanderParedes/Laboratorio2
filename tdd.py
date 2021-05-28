# Archivo para validar las operaciones realizadas por la calculadora

import unittest
from calculadora import calculadora

class CalculadoraTDD(unitprueba.pruebaCase):
    calculadora = calculadora()

    def prueba_suma_enteros(self):
        self.assertEqual(4, self.calculadora.suma(2,2))

    def prueba_suma_invalido_negativo(self):
        self.assertRaises(ArithmeticError, self.calculadora.suma, -2, 2)

    def prueba_suma_invalido_negativo_2(self):
        self.assertRaises(ArithmeticError, self.calculadora.suma, 2, -2)

    def prueba_suma_enteros_por_cero(self):
        self.assertEqual(2, self.calculadora.suma(2,0))

    def prueba_resta_enteros(self):
        self.assertEqual(0, self.calculadora.resta(2,2))

    def prueba_resta_invalido_negativo(self):
        self.assertRaises(ArithmeticError, self.calculadora.resta, -2, 2)

    def prueba_resta_invalido_negativo_2(self):
        self.assertRaises(ArithmeticError, self.calculadora.resta, 2, -2)

    def prueba_resta_enteros_por_cero(self):
        self.assertEqual(2, self.calculadora.resta(2,0))

    def prueba_mult_enteros(self):
        self.assertEqual(4, self.calculadora.multiplicar(2,2))

    def prueba_mult_enteros_por_cero(self):
        self.assertEqual(0, self.calculadora.multiplicar(2,0))

    def prueba_mult_enteros_por_uno(self):
        self.assertEqual(2, self.calculadora.multiplicar(2,1))

    def prueba_mult_invalido_negativo(self):
        self.assertRaises(ArithmeticError, self.calculadora.multiplicar, -2, 2)

    def prueba_mult_invalido_negativo_2(self):
        self.assertRaises(ArithmeticError, self.calculadora.multiplicar, 2, -2)

    def prueba_div_enteros(self):
        self.assertEqual((1,0), self.calculadora.dividir(2,2))

    def prueba_div_enteros_1(self):
        self.assertEqual((2,0), self.calculadora.dividir(4,2))

    def prueba_div_enteros_2(self):
        self.assertEqual((1,1), self.calculadora.dividir(3,2))

    def prueba_div_enteros_3(self):
        self.assertEqual((0,0), self.calculadora.dividir(0,2))

    def prueba_div_enteros_4(self):
        self.assertEqual((0,20), self.calculadora.dividir(20,70))

    def prueba_div_enteros_por_uno(self):
        self.assertEqual((2,0), self.calculadora.dividir(2,1))

    def prueba_div_enteros_por_cero(self):
        self.assertRaises(ArithmeticError, self.calculadora.dividir, -2, 0)

    def prueba_div_invalido_negativo(self):
        self.assertRaises(ArithmeticError, self.calculadora.dividir, -2, 2)

    def prueba_div_invalido_negativo_2(self):
        self.assertRaises(ArithmeticError, self.calculadora.dividir, 2, -2)

    def prueba_raiz(self):
        self.assertEqual((2,0), self.calculadora.raiz(4))

    def prueba_raiz_2(self):
        self.assertEqual((1, 4142100), self.calculadora.raiz(2))

    def prueba_raiz_3(self):
        self.assertEqual((1, 7320500), self.calculadora.raiz(3))

    def prueba_raiz_negativo(self):
        self.assertRaises(ArithmeticError, self.calculadora.raiz, -2)

if __name__ == "__main__":
    unittest.main()
