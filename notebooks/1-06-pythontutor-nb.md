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

+++ {"tags": []}

# pythontutor

+++

## ipythontutor

```{code-cell} ipython3
%load_ext ipythontutor
```

```{code-cell} ipython3
%%ipythontutor

L1 = L2 = [1, 2, 3]
L1[1:2] = [100, 200, 300]
```

## a simple call to HTML()

a simpler example, where we produce our own HTML code programatically

```{code-cell} ipython3
def my_table(a,b,c,d):
    return f"""
    <table>
    <tr><th>{a}</th><th>{b}</th></tr>
    <tr><td>{c}</td><td>{d}</td></tr>
    </table>
    """
```

```{code-cell} ipython3
# just checking
# my_table("student", "grade", "jean", 10)
```

```{code-cell} ipython3
# should render a table
from IPython.display import HTML

HTML(
my_table("student", "grade", "jean", 10)
)
```

## with HTML() from ipywidgets

```{code-cell} ipython3
from ipywidgets import HTML as ipyHTML
```

```{code-cell} ipython3
ipyHTML(my_table("student", "grade", "jean", 10))
```

+++ {"slideshow": {"slide_type": "-"}}

License CC BY-NC-ND, Thierry Parmentelat
