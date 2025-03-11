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
  title: nbautoeval
---

+++ {"tags": []}

# nbautoeval

+++

## nbautoeval

here is a first, static, test; there is also another, [better way with a dynamic interface thanks to jupyterlite](label-nbautoeval-dynamic)

```{code-cell} ipython3
from exo_pgcd import exo_pgcd

exo_pgcd.example()
```

```{code-cell} ipython3
def pgcd(a, b):
    return b % a
```

```{code-cell} ipython3
exo_pgcd.correction(pgcd)
```

+++ {"slideshow": {"slide_type": "-"}}

License CC BY-NC-ND, Thierry Parmentelat
