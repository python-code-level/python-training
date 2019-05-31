GitHub account setup
====================

Personl account
~~~~~~~~~~~~~~~

Notes on set up of GitHub accounts to ensure commits are from private / personal account for training or personal projects


Several sets of GitHub acounts and ssh keys can be used on a single machine

ssh keys should not be moved or shared between machines

This note is for the situation where a single repo will be associated with one developer account 
(there is no need to switch between personal and professional accounts)

This is achieved by noting the different global and local git config settings

Firstly in GitHub personal account settings / emails / untick the box "Keep my email address private"

Verify the global git user settings - this si most likely the professional work account


Then check the local (per repo) user settings

These are found at:

These can then be set with 




After any commit, use this command to verify the user and email address associated with the commit

```
git log
```

::
git log

``code test``

**bold**




