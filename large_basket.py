from pyodbc_data import *


total_large_baskets2019 = 0
for row in cursor2:
    if row[6]:
        total_large_baskets2019 += int(row[6])



total_large_baskets2018 = 0
for row in cursor1:
    if row[6]:
        total_large_baskets2018 += int(row[6])



total_large_baskets2017 = 0
for row in cursor:
    if row[6]:
        total_large_baskets2017 += int(row[6])


