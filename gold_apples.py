from pyodbc_data import *


total_gold_apples2019 = 0
for row in cursor2:
    if row[13]:
        total_gold_apples2019 += int(row[13])



total_gold_apples2018 = 0
for row in cursor1:
    if row[13]:
        total_gold_apples2018 += int(row[13])



total_gold_apples2017 = 0
for row in cursor:
    if row[13]:
        total_gold_apples2017 += int(row[13])