from visualization import create_map

Map = create_map()

Map.to_html(
    "outputs/india_map.html",
    title="Air Quality Map"
)

print("Map Created Successfully!")