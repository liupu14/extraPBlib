import numpy as np 
import pandas as pd 


def CalDistance(latA,lngA,latB,lnngB):
    """
    给定两个点的经纬度，计算两个点的距离
    """
    [latA,lngA,latB,lngB] = np.radians([latA,lngA,latB,lngB])
    a = np.sin((latA-latB)/2) ** 2 + np.cos(lngA) * np.cos(lngB) * np.sin((lngA-lngB)/2) ** 2
    b = 2 * np.sqrt(a)
    Distance = 6371 * b
    return Distance

def FindNearbyPoints(lat,lng,distance):
    """
    给定某个点的经纬度以及距离，计算这个点在此范围内的左下角和右上角的经纬度
    """
    r = 6371
    dlng = np.asin(np.sin(distance/(2 * r)) / np.cos(lng * np.pi /180) )
    dlng = dlng * 180 / np.pi 
    dlat = distance / r
    dlat = dlat * 180 / np.pi 
    latmin = lat - dlat 
    latmax = lat + dlat 
    lngmin = lng - dlng 
    lngmax = lng + dlng 
    return latmin,lngmin,latmax,lngmax 


