import arcpymxd = arcpy.mapping.MapDocument("current")layers = arcpy.mapping.ListLayers(mxd)for layer in layers:    if arcpy.Describe(layer).spatialReference.code == 4326:        layer.visible = 0
