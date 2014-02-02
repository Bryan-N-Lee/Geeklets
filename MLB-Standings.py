#!/usr/bin/python

'''
	Author: Bryan Lee
	Created On: 2/2/14
'''

import elementtree.ElementTree as ET
import urllib2

# There is an API request limit per hour, so watch that
url="https://erikberg.com/mlb/standings.xml"

# make empty if no home/favorite team
hometeam = "Athletics"

Team_abbrev = {	"Arizona": "ARI", "Atlanta": "ATL", "Baltimore": "BAL",
		"Boston": "BOS", "Cincinnati": "CIN", "Cleveland": "CLE",
		"Colorado": "COL", "Detroit": "DET", "Houston": "HOU",
		"Kansas City": "KC", "Miami": "MIA", "Milwaukee": "MIL",
		"Minnesota": "MIN", "Oakland": "OAK", "Philadelphia": "PHI",
		"Pittsburgh": "PIT", "San Diego": "SD", "San Francisco": "SF",
		"Seattle": "SEA", "St. Louis": "STL", "Tampa Bay": "TB",
		"Texas": "TEX", "Toronto": "TOR", "Washington": "WAS" }

Team_abbrev_multi = {	"Cubs": "CHC", "White Sox": "CHW", "Angels": "LAA",
			"Dodgers": "LAD", "Mets": "NYM", "Yankees": "NYY" }

root = ET.parse(urllib2.urlopen(url)).getroot()
#root = ET.parse(".../standings.xml").getroot()

print "%5s %3s %3s %5s %5s %4s" % ("Team", "W", "L", "PCT", "GB", "STK")

for division in root.findall('standing'):
	print division.get("content-label")
	for team in division.findall('team'):
		team_city = team.find('team-metadata').find('name').get('first')
		team_name = team.find('team-metadata').find('name').get('last')
		wins = team.find('team-stats').find('outcome-totals').get('wins')
		losses = team.find('team-stats').find('outcome-totals').get('losses')
		pct = team.find('team-stats').find('outcome-totals').get('winning-percentage')
		GB = team.find('team-stats').get('games-back')
		strk_type = team.find('team-stats').find('outcome-totals').get('streak-type')
		strk_num = team.find('team-stats').find('outcome-totals').get('streak-total')
		strk = ""
		if GB == "0.0":
			GB = "--"
		if team_city == "Chicago" or team_city == "New York" or team_city == "Los Angeles":
			team_city = Team_abbrev_multi[team_name]
		else:
			team_city = Team_abbrev[team_city]
		if strk_type == "win":
			strk = "W"+strk_num
		else:
			strk = "L"+strk_num
		if team_name == hometeam:
			print "\033[1;30m\033[1;42m%5s %3s %3s %5s %5s %4s \033[1;m\033[1;m" % (team_city, wins, losses, pct, GB, strk)
		else:
			print "%5s %3s %3s %5s %5s %4s" % (team_city, wins, losses, pct, GB, strk)
