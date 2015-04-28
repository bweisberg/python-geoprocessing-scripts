# python-geoprocessing-scripts
Tools and sample python code that work with arcpy and the ArcGIS Geoprocessing framework

##gpx_to_featureclass

batch GPX to features conversion

The problem:
We need to convert GPS tracklogs in GPX format to something we can use in ArcMap
The GPX to Feature Class GP Tool in ArcMap only provides input for one .gpx file at a time.
The batch tool in ArcMap requires the user to select each file, one at a time.
How do we quickly convert hundreds of GPS track logs in GPS format to Feature Classes?

This script reads all the gpx files in a directory and converts them to Feature Classes in a file geodatabase
If the feature class schemas match, like GPS running logs from the same debice, the Merge tool can be used to easily combine the outputs.

To run this script:
1.  Change the workspace_folder variable for your environment
2.  Open the Python window in ArcMap and paste in the code
3.  Type return/enter to execute