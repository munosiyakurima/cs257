import csv

'''this program gets the source data, which are files from Kaggle and then reads
them to separate files called athletes and noc_regions'''
#read the athlete events csv file
#read the noc csv file
#create files to hold the csv files read off the kaggle versions
#


# (1) Create a dictionary that maps athlete_id -> athlete_name
#       and then save the results in athletes.csv
athletes = {}
with open('athlete_events.csv') as original_data_file,\
    open('athletes.csv', 'w', newline='', encoding='utf-8') as athletes_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(athletes_file)
    heading_row = next(reader) # eat up and ignore the heading row of the data file
    for row in reader:
        athlete_id = row[0]
        athlete_name = row[1]
        athletes_noc = row[7]
        athletes_region = row[6]
        if athlete_id not in athletes:
            athletes[athlete_id] = athlete_name
            writer.writerow([athlete_id, athlete_name, athletes_noc, athletes_region])

# (2) Create a dictionary that maps event_name -> event_id
#       and then save the results in events.csv
event_categories = {}
with open('athlete_events.csv') as original_data_file,\
        open('event_categories.csv', 'w', newline='', encoding='utf-8') as event_categories_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(event_categories_file)
    heading_row = next(reader) # eat up and ignore the heading row of the data file
    for row in reader:
        category_name = row[12]
        if category_name not in event_categories:
            category_id = len(event_categories) + 1
            event_categories[category_name] = category_id
            writer.writerow([category_id, category_name])

# (3) For each row in the original athlete_events.csv file, build a row
#       for our new event_results.csv table
events = {}
with open('athlete_events.csv') as original_data_file,\
        open('events.csv', 'w', newline='', encoding='utf-8') as events_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(events_file)
    heading_row = next(reader) # eat up and ignore the heading row of the data file
    for row in reader:
        event_name = row[13]
        if event_name not in events:
            event_id = len(events) + 1
            events[event_name] = event_id
            event_category_id = event_categories[row[12]] # this is guaranteed to work by section (2)
            writer.writerow([event_id, event_category_id, event_name])


games = {}
with open('athlete_events.csv') as original_data_file,\
        open('games.csv', 'w', newline='', encoding='utf-8') as games_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(games_file)
    heading_row = next(reader) # eat up and ignore the heading row of the data file
    for row in reader:
        games_year_season = row[8]
        games_city = row[11]
        if games_year_season not in games:
            games_id = len(games) + 1
            games[games_year_season] = games_id
            writer.writerow([games_id, games_year_season, games_city])


athlete_medals = {}
with open('athlete_events.csv') as original_data_file,\
        open('athlete_medals.csv', 'w', newline='', encoding='utf-8') as athlete_medals_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(athlete_medals_file)
    heading_row = next(reader) # eat up and ignore the heading row of the data file
    for row in reader:
        athlete_id = row[0]
        medal = row[14]
        if (athlete_id and event_id and games_id) not in athlete_medals:
            medals_id = len(athlete_medals) + 1
            athlete_medals[athlete_id, event_id, games_id, medal] = medals_id
            games_id = games[row[8]] 
            event_id = events[row[13]]
            writer.writerow([medals_id, athlete_id, event_id, games_id, medal])
