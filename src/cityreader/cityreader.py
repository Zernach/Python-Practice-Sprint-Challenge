# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.

import csv

cities = []

class City:
  def __init__(self, row_list):
    self.city = row_list[0]
    self.state_name = row_list[1]
    self.county_name = row_list[2]
    self.lat = row_list[3]
    self.lng = row_list[4]
    self.population = row_list[5]
    self.density = row_list[6]
    self.timezone = row_list[7]
    self.zips = row_list[8]
  
  def __str__(self):
    return (f"\nCity = {self.city}\nState = {self.state_name}\nCounty = {self.county_name}\nLat = {self.lat}\nLong = {self.lng}\nPopulation = {self.population}\nDensity = {self.density}\nTimezone = {self.timezone}\nZip Codes = {self.zips}""")

def cityreader(cities=[]):
  # Implement the functionality to read from the 'cities.csv' file
  # For each city record, create a new City instance and add it to the 
  # `cities` list

  with open('cities.csv') as csvfile:
    reader = csv.reader(csvfile)
    for city_row in reader:
      cities.append(City(city_row))
  
  return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):

  # Standardize lats/longs
  if lat1 < lat2:
    lower_lat = lat1
    upper_lat = lat2
  else:
    lower_lat = lat2
    upper_lat = lat1
  
  if lon1 < lon2:
    right_lon = lon2
    left_lon = lon1
  else:
    right_lon = lon1
    left_lon = lon2

  # within will hold the cities that fall within the specified region
  within = []

  # Check if each city falls within the standardized lats/longs
  for city in cities:
    try:
      if float(city.lat) >= lower_lat and float(city.lat) <= upper_lat and float(city.lng) >= left_lon and float(city.lng) <= right_lon:
        within.append(f"{city.name}: ({city.lat}, {city.lng})")
    except:
      pass

  # Ensure that the lat and lon valuse are all floats
  # Go through each city and check to see if it falls within 
  # the specified coordinates.

  return within


# Get latitude and longitude values from the user
lat1 = float(input('1st latitude point: '))
lon1 = float(input('1st longitude point: '))
lat2 = float(input('2nd latitude point: '))
lon2 = float(input('2nd longitude point: '))

cities_within = cityreader_stretch(lat1, lon1, lat2, lon2, cities)

for city in cities_within:
  print(city)