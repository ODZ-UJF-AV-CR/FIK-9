from sondehub.amateur import Uploader
import datetime
import time
import logging

logging.basicConfig(format="%(asctime)s %(levelname)s:%(message)s", level=logging.DEBUG)

uploader = Uploader("SlimonTest",
                     uploader_position=[50.073, 14.418, 400]
                    )


uploader.add_telemetry(
    "fiktest-1", # Your payload callsign
    datetime.datetime.utcnow(),
    50.073658, # Latitude
    14.418540, # Longitude
    10000 # Altitude
)

time.sleep(10)

uploader.close()
