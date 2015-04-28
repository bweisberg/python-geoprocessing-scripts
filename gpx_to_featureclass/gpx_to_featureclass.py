import os
import sys
import glob

print "starting up..."
import arcpy
from arcpy import env

# Set local variables
workspace_folder = r'C:\Data\student\gpxrun'
env.workspace = workspace_folder
gdb_name = "gpx.gdb"
outputgdb = workspace_folder + '\\' + gdb_name + '\\'

if arcpy.Exists(outputgdb):
    print "Deleting the old geodatabase..."
    arcpy.Delete_management(outputgdb)
else:
    print "No geodatabase to delete"

# Create a File Geodatabase to store individual runs and the merged output as FC
arcpy.CreateFileGDB_management(workspace_folder, gdb_name)

env.workspace = outputgdb
print env.workspace

print "Converting the GPX to Feature Classes"
gpxlist = glob.glob(workspace_folder + "\\*.gpx")
for gpxfile in gpxlist:
  outfile = os.path.splitext(os.path.basename(gpxfile))[0]
  arcpy.GPXtoFeatures_conversion(gpxfile, outputgdb + outfile)

featureclasses = arcpy.ListFeatureClasses()
print featureclasses
print "Merging the Feature Classes"
arcpy.Merge_management(featureclasses,env.workspace + '\\' + 'all_runs')
