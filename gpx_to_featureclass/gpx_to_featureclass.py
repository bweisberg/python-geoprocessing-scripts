"""
#gpx_to_featureclass

batch GPX to features conversion

This script reads all the gpx files in a directory and
converts them to Feature Classes in a file geodatabase

To run this script:
1.  Change the workspace_folder variable for your environment
2.  Open the Python window in ArcMap and paste in the code
3.  Type return/enter to execute

"""
import os
import sys
import glob

print "starting up..."
import arcpy
from arcpy import env

# The folder where the .gpx files are and where we create the file geodatabase
workspace_folder = r'C:\Data\student\gpxrun'
env.workspace = workspace_folder
gdb_name = "gpx.gdb"
outputgdb = workspace_folder + '\\' + gdb_name + '\\'

if arcpy.Exists(outputgdb):
    print "Deleting the old geodatabase..."
    arcpy.Delete_management(outputgdb)

print "Creating a file geodatabase to store the feature classes"
arcpy.CreateFileGDB_management(workspace_folder, gdb_name)

env.workspace = outputgdb

print "Converting the .gpx files to Feature Classes"
gpxlist = glob.glob(workspace_folder + "\\*.gpx")
for gpxfile in gpxlist:
  outfile = os.path.splitext(os.path.basename(gpxfile))[0]
  print "Converting " + gpxfile
  arcpy.GPXtoFeatures_conversion(gpxfile, outputgdb + outfile)

#TODO: Merge the feature classes
#featureclasses = arcpy.ListFeatureClasses()
#arcpy.Merge_management(featureclasses,env.workspace + '\\' + 'all_runs')
