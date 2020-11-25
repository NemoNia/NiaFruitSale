from pyodbc_data import *


total_small_oranges2019 = 0
for row in cursor2:
    if row[11]:
        total_small_oranges2019 += int(row[11])



total_small_oranges2018 = 0
for row in cursor1:
    if row[11]:
        total_small_oranges2018 += int(row[11])



total_small_oranges2017 = 0
for row in cursor:
    if row[11]:
        total_small_oranges2017 += int(row[11])

