from ipyleaflet import Map, TileLayer, Layer
from traitlets import Unicode, List,  Int,  default, validate
import geojson
import os
from .._version import EXTENSION_VERSION


class CloudTileLayer(TileLayer):
    _view_name = Unicode("SuperMapCloudTileLayerView").tag(sync=True)
    _model_name = Unicode("SuperMapCloudTileLayerModel").tag(sync=True)
    _view_module = Unicode("iclientpy").tag(sync=True)
    _model_module = Unicode("iclientpy").tag(sync=True)
    _view_module_version = Unicode(EXTENSION_VERSION).tag(sync=True)
    _model_module_version = Unicode(EXTENSION_VERSION).tag(sync=True)

    mapName = Unicode('').tag(sync=True, o=True)
    type = Unicode('').tag(sync=True, o=True)


class TileMapLayer(TileLayer):
    _view_name = Unicode("SuperMapTileMapLayerView").tag(sync=True)
    _model_name = Unicode("SuperMapTileMapLayerModel").tag(sync=True)
    _view_module = Unicode("iclientpy").tag(sync=True)
    _model_module = Unicode("iclientpy").tag(sync=True)
    _view_module_version = Unicode(EXTENSION_VERSION).tag(sync=True)
    _model_module_version = Unicode(EXTENSION_VERSION).tag(sync=True)


class RankSymbolThemeLayer(Layer):
    _view_name = Unicode("SuperMapRankSymbolThemeLayerView").tag(sync=True)
    _model_name = Unicode("SuperMapRankSymbolThemeLayerModel").tag(sync=True)
    _view_module = Unicode("iclientpy").tag(sync=True)
    _model_module = Unicode("iclientpy").tag(sync=True)
    _view_module_version = Unicode(EXTENSION_VERSION).tag(sync=True)
    _model_module_version = Unicode(EXTENSION_VERSION).tag(sync=True)

    # symbolType = Unicode('Circle').tag(sync=True)
    # symbolSetting = Dict({}).tag(sync=True)
    name = Unicode('').tag(sync=True)
    sdata = List([])
    data = List([]).tag(sync=True)
    address_field_index = Int(0).tag(sync=True)
    value_field_index = Int(1).tag(sync=True)
    lng_filed_index = Int(2).tag(sync=True)
    lat_filed_index = Int(3).tag(sync=True)

    @validate('sdata')
    def _validate_sdata(self, proposal):
        if (proposal['value'] is None):
            raise Exception("error data")
        tempdata = []
        for d in proposal['value']:
            feature = get_privince_geojson_data(d[self.address_field_index])
            row = (d[self.address_field_index], d[self.value_field_index], feature["properties"]["cp"][0],
                   feature["properties"]["cp"][1])
            tempdata.append(row)
        self.data = tempdata
        return proposal['value']

    def __init__(self, name, data, address_field_index=0, value_field_index=1):
        super(RankSymbolThemeLayer, self).__init__()
        self.name = name
        self.address_field_index = address_field_index
        self.value_field_index = value_field_index
        self.sdata = data


class MapView(Map):
    _view_name = Unicode("SuperMapMapView").tag(sync=True)
    _model_name = Unicode("SuperMapMapModel").tag(sync=True)
    _view_module = Unicode("iclientpy").tag(sync=True)
    _model_module = Unicode("iclientpy").tag(sync=True)
    _view_module_version = Unicode(EXTENSION_VERSION).tag(sync=True)
    _model_module_version = Unicode(EXTENSION_VERSION).tag(sync=True)

    center = List([30.656483307485072, 104.06917333602907]).tag(sync=True, o=True)
    zoom = Int(15).tag(sync=True, o=True)
    crs = Unicode('EPSG3857').tag(sync=True, o=True)

    @default('default_tiles')
    def _default_tiles(self):
        return CloudTileLayer()


def get_privince_geojson_data(name):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "chinageojson.json"), 'r',
              encoding='utf-8') as geoJsonFile:
        fc = geojson.load(geoJsonFile)
        for i in range(0, len(fc["features"])):
            feature = fc["features"][i]
            if (name in feature["properties"]["name"]):
                return feature
