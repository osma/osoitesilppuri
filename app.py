#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Osma Suominen <osma.suominen@tkk.fi>
# Copyright (c) 2012 Aalto University and University of Helsinki
# MIT License
# see README.txt for more information

import webapp2
from osoitesilppuri import lahiosoite,postiosoite
from pyparsing import ParseException

class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.write('Hello world!')

class ParseAPI(webapp2.RequestHandler):
  def get(self):
    input = self.request.get("addr")
    try:
      xml = postiosoite.parseString(input, parseAll=True).asXML()
    except ParseException:
      try:
        xml = lahiosoite.parseString(input, parseAll=True).asXML()
      except ParseException:
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write("Failed")
        return

    self.response.headers['Content-Type'] = 'application/xml'
    self.response.write(xml)
  
  post = get

app = webapp2.WSGIApplication([
  ('/', MainPage),
  ('/parse', ParseAPI),
], debug=True)
