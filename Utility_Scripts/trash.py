from openpyxl import load_workbook
import locale

path    = 'testPoints.xlsx'
wbk     = load_workbook(path)
sheet   = wbk["Sheet1"]
cells   = sheet['A2': 'H31']

i = -1
l_rssi = []
position = []
for k in range(6):
    l_rssi.append([])

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
for pos1, pos2, c1, c2, c3, c4, c5, c6 in cells:
    i = i + 1
    position.append([])
    position[i].append(locale.atof(pos1.value))
    position[i].append(locale.atof(pos2.value))
    l_rssi[0].append(locale.atof(c1.value))
    l_rssi[1].append(locale.atof(c2.value))
    l_rssi[2].append(locale.atof(c3.value))
    l_rssi[3].append(locale.atof(c4.value))
    l_rssi[4].append(locale.atof(c5.value))
    l_rssi[5].append(locale.atof(c6.value))
    

print(len(position))
