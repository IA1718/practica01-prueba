# -*- coding: utf-8 -*-
from practica1 import *
import unittest


class TestMethods(unittest.TestCase):

    def test_ejercicio3(self):
        "Ejercicio 3: máximo"
        self.assertEqual(maximo(10, 5), 10)
        self.assertEqual(maximo(-4, 9), 9)
        self.assertEqual(maximo(3.8, 2.9), 3.8)

    def test_ejercicio4(self):
        "Ejercicio 4: principio y fin"
        self.assertEqual(principio_fin('primavera'), 'prra')
        self.assertEqual(principio_fin('invierno'), 'inno')
        self.assertEqual(principio_fin('xyz'), 'xyyz')
        self.assertEqual(principio_fin('a'), '')

    def test_ejercicio5(self):
        "Ejercicio 5: comienzo fijo"
        self.assertEqual(comienzo_fijo('babble'), 'ba**le')
        self.assertEqual(comienzo_fijo('aardvark'), 'a*rdv*rk')
        self.assertEqual(comienzo_fijo('google'), 'goo*le')
        self.assertEqual(comienzo_fijo('donut'), 'donut')

    def test_ejercicio6(self):
        "Ejercicio 6: cuenta letras ynúmeros"
        self.assertEqual(cuenta_letras_numeros('hello world! 123'), (10, 3))
        self.assertEqual(cuenta_letras_numeros('123abcde'), (5, 3))

    def test_ejercicio7(self):
        "Ejercicio 7: cuenta strings"
        self.assertEqual(cuenta_strings(['aba', 'bb', 'cdefc']), 2)
        self.assertEqual(cuenta_strings(['oso', 'ojo', 'radar', 'reconocer',
                                  'rotor', 'salas']), 6)

    def test_ejercicio8(self):
        "Ejercicio 8: combina listas"
        self.assertEqual(combina_listas([1, 2, 3], ['a', 'b', 'c']), [(1, 'a'), (2, 'b'), (3, 'c')])
        self.assertEqual(combina_listas([1, 2, 3], ['a', 'b']), 'listas no validas')

    def test_ejercicio9(self):
        "Ejercicio 9: mezcla y ordena"
        self.assertEqual(mezcla_y_ordena([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(mezcla_y_ordena([4, 1, 3], [2, 5]), [1, 2, 3, 4, 5])

    def test_ejercicio10(self):
        "Ejercicio 10: elimina adyacentes"
        self.assertEqual(elimina_adyacentes([1, 2, 2, 3]), [1, 2, 3])
        self.assertEqual(elimina_adyacentes([2, 2, 3, 3, 3]), [2, 3])
        self.assertEqual(elimina_adyacentes([1, 2, 2, 3,3,3,4,2,2]), [1, 2, 3,4,2])
        self.assertEqual(elimina_adyacentes([]), [])

    def test_ejercicio11(self):
        "Ejercicio 11: tupla a lista"
        self.assertEqual(tupla_a_lista((1, 2, 2, 3)), [1, 2, 2, 3])
        self.assertEqual(tupla_a_lista(()), [])

    def test_ejercicio12(self):
        "Ejercicio 12: diferencia conjuntos"
        self.assertEqual(diferencia_conjuntos(set(["White", "Black", "Red"]), set(["Red", "Green"])), {'Black', 'White'})


if __name__ == '__main__':
    unittest.main()



