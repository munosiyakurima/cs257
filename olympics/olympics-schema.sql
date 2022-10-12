'''The schema below shows the tables created in the olympics database'''

    '''One row represents an athlete and shows their name, NOC team and the region associated with that team'''
    CREATE TABLE athletes (
        athlete_id INTEGER,
        athlete_name TEXT,
        athletes_noc TEXT,
        athletes_region TEXT
    );

    '''One row represents the noc regions and any notes associated with it'''
    CREATE TABLE noc_regions (
        noc TEXT,
        region TEXT,
        notes TEXT
    );

    '''One row represents the sporting categories offered at the olympics'''
    CREATE TABLE event_categories (
        category_id INTEGER,
        category_name TEXT
    );

    '''One row represents an event in the olympics and the sporting category it is under'''
    CREATE TABLE events (
        event_id INTEGER,
        event_category_id INTEGER,
        event_name TEXT
    );
    
    '''One row represents the different olympic games and shows the season and city they were held in'''
    CREATE TABLE games (
        games_id INTEGER,
        games_year_season TEXT,
        games_city TEXT
    );
    
    '''One row represents an athlete and shows the medals they got in a specific event for a specific olympic game'''
    CREATE TABLE athlete_medals (
        medals_id INTEGER,
        athlete_id INTEGER,
        event_id INTEGER,
        games_id INTEGER,
        medal TEXT
    );
