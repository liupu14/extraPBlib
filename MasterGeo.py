import numpy as np 
import pandas as pd 
import geopandas as gpd 

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

def get_coor(lng,lat,Ranges=3,gridDis=0.5):
    """
    根据给定的初始经纬度信息以及设定的范围，得到该辐射范围内所有固定大小网格中心的经纬度
    参数说明：
            Ranges:中心点辐射范围，单位为千米，默认为3千米
            gridDis:每个网格的大小，默认为500米
    """
    lng_min = lng - 0.01 * Ranges 
    lng_max = lng + 0.01 * Ranges 
    lat_min = lat - 0.01 * Ranges 
    lat_max = lat + 0.01 * Ranges 

    lng_list = []
    lat_list = []

    start_lng = lng_min + 0.01 * gridDis / 2
    start_lat = lat_min + 0.01 * gridDis / 2
    end_lng = lng_max - 0.01 * gridDis / 2
    end_lat = lat_max - 0.01 * gridDis / 2

    lng_temp = start_lng 
    lat_temp = start_lat 

    while lng_temp < end_lng:
        lng_temp += 0.01 * gridDis 
        lng_list.append(lng_temp)

    while lat_temp < end_lat:
        lat_temp += 0.01 * gridDis 
        lat_list.append(lat_temp)

    coor_list = [str(ii) + "," + str(jj) for ii in lng_list for jj in lat_list]
    return coor_list 

def PointsinSections(shapePath,lng,lat):
    ShapeData = gpd.read_files(shapePath)
    target = gpd.points_from_xy(x=[lng],y=[lat])
    target = gpd.GepSeries(target)
    if ShapeData.geometry.intersects(target.geometry):
        return True 


