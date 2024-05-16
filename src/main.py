from tkinter import filedialog
from pathlib import Path
import csv

print("Launching program...")
print("Imports successful.")

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

MONTHS = {
    "TAMMIKUU": 1,
    "HELMIKUU": 2,
    "MAALISKUU": 3,
    "HUHTIKUU": 4,
    "TOUKOKUU": 5,
    "KESÄKUU": 6,
    "HEINÄKUU": 7,
    "ELOKUU": 8,
    "SYYSKUU": 9,
    "LOKAKUU": 10,
    "MARRASKUU": 11,
    "JOULUKUU": 12,
}

EXIT_PROMPT = "Exiting program..."

print("Asking user to select a CSV file..")

chosen_file_path = filedialog.askopenfilename(title = "Select the CSV file", filetypes = (("CSV Files","*.csv"),))

if not chosen_file_path:
    print("No file was selected.")
    print(EXIT_PROMPT)
    exit()

print(f"File '{chosen_file_path}' selected.")
print("Starting to read the CSV file...")

try:
    with open(chosen_file_path, newline='') as csv_file:
        file_reader = csv.reader(csv_file, delimiter=' ', quotechar='|')

        for row in file_reader:
            split_by_comma = row[0].split(',')
            species_rows.append(split_by_comma)
except Exception as e:
    print("Run into an exception while reading the given file:")
    print(e)
    print("Please ensure the file is a valid CSV file and try again.")
    print(EXIT_PROMPT)
    exit()

if (len(species_rows) < 3):
    print("No data was found in the CSV file.")
    print(EXIT_PROMPT)
    exit()

month = "na"

try:
    month = MONTHS[species_rows[0][0]]
except Exception as e:
    print("Run into an exception while recognizing the month:")
    print(e)
    print("Month number will not be specified in file naming.")

del species_rows[0]
del species_rows[0]

print("CSV reading was successful.")
print(f"Recognized a total of {len(species_rows)} species.")
print("Starting to process the data...")

try:
    for row in species_rows:
        species = row[0]

        for i, record in enumerate(row):
            if i > 0 and record == "#N/A":
                table[i].append(species)
except Exception as e:
    print("Run into an exception while processing the data:")
    print(e)
    print("Please ensure the file is a valid CSV file and try again.")
    print(EXIT_PROMPT)
    exit()

print("Data processing finished.")
print("Results are as follows:")

for day in table:
    if (len(table[day]) != 0):
        print(f"{month:02}/{day:02}: {len(table[day]):03} species")

print("Asking user to select an output destination..")

chosen_dir_path = filedialog.askdirectory(title = "Select the output destination")

try:
    Path(f"{chosen_dir_path}/tiirascraper").mkdir(parents=True, exist_ok=True)
    Path(f"{chosen_dir_path}/noformat").mkdir(parents=True, exist_ok=True)
except Exception as e:
    print("Run into an exception while creating the output directories:")
    print(e)
    print(EXIT_PROMPT)
    exit()

print("Starting to write the output files...")

try:
    for day in table:
        if (len(table[day]) != 0):
            with open(f"{chosen_dir_path}/tiirascraper/species_{month:02}_{day:02}.txt", "w+") as output_file:
                for species in table[day]:
                    output_file.write(f"{species}\n")

            with open(f"{chosen_dir_path}/noformat/{month:02}-{day:02}.txt", "w+") as output_file:
                one_string = ", ".join(table[day])
                output_file.write(one_string)
except Exception as e:
    print("Run into an exception while creating the output directories:")
    print(e)
    print(EXIT_PROMPT)
    exit()

print("File writing successful.")
print("Program execution finished.")
exit()