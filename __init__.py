#!/usr/bin/env python3


import fileinput
import os


with open("fechas.txt") as file_in:
    lines = []
    for line in file_in:
        line = line.replace("\n", "")
        lines.append(line)

for linea in lines:

    with fileinput.FileInput("example.xml", inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace("REPLACE_ME", linea), end='')
    nombre= linea.replace(":", "=")
    os.rename('example.xml', '%s.xml' % nombre)
    os.rename('example.xml.bak', 'example.xml')
    print("%s creado" % nombre)
    