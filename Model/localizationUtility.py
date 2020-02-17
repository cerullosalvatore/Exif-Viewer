"""Localization Utility

In questo file sono presenti le due funzioni utilili ad individuare le coordinate dell'immagine.
"""

def get_decimal_from_dms(dms, ref):
    """
    Questa funzione trasforma le coordinate in formato decimale.
    :param dms:
    :param ref:
    :return:
    """
    degrees = dms[0][0] / dms[0][1]
    minutes = dms[1][0] / dms[1][1] / 60.0
    seconds = dms[2][0] / dms[2][1] / 3600.0
    if ref in ['S', 'W']:
        degrees = -degrees
        minutes = -minutes
        seconds = -seconds
    return round(degrees + minutes + seconds, 5)

def get_coordinates(geotags):
    """
    Restituisce la longitutine e la latitudine dati i geotag exif.
    :param geotags: geotags exif.
    :return: latitudine e longitudine in gormto decimale
    """
    lat = get_decimal_from_dms(geotags['GPSLatitude'], geotags['GPSLatitudeRef'])
    lon = get_decimal_from_dms(geotags['GPSLongitude'], geotags['GPSLongitudeRef'])
    return (lat, lon)