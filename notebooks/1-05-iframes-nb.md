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
  title: iframes
---

+++ {"slideshow": {"slide_type": "-"}}

Licence CC BY-NC-ND, Thierry Parmentelat

+++ {"tags": []}

# iframes

```{code-cell} ipython3
from IPython.display import HTML
HTML(filename="_static/style.html")
```

## raw HTML iframe: NO !

````{admonition} do not use an html iframe tag
:class: error 

not working in jlab, and works in jupyter book only if the target is in `_static`

```html
<!-- DO NOT USE THIS -->
<iframe src="_static/addresses-final.html" width="100%" height="600px">
</iframe>
```
````

+++

## use IPython's IFrame instead

here's an example with an HTML produced with folium, and stored in `_static`  
it works [with remote URLs too, of course, see e.g. here](label-video-iframe)

```{code-cell} ipython3
from IPython.display import IFrame

IFrame("_static/addresses-final.html", "500px", "400px")
```
