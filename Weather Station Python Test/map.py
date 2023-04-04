import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# create a new Basemap instance with the desired projection
map = Basemap(projection='robin', resolution='c', lon_0=0)

# draw coastlines, countries, and grid lines
map.drawcoastlines()
map.drawcountries()
map.drawparallels(range(-90, 90, 30))
map.drawmeridians(range(-180, 180, 60))

import csv

lats = []
lons = []

# open the CSV file and read in the latitude and longitude values
with open('lat_lon_pairs.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        # print(row[0], row[1])
        lat = row[0]
        lon = row[1]
        # , lon = row[0].split(',')
        lats.append(float(lat))
        lons.append(float(lon))

# print('Latitude values:', lats)
# print('Longitude values:', lons)

# # add some points to the map
# lats = [40.7128, 51.5074, -33.8688] # example latitude points
# lons = [-74.0060, -0.1278, 151.2093] # example longitude points

x, y = map(lons, lats)
map.plot(x, y, 'ro', markersize=1)

# display the map
plt.show()
