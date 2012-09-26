#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Osma Suominen <osma.suominen@tkk.fi>
# Copyright (c) 2012 Aalto University and University of Helsinki
# MIT License
# see README.txt for more information

from osoitesilppuri import postiosoite, lahiosoite
import fileinput
for line in fileinput.input():
  line = line.decode('UTF-8')
  try:
    print postiosoite.parseString(line, parseAll=True).asXML()
  except:
    print "ei ole postiosoite"
  try:
    print lahiosoite.parseString(line, True).asXML()
  except:
    print "ei ole lähiosoite"
