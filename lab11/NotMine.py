# Smoking/Cancer Correlation Program

import math

def openFiles():
    '''
        Prompts the user for the file names to open, opens the files,
        and returns the file objects for each in a tuple of the form
        (air_pollution_datafile, cancer_datafile).

        Raises an OSError exception if the files are not successfully
        opened after four attempts of entering file names.
    '''

    # init
    air_pollution_datafile_opened = False
    cancer_datafile_opened = False
    num_attempts = 4

    # prompt for file names and attempt to open files
    while ((not air_pollution_datafile_opened) or (not cancer_datafile_opened)) and (num_attempts > 0):
        try:
            if not air_pollution_datafile_opened:
                file_name = input('Enter air pollution data from filename: ')
                air_pollution_datafile = open(file_name, 'r')
                air_pollution_datafile_opened = True

            if not cancer_datafile_opened:
                file_name = input('Enter lung cancer data from filename: ')
                cancer_datafile = open(file_name, 'r')
                cancer_datafile_opened = True

        except OSError:
            print('File not found:', file_name + '.', 'Please reenter\n')
            num_attempts = num_attempts - 1

    # if one or more files not opened, raise OSError exception
    if not air_pollution_datafile_opened or not cancer_datafile_opened:
        raise OSError('Too many attempts of reading input files')

    # return file objects if successfully opened
    else:
        return (air_pollution_datafile, cancer_datafile)


def readFiles(air_pollution_datafile, cancer_datafile):
    '''
        Reads the data from the provided file objects air_pollution_datafile
        and cancer_datafile. Returns a list of the data read from each
        in a tuple of the form (air_pollution_datafile, cancer_datafile).
    '''

    # init
    air_pollution_data = []
    cancer_data = []
    empty_str = ''

    # read past file headers
    air_pollution_datafile.readline()
    cancer_datafile.readline()

    # read data files
    eof = False

    while not eof:

        # read line of data from air_pollution_datafile
        a_line = air_pollution_datafile.readline()

        if a_line == empty_str: # check if at end-of-file
            eof = True
        else: # append line of data
            air_pollution_data.append(a_line.strip().split(','))

    eof_another = False

    while not eof_another:

        # read line of data from cancer_datafile
        c_line = cancer_datafile.readline()

        if c_line == empty_str: # check if at end-of-file
            eof_another = True
        else: # append line of data
            cancer_data.append(c_line.strip().split(','))

    # return list of data from each file
    return (air_pollution_data, cancer_data)


def calculateCorrelation(air_pollution_data, cancer_data):
    '''
        Calculates and returns the correlation value for the data
        provided in lists air_pollution_data and cancer_data
    '''

    # init
    sum_air_pollution_vals = sum_cancer_vals = 0
    sum_air_pollution_sqrd = sum_cancer_sqrd = 0
    sum_products = 0

    # edit air_pollution_data and cancer_data
    air_pollution_data_edit = []
    cancer_data_edit = []
    j = 0
    for i in range(0, len(air_pollution_data)):
        while j < len(cancer_data):
            if air_pollution_data[i][0].lower() != cancer_data[j][0].lower():
                j += 1
            else:
                air_pollution_data_edit.append(air_pollution_data[i])
                cancer_data_edit.append(cancer_data[j])
                break
        j = 0

    # calculate intermediate correlation values
    num_values = len(air_pollution_data_edit)

    for k in range(0, num_values):
        sum_air_pollution_vals = sum_air_pollution_vals + float(air_pollution_data_edit[k][1])
        sum_cancer_vals = sum_cancer_vals + float(cancer_data_edit[k][1])

        sum_air_pollution_sqrd = sum_air_pollution_sqrd + float(air_pollution_data_edit[k][1]) ** 2
        sum_cancer_sqrd = sum_cancer_sqrd + float(cancer_data_edit[k][1]) ** 2

        sum_products = sum_products + float(air_pollution_data_edit[k][1]) * float(cancer_data_edit[k][1])


    # calculate and display correlation value
    numer = (num_values * sum_products) - (sum_air_pollution_vals * sum_cancer_vals)

    denom = math.sqrt(abs(((num_values * sum_air_pollution_sqrd) - (sum_air_pollution_vals ** 2)) * ((num_values * sum_cancer_sqrd) - (sum_cancer_vals ** 2))))

    return numer / denom


# ---- main

# program greeting
print('This program will determine the correlation (-1 to 1) between')
print('data on air pollution and incidences of lung cancer\n')

try:
    # open data files
    air_pollution_datafile, cancer_datafile = openFiles()

    # read data
    air_pollution_data, cancer_data = readFiles(air_pollution_datafile, cancer_datafile)

    # calculate correlation value
    correlation = calculateCorrelation(air_pollution_data, cancer_data)

    # display correlation value
    print('r_value = ', correlation)

except OSError as e:
    print(e)
    print('Program terminated ...')

air_pollution_datafile.close()
cancer_datafile.close()