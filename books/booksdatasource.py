#!/usr/bin/env python3
'''
    booksdatasource.py
    Jeff Ondich, 21 September 2022

    For use in the "books" assignment at the beginning of Carleton's
    CS 257 Software Design class, Fall 2022.
'''

import csv


class Author:
    def __init__(self, surname='', given_name='', birth_year=None, death_year=None):
        self.surname = surname
        self.given_name = given_name
        self.birth_year = birth_year
        self.death_year = death_year

    def __eq__(self, other):
        ''' For simplicity, we're going to assume that no two authors have the same name. '''
        return self.surname == other.surname and self.given_name == other.given_name
    
    def __lt__(self, other):
        if self.surname < other.surname:
            return True
        if self.surname == other.surname and self.given_name < other.given_name:
            return True
        return False

class Book:
    def __init__(self, title='', publication_year=None, authors=[]):
        ''' Note that the self.authors instance variable is a list of
            references to Author objects. '''
        self.title = title
        self.publication_year = publication_year
        self.authors = authors

    def __eq__(self, other):
        ''' We're going to make the excessively simplifying assumption that
            no two books have the same title, so "same title" is the same
            thing as "same book". '''
        return self.title == other.title


class BooksDataSource:
    
    books_list = []
    authors_list = []

    def __init__(self, books_csv_file_name):
        ''' The books CSV file format looks like this:

                title,publication_yea(r,author_description

            For example:

                All Clear,2010,Connie Willis (1945-)
                "Right Ho, Jeeves",1934,Pelham Grenville Wodehouse (1881-1975)

            This __init__ method parses the specified CSV file and creates
            suitable instance variables for the BooksDataSource object containing
            a collection of Author objects and a collection of Book objects.
        '''
        
        
        with open(books_csv_file_name) as f:
            reader = csv.reader(f)
            for row in reader:
                book = Book(row[0], row[1], row[2])
                books_list.append(book)
                split_authors = row[2].split()
                if len(split_authors) == 3:
                    split_dates = split_authors[2].split('-')
                    author = Author(split_authors[1], split_authors[0], split_dates[0][-4:], split_dates[1][:4])
                    authors_list.append(author)
                elif len(split_authors) == 4:
                    split_dates = split_authors[3].split('-')
                    author = Author(split_authors[1] + " " + split_authors[2], split_authors[0], split_dates[0][-4:], split_dates[1][:4])
                    authors_list.append(author)

    def authors(self, search_text=None):
        ''' Returns a list of all the Author objects in this data source whose names contain
            (case-insensitively) the search text. If search_text is None, then this method
            returns all of the Author objects. In either case, the returned list is sorted
            by surname, breaking ties using given name (e.g. Ann Brontë comes before Charlotte Brontë).
        '''
        print('hello')
        authors_returned = []
        if search_text == None:
            authors_returned = authors_list
        else:
            for author in authors_list:
                if search_text.lower() in (author.given_name.lower() or author.surname.lower()):
                    authors_returned.append(author)

        return sorted(authors_returned)
        

    def books(self, search_text=None, sort_by='title'):
        ''' Returns a list of all the Book objects in this data source whose
            titles contain (case-insensitively) search_text. If search_text is None,
            then this method returns all of the books objects.

            The list of books is sorted in an order depending on the sort_by parameter:

                'year' -- sorts by publication_year, breaking ties with (case-insenstive) title
                'title' -- sorts by (case-insensitive) title, breaking ties with publication_year
                default -- same as 'title' (that is, if sort_by is anything other than 'year'
                            or 'title', just do the same thing you would do for 'title')
        '''
        books_returned = []
        if search_text == None:
            books_returned = books_list
        else:
            for book in books_list:
                if search_text.lower() in book.title.lower():
                    books_returned.append(book)
        
        #if sort_by == 'year':
        #    books_returned
        #else:
         #   books_returned

        return books_returned



    def books_between_years(self, start_year=None, end_year=None):
        ''' Returns a list of all the Book objects in this data source whose publication
            years are between start_year and end_year, inclusive. The list is sorted
            by publication year, breaking ties by title (e.g. Neverwhere 1996 should
            come before Thief of Time 1996).

            If start_year is None, then any book published before or during end_year
            should be included. If end_year is None, then any book published after or
            during start_year should be included. If both are None, then all books
            should be included.
        '''
        return []

def main():
    booksource = BooksDataSource('tinybooks.csv')

    print(booksource.authors())
  


if __name__ == '__main__':
    main()