link_speeds = {}
for datum in pub.elaboratedData:
    value = datum.basicDataValue
    location_id = value.affectedLocation.\
        locationContainedInGroup.\
        predefinedLocationReference.text
    
    # Create, the appropriate link datum
    link_speeds[location_id] = \
        float(value.averageVehicleSpeed.text)
