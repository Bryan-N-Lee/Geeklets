#!/usr/bin/python

import elementtree.ElementTree as ET
import urllib2

url="http://www.footballwebpages.co.uk/league.xml?comp=1"

# make empty if no home/favorite team
hometeam = "Liverpool"

root = ET.parse(urllib2.urlopen(url)).getroot()

print "%3s %-20s %4s %4s %-3s" % ("POS","CLUB","PD","GD","PTS")

for team in root.findall('team'):
	pos = team.find('position').text
	name = team.find('name').text
	played = team.find('played').text
	GD = team.find('goalDifference').text
	points = team.find('points').text
	# if you'd like to shorted say West Bromwich Albion to WBA,
	# then you can uncomment the following:
	#if len(name.split(' ')) > 2:
	#	shortName = ""
	#	for word in name.split(' '):
	#		shortName += word[0]
	#	name = shortName
	if name == hometeam:
		# to change highlight color, change 41 to 41-47:
		# 41 - red
		# 42 - green
		# 44 - blue
		print "\033[1;41m%3s %-20s %4s %4s %3s \033[1;m" % (pos, name, played, GD, points)
	else:
		print "%3s %-20s %4s %4s %3s" % (pos, name, played, GD, points)
