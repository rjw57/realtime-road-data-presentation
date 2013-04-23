from osgeo import osr

wgs84 = osr.SpatialReference()
wgs84.ImportFromEPSG(4326)  # Longitude, Latitude (degrees)
bng = osr.SpatialReference()
bng.ImportFromEPSG(27700)   # OS grid Easting, Northing (metres)
trans = osr.CoordinateTransformation(wgs84, bng)

segment = link_segments.values()[0]
print(segment)
((1.174898, 51.1075), (1.234404, 51.106983))

print(trans.TransformPoints(segment))
[(622341.8470642003, 139045.90819568178, -43.13303761463612),
 (626508.8899003072, 139169.91645833637, -43.055007888004184)]

print([p[:2] for p in trans.TransformPoints(segment)])
[(622341.8470642003, 139045.90819568178),
 (626508.8899003072, 139169.91645833637)]

transformed_points = list(
    [x[:2] for x in trans.TransformPoints(segment)]
    for segment in link_segments.values()
)

lc = LineCollection(transformed_points)
gca().add_collection(lc)
xlabel('Easting / m')
ylabel('Northing / m')
axis('equal')
savefig('bng-links.pdf')

im = imread('bng-map.png')
imshow(im, extent=(1e5, 7e5, 0, 7e5))
lc = LineCollection(transformed_points)
gca().add_collection(lc)
xlabel('Easting / m')
ylabel('Northing / m')
axis('image')
savefig('bng-links-2.pdf')
