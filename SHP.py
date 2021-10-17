import shapefile
from math import floor

# Helper function for converting decimal degrees to DMS (source: http://rextester.com/BRMA94677) modified for ESE file
def dd2dms(decimaldegree, direction='x'):
    if type(decimaldegree) != 'float':
        try:
            decimaldegree = float(decimaldegree)
        except:
            raise ValueError('Could not convert %s to float.'%(type(decimaldegree)))
            return 0
    if decimaldegree < 0:
        decimaldegree = -decimaldegree
        if direction == 'x':
            appendix = 'W'
        else:
            appendix = 'S'
    else:
        if direction == 'x':
            appendix = 'E'
        else:
            appendix = 'N'
    minutes = decimaldegree%1.0*60
    seconds = minutes%1.0*60
    degrees = int(floor(decimaldegree))
    minutes = int(floor(minutes))
    
    return f"{appendix}{degrees:03d}.{minutes:02d}.{seconds:02.3f}"

def readRegion(file, ICAO, region="SMR"):
    f = open(f"{ICAO}.{region}.txt","w")
    with shapefile.Reader(file) as shp:
        header = f"AERONAV:{ICAO}:{region}:ES:"
        f.write(f"{header}\n")
        #print(shp)
        shapes = shp.shapeRecords()
        for shape in shapes:
            color = shape.record.as_dict()['Color']
            f.write(f"{color}\n")
            for p in shape.shape.points:
                f.write(f"{dd2dms(p[1], 'y')} {dd2dms(p[0])}\n")
    f.close()

def readGEO(file, ICAO, region = "GEO"):
    f = open(f"{ICAO}.{region}.txt","w")
    with shapefile.Reader(file) as shp:
        #header = f"AERONAV:{ICAO}:\nGroundlayout:{region}:\n:\nGEO::"
        #f.write(f"{header}\n")
        #print(shp)
        shapes = shp.shapeRecords()
        for shape in shapes:
            color = shape.record.as_dict()['Color']
            fr = shape.shape.points[0]
            for p in shape.shape.points:
                to = p
                if fr == to:
                    continue
                f.write(f"{dd2dms(fr[1], 'y')} {dd2dms(fr[0])} {dd2dms(to[1], 'y')} {dd2dms(to[0])} {color}\n")
                fr = p
    f.close()

def readLabels(file, ICAO, region="Labels"):
    f = open(f"{ICAO}.{region}.txt", "w")
    with shapefile.Reader(file) as shp:
        shapes = shp.shapeRecords()
        for s in shapes:
            label = s.record.as_dict()['Label']
            pos = s.shape.points[0]
            f.write(f"{dd2dms(pos[1], 'y')} {dd2dms(pos[0])} {label}\n")
    f.close()            
