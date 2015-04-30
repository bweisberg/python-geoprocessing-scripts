# python-geoprocessing-scripts
Tools and sample python code that work with arcpy and the ArcGIS Geoprocessing framework

##gpx_to_featureclass

[batch GPX to features conversion](gpx_to_featureclass/gpx_to_featureclass.py)

The problem:
We need to convert multiple GPS tracklog files in GPX format to something we can use in ArcMap.
There's a GPX to Feature Class GP Tool in ArcMap but it only provides input for one .gpx file at a time.
How do we convert hundreds of GPX files to features?

This script reads all the gpx files in a directory, converts them to Feature Classes and stores them in a file geodatabase.
If the files you're convert have the same fields, like GPS running logs from the same device, the Merge tool can be used to combine the outputs into a single feature class.

To run this script:

1.   Change the workspace_folder variable for your environment
2.   Open the Python window in ArcMap and paste in the code
3.   Type return/enter to execute
