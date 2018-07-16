import xml.etree.cElementTree as ET
import pprint

datadir = "data"
datafile = "OpenStreetMap_Pierce_County.osm"

#Find out how many unique users contributed to the map of Pierce County, WI

def get_user(element):
    uid = ''
    if element.tag == "node" or element.tag == "way" or element.tag == "relation":
        uid = element.get('uid')
    return uid

def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        if get_user(element):
            users.add(get_user(element))
            users.discard('')    
        pass

    return users

users = process_map(datafile)
len(users)