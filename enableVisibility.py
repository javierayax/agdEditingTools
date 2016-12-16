import arcpy
mxd = arcpy.mapping.MapDocument("current")
layers = arcpy.mapping.ListLayers(mxd)
for layer in layers:
  if arcpy.Describe(layer).spatialReference.name == u'Unknown':
    if abs(arcpy.Describe(layer).extent.XMin) > 0 and abs(arcpy.Describe(layer).extent.XMin) < 180:
      layer.visible = 1
