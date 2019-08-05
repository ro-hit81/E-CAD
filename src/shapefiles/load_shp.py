import os
from django.contrib.gis.utils import LayerMapping
from .models import Parcel, Building, Transportation, Hydro

parcel_mapping = {
    'objectid': 'OBJECTID',
    'parcelkey': 'ParcelKey',
    'ownerid': 'OwnerId',
    'registered': 'Registered',
    'eastparcel': 'EastParcel',
    'westparcel': 'WestParcel',
    'northparce': 'NorthParce',
    'southparce': 'SouthParce',
    'parcelnoen': 'ParcelNoEn',
    'shape_area': 'SHAPE_Area',
    'geom': 'MULTIPOLYGON',
}

building_mapping = {
    'objectid': 'OBJECTID',
    'houseno': 'HouseNo',
    'parcelkey': 'ParcelKey',
    'shape_leng': 'Shape_Leng',
    'area': 'Area',
    'geom': 'MULTIPOLYGON',
}

transportation_mapping = {
    'objectid': 'OBJECTID',
    'name': 'Name',
    'shape_leng': 'SHAPE_Leng',
    'shape_area': 'SHAPE_Area',
    'geom': 'MULTIPOLYGON',
}

hydro_mapping = {
    'objectid': 'OBJECTID',
    'name': 'Name',
    'shape_leng': 'SHAPE_Leng',
    'shape_area': 'SHAPE_Area',
    'hydrotype': 'HydroType',
    'geom': 'MULTIPOLYGON',
}


parcel_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'ecad/data/parcel', 'parcel.shp'),)
def parcel_run(verbose=True):
    lm = LayerMapping(Parcel, parcel_shp,parcel_mapping, transform='False')
    lm.save(strict=True, verbose=verbose)

building_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'ecad/data/building', 'building.shp'),)
def building_run(verbose=True):
    lm = LayerMapping(Building, building_shp,building_mapping, transform='False')
    lm.save(strict=True, verbose=verbose)

transportation_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'ecad/data/transportation', 'transportation.shp'),)
def transportation_run(verbose=True):
    lm = LayerMapping(Transportation, transportation_shp,transportation_mapping, transform='False')
    lm.save(strict=True, verbose=verbose)
 
hydro_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'ecad/data/hydro', 'hydro.shp'),)
def hydro_run(verbose=True):
    lm = LayerMapping(Hydro, hydro_shp, hydro_mapping, transform='False')
    lm.save(strict=True, verbose=verbose)   