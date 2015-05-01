'''
#gpx_to_featureclass

batch GPX to features conversion

This script reads all the gpx files in a directory and
converts them to Feature Classes in a file geodatabase

To run this script in ArcMap:
1.  Change the workspace_folder variable for your environment
2.  Open the Python window in ArcMap and paste in the code
3.  Type return/enter to execute

To run this script with python
1. python gpx_to_featureclass.py <path to folder containing gpx>
'''
print('starting up')
import arcpy
import glob
import os
import sys

# The folder where the .gpx files are and where we create the file geodatabase
workspace_folder = r'C:\Data\student\gpxrun'

#: first param is .py. second is path to gpx
if len(sys.argv) == 2 and sys.argv[0]:
    workspace_folder = sys.argv[1]

if not os.path.isdir(workspace_folder) and not os.path.exists(workspace_folder):
    raise Exception('{} is not found. Update workspace_folder or pass the value '.format(workspace_folder) +
                    'in as a parameter to the script. gpx_to_featureclass.py <path to folder containing gpx>')

arcpy.env.workspace = workspace_folder
gdb_name = 'gpx.gdb'
outputgdb = os.path.join(workspace_folder, gdb_name)

if arcpy.Exists(outputgdb):
    print('Deleting the old geodatabase...')
    arcpy.Delete_management(outputgdb)

print('Creating a file geodatabase to store the feature classes')
arcpy.CreateFileGDB_management(workspace_folder, gdb_name)

arcpy.env.workspace = outputgdb

print('Converting the .gpx files to Feature Classes')
gpxlist = glob.glob(os.path.join(workspace_folder, '*.gpx'))

for gpxfile in gpxlist:
    outfile = os.path.splitext(os.path.basename(gpxfile))[0]

    print('Converting ' + gpxfile)
    arcpy.GPXtoFeatures_conversion(gpxfile, outputgdb + outfile)

print('done')

# TODO: Merge the feature classes
# featureclasses = arcpy.ListFeatureClasses()
# arcpy.Merge_management(featureclasses,env.workspace + '\\' + 'all_runs')
