# Smoking/Cancer Correlation Program
import math

def openFiles():
    '''
        Prompts the user for the file names to open, opens the files,
        and returns the file objects for each in a tuple of the form
        (airPollution_datafile, cancer_datafile).

        Raises an OSError exception if the files are not successfully
        opened after four attempts of entering file names.
    '''

    # init
    airPollution_datafile_opened = False
    cancer_datafile_opened = False
    num_attempts = 4

    # prompt for file names and attempt to open files
    while ((not airPollution_datafile_opened) or \
           (not cancer_datafile_opened)) \
            and (num_attempts > 0):
        try:
            if not airPollution_datafile_opened:
                file_name = input('Enter air pollution data file name: ')
                airPollution_datafile = open(file_name, 'r')
                airPollution_datafile_opened = True

            if not cancer_datafile_opened:
                file_name = input('Enter lung cancer data file name: ')
                cancer_datafile = open(file_name, 'r')
                cancer_datafile_opened = True

        except OSError:
            print('File not found:', file_name + '.', 'Please reenter\n')
            num_attempts = num_attempts - 1

    # if one or more files not opened, raise OSError exception
    if not airPollution_datafile_opened or not cancer_datafile_opened:
        raise OSError('Too many attempts of reading input files')

    # return file objects if successfully opened
    else:
        return (airPollution_datafile, cancer_datafile)


def readFiles(airPollution_datafile, cancer_datafile):
    '''
        Reads the data from the provided file objects smoking_datafile
        and cancer_datafile. Returns a list of the data read from each
        in a tuple of the form (smoking_datafile, cancer_datafile).
    '''

    # init
    airPollution_data = []
    cancer_data = []
    empty_str = ''

    # read past file headers
    airPollution_datafile.readline()
    cancer_datafile.readline()

    # read data files
    a_eof = False
    c_eof = False

    while not a_eof:
        # read line of data from each file
        a_line = airPollution_datafile.readline()
        if a_line == empty_str:
            a_eof = True
        else:
            # append line of data to each list
            airPollution_data.append(a_line.strip().split(','))

    while not c_eof:
        c_line = cancer_datafile.readline()
        if c_line == empty_str:
            c_eof = True
        else:
            cancer_data.append(c_line.strip().split(','))

    # return list of data from each file
    return (airPollution_data, cancer_data)


def calculateCorrelation(airPollution_data, cancer_data):
    '''
        Calculates and returns the correlation value for the data
        provided in lists airPollution_data and cancer_data
    '''

    # finding pairs
    pair = 0
    # init sums
    sum_air_vals = sum_cancer_vals = 0
    sum_air_sqrd = sum_cancer_sqrd = 0
    sum_products = 0

    for i in airPollution_data:
        for j in cancer_data:
            if i[0].lower() == j[0].lower():
                pair += 1
                # calculate
                sum_air_vals = sum_air_vals + float(i[1])
                sum_cancer_vals = sum_cancer_vals + float(j[1])

                sum_air_sqrd = sum_air_sqrd + \
                               float(i[1]) ** 2
                sum_cancer_sqrd = sum_cancer_sqrd + \
                                  float(j[1]) ** 2

                sum_products = sum_products + float(i[1]) * \
                               float(j[1])



    # calculate finally and display correlation value
    numer = (pair * sum_products) - \
            (sum_air_vals * sum_cancer_vals)

    denom = math.sqrt(abs( \
        ((pair * sum_air_sqrd) - (sum_air_vals ** 2)) * \
        ((pair* sum_cancer_sqrd) - (sum_cancer_vals ** 2)) \
        ))

    return numer / denom


# ---- main

# program greeting
print('This program will determine the correlation (-1 to 1) between')
print('data on air pollution and incidences of lung cancer\n')

try:
    # open data files
    airPollution_datafile, cancer_datafile = openFiles()

    # read data
    airPollution_data, cancer_data = readFiles(airPollution_datafile, cancer_datafile)

    # calculate correlation value
    correlation = calculateCorrelation(airPollution_data, cancer_data)

    # display correlation value
    print('r_value = ', correlation)

    airPollution_datafile.close()
    cancer_datafile.close()

except OSError as e:
    print(e)
    print('Program terminated ...')

