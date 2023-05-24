#-*- coding: utf-8 -*-
import unittest
from simpleservice.simplehandlers import HelloWorldHandler, GetStyleVersionList
import tornado.web
import tornado.testing
import json

class TestHandlers(tornado.testing.AsyncHTTPTestCase):

    def get_app(self):
        return tornado.web.Application(handlers=[(r'/$', HelloWorldHandler),
                                                 (r'/order', GetStyleVersionList)
                                                 ], io_loop=self.io_loop)

    """ Pour ce test, il faut modifier l'appel de fetch pour obtenir la reponse attendue """
    def test_hello(self):
        response = self.fetch('/')
        self.assertEqual(response.code, 200)
        self.assertEqual(response.body, 'Hello me')

    """ Pour ce test, il faut modifier l'appel de fetch pour obtenir la reponse attendue """
    def test_get_ordered_list(self):
        styles = ["standard_v1.json",
                  "standard_v2.json",
                  "standard.json",
                  "night_v1.json",
                  "night_v2.json",
                  "new_v1.json", ]
        json_payload = json.dumps(styles)
        headers = {}
        headers['Content-Type'] = 'application/json'
        response = self.fetch('/order', headers=headers, method='POST', body=json_payload)
        self.assertEqual(response.code, 200)
        self.assertEqual(response.body, json.dumps({
          'standard' : ['_v1', '_v2', ''],
            'night' : ['_v1', '_v2'],
            'new' : ['_v1']
        }))

