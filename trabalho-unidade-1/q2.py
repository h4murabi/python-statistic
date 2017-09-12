#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Objetivo: Mostrar números mínimos e máximos, de pelo menos duas variáveis, e suas amplitudes.
Descrição: O propósito é se chegar ao objetivo utilizando duas fontes de dados diferentes,
a de 2015.
"""
from __future__ import division
import csv
import string
from decimal import Decimal
from re import sub
import datetime
import copy

def takeValue(el):
    return el['value']

def takeDiff(el):
    return el['diffDate']


with open('2016.csv', 'r') as f_diarias_2016:
    csvReader = csv.reader(f_diarias_2016, delimiter=',')

    # Organizing the data
    filteredData = []
    index = 0

    for row in csvReader:
        if (row[4]).startswith('R$') :
            filteredData.append({
                'person': row[0],
                'startDate': datetime.datetime.strptime(row[1], '%d/%m/%Y'),
                'endDate': datetime.datetime.strptime(row[2], '%d/%m/%Y'),
                'diffDate': -1,
                'description': row[3],
                'value': Decimal(sub(r'[^\d.]', '', string.replace(row[4], '.', '')))
            })
            filteredData[index]['diffDate'] = (filteredData[index]['endDate'] - filteredData[index]['startDate']).days
            index = index + 1

    dataByValue = copy.copy(filteredData)
    dataByValue.sort(key=takeValue)

    dataByDiff = copy.copy(filteredData)
    dataByDiff.sort(key=takeDiff)
    
    print 'VARIAVEL: Valor das Diarias'
    print('Valor Minimo: R$' + str(dataByValue[0]['value'] / 100) + ' ( ' + dataByValue[0]['person'] + ' ) ')
    print('Valor Maximo: R$' + str(dataByValue[len(dataByValue) - 1]['value'] / 100) + ' ( ' + dataByValue[len(dataByValue) - 1]['person'] + ' ) ' )
    print 'Amplitude: ', str((dataByValue[len(dataByValue) - 1]['value'] / 100) - (dataByValue[0]['value'] / 100))

    print ''
    
    print 'VARIAVEL: Quantidade de dias das diarias'
    print('Valor Minimo: ' + str(dataByDiff[0]['diffDate']) + ' dias ( ' + dataByDiff[0]['person'] + ' ) ')
    print('Valor Maximo: ' + str(dataByDiff[len(dataByDiff) - 1]['diffDate']) + ' dias ( ' + dataByDiff[len(dataByDiff) - 1]['person'] + ' ) ' )
    print 'Amplitude: ', str((dataByDiff[len(dataByDiff) - 1]['diffDate']) - (dataByDiff[0]['diffDate']))