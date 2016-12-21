import os, arcpy
folder = r"Z:\DATOS SIG PONAL\ASPERSIONES\lineas de vuelo"
for root, dirs, files in os.walk(folder):
    for file in files:
        desc = arcpy.Describe(os.path.join(root, file))
        if desc.dataType == u'ShapeFile':
             arcpy.MakeFeatureLayer_management(desc.catalogPath)




