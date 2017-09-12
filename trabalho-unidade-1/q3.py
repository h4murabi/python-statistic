#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 11:16:15 2017

@author: paulo
"""

import csv
import string
from decimal import Decimal
from re import sub
from matplotlib import pyplot as plotter
from dateutil.parser import parse
from datetime import datetime

with open("2015.csv", "r") as f_diarias_2015:
    
    diarias = []
    diarias_por_mes = [float (0) for x in range(12)]
    
    reader = csv.reader(f_diarias_2015, delimiter=',')
    for index, linha in enumerate(reader):
        if not ((linha[2]).startswith("R$")):
            if (linha[4].startswith("R$")):
                valor_diaria = float (Decimal(sub(r'[^\d.]', '', string.replace(linha[4], '.', ''))))
                diarias.append(valor_diaria)
                if parse(linha[2], dayfirst=True):
                    data = parse(linha[2], dayfirst=True)
                    mes = data.month;
                    diarias_por_mes[mes-1] += valor_diaria;
                    
    plotter.bar([x+1 for x in range(12)], diarias_por_mes)
    plotter.title("Diarias pagas pela UFRN em 2015")
    plotter.ylabel("Valores em Reais")
    plotter.xlabel("Meses")
    plotter.show()
    
with open("2016.csv", "r") as f_diarias_2016:
    
    diarias = []
    diarias_por_mes = [float (0) for x in range(12)]
    
    reader = csv.reader(f_diarias_2016, delimiter=',')
    for index, linha in enumerate(reader):
        if not ((linha[2]).startswith("R$")):
            if (linha[4].startswith("R$")):
                valor_diaria = float (Decimal(sub(r'[^\d.]', '', string.replace(linha[4], '.', ''))) / 100)
                diarias.append(valor_diaria)
                if parse(linha[2], dayfirst=True):
                    data = parse(linha[2], dayfirst=True)
                    mes = data.month;
                    diarias_por_mes[mes-1] += valor_diaria;
                    
    plotter.bar([x+1 for x in range(12)], diarias_por_mes)
    plotter.title("Diarias pagas pela UFRN em 2016")
    plotter.ylabel("Valores em Reais")
    plotter.xlabel("Meses")
    plotter.show()