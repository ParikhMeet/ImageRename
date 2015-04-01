import os

dirPath = "."
prefixString = "MyCam_"

def renameFiles():
    files = os.listdir(dirPath)
    files.remove("ImageRename.py")
    for fileName in files:
        if os.path.isfile(fileName):
            newFileName = prefixString + fileName
            print "Renameing %s to %s." % (fileName, newFileName)
            os.rename(fileName, newFileName)

if __name__ == "__main__":
    renameFiles()
