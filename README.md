# Wrangle-OpenStreetMap-Data

The goal of this project was to use data munging techniques, such as assessing the quality of the data for validity, accuracy, completeness, consistency and uniformity, to clean the OpenStreetMap data for Pierce County, WI.

#### Objectives:
- Assess the quality of the data for validity, accuracy, completeness, consistency and uniformity.
- Parse and gather data from popular file formats such as .csv, .json, .xml, and .html
- Process data from multiple files or very large files that can be cleaned programmatically.
- Learn how to store, query, and aggregate data using SQL.

### Files in this Project

#### identifyTags.py 
- Used to identify the tags that are used in the datafile

#### auditingK.py
- Looks for tags with only lowercase letters, lowercase letters separated by a colon, and problem characters

#### uniqueUsers.py
- Determines how many unique users contributed to the dataset

#### streetTypes.py
- Compares values in the datafile to my expected list
- Updates the values to match identified standards

#### zipCodes.py
- Creates a dictionary of zip codes that were in an invalid format
- Updates the zip codes to the proper format

#### sqlPrep.py
- Parses the XML data and converts it into tabular format into CSV files
