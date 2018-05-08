# -*- coding: utf-8 -*-

import time
import types

def normalization (loadsheet, min_row, max_col, min_col):
    content = []
    for col in loadsheet.iter_cols(min_row = min_row, max_col = max_col, min_col = min_col):
        for cell in col:
            content.append(cell.value)
            
    dic = []
    match = False
    dic.append(None)

# get all value in content
    for value in content:
        if value != None:
            for item in dic:
                if value == item:
                    match = True
                    break
            if match == False:
                dic.append(value)
        match = False

# normalize
    normalize = []
    for value in content:
        for item in dic:
            if value == item:
                normalize.append(dic.index(item)/len(dic))

# make dictionary
    dictionary = {}
    key = 0
    for value in dic:
        dictionary[key] = value
        key += 1

    return dictionary, normalize

def time_normalization_datetime(loadsheet, min_row, max_col, min_col):
    timecontent = []
    for col in loadsheet.iter_cols(min_row = min_row, max_col = max_col, min_col = min_col):
        for cell in col:
            timecontent.append(cell.value)
            
    print(type(timecontent[0]))
        
    timenormalize = []
    for value in timecontent:
        time_tuple = value.timetuple()
        ts = time.mktime(time_tuple)
        timenormalize.append(ts)

    return timenormalize

def time_normalization_datestr(loadsheet, min_row, max_col, min_col):
    timecontent = []
    for col in loadsheet.iter_cols(min_row = min_row, max_col = max_col, min_col = min_col):
        for cell in col:
            timecontent.append(cell.value)
            
    print(type(timecontent[0]))
        
    timenormalize = []
    for value in timecontent:
        if isinstance (value, str):
            t_obj = time.strptime(value, "%Y.%m.%d %H:%M")
            ts = time.mktime(t_obj)
            timenormalize.append(ts)
        else:
            timenormalize.append(0)

    return timenormalize

def write(writesheet, content, col):
    i = 1
    for item in content:
        writesheet.cell(row = i, column = col).value = item
        i +=1