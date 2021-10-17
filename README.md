# SHPtoGNG
Convert Shapefiles to GNG importable data

Dependencies:
- pySHP
- pyQt5

## Usage
Create a separate ESRI Shapefile for regions and lines. Both Shapefiles need to be created with WGS 84 reference system and have to have a field named **color** that will be used to determine the features color.

Import the Regions via the GNG Import field.

Import the lines by adding a new entry in SCT Entries and pasting in the generated file contents.

Import the labels by adding a new entry in Labels and pasting in the generated file contents.

## TODO
- Add coordinate system verification
- Add shape type verification