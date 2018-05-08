# -*- coding: utf-8 -*-
from practica1 import *
import unittest


class TestMethods(unittest.TestCase):

    def test_ejercicio3(self):
        "Ejercicio 3: máximo"
        self.assertEqual(maximo(-2, 25), 25)
        self.assertEqual(maximo(9,-4), 9)
        self.assertEqual(maximo(0, 0), 0)

    def test_ejercicio4(self):
        "Ejercicio 4: principio y fin"
        self.assertEqual(principio_fin('ana'), 'anna')
        self.assertEqual(principio_fin('jonathan'), 'joan')
        self.assertEqual(principio_fin('abc'), 'abbc')
        self.assertEqual(principio_fin(''), '')

    def test_ejercicio5(self):
        "Ejercicio 5: comienzo fijo"
        self.assertEqual(comienzo_fijo('ana'), 'an*')
        self.assertEqual(comienzo_fijo('jonathan'), 'jonathan')
        self.assertEqual(comienzo_fijo('ppppp'), 'p****')

    def test_ejercicio6(self):
        "Ejercicio 6: cuenta letras ynúmeros"
        self.assertEqual(cuenta_letras_numeros('¡Hola mundo!'), (9, 0))
        self.assertEqual(cuenta_letras_numeros('1234'), (0,4))

    def test_ejercicio7(self):
        "Ejercicio 7: cuenta strings"
        self.assertEqual(cuenta_strings([]), 0)
        self.assertEqual(cuenta_strings(['ana', 'jonathan', 'gadea']), 1)

    def test_ejercicio8(self):
        "Ejercicio 8: combina listas"
        self.assertEqual(combina_listas(['a', 'b', 'c'],[1, 2, 3]), [('a',1), ('b',2), ('c',3)])

    def test_ejercicio9(self):
        "Ejercicio 9: mezcla y ordena"
        self.assertEqual(mezcla_y_ordena([1, 3], [4, 5, 6]), [1, 3, 4, 5, 6])
        self.assertEqual(mezcla_y_ordena([4, 1, 3], [2, 5,0]), [0,1, 2, 3, 4, 5])

    def test_ejercicio10(self):
        "Ejercicio 10: elimina adyacentes"
        self.assertEqual(elimina_adyacentes([1, 2, 2, 3,3,3,4]), [1, 2, 3,4])
        self.assertEqual(elimina_adyacentes([]), [])

    def test_ejercicio11(self):
        "Ejercicio 11: tupla a lista"
        self.assertEqual(tupla_a_lista((1, 2, 3)), [1, 2, 3])

    def test_ejercicio12(self):
        "Ejercicio 12: diferencia conjuntos"
        self.assertEqual(diferencia_conjuntos(set(["White", "Black", "Red","Blue"]), set(["Red", "Green"])), {'Black', 'White','Blue'})


if __name__ == '__main__':
    unittest.main()



