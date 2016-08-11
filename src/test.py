#!/usr/bin/python2
# coding=utf-8
from marxeDownloader import MarxeDownloader


# Parametros
host = 'cdaweb.gsfc.nasa.gov'
instument = 'hope'
nivel = 'l2'
sonda = 'rbspa'
sonda = 'a'
data = '2014-12-31'

working_directory = 'pub/data/rbsp/rbspa/l2/ect/hope/sci/rel03/2014/'
filename = 'rbspa_rel03_ect-hope-sci-l2_20141231_v5.0.0.cdf'
listFilename = ['rbspa_rel03_ect-hope-sci-l2_20140101_v5.0.0.cdf', 'rbspa_rel03_ect-hope-sci-l2_20140102_v5.0.0.cdf']

# Creating a instance of MarxéDownloader
mx = MarxeDownloader(host)

# Connecting
mx.connect()

# Set Output Directory
mx.set_output_directory('output/')

# Set FTP directory to download
mx.set_directory(working_directory)


# Download One Data
mx.download_one_data(filename)
# Download Many Data
mx.download_many_data(listFilename)

# Close Connection
mx.close()
