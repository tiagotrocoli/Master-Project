from openpyxl import load_workbook
import os

def storeData(data,sheetName):
    path    = "dataBase.xlsx"
    wbk     = load_workbook(path)
    page    = wbk[sheetName]
    page.append(data)
    wbk.save(path)

path = 'RSSI/'
start   = [3,14,25,36,47,58]
end     = [13,24,35,46,57,68]
j       = -1
wifis = ["TiagoLocalizacao1", "TiagoLocalizacao2", "TiagoLocalizacao0", "TiagoLocalizacao3", "TiagoLocalizacao4", "LSC_HoneyPot"]

for net in wifis:
    j = j + 1
    for filename in os.listdir(path):
        file  = open(path+filename, "r")
        lines = file.readlines()
        data = []
        data.append(float(lines[2].split(" ")[1]))
        for i in range(start[j],end[j]):
            data.append(float(lines[i]))
        storeData(data,net)
    
