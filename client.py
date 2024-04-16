import requests
import os
from datetime import datetime, timedelta, timezone
import bisect
from itertools import chain
import logging


class Client:
    """
    Download a specific forecast data file from ECMWF hosted on BASE_URL.
    "[BASE_URL]/[yyyymmdd]/[HH]z/[model]/0p25/[stream]/[yyyymmdd][HH]0000-[step]h-[stream]-[type].grib2"
        yyyymmdd (str): The forecast date in 'YYYYMMDD' format.
        HH (str): The forecast time in 'HH' format.
        step (str): Forecast step in hours.
    """

    URLS = {
        "ecmwf": "https://data.ecmwf.int/forecasts",
        "azure": "https://ai4edataeuwest.blob.core.windows.net/ecmwf",
        "aws": "https://ecmwf-forecasts.s3.eu-central-1.amazonaws.com"
    }

    STEPS_OPER = chain(range(0, 145, 3), range(150, 241, 6))
    STEPS_SCDA = range(0, 91, 3)

    def __init__(
        self,
        source="aws",
        model="ifs",
        type_='fc',
        preserve_request_order=False,
        infer_stream_keyword=True,
        debug=False,
        verify=True,
    ):
        self.source = source
        self.model = model
        self.type = type_
        self.preserve_request_order = preserve_request_order
        self.infer_stream_keyword = infer_stream_keyword
        self.debug = debug
        self.verify = verify

        if debug:
            logging.basicConfig(level=logging.DEBUG)

    @classmethod
    def reference_datetime(cls, datetime_):
        # Define reference hours and their corresponding times
        reference_hh = ['18', '00', '06', '12']
        update_time_tuple_list = [(1, 12), (7, 55), (13, 12), (19, 55)]
        update_times = [x[0] * 60 + x[1] for x in update_time_tuple_list]
        p = datetime_.hour * 60 + datetime_.minute
        position_left = bisect.bisect_left(update_times, p)
        if position_left < 2:
            datetime_ -= timedelta(days=1)
        position = (position_left - 1) if position_left > 0 else 3
        return datetime_.strftime('%Y%m%d'), reference_hh[position]

    def download(
        self,
        yyyymmdd=None,
        hh=None,
        steps=None,
        target_folder=None
    ):
        def download_data(step):
            filename = f"{yyyymmdd}{hh}0000-{step}h-{stream}-{self.type}.grib2"
            f = f"{target_folder}/{download_folder}/{filename}"
            if os.path.isfile(f):
                return 1
            url = f"{self.URLS[self.source]}/{download_folder}/{filename}"
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                with open(f, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=1048576):
                        file.write(chunk)
            else:
                print(f"Error: {response.status_code} - {response.reason}")
            return response.status_code

        if yyyymmdd is None or hh is None:
            yyyymmdd, hh = self.reference_datetime(datetime.now(timezone.utc))
        if steps is None:
            steps = self.STEPS_OPER if hh in ['00', '12'] else self.STEPS_SCDA
        if target_folder is None:
            target_folder = '.'
        stream = 'oper' if hh in ['00', '12'] else 'scda'
        download_folder = f"{yyyymmdd}/{hh}z/{self.model}/0p25/{stream}"
        if not os.path.isdir(d := f"{target_folder}/{download_folder}"):
            os.makedirs(d)

        res = 0
        try:
            iter(steps)
            for p in steps:
                res = download_data(p)
        except TypeError:
            res = download_data(steps)
        return res
