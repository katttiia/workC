import os
import json
from itertools import count
import operator

transactionlist = []
put = os.getcwd()+"\\transactions"
for i in os.listdir(put):
    soedput = os.path.join(put, i)
    with open(soedput, "r") as file:
        try:
            dat = json.load(file)
            transactionlist.append(dat)
        finally:
            continue
transactionlist = sorted(transactionlist, key=operator.itemgetter('index')) 

transac = []
for r in transactionlist:
    ind = transactionlist.index(r)
    if r['index'] != transactionlist[ind-1]['index']:
        transac.append(r)


for el in transactionlist:
    if el['hash'].endswith("000"):
        print(el)
        print('1. Индекс:', el['index'], 'Автор:', el['transactions'][-1]['to'])


for element in transactionlist:
    if element['index'] == 71:
        print('7. Вознаграждение:', element['transactions'][-1]['value'])


t = 0
for r in transac:
    if r['transactions'][-1]['value'] == transac[40]['transactions'][-1]['value']:#'
        t += 1
print('8. Период сокращения размера вознаграждения:', t)

# ind = transactionlist.index(r)
# r['index'] != transactionlist[ind-1]['index']

# print('suka bluyat')

# print(p['index'])
# for p in transac:
#     print(p['transactions'][-1]['value'])

cur = transac[16]['transactions'][-1]['value']
c = 1
for i in transactionlist:
    if i['transactions'][-1]['value'] > cur:
        continue
    elif i['transactions'][-1]['value'] == cur:
        c+=1
    else: break
print('9. Коэффициент сокращения: ', transactionlist[c+2]['transactions'][-1]['value'] / transactionlist[c-1]['transactions'][-1]['value'])


# for h in transactionlist:
#     print(h)

scrt = []
inf = []
for h in transac:
    if h['secret_info'] != '':
        scrt.append(h['index'])
        inf.append(h['secret_info'])
print('11. Номера блоков с информацией в secret_info:', *scrt)
print('12. Информация в secret_info:', *inf)


