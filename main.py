#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("index2.html")

    def post(self):
        num_a = float(self.request.get("a_vnos"))
        num_b = float(self.request.get("b_vnos"))
        oper = self.request.get("operVnos")

        if oper == "+":
            num_c = num_a + num_b
            if float(num_a) == int(num_a):
                num_a = int(num_a)
            if float(num_b) == int(num_b):
                num_b = int(num_b)
            if float(num_c) == int(num_c):
                num_c = int(num_c)

        elif oper == "-":
            num_c = num_a - num_b
            if float(num_a) == int(num_a):
                num_a = int(num_a)
            if float(num_b) == int(num_b):
                num_b = int(num_b)
            if float(num_c) == int(num_c):
                num_c = int(num_c)

        elif oper == "*":
            num_c = num_a * num_b
            if float(num_a) == int(num_a):
                num_a = int(num_a)
            if float(num_b) == int(num_b):
                num_b = int(num_b)
            if float(num_c) == int(num_c):
                num_c = int(num_c)

        elif oper == "/":
            num_c = num_a / num_b
            if float(num_a) == int(num_a):
                num_a = int(num_a)
            if float(num_b) == int(num_b):
                num_b = int(num_b)
            if float(num_c) == int(num_c):
                num_c = int(num_c)


        params = {"a_vnos":num_a, "b_vnos":num_b, "operVnos":oper, "rezultat":num_c, "sporocilo": "Rezultat je ", "je1":"=", "je0":"= 0"}
        return self.render_template("index2.html",params)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)
