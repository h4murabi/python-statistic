from csv import reader
from matplotlib import pyplot as plt
from math import pow, sqrt

with open('data.csv', 'rb') as csvFile:
    csvReader = reader(csvFile, delimiter=';', quotechar='|')
  
    averages = []
    total = 0
    summ = 0
    
    for row in csvReader:
        averages.append(( float(row[1]) + float(row[2])) / 2)
        total += float(row[1]) + float(row[2]) / 2
        
    av = total / len(averages)
    
    for a in averages :
        summ += pow((a - av), 2)
    
    print 'Amplitude: ' + format(max(averages) - min(averages))
    print 'Desvio padrão: ' + format(sqrt(summ / len(averages)))
    
    plt.bar(range(1,31), averages)
    plt.title("Grafico de medias")
    plt.ylabel("Nota")
    plt.xlabel("Aluno")
    plt.show()
