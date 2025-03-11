---
jupytext:
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
  title: introduction
---

```{code-cell} ipython3
from IPython.display import HTML
HTML(filename="_static/style.html")
```

# introduction

we're testing **jupyterlab**, together with  the rendering under **jupyter-book v2** (aka mystmd), and try to make sure both outputs are consistent

```{code-cell} ipython3
# this is the required piece
#%pip show jupyterlab-myst jupyterlab-jupytext jupyterlab-courselevels
```

+++ {"tags": [], "jp-MarkdownHeadingCollapsed": true}

````{admonition} what we do in this series of sample notebooks
:class: important

summarize most of our notebook recipes, regarding among others

* regular admonitions, including collapsible (texts where some part is toggable with a right or down arrow)
  note that collapsible also applies to admonitions

* exercises
* hide-input artefact (a code cell whose input code is hidden)
* miscell usual tricks (link to a downloadable file, iframe with some static html, ...)
* courselevels - mostly deprecated:
  * using tags to specifiy a level among basic=green, intermediate=blue, advanced=red
  * also the ability to put a frame around a cell
* mermaid: some inline (git)graphs using `mermaid.js`
````

+++ {"tags": []}

````{admonition} for what targets
:class: seealso

and check how that renders in the following contexts

* jupyter book output, which is now our primary output medium
* jlab4, with a cocktail of extensions, at least
  * `jupytext`, `jupyterlab-myst`, and more optionnally now, `jupyterlab-courselevels`
* notebook 7, although much less crucial at this point  
  note that nb7 runs on top of jlab4, so this is much less problematic than nb classic
````

+++

License CC BY-NC-ND, Thierry Parmentelat
