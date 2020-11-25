from pyodbc_data import *

total_large_grapefruit2019 = 0

for row in cursor2:
    if row[8]:
        total_large_grapefruit2019 += int(row[8])


total_large_grapefruit2017 = 0

for row in cursor:
    if row[8]:
        total_large_grapefruit2017+= int(row[8])


total_large_grapefruit2018 = 0

for row in cursor1:
    if row[8]:
        total_large_grapefruit2018 += int(row[8])

