#!/bin/bash

wget http://apps.sfgov.org/datafiles/view.php?file=sfgis/building_footprint.zip -o building_footprint.zip
unzip building_footprint.zip
ogr2ogr -s_srs EPSG:2872 -t_srs EPSG:4326 bf_ll.shp building_footprint.shp
python split.py

