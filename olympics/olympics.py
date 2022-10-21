'''
    olympics.py
    Author: Muno Siyakurima
'''

from signal import signal, SIGPIPE, SIG_DFL  
signal(SIGPIPE,SIG_DFL) 

import sys
import argparse
import psycopg2
import config


def get_connection():
    ''' Returns a database connection object with which you can create cursors,
        issue SQL queries, etc. This function is extremely aggressive about
        failed connections--it just prints an error message and kills the whole
        program. Sometimes that's the right choice, but it depends on your
        error-handling needs. '''
    try:
        return psycopg2.connect(database=config.database,
                                user=config.user,
                                password=config.password)
    except Exception as e:
        print(e, file=sys.stderr)
        exit()

def get_athletes_by_noc(search_text):
    ''' Returns a list of the full names of all athletes from a particular NOC.'''

    athletes = []
    try:
        query = '''SELECT athletes.athlete_name
                   FROM athletes
                   WHERE athletes.athletes_noc = %s'''
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (search_text,))
        for row in cursor:
            athlete_name = row[0]
            athletes.append(f'{athlete_name}')

    except Exception as e:
        print(e, file=sys.stderr)

    connection.close()
    return athletes


def get_num_of_golds():
    '''Returns a dictionary of the number of golds which an NOC has in total from the olympic games'''
    
    noc_golds = {}
    try:
        query = '''SELECT athletes.athletes_noc, count(medal) AS golds 
                    FROM athletes,athlete_medals 
                    WHERE athletes.athlete_id = athlete_medals.athlete_id 
                    AND medal='Gold' 
                    GROUP BY athletes.athletes_noc 
                    ORDER BY golds desc;'''
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        for row in cursor:
            noc = row[0]
            number = row[1]
            noc_golds[noc]=number
    except Exception as e:
        print(e, file=sys.stderr)
    connection.close()
    return noc_golds

def get_top_gold_medalists():
    '''Returns a dictionary of the top 50 athletes with the most gold medals over the olympic games 
    and the number of gold medals they have'''

    gold_medalists={}
    try:
        query = '''SELECT athletes.athlete_name,count(medal) 
        AS golds 
        FROM athletes, athlete_medals
        WHERE athletes.athlete_id = athlete_medals.athlete_id 
        AND athlete_medals.medal='Gold' 
        GROUP BY athletes.athlete_name 
        ORDER BY golds desc LIMIT 50'''
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        for row in cursor:
            name = row[0]
            golds = row[1]
            gold_medalists[name] = golds
    except Exception as e:
        print(e,file=sys.stderr)
    connection.close()
    return gold_medalists

def main():
    
    '''Parse in the arguments and also show the help statements for each option'''
    parser = argparse.ArgumentParser()
    parser.add_argument("-a","--athletesnoc",default=None,help="Displays all athletes from the specified NOC",type=str)
    parser.add_argument("-n","--nocgolds",action='store_true',default=None,help="Lists all the NOC's and the number of gold medals each has won, in decreasing order of gold medals")
    parser.add_argument("-g","--goldmedalists",action='store_true',default=None,help="Shows the top fifty athletes based on number of gold medals earned throughout the olympic games in this dataset")
    args=parser.parse_args()
    

    if args.athletesnoc:
        noc = args.athletesnoc
        athletes = get_athletes_by_noc(noc)
        for a in athletes:
            print(a)
    elif args.nocgolds:
        golds = get_num_of_golds()
        for key in golds:
            print(str(key)+": "+str(golds[key]))
    elif args.goldmedalists:
        athletegolds = get_top_gold_medalists()
        for key in athletegolds:
            print(str(key)+": "+str(athletegolds[key]))
            


if __name__ == '__main__':
    main()