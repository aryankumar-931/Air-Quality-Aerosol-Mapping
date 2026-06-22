import ee

PROJECT_ID = "my-project-497608"

ee.Initialize(project=PROJECT_ID)

dataset = (
    ee.ImageCollection("MODIS/061/MCD19A2_GRANULES")
    .filterDate("2024-01-01", "2024-01-31")
)

first_image = dataset.first()

print("Dataset Loaded Successfully!")
print("\nBand Names:")

bands = first_image.bandNames().getInfo()

for band in bands:
    print("-", band)