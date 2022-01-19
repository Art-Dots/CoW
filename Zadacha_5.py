#Составить частотный словарь(частота встречаемости каждого символа) для
#текста из файла lorem.txt

from collections import Counter

with open("lorem.txt") as f:
    c = Counter()
    for x in f:
        c += Counter(x.strip())
print(c)
