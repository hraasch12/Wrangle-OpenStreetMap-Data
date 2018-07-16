import xml.etree.cElementTree as ET
import pprint
from collections import defaultdict
import re

datadir = "data"
datafile = "OpenStreetMap_Pierce_County.osm"

def audit_zipcode(file_zipcodes, zipcode):
    twoDigits = zipcode[0:2]
    
    if not twoDigits.isdigit():
        file_zipcodes[twoDigits].add(zipcode)

        
def is_zipcode(elem):
    return (elem.attrib['k'] == "addr:postcode")

def audit_zip(osmfile):
    osm_file = open(osmfile, "r", errors = 'ignore')
    file_zipcodes = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_zipcode(tag):
                    audit_zipcode(file_zipcodes,tag.attrib['v'])

    return file_zipcodes

pierce_zipcode = audit_zip(datafile)
pprint.pprint(dict(pierce_zipcode))

def update_zip(zipcode):
    testNum = re.findall('[a-zA-Z]*', zipcode)
    if testNum:
        testNum = testNum[0]
    testNum.strip()
    if testNum == "WI":
        convertedZipcode = (re.findall(r'\d+', zipcode))
        if convertedZipcode:
            if convertedZipcode.__len__() == 2:
                return (re.findall(r'\d+', zipcode))[0] + "-" +(re.findall(r'\d+', zipcode))[1]
            else:
                return (re.findall(r'\d+', zipcode))[0]

for street_type, ways in pierce_zipcode.items():
    for name in ways:
        better_name = update_zip(name)
        print(name, "=>", better_name)