'''Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года по настоящее время.

Одним из атрибутов преступления является его тип – Primary Type.

Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.

Файл с данными:
Crimes.csv
'''

import csv
import collections

cr=[]
with open ("Crimes.csv") as f:
    reader=csv.DictReader(f)
    for r in reader:
        #print(r)
        if "2015" in r['Date']:
            cr.append(r['Primary Type'])
    print(cr)
    c=collections.Counter(cr)
    print(c)