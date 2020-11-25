from pyodbc_data import *


total_gala_apples2019 = 0
for row in cursor2:
    if row[15]:
        total_gala_apples2019 += int(row[15])



total_gala_apples2018 = 0
for row in cursor1:
    if row[15]:
        total_gala_apples2018 += int(row[15])



total_gala_apples2017 = 0
for row in cursor:
    if row[15]:
        total_gala_apples2017 += int(row[15])