#-*- coding: utf-8 -*-
import pytest
from simpleservice.classic_functions import reverse_list, generated_value, group_by_owners, is_palyndrome, get_style_and_version



class TestClassicFunctions:

    def test_reverse(self):
        """ Implémenter la fonction reverse_list() pour obtenir le resultat attendu """
        input=range(0,10)
        assert reverse_list(input) == [9,8,7,6,5,4,3,2,1,0]

    def test_group_by_owners(self):
        """ Implementer la fonction group_by_owners() pour obtenir le resultat attendu """
        files = {
            'First.txt' : 'Thierry',
            'Second.txt' : 'Mounir',
            'Third.txt' : 'Thierry'
        }
        assert group_by_owners(files) == {'Thierry': ['First.txt', 'Third.txt'], 'Mounir': ['Second.txt']}

    def test_palyndrome(self):
        """ Implementer la fonction is_palyndrome() pour obtenir le resultat attendu """
        assert is_palyndrome("Hannah")
        assert is_palyndrome("radar")
        assert not is_palyndrome("tototutu")

    def test_get_style_version(self):
        """ Implementer la fonction get_style_version() pour obtenir le resultat attendu """
        assert get_style_and_version("standard.json") == ('standard', '')
        assert get_style_and_version("standard_v5.json") == ('standard', '_v5')

    def test_generated_value(self):
        """ Implementer le generateur generated_value() pour obtenir le resultat attendu """
        input = [9,8,7,6,5,4,3,2,1,0]
        result = [r for r in generated_value()]
        assert result == input


