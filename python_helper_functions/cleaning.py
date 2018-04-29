# cleaning.py
#
# Amerens Jongsma
#
# specific function to clean up and select only necessary data from csv file
# in the end the output only contains data of the Happiness score of
# countries in Southeast Asia

import csv
import json
import sys


# FUNCTION TO CONVERT ALL PLACES IN shootings.csv TO ZIP CODES
# 1033,Granby,Massachusetts,MA,Hampshire,42.2557,-72.52

def cleaning(csvfile, clean_csvfile, zipcodes):
    data = []
    location = []
    postalcodes = []
    csv_file = open(csvfile, "r")

    for row in csv_file:
        splitted = row.split(',')
        data.append(splitted)
    print(data)
    # finding all data from Southeast Asian countries
    for row in data:
        if row[1] == "Southeastern Asia":
            country = row[0]
            score = row[3]
            southeast_asia.append([country, score])
    first_row = (data[0][0], data[0][3])

    with open(clean_csvfile, 'w') as outfile:
        writer = csv.writer(outfile)
        x = 0
        writer.writerow(first_row)
        for x in range(0, len(southeast_asia)):
            writer.writerow(southeast_asia[x])
            x += 1

#  function ran on shootings.csv and us_zipcodes.csv
# cleaning('/datasets/shootings.csv', 'clean_csvfile.csv', '/datasets/us_zipcodes.csv')
