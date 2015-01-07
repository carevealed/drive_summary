#!/usr/bin/python
from sys import argv, stdout, stderr
from os import path

from driveSummary.driveSummary import get_data, report


def main():
    other_files = []
    try:
        input_argument = str(argv[1])
    except IndexError:
        print "Usage: " + path.basename(__file__) + " directory"
        return
    # check if path is valid
    if not path.isdir(input_argument):
        stderr.write(str("\"" + input_argument + "\"is not a valid directory"))
        return
    else:
        print "Checking: " + input_argument,
        stdout.flush()

        other_files, data = get_data(input_argument)

        print "...done"

        print report(data, other_files) # Generate a report


if __name__ == '__main__':
    main()
