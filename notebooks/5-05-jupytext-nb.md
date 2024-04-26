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

## using jupytext

on one specific notebook that is jupytext-encoded in Python

```{notebooklite} hello-world-jupytext-nb.md
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
