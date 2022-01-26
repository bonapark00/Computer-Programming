"""
Name: Jaeyeon Park
Student ID: 2020147519
Lab problem: lab12_p3.py
"""

import random


def generatingKeys():
    """
    Generating Keys
    and return dictionary of 'origin: code'
    """

    # open '.key' file
    file_key = open(filename[:-3] + 'key', 'w')

    # make list of range(32, 48-57, 65-90, 97-122)
    # these values are UTF-8 code of 'space, number, and alphabet'
    list_origin = [32] + list(range(48, 58)) + \
                  list(range(65, 91)) + list(range(97, 123))
    list_code = [32] + list(range(48, 58)) + \
                list(range(65, 91)) + list(range(97, 123))

    # init
    dict_key = {}

    # for each 'origin' value, make corresponding 'code' randomly
    for i in list_origin:
        code = random.choice(list_code)
        while (chr(code) in dict_key.values()) or (i == code):
            code = random.choice(list_code)
        dict_key[chr(i)] = chr(code)

    # write 'origin, code' in '.key' file
    for i in dict_key.keys():
        file_key.write(str(i) + ',' + str(dict_key[i]) + '\n')

    # close file
    file_key.close()

    # return key dictionary (origin:code)
    return dict_key


def encrypting(file_txt):
    """
    by using keys from '.key' file,
    encrypt 'file.txt' file and write them in '.enc' file
    """

    # generate keys
    dict_keys = generatingKeys()

    # make '.enc' file
    file_enc = open(filename[:-3] + 'enc', 'w')

    # write coded message in '.enc' file
    for line in file_txt:
        for chr in line:
            if chr in dict_keys.keys():
                file_enc.write(str(dict_keys[chr]))
            else:
                file_enc.write(str(chr))

    # close files
    file_txt.close()
    file_enc.close()


def decrypting(file_enc):
    """
    by using keys from '.key' file,
    Decrypt '.enc' file and write them into '.txt' file
    """

    # open files
    file_txt = open(filename[:-3] + 'txt', 'w')
    file_keys = open(filename[:-3] + 'key', 'r')

    # init
    dict_keys = {}

    # read '.key' file
    k_eof = False
    while not k_eof:
        line_keys = file_keys.readline()
        if line_keys == '':
            k_eof = True
        else:
            line_keys = line_keys.strip('\n').split(',')
            dict_keys[line_keys[1]] = line_keys[0]

    # do decrypt
    for line in file_enc:
        for chr in line:
            if chr in dict_keys.keys():
                file_txt.write(str(dict_keys[chr]))
            else:
                file_txt.write(str(chr))

    # close files
    file_txt.close()
    file_keys.close()
    file_enc.close()


# main

# get file name
filename = input('Enter a file name: ')

# check file name error
try:
    file = open(filename, 'r')
    if filename[-3:] == 'txt':  # need to encode it
        encrypting(file)
    elif filename[-3:] == 'enc':  # need to decode it
        decrypting(file)

except FileNotFoundError:
    print('Error! File is Not Found!')


