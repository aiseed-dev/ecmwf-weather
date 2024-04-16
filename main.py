from ecmwf.opendata import Client as EcmwfClient
from client import Client
import pygrib

def sample():
    client = EcmwfClient()

    client.retrieve(
        step=240,
        type="fc",
        target="data2.grib2",
    )


# Grib2ファイルをpygribを使ってpythonで扱う
def use_grib2(filename):
    with pygrib.open(filename) as grbs:
        # Fileの内容をイテレート
        for grb in grbs:
            # metadataを表示
            print(grb)

            # dataを表示
            data = grb.values
            # print(data)

        # fileを閉じる
        grbs.close()

def main():
    client = Client()
    client.download(target_folder='data')


if __name__ == "__main__":
    main()
