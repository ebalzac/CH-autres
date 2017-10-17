
# coding: utf-8

import sys
import os
import fnmatch
import re
from lxml import etree

path=input('Entrez le chemin de votre dossier source avec "/" final et sans guillemets\n')

ns = {"ns": "http://www.tei-c.org/ns/1.0"}

for idx, fileTemp in enumerate(fnmatch.filter(os.listdir(path), '*.xml')):
    fileTemp=fileTemp.replace("/",":")
    tree = etree.parse(path+fileTemp)
    
    for idx,elem in enumerate(tree.findall('.//ns:pb[@facs]',namespaces=ns)):
        tmpFac=elem.attrib["facs"]
        match=re.search(r"f[0-9#]+",tmpFac)
        page=match.group()[1:]
        if idx==0:
            indexPage=int(page)
            facs=tmpFac
        if idx>0:
            facs=re.sub(r"f[0-9#]+","f"+str(indexPage+idx),tmpFac)
        elem.attrib["facs"]=facs
        
    tree.write(path+fileTemp, xml_declaration=True,encoding='utf-8')
    print("Fait pour le fichier "+fileTemp)

