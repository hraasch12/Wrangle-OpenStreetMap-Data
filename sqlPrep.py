{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'zipCodes' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-6-a23be0fc3fd6>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[0;32m    177\u001b[0m                     \u001b[0mway_tags_writer\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mwriterows\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mel\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'way_tags'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    178\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 179\u001b[1;33m \u001b[0mprocess_map\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdatafile\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mvalidate\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m<ipython-input-6-a23be0fc3fd6>\u001b[0m in \u001b[0;36mprocess_map\u001b[1;34m(file_in, validate)\u001b[0m\n\u001b[0;32m    164\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    165\u001b[0m         \u001b[1;32mfor\u001b[0m \u001b[0melement\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mget_element\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfile_in\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mtags\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'node'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'way'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 166\u001b[1;33m             \u001b[0mel\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mshape_element\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0melement\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    167\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mel\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    168\u001b[0m                 \u001b[1;32mif\u001b[0m \u001b[0mvalidate\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mTrue\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m<ipython-input-6-a23be0fc3fd6>\u001b[0m in \u001b[0;36mshape_element\u001b[1;34m(element, node_attr_fields, way_attr_fields, problem_chars, default_tag_type)\u001b[0m\n\u001b[0;32m     72\u001b[0m                     \u001b[1;32mcontinue\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     73\u001b[0m                 \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 74\u001b[1;33m                     \u001b[0mnew_dict\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mtag_dictionary\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0melement\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0msecondary\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mdefault_tag_type\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     75\u001b[0m                     \u001b[1;32mif\u001b[0m \u001b[0mnew_dict\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     76\u001b[0m                         \u001b[0mtags\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mnew_dict\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m<ipython-input-6-a23be0fc3fd6>\u001b[0m in \u001b[0;36mtag_dictionary\u001b[1;34m(element, secondary, default_tag_type)\u001b[0m\n\u001b[0;32m     45\u001b[0m             \u001b[0mvalue\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mupdateStreetNames\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mupdate_street\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msecondary\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mattrib\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'v'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mmapping\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     46\u001b[0m         \u001b[1;32melif\u001b[0m \u001b[0mfield\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;34m'postcode'\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 47\u001b[1;33m             \u001b[0mvalue\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mzipCodes\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mupdate_zip\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msecondary\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mattrib\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'v'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     48\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     49\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0misinstance\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mvalue\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstr\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'zipCodes' is not defined"
     ]
    }
   ],
   "source": [
    "import xml.etree.cElementTree as ET\n",
    "import re\n",
    "import csv\n",
    "import cerberus\n",
    "import pymongo\n",
    "import schema\n",
    "import unicodecsv\n",
    "\n",
    "datadir = \"data\"\n",
    "datafile = \"OpenStreetMap_Pierce_County.osm\"\n",
    "\n",
    "NODES_PATH = \"nodes.csv\"\n",
    "NODE_TAGS_PATH = \"nodes_tags.csv\"\n",
    "WAYS_PATH = \"ways.csv\"\n",
    "WAY_NODES_PATH = \"ways_nodes.csv\"\n",
    "WAY_TAGS_PATH = \"ways_tags.csv\"\n",
    "\n",
    "LOWER_COLON = re.compile(r'^([a-z]|_)+:([a-z]|_)+')\n",
    "PROBLEMCHARS = re.compile(r'[=\\+/&<>;\\'\"\\?%#$@\\,\\. \\t\\r\\n]')\n",
    "\n",
    "SCHEMA = schema.schema\n",
    "\n",
    "NODE_FIELDS = ['id', 'lat', 'lon', 'user', 'uid', 'version', 'changeset', 'timestamp']\n",
    "NODE_TAGS_FIELDS = ['id', 'key', 'value', 'type']\n",
    "WAY_FIELDS = ['id', 'user', 'uid', 'version', 'changeset', 'timestamp']\n",
    "WAY_TAGS_FIELDS = ['id', 'key', 'value', 'type']\n",
    "WAY_NODES_FIELDS = ['id', 'node_id', 'position']\n",
    "\n",
    "def tag_dictionary(element, secondary, default_tag_type):\n",
    "    new = {}\n",
    "    new['id'] = element.attrib['id']\n",
    "    if \":\" not in secondary.attrib['k']:\n",
    "        new['key'] = secondary.attrib['k']\n",
    "        new['type'] = 'regular'\n",
    "    else:\n",
    "        after_colon = secondary.attrib['k'].index(\":\") + 1\n",
    "        new['key'] = secondary.attrib['k'][after_colon:]\n",
    "        new['type'] = secondary.attrib['k'][:after_colon - 1]\n",
    "    \n",
    "    value = secondary.attrib['v']\n",
    "    \n",
    "    if secondary.attrib['k'].startswith('addr:') == 1 and secondary.attrib['k'].count(':') < 2:\n",
    "        field = secondary.attrib['k'][5:]\n",
    "        if field == 'street':\n",
    "            value = updateStreetNames.update_street(secondary.attrib['v'],mapping)\n",
    "        elif field == 'postcode':\n",
    "            value = zipCodes.update_zip(secondary.attrib['v'])\n",
    "    \n",
    "    if isinstance(value, str):\n",
    "        new['value'] = value\n",
    "    else:\n",
    "        new['value'] = str(value)\n",
    "\n",
    "    return new\n",
    "\n",
    "def shape_element(element, node_attr_fields=NODE_FIELDS, way_attr_fields=WAY_FIELDS,\n",
    "                  problem_chars=PROBLEMCHARS, default_tag_type='regular'):\n",
    "\n",
    "    node_attribs = {}\n",
    "    way_attribs = {}\n",
    "    way_nodes = []\n",
    "    tags = []  # Handle secondary tags the same way for both node and way elements\n",
    "\n",
    "    if element.tag == 'node':\n",
    "        for name, value in element.attrib.items():\n",
    "            if name in node_attr_fields:\n",
    "                node_attribs[name] = value\n",
    "\n",
    "        for secondary in element.iter():\n",
    "            if secondary.tag == 'tag':\n",
    "                if problem_chars.match(secondary.attrib['k']) is not None:\n",
    "                    continue\n",
    "                else:\n",
    "                    new_dict = tag_dictionary(element, secondary, default_tag_type)\n",
    "                    if new_dict is not None:\n",
    "                        tags.append(new_dict)\n",
    "        return {'node': node_attribs, 'node_tags': tags}\n",
    "\n",
    "    elif element.tag == 'way':\n",
    "        for name, value in element.attrib.items():\n",
    "            if name in way_attr_fields:\n",
    "                way_attribs[name] = value\n",
    "\n",
    "        counter = 0\n",
    "        for secondary in element.iter():\n",
    "            if secondary.tag == 'tag':\n",
    "                if problem_chars.match(secondary.attrib['k']) is not None:\n",
    "                    continue\n",
    "                else:\n",
    "                    new_dict = tag_dictionary(element, secondary, default_tag_type)\n",
    "                    if new_dict is not None:\n",
    "                        tags.append(new_dict)\n",
    "            elif secondary.tag == 'nd':\n",
    "                newnd = {}\n",
    "                newnd['id'] = element.attrib['id']\n",
    "                newnd['node_id'] = secondary.attrib['ref']\n",
    "                newnd['position'] = counter\n",
    "                counter += 1\n",
    "                way_nodes.append(newnd)\n",
    "        return {'way': way_attribs, 'way_nodes': way_nodes, 'way_tags': tags}\n",
    "\n",
    " \n",
    "\n",
    " # ================================================== #\n",
    "#               Helper Functions                     #\n",
    "# ================================================== #\n",
    "def get_element(osm_file, tags=('node', 'way', 'relation')):\n",
    "\n",
    "\n",
    "    context = ET.iterparse(osm_file, events=('start', 'end'))\n",
    "    _, root = next(context)\n",
    "    for event, elem in context:\n",
    "        if event == 'end' and elem.tag in tags:\n",
    "            yield elem\n",
    "            root.clear()\n",
    "\n",
    "\n",
    "def validate_element(element, validator, schema=SCHEMA):\n",
    "\n",
    "    if validator.validate(element, schema) is not True:\n",
    "        field, errors = next(validator.errors.items())\n",
    "        message_string = \"\\nElement of type '{0}' has the following errors:\\n{1}\"\n",
    "        error_strings = (\n",
    "            \"{0}: {1}\".format(k, v if isinstance(v, str) else \", \".join(v))\n",
    "            for k, v in errors.items()\n",
    "        )\n",
    "        raise cerberus.ValidationError(\n",
    "            message_string.format(field, \"\\n\".join(error_strings))\n",
    "        )\n",
    "\n",
    "\n",
    "class UnicodeDictWriter(csv.DictWriter, object):\n",
    "\n",
    "    def writerow(self, row):\n",
    "        super(UnicodeDictWriter, self).writerow({\n",
    "            k: (v.encode('utf-8') if isinstance(v, unicode) else v) for k, v in row.items()\n",
    "        })\n",
    "\n",
    "    def writerows(self, rows):\n",
    "        for row in rows:\n",
    "            self.writerow(row)\n",
    "\n",
    "\n",
    "# ================================================== #\n",
    "#               Main Function                        #\n",
    "# ================================================== #\n",
    "def process_map(file_in, validate=False):\n",
    "    \n",
    "    with open(NODES_PATH, 'wb') as nodes_file, \\\n",
    "         open(NODE_TAGS_PATH, 'wb') as nodes_tags_file, \\\n",
    "         open(WAYS_PATH, 'wb') as ways_file, \\\n",
    "         open(WAY_NODES_PATH, 'wb') as way_nodes_file, \\\n",
    "         open(WAY_TAGS_PATH, 'wb') as way_tags_file:\n",
    "\n",
    "        nodes_writer = unicodecsv.DictWriter(nodes_file, NODE_FIELDS)\n",
    "        node_tags_writer = unicodecsv.DictWriter(nodes_tags_file, NODE_TAGS_FIELDS)\n",
    "        ways_writer = unicodecsv.DictWriter(ways_file, WAY_FIELDS)\n",
    "        way_nodes_writer = unicodecsv.DictWriter(way_nodes_file, WAY_NODES_FIELDS)\n",
    "        way_tags_writer = unicodecsv.DictWriter(way_tags_file, WAY_TAGS_FIELDS)\n",
    "\n",
    "        nodes_writer.writeheader()\n",
    "        node_tags_writer.writeheader()\n",
    "        ways_writer.writeheader()\n",
    "        way_nodes_writer.writeheader()\n",
    "        way_tags_writer.writeheader()\n",
    "\n",
    "        validator = cerberus.Validator()\n",
    "\n",
    "        for element in get_element(file_in, tags=('node', 'way')):\n",
    "            el = shape_element(element)\n",
    "            if el:\n",
    "                if validate is True:\n",
    "                    validate_element(el, validator)\n",
    "\n",
    "                if element.tag == 'node':\n",
    "                    nodes_writer.writerow(el['node'])\n",
    "                    node_tags_writer.writerows(el['node_tags'])\n",
    "                elif element.tag == 'way':\n",
    "                    ways_writer.writerow(el['way'])\n",
    "                    way_nodes_writer.writerows(el['way_nodes'])\n",
    "                    way_tags_writer.writerows(el['way_tags'])\n",
    "    \n",
    "process_map(datafile, validate=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [default]",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
