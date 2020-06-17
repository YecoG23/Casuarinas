import os

##GDAL CONFIGURATION

if os.name == 'nt':
    import platform
    OSGEO4W = r"C:\OSGeo4W"
    if '64' in platform.architecture()[0]:
        OSGEO4W += "64"
        assert os.path.isdir(OSGEO4W), "Directory does not exist: " + OSGEO4W
        os.environ['OSGEO4W_ROOT'] = OSGEO4W
        os.environ['GDAL_DATA'] = OSGEO4W + r"\share\gdal" 
        os.environ['PROJ_LIB'] = OSGEO4W + r"\share\proj"
        GDAL_LIBRARY_PATH = r'C:\OSGeo4W64\bin\gdal300'
        os.environ['PATH'] = OSGEO4W + r"\bin;" + os.environ['PATH']


#LEAFLET CONFIG
LEAFLET_CONFIG = {
# 'SPATIAL_EXTENT': (-76.9798,-12.1602, -76.9757,-12.1545),
'DEFAULT_CENTER': (-12.157639, -76.976689),
'DEFAULT_ZOOM': 16,
'TILES': [('Mapbox','https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoieWVjbzIzIiwiYSI6ImNrNnZvdnNhdjAwM2Uza285cnVzejFnbGcifQ.NY_Z2Zm2h7wH2LWo9-HGCw',
 {'attribution': 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
 'id':'mapbox/streets-v11',
 'accessToken':'your.mapbox.access.token'})],
'MIN_ZOOM': 3,
'MAX_ZOOM': 24,
# 'SRID': 3857,
}