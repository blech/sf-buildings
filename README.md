sf-buildings
============

Taking the [SF Data](https://data.sfgov.org/) [building footprints](https://data.sfgov.org/Facilities-and-Structures/Building-Footprints-Zipped-Shapefile-Format-/jezr-5bxm) and [converting them](https://github.com/blech/sf-buildings/blob/master/convert.sh) to a useful format (thanks [migurski](https://github.com/migurski)!), before [splitting them](https://github.com/blech/sf-buildings/blob/master/split.py) and converting them to [TopoJSON](https://github.com/mbostock/topojson/wiki) so GitHub can [display them](https://github.com/blech/sf-buildings/blob/master/topojson/bf_ll-4_1.topojson).

After that I realised I was [reinventing the wheel](http://tilestache.org/) and decided just to render the shapefile as a PNG layer, so I used [TileMill](https://www.mapbox.com/tilemill/) to make [a small San Francisco map](http://blech.github.io/sf-buildings/#16/37.7879/-122.4055).

(With apologies to [Map Time SF](http://maptimesf.tumblr.com/post/53078858337/explorations-in-qgis-from-the-very-first-map-time).)