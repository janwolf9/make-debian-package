#!/usr/bin/python3
import sys
import os

package_name = sys.argv[1]
script_name = sys.argv[2]

def writecontrolfile():
    f=open(""+ package_name +"/DEBIAN/control", "w")
    f.write("Package: "+ package_name +" \nVersion: 1.4.2 \nArchitecture: all \nEssential: no \nSection: web \nPriority: optional \nDepends: python (>=2.3) \nMaintainer: Jan Wolf \nInstalled-Size: 96 \nDescription: The Server Density monitoring agent.\n")

os.system("mkdir "+ package_name +" && mkdir "+ package_name +"/DEBIAN")
os.system("mkdir -p "+ package_name +"/usr/local/bin")
os.system("cp "+ script_name +" "+package_name+"/usr/local/bin/")

writecontrolfile()

os.system("dpkg-deb --build "+ package_name +"")