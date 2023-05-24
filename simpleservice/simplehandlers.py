#-*- coding: utf-8 -*-

import tornado

class HelloWorldHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument('name','you')
        self.write("Hello {}".format(name))


class GetStyleVersionList(tornado.web.RequestHandler):
    def post(self):
        print(self.request.body) # json string