pub = model.payloadPublication
location_sets = pub.predefinedLocationSet

link_segments = {}
for loc_set in location_sets:
    for loc_elem in loc_set.predefinedLocation:
        loc = loc_elem.predefinedLocation
        linear = loc.tpeglinearLocation

        to_coord = linear.to.pointCoordinates
        to = ( float(to_coord.longitude),
               float(to_coord.latitude) )
        from_coord = linear['from'].pointCoordinates
        from_ = ( float(from_coord.longitude),
                  float(from_coord.latitude) )
        
        link_segments[loc_elem.attrib['id']] = (from_, to)
