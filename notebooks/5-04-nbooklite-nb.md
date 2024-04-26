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

# `notebooklab`

each comes in two flavours, with or without a notebook name

+++

## nb no args


```{notebooklite}
:theme: JupyterLab Light
:width: 100%
:height: 300px
:prompt: notebooklite no args
:prompt_color: red
```

+++

## nb on hello-world.ipynb

omitting the theme

```{notebooklite} test-nb.ipynb
:width: 100%
:height: 300px
:prompt: notebooklite on one notebook
:prompt_color: orange
```

+++

## same inside a dropdown

````{admonition} a notebook inside a dropdown
:class: dropdown

```{notebooklite} test-nb.ipynb
:width: 100%
:height: 300px
:prompt: notebooklite on one notebook
:prompt_color: orange
```
````
