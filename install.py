import settings

import os
from lib._functions import createFolder, getFileList
from lib.__text_file_helper import TextFileHelper
#class Installer():
#    def __init__(self):
#        self.dstFolder=
#        self.srcFolder=
#        # fail when _function.py found in ~/Development/_scripts
#        self.srcFolder = os.getcwd()
#        print('srcFolder')
#        self.dstFolder = '{}/Development/_tools'.format(os.path.expanduser('~'))
#def file_exists(folder, filename):
#    exists = os.path.isfile('{}/{}'.format(folder, filename))
#    return exists

def main():

    # fail when _function.py found in ~/Development/_scripts
    # create folders when folders NF
    # copy when
    srcFolder = os.getcwd()
    srcLibFolder = '{}/lib'.format(srcFolder)
    srcScrptFolder = '{}/scripts'.format(srcFolder)
    print('srcFolder')
    #   + <USER>
    #       + Development
    #           + _tools
    #               + lib

    dstFolder = '{}/Development/_tools'.format(os.path.expanduser('~'))
    dstLibFolder = '{}/lib'.format(dstFolder)
    dstScrptFolder = '{}/scripts'.format(dstFolder)

    # create folder when NF
    print('* install _tools at', dstFolder)
    print('* install python library at', dstLibFolder)
    print('* install python scripts at', dstScrptFolder)

    createFolder(dstLibFolder)
    createFolder(dstScrptFolder)
    #
    # lib
    # /Development/lyttlebit/00_tools/py_workspace/lib

    src_folder = '{}/lib'.format(srcFolder)
    dst_folder = '{}/lib'.format(dstFolder)
    fileNames = getFileList(src_folder, ext='py')
    for fn in fileNames:
        srcFn = fn
        dstFn = fn
        print('* copy {} to {}'.format(srcFn, dstFn))

        TextFileHelper(src_folder, srcFn) \
            .copyTo(dst_folder, dstFn)
    #
    # scripts
    # /Development/lyttlebit/00_tools/py_workspace/scripts

    src_folder = '{}/scripts'.format(srcFolder)
    dst_folder = '{}/scripts'.format(dstFolder)
    fileNames = getFileList(src_folder, ext='sh')
    for fn in fileNames:
        srcFn = fn
        dstFn = fn
        print('* copy {} to {}'.format(srcFn, dstFn))

        TextFileHelper(src_folder, srcFn) \
            .copyTo(dst_folder, dstFn)
    #
    # scripts
    # /Development/lyttlebit/00_tools/py_workspace
    src_folder = srcFolder
    dst_folder = dstFolder
    fileNames = getFileList(src_folder, ext='sh')
    for fn in fileNames:
        srcFn = fn
        dstFn = fn
        print('* copy {} to {}'.format(srcFn, dstFn))

        TextFileHelper(src_folder, srcFn) \
            .copyTo(dst_folder, dstFn)

    exit(0)
    # copy *.py to ~/Developement/_tools/lib
    # copy *.sh to ~/Developement/_tools
    '''
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
    '''
if __name__ == "__main__":
    # execute as script
    main()