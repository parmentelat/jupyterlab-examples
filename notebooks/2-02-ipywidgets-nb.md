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

+++

# ipywidgets

curious to see how it goes; in a nutshell:

- fine in jlab
- jb1: html output has the widgets,  but they don't interact (frozen output)
- jb2: not working at all, needs a kernel connection to display the widgets

```{code-cell} ipython3
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
```

## from the doc (no graphic)

```{code-cell} ipython3
def f(x):
    return x
```

```{code-cell} ipython3
interact(f, x=10);
```

## from the doc (with interactive_output)

```{code-cell} ipython3
import ipywidgets as widgets
from IPython.display import display

a = widgets.IntSlider(value=5, min=0, max=10)

def f1(a):
    display(a)

def f2(a):
    display(a * 2)

out1 = widgets.interactive_output(f1, {'a': a})
out2 = widgets.interactive_output(f2, {'a': a})

display(a)
display(out1)
display(out2)
```

## basic plot

```{code-cell} ipython3
%matplotlib ipympl
```

```{code-cell} ipython3
import ipywidgets as widgets
```

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0, 4*np.pi, 200)

def frequency(f):
    plt.clf()
    Y = np.sin(f*X)
    plt.plot(X, Y)
    plt.show()
```

```{code-cell} ipython3
plt.figure()

interact(frequency, f=widgets.FloatSlider(min=1, max=10, value=2));
```

License CC BY-NC-ND, Thierry Parmentelat
