import os
import subprocess
import webbrowser
from _functions import prompt, get_env_value, verify,createFolder,\
                hasRemoteProject,isCloned,getCurrentBranch
from __dev_env import DevEnv
from _functions import prompt, get_env_value, verify,\
                hasRemoteProject, isCloned, getCurrentBranch, folder_exists,\
                getDevelopment,getOrganization,getWorkspace,getProject, getBranch

def getParameterPrompts():
    return {
        'WS_ORGANIZATION': prompt('WS_ORGANIZATION', getOrganization()),
        'WS_WORKSPACE': prompt('WS_WORKSPACE', getWorkspace()),
        'GH_USER': prompt('GH_USER', get_env_value('GH_USER')),
        'GH_PROJECT': prompt('GH_PROJECT',getProject()),
        'GH_BRANCH': prompt('GH_BRANCH', getBranch()),
        'GH_MESSAGE': prompt('GH_MESSAGE', get_env_value('GH_MESSAGE'))
    }

def main():
    #devEnv = DevEnv().open().show() # needed for prompts

    devfolder = '{}/Development'.format(os.path.expanduser('~'))
    print('Development', getDevelopment())
    print('Organization', getOrganization())
    print('Workspace', getWorkspace())
    print('Project', getProject())
    print('Branch', getBranch())
    #
    # only run from the <gh_project>scripts folder
    #
    print('cwd', os.getcwd())
    if not os.getcwd().endswith('scripts'):
        print('Stopping... Not a project/repo scripts folder.')
        exit(0)

    # WS_ prefix indicates a path part eg ~/Development/<WS_ORGANIZATION>/<WS_WORKSPACE>
    print('folder', devfolder)
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
    #exit(0)
    #
    # Stop when ~/Development NF
    #
    folder = devfolder
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
    # Stop when ~/Development/<WS_ORGANIZATION> NF
    #
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
    # Stop when ~/Development/<WS_ORGANIZATION>/<WS_WORKSPACE> NF
    #
    folder = '{}/{}'.format(folder,prompts['WS_WORKSPACE'])
    print('* checking folder {} '.format(folder), end='')
    if not folder_exists(folder):
        print('stopping...workspace not found')
        exit(0)
    print('ok')
    #
    # Stop when ~/Development/<WS_ORGANIZATION>/<WS_WORKSPACE>/<GH_PROJECT> NF
    #
    folder = '{}/{}'.format(folder,prompts['GH_PROJECT'])
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
    # Fail when branch is TBD or main
    #
    if getBranch() == 'TBD':
        print('stopping...Bad branch')
        exit(0)
    if getBranch() == 'main':
        print('stopping...Cannot use "main" branch')
        exit(0)
    #
    # confirm branch
    #
    if getCurrentBranch(folder) == 'main':
        print('stopping... commit to "main" branch not allowed!')
        exit(0)

    if getCurrentBranch(folder) == 'TBD':
        print('stopping... branch not found {} how about {}'.format(prompts['GH_BRANCH'], getCurrentBranch(folder)))
        exit(0)

    #if getCurrentBranch(folder) != prompts['GH_BRANCH']:
    #    print('stopping... branch not found {} how about {}'.format(prompts['GH_BRANCH'], getCurrentBranch(folder)))
    #    exit(0)

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

    #print('* update environment')
    #devEnv.upsert(prompts)
    #print('* save .env')
    #devEnv.save()

    print('open browser')
    #command = 'open -a safari "https://github.com/{}/{}"'.format(prompts['GH_USER'], prompts['GH_PROJECT'])
    #os.system(command)
    url = "https://github.com/{}/{}".format(prompts['GH_USER'], prompts['GH_PROJECT'])
    #command =['open', '-a', 'safari', url]
    #subprocess.Popen(command)

    os.system('git status')
    print('done')

    # the webbrowser blocks the funtioning of the command window while the browser is open
    webbrowser.get('safari').open(url, new=2)

if __name__ == "__main__":
    # execute as script
    main()
