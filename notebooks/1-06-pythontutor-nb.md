---
celltoolbar: Edit Metadata
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
  title: pythontutor
---

+++ {"slideshow": {"slide_type": "-"}}

Licence CC BY-NC-ND, Thierry Parmentelat

+++ {"tags": []}

# pythontutor

```{code-cell} ipython3
from IPython.display import HTML
HTML(filename="_static/style.html")
```

## ipythontutor

```{code-cell} ipython3
%load_ext ipythontutor
```

```{code-cell} ipython3
%%ipythontutor

L1 = L2 = [1, 2, 3]
L1[1:2] = [100, 200, 300]
```
