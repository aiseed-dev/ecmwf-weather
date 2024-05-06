import pygrib as pg
import numpy as np


class ECMWFData:
    def __init__(self, file_path):
        self.file_path = file_path
        self.grbindx_single = pg.index(self.file_path, 'shortName')
        self.grbindx_pressure = pg.index(self.file_path, 'shortName', 'level', 'typeOfLevel')

    def extract_single(self, short_name):
        return self.grbindx_single.select(shortName=short_name)[0]

    def extract_pressure(self, short_name, level):
        return self.grbindx_pressure.select(shortName=short_name, level=level, typeOfLevel='isobaricInhPa')[0]


