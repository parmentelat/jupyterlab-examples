---
celltoolbar: Edit Metadata
jupytext:
  cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
  notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
nbhosting:
  title: miscell MyST
---

+++ {"slideshow": {"slide_type": "-"}}

Licence CC BY-NC-ND, Thierry Parmentelat

+++ {"tags": []}

# miscell MyST

```{code-cell} ipython3
from IPython.display import HTML
HTML(filename="_static/style.html")
```

## equations and dollarmath

this requires extra config, search for `dollarmath`

same for latex-math inline $\forall x\in \mathbb{C}$ like this, or double-dollars like that

$$
\forall x\in \mathbb{C}
$$

+++

## strikethrough

works in jbook, but not in jlab (go figure)  
this requires an extra step **in the sphinx config** ~~so that one can see text in strikethrough mode~~

+++

## the MyST download role

+++ {"tags": []}

mostly we use this to create a link to download an exercise as a zip -- 
heavily used in `flotpython-exos`

{download}`commencez par télécharger le zip<./downloadable.zip>`
