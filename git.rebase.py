import os
import subprocess
from _functions import prompt, get_env_value, verify,createFolder,\
                hasRemoteProject,isCloned,getCurrentBranch
from dev_env import DevEnv
from _functions import prompt, get_env_value, verify,\
                hasRemoteProject, isCloned, getCurrentBranch, folder_exists,\
                getDevelopment,getOrganization,getWorkspace,getProject

def getParameterPrompts():
    return {
        'WS_ORGANIZATION': prompt('WS_ORGANIZATION', get_env_value('WS_ORGANIZATION')),
        'WS_WORKSPACE': prompt('WS_WORKSPACE', get_env_value('WS_WORKSPACE')),
        'GH_USER': prompt('GH_USER', get_env_value('GH_USER')),
        'GH_PROJECT': prompt('GH_PROJECT',get_env_value('GH_PROJECT')),
        'GH_BRANCH': prompt('GH_BRANCH', get_env_value('GH_BRANCH')),
        'GH_MESSAGE': prompt('GH_MESSAGE', get_env_value('GH_MESSAGE'))
    }

def main():
    devEnv = DevEnv().open() # needed for prompts

    devfolder = os.path.expanduser('~')
    # WS_ prefix indicates a path part eg ~/Development/<WS_ORGANIZATION>/<WS_WORKSPACE>
    #prompts = {
    #    'WS_ORGANIZATION': prompt('WS_ORGANIZATION', get_env_value('WS_ORGANIZATION')),
    #    'WS_WORKSPACE': prompt('WS_WORKSPACE', get_env_value('WS_WORKSPACE')),
    #    'GH_USER': prompt('GH_USER', get_env_value('GH_USER')),
    #    'GH_PROJECT': prompt('GH_PROJECT',get_env_value('GH_PROJECT')),
    #    'GH_BRANCH': prompt('GH_BRANCH', get_env_value('GH_BRANCH')),
    #}
    prompts = getParameterPrompts()

    #
    # Stop when path related items 'WS_' are invalid
    #
    if not verify(prompts, prefix='WS_'): #
        print('Stop...Invalid WS value found')
        exit(0)
    #
    # Stop when path related items 'GH_' are invalid
    #
    if not verify(prompts, prefix='GH_'):  #
        print(prompts)
        print('Stop...Invalid GH value found')
        exit(0)

    print('Development', getDevelopment())
    print('Organization', getOrganization())
    print('Workspace', getWorkspace())
    print('Project', getProject())
    #
    # confirm development folder
    #     ~/Development
    folder = os.getcwd().replace('/_scripts', '')
    print('* checking folder {} '.format(folder), end='')
    if not folder_exists(folder):
        print('stopping...development not found')
        exit(0)
    print('ok')
    #
    # Switch to development folder
    #
    os.chdir(folder)
    #
    # confirm organization folder
    #     ~/Development/<WS_ORGANIZATION>
    # folder = '{}/{}'.format(os.getcwd().replace('/_scripts', '/{}'.format(prompts['WS_ORGANIZATION'])))
    folder = '{}/{}'.format(folder,prompts['WS_ORGANIZATION'])
    print('* checking folder {} '.format(folder), end='')
    if not folder_exists(folder):
        print('stopping...organization not found')
        exit(0)
    print('ok')
    #
    # Switch to organization folder
    #
    os.chdir(folder)
    #
    # confirm workspace folder
    #     ~/Development/<WS_ORGANIZATION>/<WS_WORKSPACE>
    folder = '{}/{}'.format(os.getcwd().replace('/_scripts','/{}'.format(prompts['WS_ORGANIZATION'])), prompts['WS_WORKSPACE'])
    print('* checking folder {} '.format(folder), end='')
    if not folder_exists(folder):
        print('stopping...workspace not found')
        exit(0)
    print('ok')
    #
    # confirm project folder
    #     ~/Development/<WS_ORGANIZATION>/<WS_WORKSPACE>/<GH_PROJECT>
    folder = '{}/{}/{}'.format(os.getcwd().replace('/_scripts','/{}'.format(prompts['WS_ORGANIZATION'])), prompts['WS_WORKSPACE'],prompts['GH_PROJECT'])
    print('* checking folder {} '.format(folder), end='')
    if not folder_exists(folder):
        print('stopping...project/repo not found')
        exit(0)
    print('ok')
    #
    # check for project repo
    #
    url = 'https://github.com/{}/{}.git'.format(prompts['GH_USER'], prompts['GH_PROJECT'])
    print('* checking for project repo', url, end='')
    #
    # Fail when remote repo NF
    #
    if not hasRemoteProject(url):
        print('Stop...Repo doenst exist')
        exit(0)
    print(' ok')
    #
    # Switch to repo folder
    #
    os.chdir(folder)
    print('* Switch to ', folder)
    #
    # confirm branch
    #
    if getCurrentBranch(folder) == 'main':
        print('stopping... commit to "main" branch not allowed!')
        exit(0)

    if getCurrentBranch(folder) != prompts['GH_BRANCH']:
        print('stopping... branch not found {} how about {}'.format(prompts['GH_BRANCH'], getCurrentBranch(folder)))
        exit(0)

    print('* current branch', getCurrentBranch(folder))

    # checkout branch
    command = 'git checkout {}'.format(prompts['GH_BRANCH'])
    os.system(command)
    # add
    os.system('git add .')
    # commit
    command = 'git commit -m {}'.format(prompts['GH_MESSAGE'])
    os.system(command)
    # checkout main
    os.system('git checkout main')
    # pull origin main
    os.system('git pull origin main')
    # checkout branch
    command = 'git checkout {}'.format(prompts['GH_BRANCH'])
    os.system(command)
    # feedback
    os.system('git branch')
    # rebase
    command = 'git rebase {}'.format(prompts['GH_BRANCH'])
    os.system(command)
    if prompt('PUSH?', 'N') not in ['N','n']:
        command = 'git push origin {}'.format(prompts['GH_BRANCH'])
        os.system(command)

    print('* update environment')
    devEnv.upsert(prompts)
    print('* save .env')
    devEnv.save()

    print('open browser')
    command = 'open -a safari "https://github.com/{}/{}"'.format(prompts['GH_USER'], prompts['GH_PROJECT'])
    os.system(command)
    os.system('git status')

if __name__ == "__main__":
    # execute as script
    main()
