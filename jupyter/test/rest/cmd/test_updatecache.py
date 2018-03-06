from unittest import TestCase
from iclientpy.rest.cmd.updatecache import main


class TestUpdateCache(TestCase):
    def test(self):
        def fun(*arg, **kwargs):
            self.assertDictEqual(kwargs, {'address': 'http://localhost:8090/iserver', 'username': 'admin',
                                          'password': 'iServer123', 'component_name': 'cache-World',
                                          'w_loc': '..\\..\\..\\data\\WorldNew\\World.sxwu', 'map_name': 'World',
                                          'original_point': (-180.0, 90.0), 'cache_bounds': (0.0, 0.0, 180.0, 90.0),
                                          'scale': [4000000.0, 8000000.0], 'remote_workspace': False, 'quite': True,
                                          'update': False})

        main(
            r"-l http://localhost:8090/iserver --user admin --password iServer123  --component-name cache-World -w ..\..\..\data\WorldNew\World.sxwu -m World -o '-180,90' -b 0,0,180,90 -s 4000000,8000000 --rw=False --quite"
                .split(' '),
            fun)
