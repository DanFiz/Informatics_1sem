import matplotlib.pyplot as plt
import numpy as np
frequency0 = {}
frequency = {}
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabet_list=[]
for i in alphabet:
    alphabet_list.append(i)
frequency_list = [8.01, 1.59, 4.54, 1.7, 2.98, 8.45, 0.04, 0.94, 1.65, 7.35, 1.21, 3.49, 4.4, 3.21, 6.7, 10.97,2.81, 4.73, 5.47, 6.26, 2.62, 0.26, 0.97, 0.48, 1.44, 0.73, 0.36, 0.04, 1.9, 1.74, 0.32, 0.64,2.01]

frequency_list_array=np.array(frequency_list)
for i in range(len(alphabet_list)):
    frequency0.update({alphabet[i]: frequency_list[i]})
    frequency.update({alphabet[i]: 0})
le=0
with open('input.txt',encoding='UTF-8') as f:
    lines=f.readlines()
    print(lines)
    for i in lines[0]:
        if i in alphabet_list:
            le+=1
            j = i
            frequency[j.lower()] += 1
            print(j.lower())
for i in range(len(alphabet_list)):
    if le !=0:
        frequency[alphabet[i]]/=le
        frequency[alphabet[i]]*=100
frequency_array=np.array(frequency.values())
alphabet_array=np.array(alphabet_list)
plt.figure(figsize=(12,9))
print(len(alphabet_array))
print(len(frequency.values()))
print(len(frequency_list_array))
plt.errorbar(alphabet_array,frequency.values(),color='r',marker='o',label='Закодированный')
plt.errorbar(alphabet_array,frequency_list_array,color='b',marker='s',label='Незакодированный')
plt.legend()
plt.grid()
plt.show()