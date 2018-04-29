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
#  example us_zipcodes.csv
# 1033,Granby,Massachusetts,MA,Hampshire,42.2557,-72.52

# example shootings.csv
# 2,San Francisco UPS shooting,"San Francisco, CA",6/14/2017,"Jimmy Lam, 38, fatally shot three coworkers and wounded two others inside a UPS facility in San Francisco. Lam killed himself as law enforcement officers responded to the scene.",3,2,5,Yes,Asian,M,,
# 4,Florida awning manufacturer shooting,"Orlando, Florida",6/5/2017,"John Robert Neumann, Jr., 45, a former employee of manufacturer Fiamma Inc. fatally shot five workers at the company, and then killed himself on the scene. He'd been fired from the company in April. The attack took place a week before the one-year anniversary of the Orlando nightclub massacre.",5,0,5,Unclear,,M,,
#13,"Forestville, Maryland Drive-by","42486, ",4/26/2016,"Shooter shot from his car at people standing on the street at 1:30 AM. Police don't believe the woman who died was the target, and do not believe the shooting was random.",1,4,5,Unknown,Unknown,Unknown,38.845113,-76.874972


def cleaning(csvfile, clean_csvfile, zipcodes):
    data = []
    location = []
    # postalcodes = []

    csv_file = open(csvfile, "r")

    for row in csv_file:
        splitted = row.split(',')
        data.append(splitted)
    # print(data)
    # finding all data from Southeast Asian countries
    for row in data:
        split_location = row[2].split(',')
        location.append(split_location)

    print(location)

    #     if row[1] == "Southeastern Asia":
    #         country = row[0]
    #         score = row[3]
    #         southeast_asia.append([country, score])
    # first_row = (data[0][0], data[0][3])

    with open(clean_csvfile, 'w') as outfile:
        writer = csv.writer(outfile)
        x = 0
        # writer.writerow(first_row)
        for x in range(0, len(location)):
            writer.writerow(location[x])
            x += 1

#  function ran on shootings.csv and us_zipcodes.csv
cleaning('shootings.csv', 'clean_csvfile.csv', '/datasets/us_zipcodes.csv')
