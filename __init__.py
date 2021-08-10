#!/usr/bin/env python3


import fileinput
import os
import shutil

lines = []

initialFiles = 67
quantity = 4
dirName = "filecreator"


if os.path.isdir("./%s" % dirName):
    shutil.rmtree("./%s" % dirName)

os.mkdir("./%s" % dirName)

shutil.copyfile('example.xml', 'example.xml.bak')


for linea in range(1, (initialFiles*quantity)):

    with fileinput.FileInput("example.xml", inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace("REPLACE_ME", str(linea)), end='')
    nombre = str(linea)
    os.rename('example.xml', './%s/%s.xml' % (dirName, nombre))
    shutil.copyfile('example.xml.bak', 'example.xml')
    print("%s creado" % nombre)
