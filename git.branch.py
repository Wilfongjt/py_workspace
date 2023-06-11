import os
import subprocess
from _functions import prompt, get_env_value, verify,createFolder,\
                hasRemoteProject,isCloned,getCurrentBranch, folder_exists
from __dev_env import DevEnv
from __text_file_helper import TextFileHelper

def getParameterPrompts():
    return {
        'WS_ORGANIZATION': prompt('WS_ORGANIZATION', get_env_value('WS_ORGANIZATION')),
        'WS_WORKSPACE': prompt('WS_WORKSPACE', get_env_value('WS_WORKSPACE')),
        'GH_USER': prompt('GH_USER', get_env_value('GH_USER')),
        'GH_PROJECT': prompt('GH_PROJECT',get_env_value('GH_PROJECT')),
        'GH_BRANCH': prompt('GH_BRANCH', get_env_value('GH_BRANCH')),
    }

def main():
    # Create environment file When NF
    # Open enviroment file When found in current folder

    print('starting folder', os.getcwd())
    devEnv = DevEnv().open()
    devfolder = '{}/Development'.format(os.path.expanduser('~'))
    srcFolder = '{}/Development/_tools'.format(os.path.expanduser('~'))

    #
    # Get Parameterxs from Usert
    #
    prompts = getParameterPrompts()
    #
    # Stop when path related items 'WS_' are invalid
    #
    if not verify(prompts, prefix='WS_'): #
        print(prompts)
        print('Stop...Invalid WS value found')
        exit(0)

    #
    # Stop when path related items 'GH_' are invalid
    #
    if not verify(prompts, prefix='GH_'):  #
        print(prompts)
        print('Stop...Invalid GH value found')
        exit(0)

    #
    # check for WS_WORKSPACE folder ~/Development/<WS_ORGANIZATION>/<WS_WORKSPACE>
    #
    folder = '{}/{}/{}'.format(devfolder, prompts['WS_ORGANIZATION'], prompts['WS_WORKSPACE'])
    print('* check for workspace folder {} '.format(folder))

    # wsEnv = DevEnv(folder=folder, filename='{}.env'.format(prompts['GH_PROJECT'])).open()

    #
    # check for GH_PROJECT repo https://github.com/<GH_USER>/<GH_PROJECT>.git
    #
    url = 'https://github.com/{}/{}.git'.format(prompts['GH_USER'], prompts['GH_PROJECT'])
    print('* checking for project repo', url)
    #
    # Fail when remote repo NF
    #
    if not hasRemoteProject(url):
        print('Stop...Repo doenst exist')
        exit(0)

    createFolder(folder)

    #
    # Change environment to match prompts
    #
    devEnv.upsert(prompts)
    print('* save .env')
    devEnv.save()
    #
    # Switch to workspace folder
    #
    print('* switch to workspace ', folder)
    os.chdir(folder)

    #
    # Clone when local repo NF
    #
    folder = '{}/{}'.format(folder, prompts['GH_PROJECT'])

    if not isCloned(folder):
        print('* cloning...', end='')
        command = 'git clone {}'.format(url)
        os.system(command)
    else:
        print('* skipping...clone. "{}" is already cloned.'.format(prompts['GH_PROJECT']))
    #
    # Switch to project/repo folder
    #
    os.chdir(folder)
    print('* switch to project/repo', folder)
    #
    # CHECKOUT branch
    #

    if getCurrentBranch(folder) != prompts['GH_BRANCH']:
        command = 'git checkout -b {}'.format(prompts['GH_BRANCH'])
        print('* command', command, end='')
        os.system(command)
        #print('')
    else:
        print('* skipping...checkout. "{}" is already checked out.'.format(prompts['GH_BRANCH']))

    #
    # create project/repo script folder
    #
    scriptsfolder = '{}/scripts'.format(folder)
    print('* create repo/script folder')
    createFolder(scriptsfolder)
    #
    # copy rebase.sh to repo/scripts
    #
    TextFileHelper(srcFolder, 'git.rebase.sh').copyTo(scriptsfolder,'git.rebase.sh')

    print('\n* confirm current branch', getCurrentBranch(folder))
    print('* update environment')

    #
    # Save environment to project/repo
    #
    #wsEnv = DevEnv(folder=scriptsfolder, filename='{}.env'.format(prompts['GH_PROJECT'])).open().save()
    wsEnv = DevEnv(folder=scriptsfolder, filename='git.rebase.env').open().save()



if __name__ == "__main__":
    # execute as script
    main()