
# Workspace Toos

# Create a repeatable repository development process
```
local      Initialize
             |
           Clone
             |
           Branch <--------------- +
             |                     ^
           Code <------------ +    |
             |                |    | 
           Rebase --------- > +    |
             |                     |
           (push)                  |  
             .                     .
GitHub       .                     .
             .                     .
           Pull-Request            ^
             |                     |
           Merge                   |
             |                     | 
             + ------------------> +
```

* Organization is the common name of repository owner 
* Workspace is the name of a group of repositories
* Project is the name of the repository
* Branches is the name of current repository branch

## Using workspace tools
* clone ws_workspace


## What Install.py Does
* Creates development-folder "~/Development" when not found
* Creates organization-folder "~/Development/<Organization>" when not found
* Creates workspace-folder "~/Development/<Organization>/<Workspace>" when not found
* Creates project-folder "~/Development/<Organization>/<Workspace>/<Repository>" when not found
* Creates script-folder "~/Development/<Organization>/<Workspace>/<Repository>/scripts" when not found

* Installs bash scripts in develpment-folder "~/Development"
* Installs python scripts in lib-folder "~/Development/_tools/lib"
* Installs bash scripts in "~/Development/_tools/scripts"
* Clones GitHub repository <Project> in "~/Development/<Organization>/<Workspace>/<Project>"
* Installs bash scripts into <Project> "~/Development/<Organization>/<Workspace>/<Project>/scripts"
* Checks out a repository branch <Branch>

## Tools run from 
* install location is ~/Development/_tools
* run install script to install tools

* git.branch.sh installs in ~/Development/_tools
* 

## Development Folder
+ <USER>
  + Development
    + <Organization>
        + <Workspace>
            + <Project>
            + ...
  
Fix
* have git.branch.sh put .env in <project>/scripts
* have git.rebase.sh initialize from <project>/scripts/.env