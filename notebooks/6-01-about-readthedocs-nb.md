---
jupytext:
  encoding: '# -*- coding: utf-8 -*-'
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
language_info:
  name: python
  nbconvert_exporter: python
  pygments_lexer: ipython3
nbhosting:
  title: an nbhosting title
---

```{code-cell} ipython3
:tags: [raises-exception]

from IPython.display import HTML
HTML(filename="_static/style.html")
```

# initializing readthedocs

setting up the readthedocs project often turns up painful  
here's a few notes about that stage - as of 2023 september

+++

## how it should work

* from the rtd home page, click on the "import a project" button
* in principle, the project should be visible in the list of github projects
* but it was not, so I went for the "manual import" button - but **DON'T DO
  THAT**, see below instead

my understanding is that the automatic import should do everything, including
setting up the webhook in github that allows rtd to be notified of pushes

+++

## BUT

* this had been failing me for a long time, and in that case builds wouldn't
  trigger automatically on a push

* note that until this works smoothly, it's always possible to trigger builds
  manually

+++

## how I fixed it

* noticed that <https://github.com/settings/applications> had no entry for
  readthedocs

* went to <https://readthedocs.org/accounts/social/connections/> and from there
  (or *username* -> *Settings* -> *Connected Services*) and
  + disconnected github
  + reconnected github

* this gave me a chance to **add access to organizations** - in particular I added
  the `ue12-p23` orga that is current at this stage

* might need to **redo this over time ?**, as the orga changes

+++

## epilogue

at that point I had to logout and back in readthedocs

I could then import the project - as it did show up in the list, which it did
not before - and the webhook got added automatically, and I was all set

+++

## postscriptum

* on a later attempt, I could see no importable repo at all - had to unselect the
`conda-forge` thingy in the 'filter repositories' box

go figure...

* and later on still, trying to import a project was still displaying 'no
  webhook' in red  
  I had to logout and log back in, and then it was fine and I could import
  successfully with a green message saying the webhook was added

+++

## final trick

within the rtd builds page, for using the whole width, type in the console

```js
document.querySelector("#content>.wrapper").style.width = "100%"
```

+++

License CC BY-NC-ND, Thierry Parmentelat
