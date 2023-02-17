cont = ['','','','','','','']
area = [, , , , , ,]
s = 0
k = 0
for i in range (len (cont )):
    if area [i] > 2000:
        print(cont [i], '-' , area [i], 'тис. кв. км')
        s = s + area [i]
        k = k + 1
print(s, 'тис.кв км')
print(k, 'континетів')

s1 = 0
for i in range (len(cont)):
    if cont[i] == 'Asia' or cont [i] == 'EU':
        s1 = s1+area[i]
print('Площа Євразії', s1, '')
s2 = 0
for i in range(len(cont)):
    if cont[i] == '' or cont [i] = '':
        s2 = s2 + area[i]
print('', s2, '')

cont = ['','','','','','','','']
area = [, , , , , , , ]
k1 = 0
for i in range(len(cont)):
        print(cont[i], '-', area[i], '')
        k1 = k1 + 1
print(k1, '')
p = sum(area)
print('',p,'')
