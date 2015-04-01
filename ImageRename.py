import os
import sys

dirPath = "."
defaultPrefixString = "MyCam_"

def renameFiles(prefixString):
    if not prefixString:
        prefixString = defaultPrefixString
    files = os.listdir(dirPath)
    files.remove("ImageRename.py")
    for fileName in files:
        if os.path.isfile(fileName):
            newFileName = prefixString + fileName
            print "Renameing %s to %s." % (fileName, newFileName)
            os.rename(fileName, newFileName)

if __name__ == "__main__":
    try:
        prefixString = sys.argv[1]
        renameFiles(prefixString)
    except IndexError:
        renameFiles("")

