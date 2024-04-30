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
---

Licence CC BY-NC-ND, Thierry Parmentelat

+++

# matplotlib rendering

```{code-cell} ipython3
from IPython.display import HTML
HTML(filename="_static/style.html")
```

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0, 2*np.pi)
Y = np.sin(X)
```

## the right choice

+++

* `%matplotlib notebook` is advertised as no longer working
  and indeed one gets `Javascript Error: IPython is not defined`
* `%matplotlib widget` has been mentioned sometimes;
  it seems to work but it won't render properly in the jupyter book (or was it in vs-code ?)
* so I will settle on using `%matplotlib ipympl`
  which actually sounds like an alias for `widget` but works better in vs-code  

  **note** that either `notebook` or `ipympl` requires `pip install ipympl`  
  this module is also sometimes referred to as `jupyterlab-matplotlib`

```{code-cell} ipython3
# this produces an interactive plot under jupyter lab
# with jupyter book, it should also be interactive (and it was working at some point)
# but as of 2024 at least, we get a static plot
# 
# of potential interest:
# 
# https://github.com/executablebooks/jupyter-book/issues/1053
# https://github.com/executablebooks/jupyter-book/issues/1991
# https://jupyterbook.org/en/stable/advanced/sphinx.html#custom-css-or-javascript
# https://jupyterbook.org/en/stable/interactive/interactive.html#ipywidgets

%matplotlib ipympl
```

```{code-cell} ipython3
# this plot should be interactive

plt.figure(figsize=(10, 2))
plt.plot(X, Y);
```

```{code-cell} ipython3
# basic imshow - same: is resizable / zoomable under jlab but jbook makes it static

I, J = np.indices((4, 4))
grid = (I + J) % 2

plt.figure()
plt.imshow(grid)
plt.figure()
plt.imshow(1-grid);
```

```{code-cell} ipython3

```
