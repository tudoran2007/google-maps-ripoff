from objects import city, map

googlemaps = map()

#add basic cities and connections. This map should look something like this (ignore the bad drawing): https://imgur.com/a/AINDhyA
googlemaps.addcity("Paris", "Berlin", "Brussels")
googlemaps.addcity("Brussels", "Paris", "Amsterdam")
googlemaps.addcity("Amsterdam", "Brussels", "Berlin")
googlemaps.addcity("Berlin", "Paris","Amsterdam", "Warsaw", "Prague")
googlemaps.addcity("Warsaw", "Berlin", "Prague")
googlemaps.addcity("Prague", "Berlin", "Warsaw")