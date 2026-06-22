import geemap
from modis import get_aod_image
from sentinel import get_no2_image

def create_map(start_date, end_date):

    Map = geemap.Map(center=[22.5, 78.9], zoom=5)

    aod = get_aod_image(start_date, end_date)

    no2 = get_no2_image(start_date, end_date)

    Map.addLayer(
        aod,
        {
            "min": 0,
            "max": 1000,
            "palette": ["blue", "green", "yellow", "orange", "red"]
        },
        "MODIS AOD"
    )

    Map.addLayer(
        no2,
        {
            "min": 0,
            "max": 0.0002,
            "palette": ["blue", "green", "yellow", "orange", "red"]
        },
        "NO2"
    )

    return Map