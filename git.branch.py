import os
import subprocess
from _functions import prompt, get_env_value, verify,createFolder,\
                hasRemoteProject,isCloned,getCurrentBranch, folder_exists
from _dev_env import DevEnv
def getParameterPrompts():
    return {
        'WS_ORGANIZATION': prompt('WS_ORGANIZATION', get_env_value('WS_ORGANIZATION')),
        'WS_WORKSPACE': prompt('WS_WORKSPACE', get_env_value('WS_WORKSPACE')),
        'GH_USER': prompt('GH_USER', get_env_value('GH_USER')),
        'GH_PROJECT': prompt('GH_PROJECT',get_env_value('GH_PROJECT')),
        'GH_BRANCH': prompt('GH_BRANCH', get_env_value('GH_BRANCH')),
    }


def main():
    devEnv = DevEnv().open()
    devfolder = os.path.expanduser('~')
    #print(getFolderNameList(devfolder))

    # WS_ prefix indicates a path part eg ~/Development/<WS_ORGANIZATION>/<WS_WORKSPACE>
    #
    # Get Parameters from Usert
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
    # check for workspace folder
    # ~/Development/<WS_ORGANIZATION>/<WS_WORKSPACE>
    folder = '{}/{}'.format(os.getcwd().replace('/_scripts','/{}'.format(prompts['WS_ORGANIZATION'])), prompts['WS_WORKSPACE'])
    print('* check for workspace folder {} '.format(folder))

    #
    # check for project repo
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
    # Switch to workspace folder
    #
    os.chdir(folder)

    #
    # Clone when local repo NF
    #
    folder = '{}/{}'.format(folder, prompts['GH_PROJECT'])

    if not isCloned(folder):
        print('* cloning...', end='')
        command = 'git clone {}'.format(url)
        os.system(command)

    #
    # Switch to repo folder
    #
    os.chdir(folder)
    print('* switch to ', folder)
    #
    # CHECKOUT branch
    #

    if getCurrentBranch(folder) != prompts['GH_BRANCH']:
        command = 'git checkout -b {}'.format(prompts['GH_BRANCH'])
        print('* command', command, end='')
        os.system(command)
        #print('')

    print('\n* confirm current branch', getCurrentBranch(folder))
    print('* update environment')
    devEnv.upsert(prompts)
    print('* save .env')
    devEnv.save()

if __name__ == "__main__":
    # execute as script
    main()