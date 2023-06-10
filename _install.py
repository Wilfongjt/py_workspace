import os
import shutil
from _functions import prompt, createFolder, \
                       TextFileHelper, getFileList
#class Installer():
#    def __init__(self):
#        self.dstFolder=
#        self.srcFolder=
#        # fail when _function.py found in ~/Development/_scripts
#        self.srcFolder = os.getcwd()
#        print('srcFolder')
#        self.dstFolder = '{}/Development/_tools'.format(os.path.expanduser('~'))

def main():
    # fail when _function.py found in ~/Development/_scripts
    srcFolder = os.getcwd()
    print('srcFolder')
    dstFolder = '{}/Development/_tools'.format(os.path.expanduser('~'))
    # create folder when NF
    print('* install _tools at', dstFolder)
    createFolder(dstFolder)
    # switch to _tools folder
    #os.chdir(dstFolder)

    # copy _functions.py to ~/Developement/_scripts
    #print('* copy _functions.py')

    pythonFileNames = getFileList(srcFolder, ext='py')
    for pfn in pythonFileNames:
        srcFile = pfn
        dstFile = pfn
        src = '{}/{}'.format(srcFolder, srcFile)
        dst = '{}/{}'.format(dstFolder, dstFile)
        if pfn != '_install.py':
            print('* copy {} to {}'.format(src,dst))
            TextFileHelper(srcFolder, srcFile)\
                    .copyTo(dstFolder, dstFile)

if __name__ == "__main__":
    # execute as script
    main()