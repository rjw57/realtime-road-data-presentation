import ephem

def sun_altitude(date):
    """
    Return the altitude, in radians, of
    the Sun on a given date ant time as
    observed from London.
    """
    london = ephem.city('London')
    london.date = date
    return ephem.Sun(london).alt
