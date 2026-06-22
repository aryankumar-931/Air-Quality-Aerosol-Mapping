import ee

PROJECT_ID = "my-project-497608"

ee.Initialize(project=PROJECT_ID)

# Sentinel-5P NO2 Dataset
dataset = (
    ee.ImageCollection("COPERNICUS/S5P/OFFL/L3_NO2")
    .filterDate("2024-01-01", "2024-01-31")
)

print("Sentinel-5P Dataset Loaded Successfully!")

first_image = dataset.first()

print("\nBand Names:")

bands = first_image.bandNames().getInfo()

for band in bands:
    print("-", band)