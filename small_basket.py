from pyodbc_data import *


total_small_baskets2019 = 0
for row in cursor2:
    if row[5]:
        total_small_baskets2019 += int(row[5])



total_small_baskets2018 = 0
for row in cursor1:
    if row[5]:
        total_small_baskets2018 += int(row[5])



total_small_baskets2017 = 0
for row in cursor:
    if row[5]:
        total_small_baskets2017 += int(row[5])