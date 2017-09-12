#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 15:28:16 2017

@author: paulo
"""

import csv
import string
import math
from re import sub
from decimal import Decimal


def print_mediana(array):
    array_len = len(array)
    
    if(array_len % 2 == 0): 
        return array[(array_len / 2)]
    else:
        mediana_baixo = array[int (math.floor(array_len / 2))]
        mediana_alto = array[int (math.ceil(array_len / 2))]
        return (mediana_baixo + mediana_alto) / 2

# OPEN 2015 CSV DIARIAS FILE
with open("2015.csv", 'r') as f_diarias_2015:
    reader = csv.reader(f_diarias_2015, delimiter=',')
    dinheiro_publico_2015 = []
    media_2015 = 0.0
    mediana_2015 = 0
    desvio_padrao_2015 = 0
    
    # ITERATE FILE LINES
    for index, linha in enumerate(reader):
        # ELIMINATE VALUES DIFFERENT THAN CURRENCY
        if (linha[4]).startswith("R$"):
            # CONVERT CURRENCY TO DECIMAL NUMBERS
            dinheiro_publico_2015.append(Decimal(sub(r'[^\d.]', '', string.replace(linha[4], '.', ''))))
    
    for quantia in dinheiro_publico_2015:
        # FORMAT CURRENCY ACTUAL VALUE
        quantia = float(quantia)
        print (quantia)
        media_2015 += quantia
    
    # CALCULATE 2015 AVERAGE
    media_2015 = media_2015 / len(dinheiro_publico_2015)
    print "Media de diarias em 2015: " + str('R${:,.2f}'.format(media_2015))
    print "Mediana das diarias em 2015: " + str('R${:,.2f}'.format(print_mediana(dinheiro_publico_2015)))
    

with open("2016.csv", 'r') as f_diarias_2016:
    
    dinheiro_publico_2016 = []
    media_2016 = 0.0
    mediana_2016 = 0
    desvio_padrao_2016 = 0.0
    
    reader = csv.reader(f_diarias_2016, delimiter=',')
    
    for index, linha in enumerate(reader):
        if (linha[4]).startswith("R$"):
           dinheiro_publico_2016.append(Decimal(sub(r'[^\d.]', '', string.replace(linha[4], '.', ''))))
            
    for i in dinheiro_publico_2016:
        i = float(i/100)
        media_2016 += i
    
    media_2016 = media_2016 / len(dinheiro_publico_2016)
    print "Media de diarias: " + str('R${:,.2f}'.format(media_2016))
    
    
    print "Mediana das diarias: " + str('R${:,.2f}'.format(print_mediana(dinheiro_publico_2016)))
        
    for d in dinheiro_publico_2016:
        desvio_padrao_2016 += (pow((float (d)-media_2016), 2))
    desvio_padrao_2016 = (desvio_padrao_2016 / len(dinheiro_publico_2016))
    desvio_padrao_2016 = math.sqrt(desvio_padrao_2016)
    print "Desvio Padrao: " + str(desvio_padrao_2016)