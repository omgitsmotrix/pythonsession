#!usr/local/bin/python
# -*- coding: utf-8 -*-

dictionary = {}

firstRestaurant = 'pret,walthamstow,$'

(name, location, currency) = firstRestaurant.split(",") 

dictionary[name] = {"location":location, "currency": currency}

print dictionary["pret"]

