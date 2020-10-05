import glob
from pathlib import Path
from read_xml_bsoup import read_xml_bsoup

import os
from os import listdir
from os.path import isfile, join

from create_page import create_page
from read_xml_bsoup import read_xml_bsoup


xmlfiles_path = "./SARIT-corpus-master"
# onlyfiles = [f

exclude_list = set(["00-sarit-tei-header-template.xml"])

for file in glob.glob("./SARIT-corpus-master/*.xml"):
    if isfile(file) and os.path.basename(file) not in exclude_list:
        print(os.path.basename(file))
        title, content = read_xml_bsoup(file)
        print(title)
        print(content)
        # create_page(title, content)
