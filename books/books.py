from ast import arg
from re import search
import sys
import csv
import booksdatasource

def usage_statement():
    statement = ' Usage:\n'
    statement += ' python3 books.py title [-t | -y] search_string | [-h]\n'
    statement += ' python3 books.py author [-h] | search_string\n'
    statement += ' python3 books.py years [-h] | start_date end_date '
    return statement

def parse_command_line():
    arguments = {}
    if sys.argv[1] == 'title':
        arguments['title'] = sys.argv[1]
        if len (sys.argv) < 3:
            print(usage_statement)
            exit()
        elif len(sys.argv) == 3:
            if sys.argv[2] == '-h':
                print(usage_statement)
                exit()
            else:
                #function for searching string
                arguments['search_string'] = sys.argv[2]
        elif len(sys.argv) == 4:
            if sys.argv[2] == ('-t' or '-y'):
                arguments['[-t | -y]'] = sys.argv[2]
                arguments['search_string'] = sys.argv[3]
            else:
                print(usage_statement())
                exit()   
        else:
            print(usage_statement())
            exit()
    return arguments

def main(arguments):
    program = arguments['title']

    options = arguments['[-t | -y]']
    search = arguments['search_string']
    print(f'HI, {program} {options} {search}')

arguments = parse_command_line()

main(arguments)
    
