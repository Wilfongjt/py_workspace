import os
import shutil
from _functions import prompt, createFolder, getFileList
from __text_file_helper import TextFileHelper
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
    # create folders when folders NF
    # copy when
    srcFolder = os.getcwd()
    print('srcFolder')
    dstFolder = '{}/Development/_tools'.format(os.path.expanduser('~'))

    # create folder when NF
    print('* install _tools at', dstFolder)
    createFolder(dstFolder)

    # copy _functions.py to ~/Developement/_scripts
    exts = ['py','sh']
    for ext in exts:
        pythonFileNames = getFileList(srcFolder, ext=ext)
        for pfn in pythonFileNames:
            srcFile = pfn
            dstFile = pfn
            src = '{}/{}'.format(srcFolder, srcFile)
            dst = '{}/{}'.format(dstFolder, dstFile)
            if pfn != 'install.py':
                print('* copy {} to {}'.format(src,dst))
                TextFileHelper(srcFolder, srcFile)\
                        .copyTo(dstFolder, dstFile)
                if dstFile.endswith('.sh'):
                    command = 'chmod 777 {}/{}'.format(dstFolder,dstFile)
                    os.system(command)

if __name__ == "__main__":
    # execute as script
    main()