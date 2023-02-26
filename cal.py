import os


result = {}


for file in os.listdir('dataset'):
    print(file)

        
for k in result:
    average = sum(result[k])/len(result[k])
    print(f'{k} {round(average*100, 2)}')
