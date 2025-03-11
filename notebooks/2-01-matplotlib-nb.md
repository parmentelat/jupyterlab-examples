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

# matplotlib rendering

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
# but as of Apr 2024 at least, if we keep %matplotlib ipympl we do not get any plot - not even a static one
# 
# of potential interest:
# 
# https://github.com/executablebooks/jupyter-book/issues/1053
# https://github.com/executablebooks/jupyter-book/issues/1991
# https://jupyterbook.org/en/stable/advanced/sphinx.html#custom-css-or-javascript
# https://jupyterbook.org/en/stable/interactive/interactive.html#ipywidgets
#
# for this to render anything at all under jbook, I've had to tweak the jbook config file
# as per https://github.com/agoose77/phd-thesis/blob/03d6392032e0066aa14e8c3a9a99de9f04762cdd/_config.yml#L185-L193
# this looks fragile...

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

License CC BY-NC-ND, Thierry Parmentelat
