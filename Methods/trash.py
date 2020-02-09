from openpyxl import load_workbook
import locale

path    = 'testPoints.xlsx'
wbk     = load_workbook(path)
sheet   = wbk["Sheet1"]
cells   = sheet['A2': 'H181']

i = -1
l_rssi = []
position = []
for k in range(6):
    l_rssi.append([])

sum = [0, 0, 0, 0, 0, 0]
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
for pos1, pos2, c1, c2, c3, c4, c5, c6 in cells:
    i = i + 1
    sum[0] = sum[0] + locale.atof(c1.value)
    sum[1] = sum[1] + locale.atof(c2.value)
    sum[2] = sum[2] + locale.atof(c3.value)
    sum[3] = sum[3] + locale.atof(c4.value)
    sum[4] = sum[4] + locale.atof(c5.value)
    sum[5] = sum[5] + locale.atof(c6.value)
    if (i+1) % 10 == 0:
        print(int(i/10))
        position.append([])
        position[int(i/10)].append(locale.atof(pos1.value))
        position[int(i/10)].append(locale.atof(pos2.value))
        l_rssi[0].append(sum[0]/10)
        l_rssi[1].append(sum[1]/10)
        l_rssi[2].append(sum[2]/10)
        l_rssi[3].append(sum[3]/10)
        l_rssi[4].append(sum[4]/10)
        l_rssi[5].append(sum[5]/10)
        sum[0] = sum[1] = sum[2] = sum[3] = sum[4] = sum[5] = 0
        
        
print(len(l_rssi[0]))
print(l_rssi[0])
