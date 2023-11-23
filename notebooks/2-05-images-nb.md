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
language_info:
  name: python
  nbconvert_exporter: python
  pygments_lexer: ipython3
nbhosting:
  title: React apps basics
---

+++ {"slideshow": {"slide_type": "-"}}

Licence CC BY-NC-ND, Thierry Parmentelat

+++ {"tags": []}

# images

```{code-cell} ipython3
from IPython.display import HTML
HTML(filename="_static/style.html")
```

several variations on inserting an image

+++ {"tags": []}

## regular markdown

![alt text](media/board-8x8.png)

+++

## MyST Syntax

we can set more layout parameters here

```{image} media/board-8x8.png
:width: 100px
:align: center
```

+++

## inside admonitions (no dropdown)

testing within plainly visible admonitions - not messing with the size this time

```{admonition} no dropdown and regular markdown
![](media/board-8x8-small.png)
```

````{admonition} no dropdown and with MyST syntax
```{image} media/board-8x8-small.png
```
````

+++

## inside dropdown admonitions

same within dropdown admonitions

```{admonition} with dropdown and regular markdown
:class: dropdown
![](media/board-8x8-small.png)
```

````{admonition} with dropdown and with MyST syntax
:class: dropdown
```{image} media/board-8x8-small.png
```
````

+++

## bug reproduction

mostly the same as previous example, but **specifying a width** breaks it:  
when toggled off, a large portion of wasted vertical space is used

````{admonition} with dropdown, MyST syntax and width
:class: dropdown seealso

```{image} media/board-8x8-small.png
:width: 500px
```
````

+++

## with workaround

issue already reported in <https://github.com/executablebooks/jupyter-book/issues/1928> 
and specifically a workaround is proposed in <https://github.com/executablebooks/jupyter-book/issues/1928#issuecomment-1552719064>

so, same as before, but wrapped inside a `{div}` wrapper; this

* works fine in the html output
* but breaks in jupyter with a `div - Unknown Directive` message
* follow-up here https://github.com/executablebooks/jupyter-book/issues/1928

`````{admonition} with dropdown, MyST syntax and width
:class: dropdown seealso
````{div}
```{image} media/board-8x8-small.png
:width: 500px
```
````
`````
