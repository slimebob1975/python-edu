#!/usr/bin/python
#
# LearningWell code challenge, September 2019
# Author: Robert U S Granat, robert.u.s.granat@gmail.com
#
# For execution in Windows:
# - Install Python with changes to PATH (python available in command window)
# - Install pip: download get-pip.py from https://bootstrap.pypa.io/get-pip.py
# - In command window:
#       python get-pip.py
#       pip install -q pyscbwrapper
#       pip install -q requests
#
# To run from within IDLE, press F5
# To run from prompt, type: python learningwell.py
#
# Script not tested in Linux
#
import time

# See first that we have the right enviroment 
try:
    from pyscbwrapper import SCB
except:
    print("There are missing modules. Please see source code for details.")
    exit()

# Move on. Create a scb object for communicating data with the database.
scb = SCB('sv', 'ME', 'ME0104', 'ME0104D', 'ME0104T4')

# Our task is to find the highest election rates and corresponding disctricts
# for all election years up until now. First, get the election years.
electionYears = scb.get_variables()['valår']

# Next, loop over those retrieved election years
for year in electionYears:

    # For each year, get the available election districts (those might
    # change from election year to election year???)
    electionDistricts = scb.get_variables()['region']
    electionDistricts.remove('Riket')   # Remove for the whole country

    # Set and make a data query for the retrieved districts
    scb.set_query( region = electionDistricts, 
                   tabellinnehåll = ["Valdeltagande i riksdagsval, procent"], 
                   valår = year)

    # Data retreival sometimes triggers an error
    while True:
        try:
            electionData = (scb.get_data())['data']
            break
        except:
            time.sleep(5)  
        
    # Extract all needed data from query (some numbers are not available)
    electionRates = []
    for data in electionData:
        try:
            # Data is returned as a list of dictionaries
            # TODO: extract values without using the zero index,
            # possibly using district code numbers as keys instead
            electionRates.append(float((data['values'])[0]))
        except:
            electionRates.append(float("nan"))

    # For the current year, we now have the district names, and the voting
    # rates. Lets find the maximum rate and district name(s) for the year.
    maximum = max(electionRates)
    maxDistrict = ""
    for i in range(len(electionDistricts)):
        rate = electionRates[i]
        if electionRates[i] == maximum:
            if maxDistrict == "":
                maxDistrict = electionDistricts[i]
            else:
                maxDistrict += ", " + str(electionDistricts[i])

    # Print result for current year
    print('{0:>5}\t{1:<20s}\t{2:<4.1f}%'.format(int(year),maxDistrict,
                                                float(maximum)))

# End of program
