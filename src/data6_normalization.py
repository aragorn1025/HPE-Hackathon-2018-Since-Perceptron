# -*- coding: utf-8 -*-

from openpyxl import load_workbook
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

def savefig(fig, file_name):
    fig.savefig(temp_dir + file_name + '.png')
    print('Image file saved:', temp_dir + file_name + '.png')


# open file
loadfile = '../data/data6.xlsx'
# wriltefile = './temp/data6_normalization.xlsx'
wb = load_workbook(loadfile)
# get all sheets in the file
sheets = wb.get_sheet_names()
# get the first sheet name
sheet0 = sheets[0]

# create new sheet
if len(sheets) <2:
    wb.create_sheet('Normalization', index=1)
    sheets = wb.get_sheet_names()

sheet1 = sheets[1]

# get sheets
ws = wb.get_sheet_by_name(name = sheet0)
writesheet = wb.get_sheet_by_name(name = sheet1)
# get the row number from the sheet
rows = ws.rows
# get the column number
columns = ws.columns

content = []

# get 故障原因
for col in ws.iter_cols(min_row=2, max_col=4, min_col=4):
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
wb.save(loadfile)