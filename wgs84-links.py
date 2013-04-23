print(link_segments.values()[:5])

[((1.174898, 51.1075), (1.234404, 51.106983)),
 ((-1.519843, 53.73263), (-1.519193, 53.732506)),
 ((0.313035, 51.43044), (0.320784, 51.430897)),
 ((-2.023598, 52.672565), (-2.031822, 52.674973)),
 ((-1.204398, 52.617138), (-1.20728, 52.621113))]

from matplotlib.collections import LineCollection
lc = LineCollection(link_segments.values())
gca().add_collection(lc)
xlabel('Degrees East')
ylabel('Degrees North')
axis('equal')
savefig('wgs84-links.pdf')
