# SHPtoGNG
Convert Shapefiles to GNG importable data

Dependencies:
- pySHP
- pyQt5

## Usage
Create a separate ESRI Shapefile for regions, lines and labels. Both Shapefiles need to be created with WGS 84 reference system and have to have a field named **Color** that will be used to determine the features color. Labels use a field called **Label**.

Import the Regions via the GNG Import field.

Import the lines by adding a new entry in SCT Entries and pasting in the generated file contents.

Import the labels by adding a new entry in Labels and pasting in the generated file contents.

## TODO
- Add coordinate system verification
- Add shape type verification