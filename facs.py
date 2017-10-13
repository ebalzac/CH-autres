
# coding: utf-8


import sys
import os
import fnmatch
from bs4 import BeautifulSoup as soup
import re


path=input('Entrez le chemin de votre dossier source avec "/" final et sans guillemets\n')
for idx, fileTemp in enumerate(fnmatch.filter(os.listdir(path), '*.xml')):
    fileTemp=fileTemp.replace("/",":")
    tei = open(path+fileTemp).read()
    print("\n"+fileTemp)
    xmlSoup = soup(tei,"xml")
    
    for idx,elem in enumerate(xmlSoup.find_all('pb',attrs={"facs":True})):
        tmpFac=elem["facs"]
        match=re.search(r"f[0-9#]+",tmpFac)
        page=match.group()[1:]
        if idx==0:
            indexPage=int(page)
            facs=tmpFac
        if idx>0:
            facs=re.sub(r"f[0-9#]+","f"+str(indexPage+idx),tmpFac)
        elem["facs"]=facs
    
    f = open('/home/odysseus/Bureau/maxime/'+fileTemp, 'w')
    f.write(xmlSoup.prettify())
    f.close()     
    print("Fait pour le fichier "+fileTemp)

