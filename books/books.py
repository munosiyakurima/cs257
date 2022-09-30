import sys
import csv
import booksdatasource

def usage_statement():
    statement = ' Usage:\n'
    statement += ' python3 books.py title [-t | -y] search_string | [-h]\n'
    statement += ' python3 books.py author [-h] | search_string\n'
    statement += ' python3 books.py years [-h] | <start_date|none end_date|none>'
    return statement

def parse_command_line():
    arguments = {}
    if len(sys.argv) < 2:
        print(usage_statement())
        exit()
    if sys.argv[1] == 'title':
        arguments['title'] = sys.argv[1]
        if len(sys.argv) == 2:
            arguments['search_string'] = None
            arguments['[-t | -y]'] = '-t'
        elif len(sys.argv) == 3:
            if sys.argv[2] == '-h':
                print(usage_statement())
                exit()
            else:
                arguments['search_string'] = sys.argv[2]
                arguments['[-t | -y]'] = '-t'
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
    elif sys.argv[1] == 'author':
        arguments['title'] = sys.argv[1]
        if len (sys.argv) == 2:
            arguments['search_string'] = None
        elif len(sys.argv) == 3:
            if sys.argv[2] == '-h':
                print(usage_statement())
                exit()
            else:
                arguments['search_string'] = sys.argv[2]
        else:
            print(usage_statement())
            exit()

    elif sys.argv[1] == 'years':
        if len (sys.argv) < 4:
            print(usage_statement())
            exit()
        elif len(sys.argv) == 4:
            arguments['title'] = sys.argv[1]
            if (sys.argv[2] == 'none') or sys.argv[2].isnumeric():
                arguments['start_date'] = sys.argv[2]
            else:
                print(usage_statement())
                exit()
            if (sys.argv[3] == 'none') or sys.argv[3].isnumeric():
                arguments['end_date'] = sys.argv[3]
            else:
                print(usage_statement())
                exit()  
        else:
            print(usage_statement())
            exit()
    else:
        print(usage_statement())
        exit()

    return arguments

def main(arguments):
    booksource = booksdatasource.BooksDataSource('tinybooks.csv')
    program = arguments['title']
    if program == 'title':
        options = arguments['[-t | -y]']
        search = arguments['search_string']
        if options == '-t':
            title_books = booksource.books(search_text = search)
        else:
            title_books = booksource.books(search_text = search, sort_by = 'year')
        
        for book in title_books:
            print(book.title)

    elif program == 'author':
        search = arguments['search_string']
        author_books = booksource.authors(search)
        for author in author_books:
            print(author.surname + ", " + author.given_name)
    elif program == 'years':
        start_date = arguments['start_date']
        end_date = arguments['end_date']
        year_books = booksource.books_between_years(start_year = start_date, end_year = end_date)
        for book in year_books:
            print(book.title + " " + book.publication_year)
    
    


arguments = parse_command_line()

main(arguments)
    
