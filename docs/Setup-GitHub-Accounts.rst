GitHub account setup
====================

Personal account
~~~~~~~~~~~~~~~~

**Using Git commands**  [#]

Notes on set up of GitHub accounts to ensure commits are from private / personal account for training or personal projects

- Several sets of GitHub acounts and ssh keys can be used on a single machine

- ssh keys should not be moved or shared between machines

This note is for the situation where a single repo will be associated with one developer account 
(there is no need to switch between personal and professional accounts)

This is achieved by noting the different global and local git config settings

Firstly in GitHub personal account settings / emails / untick the box "Keep my email address private"

Verify the global git user settings - this is most likely the professional work account:

``git config --global --list``

This shows the user that is globally associated with this machine and th ecurrently logged in user account

If no config has been set it can be configured via a text editor, prompted via:

``git config --global --edit``

Typically for personal or training use an alternative GitHub account is linked to a specific repo. 

Within the target repo check any current config files:

``git config --local --list``

This lists the user setings associated within the current repo. These files are located at:

.git/config

If the user sectino is missing, or to set the user to an alternative account:

``git config user.name "python training"``
``git config user.email "python-training@outlook.com"``

Setting user details at the local repo level overrides the global settings.

To test that the correct user credential are being applied in a given situation. Create or modify a file within the repo. Git add and git commit the file.  

After any commit, the following command can be used to verify the user and email address associated with the commit:

`` git log ``

.. prompt:: bash
    git log
    cd test

--------------

-- [#note] Git commands apply to both linux and windows command lines
.. [#note] Git commands apply to both linux and windows command lines






