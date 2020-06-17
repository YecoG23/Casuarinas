import os
from django.contrib.gis.utils import LayerMapping
from .models import Buzon


Buzon_mapping = {
	# 'nombre':'Layer',
	'geom' : 'POINT',
}

buzon_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'static','Buzones-4326.shp'))

def run(verbose=True):
	lm = LayerMapping(Buzon, buzon_shp, Buzon_mapping, transform=False)
	lm.save(strict=True, verbose = verbose)
