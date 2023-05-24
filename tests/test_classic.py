#-*- coding: utf-8 -*-
import unittest
from simpleservice.classic_functions import reverse_list, generated_value, group_by_owners, is_palyndrome, get_style_and_version
import tornado.web


class TestClassicFunctions(unittest.TestCase):

    """ Implémenter la fonction reverse_list() pour obtenir le resultat attendu """
    def test_reverse(self):
        input=range(0,10)
        self.assertEqual(reverse_list(input), [9,8,7,6,5,4,3,2,1,0])

    """ Implementer le generateur generated_value() pour obtenir le resultat attendu """
    def test_generated_value(self):
        input = [9,8,7,6,5,4,3,2,1,0]
        result = [r for r in generated_value()]
        self.assertEqual(result, input)

    """ Implementer la fonction group_by_owners() pour obtenir le resultat attendu """
    def test_group_by_owners(self):
        files = {
            'First.txt' : 'Thierry',
            'Second.txt' : 'Mounir',
            'Third.txt' : 'Thierry'
        }
        self.assertEqual(group_by_owners(files), {'Thierry': ['First.txt', 'Third.txt'], 'Mounir': ['Second.txt']})

    """ Implementer la fonction is_palyndrome() pour obtenir le resultat attendu """
    def test_palyndrome(self):
        self.assertEqual(is_palyndrome("Hannah"), True)
        self.assertEqual(is_palyndrome("radar"), True)
        self.assertEqual(is_palyndrome("tototutu"), False)

    """ Implementer la fonction get_style_version() pour obtenir le resultat attendu """
    def test_get_style_version(self):
        self.assertEqual(get_style_and_version("standard.json"), ('standard', ''))
        self.assertEqual(get_style_and_version("standard_v5.json"), ('standard', '_v5'))

if __name__ == '__main__':
    unittest.main()

