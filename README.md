
# Maintaining a Consistant Development Environment

I've never had good luck keeping my development environment consistant from project to project. 
The inconsistancy has lead to many wasted hours trying to reinvent my development process. 
This repo is my attempt to formalize my development environment.

## Contents
* Goal
* Strategy
* Definitions
* Point of View
* Installation
  * Dependencies
  * Repository Installation
  * Tool Installation
* Usage
  * install.py
  * git.ws.sh
  * git.rebase.sh
  * bk.sh
* Documentation
  * install.py
  * git.branch.py
  * git.rebase.py
  * bk.sh
## Goal: 
Write more code and stop wasting time on bookkeeping stuff.
* 
## Strategy:
* Use scripts to create and maintain development folders.
* Use scripts to retrieve and update repositories.
* Use scripts to backup and restore files.

## Definitions
* __\<GH_ACCOUNT>__ is a specific github account.
* __Remote Source__ is the py_workspace repository on GitHub.
* __Source__ is the py_workspace repository.
* __Developement__ is the name of the folder where I put all my code.
* __Organization__ is a person or a client. 
* __\<ORGANIZATION>__ is a specific organization (no spaces).
* __Workspace__ is a group of projects.
* __\<WORKSPACE>__ is a specific workspace (no spaces).
* __Project__ is a repository.
* __\<PROJECT>__ is a specific repository (no spaces).
* __Branch__ is the name of current repository branch.

## Point of View
* As a developer, I can write code for myself, an organization, or many organizations.
* An organization can have one or more workspaces
* A workspace can have one or more projects
* A project is a repository
* As a developer, I forget things, so keep track of the organizations, workspaces, projects and branches.
* As a developer, scripts help me maintain consistancy.

## Installation
### Dependencies
#### Python 3
1. Install Python 3

### The Repository Installation
Install the Installer  

#### Tasks and Commands
1. Open a command window

1. Navigate to your home folder, eg cd ~/
    ```commandline
    cd ~
    ```
1. Create one folder to store all development ... aka the development folder
    ```commandline
    mkdir Development/
    ```
1. Create an organization ... aka the organization folder
    ```commandline
    cd Development/
    mkdir <ORGANIZATION>/
    ```
1. Create a workspace ... aka the workspace folder
    ```commandline
    cd <ORGANIZATION>/
    mkdir <WORKSPACE>/
    ```
1. Clone ws_workspace ... aka create a project folder
    ```commandline
    cd <WORKSPACE>/
    git clone  https://github.com/<<GH_ACCOUNT>>/<PROJECT>.git
    cd <PROJECT>/
    ```
### Tools Installation
1. Open a command window

1. Run the Tool Install script
   ```commandline
   cd ~/<ORGANIZATION>/<WORKSPACE>/py_workspace/
   python3 install.py
   ```

# Usage

* Create new organization, workspace, and project folders
* Add scripts to project to download and upload github changes

## Install.py Tools
 
 To use the tools, you must install them on your computer.
 
 1. __Clone py_workspace__
 
      * Navigate to the py_workspace clone folder
      * from the command line: python3 install.py
      * Install.py does the following:
 
1. __Initialize Application Folders__
 
      * Create tools folder when folder is not found, eg ~/<<GH_ACCOUNT>>/Development/_tools
      * Create bash script folder when folder is not found, eg ~/<<GH_ACCOUNT>>/Development/_tools/scripts
      * Create python library folder when folder is not found, eg ~/<<GH_ACCOUNT>>/Development/_tools/lib

1. __Initialize Environment__
 
      * Create .env file when environment file is not found, ~/<<GH_ACCOUNT>>/Development/_tools/.env

1. __Install Bash Scripts__
 
      * Copy Tool Scripts to when "_tools/" exists
      * Copy Project Scripts when "_tool/scripts" exists

1. __Install Python Scripts__
 
      * Copy Python lib Scripts when "_tools/lib" folder exists

## Installation

```
   + _tools
      - git.ws.sh
      - .env
      + scripts
         - bk.sh
         - git.branch.sh
         - git.rebase.sh
      + lib
         - __recorder.py
         - _functions.py
         - trunk.py
         - git.branch.py
         - __text_file_helper.py
         - __dev_env.py
         - git.rebase.py
```

# Branch Process
 
1. __Initialize Environment__
 
      * Create default environment file When .env not found
 
      * Open enviroment file When found in <SOURCE> folder
 
1. __Collect and Define Inputs__
 
      * Confirm and Update Inputs with User
 
      * Imput WS_WORKSPACE URI eg ~/Development/<WS_ORGANIZATION>/<WS_WORKSPACE>
 
      * Imput remote repo URL eg https://github.com/<GH_USER>/<GH_PROJECT>.git
 
1. __Validate Inputs__
 
      * Stop When workspace ('WS_') settings are invalid
 
      * Stop When GitHub ('GH_') settings are invalid
 
      * Stop When remote repo is not found
 
1. __Setup for Develpment__
 
      * Create Workspace folder When folder doesnt exist
 
      * Load settings into environment variables
 
      * Save environment to .env file in py_workspace folder
 
      * Clone the repository (aka Project) When repository is not cloned
 
      * CHECKOUT branch ... get ready for development
 
1. __Install Utility Scripts__
 
      * Create scripts folder in repository clone eg <PROJECT>/scripts
 
      * Copy _tools/scripts/*.sh to <PROJECT>/scripts
 
      * Save environment to <PROJECT>/scripts
# Code
#  class Comments(list)
 
Given a folder and filename, Open and read the comment line in the file.
 
__Open and Load a given file on request.__ 
 
* process line when line starts with "class"
* process line when line is double comment... eg "##"
 
__Convert comments to markdown on request__ 
 
* markdown is bold when "on request" is found
* markdown is list item when "when" is found
* markdown is H1 when "# class" is found
* markdown is normal when line is # unknown

## git.branch

## git.rebase

