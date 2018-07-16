import xml.etree.cElementTree as ET
import pprint
import re

datadir = "data"
datafile = "OpenStreetMap_Pierce_County.osm"

#Parse through the file and create dictionary of tags
    def count_tags(filename):
        tags = {}
        for event, elem in ET.iterparse(filename, events=(\"start\",)):
            add_tag(elem.tag, tags)
        return tags
    
    def add_tag(tag, tags):
        if tag not in tags:
            tags[tag] = 1
        else:
            tags[tag] += 1
                                                          
    tag_list = count_tags(datafile)
    pprint.pprint(tag_list)