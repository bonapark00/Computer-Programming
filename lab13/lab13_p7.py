"""
Name: Jaeyeon Park
Student ID: 2020147519
Lab problem: lab13_p7.py
"""
import os


def searchDir(directory, s):
    """
    Recursively searches 'directory' for .txt files
    that contain string s.
    """
    # init
    lst = []

    # get list of the names of files and folders in directory.
    files = os.listdir(directory)

    for file in files:
        fullname = directory + '/' + file

        # if the file is subfolder of directory, do recursion.
        if os.path.isdir(fullname):
            lst += searchDir(fullname, s)

        else:
            # if the file is single file
            if os.path.isfile(fullname):
                # search only txt files
                if fullname[-3:] == 'txt':
                    try:
                        f = open(fullname, 'r')
                        # init
                        s_in_file = False
                        # read one line as a string
                        line = f.readline()
                        while line != '':
                            # search for the word
                            if s in line:
                                s_in_file = True
                            line = f.readline()
                        # if the word is in file
                        if s_in_file == True:
                            lst += [fullname]
                        f.close()
                    # handle OSError
                    except OSError:
                        print('OSError!')

    return lst




