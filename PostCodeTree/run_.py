import csv
from pyqtree import Index
from pcpoint import PostCodePoint

pcFile = "postcodes.csv"

# Latitudes: 54.596553 to 54.603728
# Longitudes: -5.937032 to -5.922495
pcBounds = (54.596552, -5.937033, 54.603729, -5.922494)

pcIndex = Index(bbox = pcBounds)

with open(pcFile) as csvfile:
    pcReader = csv.DictReader(csvfile)

    print "populating qtree"

    for row in pcReader:
        postcode = PostCodePoint(row['Postcode'])
        lat = row['Latitude']
        lon = row['Longitude']

        pcIndex.insert(postcode, (lat, lon, lat, lon))

    print "qtree populated"
    print "attempt delaunay?"

