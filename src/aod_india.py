'''import ee

PROJECT_ID = "my-project-497608"

ee.Initialize(project=PROJECT_ID)

# India Approximate Bounding Box
india = ee.Geometry.Rectangle([68, 6, 98, 38])

# January 2024 MODIS Data
dataset = (
    ee.ImageCollection("MODIS/061/MCD19A2_GRANULES")
    .filterDate("2024-01-01", "2024-01-31")
    .select("Optical_Depth_055")
)

# Mean AOD Image
aod = dataset.mean()

# Mean value over India
stats = aod.reduceRegion(
    reducer=ee.Reducer.mean(),
    geometry=india,
    scale=1000,
    maxPixels=1e13
)

print("Average AOD Over India:")
print(stats.getInfo())'''


import ee

PROJECT_ID = "my-project-497608"

ee.Initialize(project=PROJECT_ID)

india = ee.Geometry.Rectangle([68, 6, 98, 38])

dataset = (
    ee.ImageCollection("MODIS/061/MCD19A2_GRANULES")
    .filterDate("2024-01-01", "2024-01-31")
    .select("Optical_Depth_055")
)

print("Number of Images:")
print(dataset.limit(5).size().getInfo())