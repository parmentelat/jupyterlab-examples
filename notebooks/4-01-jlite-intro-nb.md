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

- https://jupyterlite-sphinx.readthedocs.io/en/latest/

+++

## prerequisites

````{admonition} WARNING: not necessarily up-to-date/complete
:class: danger

at this point, here's the changes made to enable jupyter-lite in the jupyter-book output

- in `notebooks/requirements-rtd.yml`
  - add `jupyterlite-pyodide-kernel`
  - and `jupyterlite-sphinx`
- in `_config.yml`:
  - `sphinx.config.html_extra_path`: append `lite`
  - `sphinx.config.jupyterlite_dir`: set to `.`
  - `sphinx.extra_extensions`: append `jupyterlite_sphinx`
````

+++

## status

probably not production-ready yet, but kind of working !

### dependencies

at this point we don't get `nbautoeval` pre-installed  
there are instructions here <https://jupyterlite-sphinx.readthedocs.io/en/latest/configuration.html#pre-installed-packages> on how to do that, but that relies on `jupyterlab-xeus` while we have gone so far with `jupyterlite-pyodide-kernel`  
which btw does not seem to install on the latest version (getting 0.2.3, while 0.3 is out too)

not a showstopper, as one can do `%pip install nbautoeval` in the notebook and that does the trick

### development: use a http server !

deploying locally (i.e. reading doc using `file://` protocol) results in many errors like so
> Access to internal resource ... from origin 'null' origin has been blocked by CORS policy

it is **mandatory to use a local http server** to work around CORS limitations and similar business  
start your server with something like
```bash
python -m http.server -d _build/html
```

### devel: beware of service workers in chrome

also I ended up using safari (!) because somehow on chrome the *service workers* thingy gets in my way - as if everything was cached all the time - and I keep on getting distracted...

### deployment

when deployed on *readthedocs.io* things seem to be working rather fine (with safari again); need to check about chrome in this context.

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

License CC BY-NC-ND, Thierry Parmentelat
