#!/usr/bin/python

import os.path
import sys
import grass.script as grass

class directoryReader (object):
    
    def ReadFiles (self, directory, extension):
        if (os.path.exists(directory)) :
            if (os.path.isdir(directory)) :
                fileList = os.listdir(directory)
                for fileName in fileList :
#                  if (os.path.isdir(os.path.join(directory,fileName))) :
                      
                  if (os.path.isfile(os.path.join(directory,fileName))) :
                      if (fileName[-3:] == extension) :
                          print os.path.join(directory, fileName)
                          grass.run_command("r.in.gdal", flags='o', overwrite=True, input=fileName, output=fileName + ".test")

    def run(self):
        dir = sys.argv[1]
        ext = sys.argv[2]
        self.ReadFiles(dir, ext)

if __name__ == '__main__':
    obj = directoryReader()
    obj.run()
