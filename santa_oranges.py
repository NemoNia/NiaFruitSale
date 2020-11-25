from pyodbc_data import *


total_santa_oranges2019 = 0
for row in cursor2:
    if row[10]:
        total_santa_oranges2019 += int(row[10])



total_santa_oranges2018 = 0
for row in cursor1:
    if row[10]:
        total_santa_oranges2018 += int(row[10])



total_santa_oranges2017 = 0
for row in cursor:
    if row[10]:
        total_santa_oranges2017 += int(row[10])
