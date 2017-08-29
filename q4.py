from csv import reader
from matplotlib import pyplot as plt

with open('data.csv', 'rb') as csvFile:
    csvReader = reader(csvFile, delimiter=';', quotechar='|')
    
    frequency = []
    
    for row in csvReader:
        frequency.append(int(row[3]))
        
    print frequency
    
    plt.bar(range(1,31), frequency)
    plt.title("Grafico de falta dos alunos")
    plt.ylabel("Faltas")
    plt.xlabel("Aluno")
    plt.show
