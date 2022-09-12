# Globus by Example


Examples

* HTTPS 
* Get User ID
* Set ACL

1. [Goal](#tldr)
2. [Globus by Example](#develop-by-examples)
  1. Auth
    1. Get User ID
    2. Creating an App
    3. Creating a Resource Server
    4. Auth Weird Sauce
    5. Listing of the scopes, what they can do, etc. Especially the special scopes
    
  2. Transfer
    1. Submit a Transfer request
    2. HTTPS - recursive upload, download
    3. Set ACL
    4. Transfer with a client credential, or on behalf of a user)
    5. Create the link from the webUI in Python

  3. Search
  4. Flows
  5. Groups
    1. How to check if someone is in a group

* Client credential stored on github
* has requirements.txt, check for compatibility

  6. Timer?




  
  7. Dealing with Client Credentials (e.
  
  11. How to add someone to a group
  12. Search update
  13. How to detect a Globus Connect Personal ID



7. [About Globus](#about-jupyterlab)
8. [Credits](#credits)
9. [Community Guidelines and Code of Conduct](#community-guidelines-and-code-of-conduct)


## TL;DR

The goal of this repository is to show how to develop extensions for [JupyterLab](https://github.com/jupyterlab/jupyterlab), presented as short tutorial series.

To get started:

```bash
# clone the repository
git clone https://github.com/jupyterlab/extension-examples.git jupyterlab-extension-examples

# go to the extension examples folder
cd jupyterlab-extension-examples

# create a new environment
conda env create

# activate the environment
conda activate jupyterlab-extension-examples

# go to the hello world example
cd hello-world

# install the extension in editable mode
python -m pip install -e .

# install your development version of the extension with JupyterLab
jupyter labextension develop . --overwrite

# build the TypeScript source after making changes
jlpm run build

# start JupyterLab
jupyter lab
```
