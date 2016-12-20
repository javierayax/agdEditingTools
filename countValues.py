import arcpy
dicFields = {}
layer = "Aspersiones"

fields = [field.name for field in arcpy.ListFields(layer)]
for field in fields:
    dicFields[field] = 0

with arcpy.da.SearchCursor(layer, fields) as cursor:
    for row in cursor:
        i = 0
        print row
        for field in fields:
            value = row[i]
            print value
            if value == None:
                dicFields[fields[i]] += 1
            i+=1

