# -*- coding: utf-8 -*-

from openpyxl import load_workbook
from openpyxl import Workbook
import os
import shutil

temp_dir = './temp/'
if os.path.exists(temp_dir):
    shutil.rmtree(temp_dir)
    os.makedirs(temp_dir)
    print('Clear the directory: {}\n'.format(temp_dir))
else:
    os.makedirs(temp_dir)
    print('Create the directory: {}\n'.format(temp_dir))

# open file
loadfile = '../data/data6.xlsx'
loadbook = load_workbook(loadfile)
# get all sheets in the file
sheets = loadbook.get_sheet_names()
# get the first sheet name
sheet0 = sheets[0]

# create new file
writefile = './temp/data6_normalization.xlsx'
writebook = Workbook()

# get sheets
loadsheet = loadbook.get_sheet_by_name(name = sheet0)
writesheet = writebook.active
# get the row number from the sheet
rows = loadsheet.rows
# get the column number
columns = loadsheet.columns

content = []

# get 故障原因
for col in loadsheet.iter_cols(min_row = 2, max_col = 4, min_col = 4):
    for cell in col:
        content.append(cell.value)
#    print(content)

dic = []
match = False

# get all value in content
for i in content:
    for j in dic:
        if i == j:
            match = True
            break
    if match == False:
        dic.append(i)
    match = False

# normalize
normalize = []
for i in content:
    for j in dic:
        if i == j:
            normalize.append(dic.index(j))

# normalizec = list(zip(normalize))
print(normalize)

# make dictionary
d = {}
count = 0
for i in dic:
    d[count] = i
    count = count + 1
print(d)

# write in sheet
writesheet.append(normalize)
# save file
writebook.save(writefile)