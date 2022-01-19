import numpy as np
import re


file = open('Hello.cow', 'r')
res = file.read()
r = re.sub(r'\n', r' ', res)
r = r.split(' ')

stack=[]
d = {}
ind = 0
result = np.zeros(1000)


for item in r:
    if item == 'MOO': 
        stack.append(ind)
    if item == 'moo':  
        d[ind]=stack[len(stack)-1]
        d[stack.pop()]=ind
    ind+=1
index = 0
i = 0


while(i!= len(r)):
    if r[i] == 'MoO':  
        result[index] += 1
    if r[i] == 'MOo': 
        result[index] -= 1
    if r[i] == 'moO':
        index += 1 
    if r[i] == 'mOo':
        index -= 1 
    if r[i] == 'OOM': 
        print(chr(int(result[index])))
    if r[i] == 'Moo': 
        if r[index] != 0:
            print(chr(int(result[index])))
    if r[i] == 'OOO': 
        r[index] = 0
    if r[i] == 'moo': 
        i = d[i]-1
    if r[i] == 'MOO':
        if result[index] == 0:
            i = d[i]
    if r[i] == '':
        pass
    else:
        i += 1
        continue
    i += 1
