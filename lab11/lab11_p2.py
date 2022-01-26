def copyFiles(f1, f2, f3):
    """
    copy content of the first and second file to the third file.
    if f1,f2 or f3 cannot be opened, -1 is returned.
    Otherwise, the copy operation is performed and 0 is returned.
    """
    # open files for reading and writing
    try:
        file1 = open(f1, 'r')
        file2 = open(f2, 'r')
        file3 = open(f3, 'w')
        # read lines in first and second file
        # then write lines in third file
        line_file1 = file1.readline()
        while line_file1 != '':
            file3.write(line_file1)
            line_file1 = file1.readline()

        line_file2 = file2.readline()
        while line_file2 != '':
            file3.write(line_file2)
            line_file2 = file2.readline()
        # close files
        file1.close()
        file2.close()
        file3.close()

        returnValue = 0

    except OSError:
        returnValue = -1

    return returnValue













