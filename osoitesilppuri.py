#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Osma Suominen <osma.suominen@tkk.fi>
# Copyright (c) 2012 Aalto University and University of Helsinki
# MIT License
# see README.txt for more information


from pyparsing import *

finalphas = alphas + u'åäöéÅÄÖÉ'
addralphas = finalphas + "'" # e.g. Tarkk'ampujankatu

kadunnimi = Combine(OneOrMore(Word(addralphas)),
                    joinString=" ",
                    adjacent=False).setResultsName("kadunnimi")
                  
numero = Word(nums).setResultsName("numero")
jakokirjain = Word(alphas, max=1).leaveWhitespace().setResultsName("jakokirjain")

osoitenumero = Group(numero + Optional(jakokirjain)).setResultsName("osoitenumero")
osoitenumerovali = Group(osoitenumero + Suppress("-") + osoitenumero).setResultsName("osoitenumerovali")

kirjain = Word(alphas, max=1).setResultsName("kirjain")
asuntolyhenne = Regex("(as|bst)\.?").setResultsName("asuntolyhenne")
huoneistotunnus = Group((kirjain | asuntolyhenne) + Optional(numero + Optional(jakokirjain))).setResultsName("huoneistotunnus")

lahiosoite = (kadunnimi + \
             Optional((osoitenumerovali | osoitenumero) + \
                      Optional(huoneistotunnus))).setResultsName("lahiosoite")
postinumero = Word(nums, exact=5).setResultsName("postinumero")
postitoimipaikka = Combine(OneOrMore(Word(finalphas)),
                           joinString=" ",
                           adjacent=False).setResultsName("postitoimipaikka")

postiosoite = (lahiosoite + Optional(Suppress(',')) + Optional(postinumero) + postitoimipaikka).setResultsName("postiosoite")
