#!/usr/bin/python
# splits a shapefile into a 6x6 grid of TopoJSON files

# TODO pull extents automatically using ogrinfo -al -so
#      ogrinfo -al -so bf_ll.shp | grep 'Extent'
# CRAZY adaptive splits based on polygon count (NB I am not that clever)

import subprocess

squares = 6

bl = (-122.514259, 37.705243)
tr = (-122.357631, 37.831965)

xinc = (tr[0]-bl[0])/squares
yinc = (tr[1]-bl[1])/squares

for x in range(0,squares):
    for y in range(0,squares):

        x1 = bl[0]+x*xinc
        x2 = bl[0]+(x+1)*xinc

        y1 = tr[1]-y*yinc
        y2 = tr[1]-(y+1)*yinc

        ogr2ogr = "/usr/bin/ogr2ogr -spat %s %s %s %s -f GeoJSON bf_ll-%s_%s.geojson bf_ll.shp" % (x1, y2, x2, y1, x, y)
        topojson = "/usr/bin/topojson bf_ll-%s_%s.geojson -o topojson/bf_ll-%s_%s.topojson" % (x, y, x, y)

        print ogr2ogr

        subprocess.call(ogr2ogr, shell=True)
        subprocess.call(topojson, shell=True)
        subprocess.call("rm bf_ll-%s_%s.geojson" % (x, y), shell=True)

        print "Completed block %s %s" % (x, y)

