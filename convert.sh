wget http://apps.sfgov.org/datafiles/view.php?file=sfgis/building_footprint.zip -o building_footprint.zip
unzip building_footprint.zip
ogr2ogr -s_srs EPSG:2872 -t_srs EPSG:4326 bf_ll.shp building_footprint.shp
ogrinfo -al -so bf_ll.shp | grep 'Extent'
ogr2ogr -spat -122.409840333 37.7897243333 -122.383735667 37.8108446667 -f GeoJSON bf_ll-4_4.json bf_ll.shp
node_modules/.bin/topojson bf_ll-4_4.json > bf_ll-4_4.topojson

# a full list of splits can be built from ogr2ogr -spat -122.409840333 37.7897243333 -122.383735667 37.8108446667 -f GeoJSON bf_ll-4_4.json bf_ll.shp
