---
jupytext:
  formats: md:myst
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
---

Licence CC BY-NC-ND, Thierry Parmentelat

```{raw-cell}
---
raw_mimetype: ''
slideshow:
  slide_type: ''
tags: []
---
from IPython.display import HTML
HTML(filename="_static/style.html")
```

# Jupyter lite

main objectives

- embed a repl in a notebook on rtd
- embed nbautoeval exercises right in readthedocs - not quite sure yet what that should look like

jtpio's recipes are for pure ReST and .ipynb notebooks, so using MyST for both notebooks and doc sources may be a little challenging..

+++

## references

- mostly jtpio blog here
<https://blog.jupyter.org/jupyter-everywhere-f8151c2cc6e8>

+++

## prerequisites

at this point, here's the changes made to enable jupyter-lite in the jupyter-book output

- in `notebooks/requirements-rtd.yml`
  - add `jupyterlite-pyodide-kernel`
  - and `jupyterlite-sphinx`
- in `_config.yml`:
  - `sphinx.config.html_extra_path`: append `lite`
  - `sphinx.config.jupyterlite_dir`: set to `.`
  - `sphinx.extra_extensions`: append `jupyterlite_sphinx`

+++

## status

deploying locally (i.e. reading doc using `file://` protocol) results in many errors like so

> Access to internal resource ... from origin 'null' origin has been blocked by CORS policy

+++

## references

- the most helpful one was this  
  <https://blog.jupyter.org/jupyter-everywhere-f8151c2cc6e8>
- more details in the jupyterlite rtd pages  
  <https://jupyterlite.readthedocs.io/en/latest/howto/deployment/sphinx.html>
- a real-scale deployment on rtd (ipycanvas)
  - output <https://ipycanvas.readthedocs.io/en/master/lite/lab/>
  - entry point <https://ipycanvas.readthedocs.io/>
  - github repo <https://github.com/jupyter-widgets-contrib/ipycanvas>

- another story by psychemedia
  <https://psychemedia.github.io/storynotes/running-the-book-code.html?highlight=jupyterlite>

+++

## a simple REPL - MyST

using MyST syntax with triple backticks - here with `replite` we can in theory get a REPL

```{replite}
:kernel: python
:theme: JupyterLab Light
:width: 100%
:height: 300px
:prompt: replite
:prompt_color: gray

print('Hello from a JupyterLite console!')
```

+++

## `jupyterlite` & `notebooklab`

each comes in two flavours, with or without a notebook name

+++

### jlab no args

```{jupyterlite}
:theme: JupyterLab Light
:width: 100%
:height: 300px
:prompt: jupyterlite no args
:prompt_color: green
```

+++

### jlab on hello-world.ipynb

omitting the theme

```{jupyterlite} hello-world.ipynb
:width: 100%
:height: 300px
:prompt: jupyterlite on one notebook
:prompt_color: blue
```

+++

### nb no args


```{notebooklite}
:theme: JupyterLab Light
:width: 100%
:height: 300px
:prompt: notebooklite no args
:prompt_color: red
```

+++

### nb on on test-nb.ipynb

omitting the theme

```{notebooklite} test-nb.ipynb
:width: 100%
:height: 300px
:prompt: notebooklite on one notebook
:prompt_color: orange
```

+++

## inside dropdowns

like for images this needs to go inside a `{div}` thingy

`````{admonition} a hidden repl
:class: dropdown

````{div}
```{replite}
:kernel: python
:theme: JupyterLab Light
:width: 100%
:height: 300px
:prompt: replite
:prompt_color: pink

print('Hello from a JupyterLite console!')
```
````
`````

+++

## using jupytext

on one specific notebook that is jupytext-encoded in Python

```{notebooklite} test-jupytext1-nb.py
:width: 100%
:height: 300px
:prompt: notebooklite on one notebook
:prompt_color: aquamarine
```

+++

## all together

open one jupytext notebook inside a dropdown, and test another jupytext format (here myst)

on one specific notebook that is jupytext-encoded

`````{admonition} a hidden jupytext notebook
:class: dropdown

````{div}
```{notebooklite} test-jupytext2-nb.md
:width: 100%
:height: 300px
:prompt: notebooklite on one notebook
:prompt_color: yellow
```
````
`````
