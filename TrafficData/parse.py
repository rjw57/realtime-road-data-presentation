link_data = {}
for datum in pub.elaboratedData:
    value = datum.basicDataValue
    location_id = value.affectedLocation.\
            locationContainedInGroup.\
            predefinedLocationReference.text
    
    # Get, or create, the appropriate link datum
    try:
        link_datum = link_data[location_id]
    except KeyError:
        link_datum = {}
        link_data[location_id] = link_datum
        
    link_datum['location_id'] = location_id
    link_datum['speed'] = float(value.averageVehicleSpeed.text)
