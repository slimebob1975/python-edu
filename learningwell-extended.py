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
import statistics

# See first that we have the right enviroment 
try:
    from pyscbwrapper import SCB
except:
    print("There are missing modules. Please see source code for details.")
    exit()

# Print a headline for the data presentation
print('{0:>5s}\t{1:<4s}\t{2:<20s}\t{3:<4s}\t{4:<20s}\t{5:<4s}\n{6:>79s}'. \
     format('Valår','Riket','Distr. m högst delt.','Proc',
            'Distr. m lägst delt.','Proc','='*79))

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
    average = 0.0
    numNonNans = 0
    for data in electionData:
        try:
            # Data is returned as a list of dictionaries
            # TODO: extract values without using the zero index,
            # possibly using district code numbers as keys instead
            electionRates.append(float((data['values'])[0]))
            average += electionRates[-1]
            numNonNans += 1
        except:
            electionRates.append(float("nan"))
    average /= numNonNans

    # For the current year, we now have the district names, and the voting
    # rates. Lets find the maximum rate and district name(s) for the year.
    maximum = max(electionRates)
    minimum = min(electionRates)
    maxDistrict = ""
    minDistrict = ""
    for i in range(len(electionDistricts)):
        if electionRates[i] == maximum:
            if maxDistrict == "":
                maxDistrict = electionDistricts[i]
            else:
                maxDistrict += ", " + str(electionDistricts[i])
        if electionRates[i] == minimum:
            if minDistrict == "":
                minDistrict = electionDistricts[i]
            else:
                minDistrict += ", " + str(electionDistricts[i])

    # Print result for current year
    print('{0:>5d}\t{1:<4.1f}%\t{2:<20s}\t{3:<4.1f}%\t{4:<20s}\t{5:<4.1f}%'. \
          format(int(year),average,maxDistrict,float(maximum),minDistrict,
                 float(minimum)))

# End of program
