import sys
import csv
import booksdatasource

def usage_statement():
    statement = ' Usage:\n'
    statement += ' python3 books.py title [-t | -y] <search_string>\n'
    statement += ' python3 books.py author <search_string>\n'
    statement += ' python3 books.py years <start_date|none> <end_date|none>\n'
    statement += ' python3 books.py -h'
    exit()

def print_error():
    print("Invalid command line syntax, please check usage statement: python3 books.py -h")
    exit()

def parse_command_line():
    arguments = {}
    if len(sys.argv) < 2:
        print(usage_statement())
    if sys.argv[1] == 'title':
        arguments['method'] = sys.argv[1]
        if len(sys.argv) == 2:
            arguments['search_string'] = None
            arguments['[-t | -y]'] = '-t'
        elif len(sys.argv) == 3:
            if sys.argv[2] == '-t' or sys.argv[2] == '-y':
                arguments['[-t | -y]'] = sys.argv[2]
                arguments['search_string'] = None
            else:
                arguments['search_string'] = sys.argv[2]
                arguments['[-t | -y]'] = '-t'
        elif len(sys.argv) == 4:
            if sys.argv[2] == '-t' or sys.argv[2] == '-y':
                arguments['[-t | -y]'] = sys.argv[2]
                arguments['search_string'] = sys.argv[3]
            else:
                print_error()
        else:
            print_error()
    elif sys.argv[1] == 'author':
        arguments['method'] = sys.argv[1]
        if len (sys.argv) == 2:
            arguments['search_string'] = None
        elif len(sys.argv) == 3:
            arguments['search_string'] = sys.argv[2]
        else:
            print_error()

    elif sys.argv[1] == 'years':
        if len (sys.argv) < 4:
            print_error()
        elif len(sys.argv) == 4:
            arguments['method'] = sys.argv[1]
            if (sys.argv[2] == 'none') or sys.argv[2].isnumeric():
                arguments['start_date'] = sys.argv[2]
            else:
                print_error()
            if (sys.argv[3] == 'none') or sys.argv[3].isnumeric():
                arguments['end_date'] = sys.argv[3]
            else:
                print_error()  
        else:
            print_error()
    elif sys.argv[1] == '-h':
        f = open('usage.txt', 'r')
        content = f.read()
        print(content)
        exit()


    return arguments

def main(arguments):
    booksource = booksdatasource.BooksDataSource('tinybooks.csv')
    method = arguments['method']
    if method == 'title':
        options = arguments['[-t | -y]']
        search = arguments['search_string']
        if options == '-t':
            title_books = booksource.books(search_text = search)
        else:
            title_books = booksource.books(search_text = search, sort_by = 'year')
        
        for book in title_books:
            print(book.title)

    elif method == 'author':
        search = arguments['search_string']
        author_books = booksource.authors(search_text = search)
        for author in author_books:
            print()
            print(author.surname + ", " + author.given_name)
            for book in booksource.books():
                multiple_authors = book.authors.split(' and ')
                for a in multiple_authors:
                    names = a.split()
                    if len(names) == 3:
                        if author.given_name == names[0] and author.surname == names[1]:
                            print (book.title)
                    else: 
                        if author.given_name == names[0] and author.surname == (names[1] + " " + names[2]):
                            print(book.title)
            
    elif method == 'years':
        start_date = arguments['start_date']
        end_date = arguments['end_date']
        year_books = booksource.books_between_years(start_year = start_date, end_year = end_date)
        for book in year_books:
            print(book.title + ", " + book.publication_year)
    
    


arguments = parse_command_line()

main(arguments)
    
