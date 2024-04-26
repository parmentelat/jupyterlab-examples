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
