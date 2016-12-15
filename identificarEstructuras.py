mxd = arcpy.mapping.MapDocument("current")
layers = arcpy.mapping.ListLayers(mxd)

for layer in layers:
    describe = arcpy.Describe(layer)
    sr = describe.spatialReference
    print sr.name
    
total = 0
for layer in layers:
    n = long(arcpy.GetCount_management(layer).getOutput(0))
    print n 
    total += n

          
dicFields = {}
for layer in layers:
    fields = [field.name + "-" + field.type + "-" + str(field.length) for field in arcpy.ListFields(layer)]
    for field in fields:
        if field not in dicFields.keys():
            dicFields[field] = 1
        else:
            dicFields[field] = dicFields[field] + 1
           

import collections
od = collections.OrderedDict(sorted(dicFields.items()))

     
for key in dicFields.keys():
    try:
        arcpy.AddField_management("AeronavesImpactadas", key, "TEXT", field_length = 255)
    except:
        print key
        
for layer in layers:
    try:
        arcpy.Append_management(layer, "AeronavesImpactadas", "NO_TEST")
    except:
        print layer.name
        



for key, value in sorted(dicFields.iteritems(), key= lambda (k,v): (v,k), reverse = True):
    print "%s: %s" % (key, value)


def formater(value):
 try:
  return "%s/%s/20%s" % (value[4:6], value[2:4], value[0:2])
 except:
  pass
