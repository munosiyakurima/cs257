import sys
import csv
import booksdatasource

def usage_statement():
    statement = f' Usage: {sys.argv[0]} title, {sys.argv[1]} [-t | -y | -h], {sys.argv[2]} S\n,\n'
    #python3 books.py author [-h] S
	#python3 books.py years [-h] A B
    return statement

def parse_command_line():
    arguments = {}
    if len(sys.argv) == 4:
        arguments['title'] = sys.argv[1]
        arguments['[-t | -y | -h]'] = sys.argv[2]
        arguments['S'] = sys.argv[3]
    return arguments

def main(arguments):
    title = arguments['title']
    options = arguments['[-t | -y | -h]']
    search = arguments['S']
    print(f'HI, {title} {options} {search}')

arguments = parse_command_line()
if 'title' and '[-t | -y | -h]' and 'S' not in arguments:
    print(usage_statement())
else:
    main(arguments)
    
