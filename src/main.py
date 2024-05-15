import pathlib
import csv

ABSOLUTE_PATH = pathlib.Path().resolve()

species_rows = []
table = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
    10: [],
    11: [],
    12: [],
    13: [],
    14: [],
    15: [],
    16: [],
    17: [],
    18: [],
    19: [],
    20: [],
    21: [],
    22: [],
    23: [],
    24: [],
    25: [],
    26: [],
    27: [],
    28: [],
    29: [],
    30: [],
    31: [],
}

with open(f'{ABSOLUTE_PATH}/src/input/kopio.csv', newline='') as csvfile:
    file_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')

    for row in file_reader:
        split_by_comma = row[0].split(',')
        species_rows.append(split_by_comma)

del species_rows[0]
del species_rows[0]

for row in species_rows:
    species = row[0]

    for i, record in enumerate(row):
        if i > 0 and record == "#N/A":
            table[i].append(species)

print(table)