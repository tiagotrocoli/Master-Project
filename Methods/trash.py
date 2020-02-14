from openpyxl import load_workbook
from statistics import variance
import locale

path    = 'testPoints.xlsx'
wbk     = load_workbook(path)
sheet   = wbk["Sheet1"]
cells   = sheet['A2': 'H181']

i = -1
position = []


l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
l6 = []
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
for pos1, pos2, c1, c2, c3, c4, c5, c6 in cells:
    i = i + 1
    l1.append(locale.atof(c1.value))
    l2.append(locale.atof(c2.value))
    l3.append(locale.atof(c3.value))
    l4.append(locale.atof(c4.value))
    l5.append(locale.atof(c5.value))
    l6.append(locale.atof(c6.value))
    if (i+1) % 10 == 0:
        position.append([])
        position[int(i/10)].append(locale.atof(pos1.value))
        position[int(i/10)].append(locale.atof(pos2.value))
        print(round(variance(l1),2), round(variance(l2),2), round(variance(l3),2), round(variance(l4),2), round(variance(l5),2), round(variance(l6),2))
        l1.clear()
        l2.clear()
        l3.clear()
        l4.clear()
        l5.clear()
        l6.clear()

print('\n'.join(str(x) for x in position[0]))
print("---------------------------")
print('\n'.join(str(x) for x in position[1]))
print("---------------------------")