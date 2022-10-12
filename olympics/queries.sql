SELECT noc_regions.noc FROM noc_regions;

SELECT athletes.athlete_name 
FROM athletes
WHERE athletes.athletes_noc = 'JAM';

SELECT athlete_medals.medal, games.games_year_season, events.event_name
FROM athletes, athlete_medals, games, events
WHERE athletes.athlete_id = athlete_medals.athlete_id
AND athlete_medals.games_id = games.games_id
AND athlete_medals.event_id = events.event_id
AND athletes.athlete_name LIKE 'Gregory Efthimios%'
ORDER BY games.games_year_season;
 

