#!/usr/bin/python

bl = (-122.514259, 37.705243)
tr = (-122.357631, 37.831965)

xinc = (tr[0]-bl[0])/6
yinc = (tr[1]-bl[1])/6

for y in range(0,5):
    for x in range(0,5):

        x1 = bl[0]+x*xinc
        x2 = bl[0]+(x+1)*xinc
        
        y1 = bl[1]+y*yinc
        y2 = bl[1]+(y+1)*yinc
                
        print "ogr2ogr -spat %s %s %s %s -f GeoJSON bf_ll-%s_%s.json bf_ll.shp" % (x1, y1, x2, y2, x, y)