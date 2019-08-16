# Documentation

Docs are built using Sphinx, making use of a theme from readthedocs.

## Sphinx installation

Using python 3.7 to be consistent with the library requirements, and preferably
using the same virtual environment used to build the library:

```
> pip install sphinx sphinx-rtd-theme sphinxcontrib.youtube
```

## Deploying to Github

Docs are built and deployed to github pages. This uses a special branch 'gh-pages' of the main repository to hold 
compiled HTML generated from Sphinx. To set this up you need to create a checkout of this branch in parallel with the
main repository. From the root of the CVzero git checkout:

```
> cd ..
> mkdir cvzero-pages
> cd cvzero-pages
> git checkout git@github.com:OpenPiRobotics/CVzero.git html
> cd html
> git branch gh-pages
> git symbolic-ref HEAD refs/heads/gh-pages
> rm .git/index
> git clean -fdx
```

This will create the appropriate structure on disk, a repository parallel to the main one where the pages
will be built. Now running ```make html``` from this directory will build the docs, commit them and push them to github.
In order for github's pages system to publish files and directories with an underscore at the start of their name you
may need to also add a ```.nojekyll``` file (no content needed) at the root of the pages branch.

If this setup stage has already been done you can simply clone the gh-pages branch:

```
> cd ..
> mkdir cvzero-pages
> cd cvzero-pages
> git clone git@github.com:OpenPiRobotics/CVzero.git --branch gh-pages html
```