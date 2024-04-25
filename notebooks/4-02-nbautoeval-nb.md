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

# nbautoeval in jlite

+++

## using a relay notebook

and written in ipynb because for now jupyterlite-sphinx does not handle jupytext notebooks

`````{admonition} the pgcd exercise (in a dropdown)
:class: dropdown

````{div}
```{notebooklite} exo-pgcd-nb.ipynb
:width: 100%
:height: 100vh
:prompt: the pgcd exercise
:prompt_color: blue
```
````
`````
