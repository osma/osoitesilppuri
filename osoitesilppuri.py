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
                  
osoitenumero = Combine(Word(nums) + Optional("-" + Word(nums))).setResultsName("osoitenumero")
osoitejakokirjain = Word(alphas, max=1).leaveWhitespace().setResultsName("osoitejakokirjain")
ht_kirjain = Word(alphas, max=1).setResultsName("kirjain")
ht_asunto = Regex("(as|bst)\.?").setResultsName("asuntolyhenne")
ht_numero = Word(nums).setResultsName("numero")
ht_jakokirjain = Word(alphas, max=1).setResultsName("jakokirjain")
huoneistotunnus = Group((ht_kirjain | ht_asunto) + Optional(ht_numero + Optional(ht_jakokirjain))).setResultsName("huoneistotunnus")

lahiosoite = (kadunnimi + \
             Optional(osoitenumero + \
                      Optional(osoitejakokirjain) + \
                      Optional(huoneistotunnus))).setResultsName("lahiosoite")
postinumero = Word(nums, exact=5).setResultsName("postinumero")
postitoimipaikka = Combine(OneOrMore(Word(finalphas)),
                           joinString=" ",
                           adjacent=False).setResultsName("postitoimipaikka")

postiosoite = (lahiosoite + Optional(Suppress(',')) + postinumero + postitoimipaikka).setResultsName("postiosoite")


