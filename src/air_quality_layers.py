import ee

PROJECT_ID = "my-project-497608"

ee.Initialize(project=PROJECT_ID)


def get_aod_layer(start_date, end_date):

    india = ee.Geometry.Rectangle([68, 6, 97, 38])

    modis = (
        ee.ImageCollection("MODIS/061/MCD19A2_GRANULES")
        .filterDate(str(start_date), str(end_date))
        .filterBounds(india)
        .select("Optical_Depth_055")
        .mean()
    )

    vis_params = {
        "min": 0,
        "max": 1000,
        "palette": ["blue", "green", "yellow", "red"]
    }

    return modis.getMapId(vis_params)

def get_no2_layer(start_date, end_date):

    india = ee.Geometry.Rectangle([68, 6, 97, 38])

    no2 = (
        ee.ImageCollection("COPERNICUS/S5P/OFFL/L3_NO2")
        .filterDate(str(start_date), str(end_date))
        .filterBounds(india)
        .select("tropospheric_NO2_column_number_density")
        .mean()
    )

    vis_params = {
        "min": 0,
        "max": 0.0002,
        "palette": ["blue", "cyan", "yellow", "red"]
    }

    return no2.getMapId(vis_params)

def get_aod_stats(start_date, end_date):

    india = ee.Geometry.Rectangle([68, 6, 97, 38])

    collection = (
        ee.ImageCollection("MODIS/061/MCD19A2_GRANULES")
        .filterDate(str(start_date), str(end_date))
        .filterBounds(india)
        .select("Optical_Depth_055")
    )

    image_count = collection.size().getInfo()

    mean_image = collection.mean()

    stats = mean_image.reduceRegion(
        reducer=ee.Reducer.mean(),
        geometry=india,
        scale=10000,
        maxPixels=1e13
    )

    avg_aod = stats.get("Optical_Depth_055").getInfo()

    return avg_aod, image_count


def get_no2_stats(start_date, end_date):

    india = ee.Geometry.Rectangle([68, 6, 97, 38])

    collection = (
        ee.ImageCollection("COPERNICUS/S5P/OFFL/L3_NO2")
        .filterDate(str(start_date), str(end_date))
        .filterBounds(india)
        .select("tropospheric_NO2_column_number_density")
    )

    image_count = collection.size().getInfo()

    mean_image = collection.mean()

    stats = mean_image.reduceRegion(
        reducer=ee.Reducer.mean(),
        geometry=india,
        scale=10000,
        maxPixels=1e13
    )

    avg_no2 = stats.get(
        "tropospheric_NO2_column_number_density"
    ).getInfo()

    return avg_no2, image_count