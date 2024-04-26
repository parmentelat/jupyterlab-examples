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

# a simple REPL - MyST

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
