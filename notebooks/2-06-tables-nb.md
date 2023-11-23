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

# tables

```{code-cell} ipython3
from IPython.display import HTML
HTML(filename="_static/style.html")
```

several variations on using tables

+++ {"tags": []}

## regular markdown

| country | capital | joined in |
| --- | --- | --- |
| Germany | Berlin | 1958 |
| Italy | Rome | 1958 |
| France | Paris | 1958 |
| UK | London | 1973 |
| Spain | Madrid | 1986 |

+++

## using left/right/center markers

won't work properly in Jlab

| country | capital | joined in |
| ---: | :---: | :--- |
| Germany | Berlin | 1958 |
| Italy | Rome | 1958 |
| France | Paris | 1958 |
| UK | London | 1973 |
| Spain | Madrid | 1986 |

+++

## inside admonitions (no dropdown)

testing within plainly visible admonitions - not messing with the size this time

```{admonition} no dropdown and regular markdown
| country | capital | joined in |
| ---: | :---: | :--- |
| Germany | Berlin | 1958 |
| Italy | Rome | 1958 |
| France | Paris | 1958 |
| UK | London | 1973 |
| Spain | Madrid | 1986 |
```

+++

## inside dropdown admonitions

same within dropdown admonitions; we're experiencing the same bug as with sized images:

```{admonition} with dropdown and regular markdown
:class: dropdown
| country | capital | joined in |
| ---: | :---: | :--- |
| Germany | Berlin | 1958 |
| Italy | Rome | 1958 |
| France | Paris | 1958 |
| UK | London | 1973 |
| Spain | Madrid | 1986 |
```

+++

## the workaround

to fix the above example, we add a `{div}` env around it all

````{admonition} with dropdown and regular markdown
:class: dropdown

```{div}
| country | capital | joined in |
| ---: | :---: | :--- |
| Germany | Berlin | 1958 |
| Italy | Rome | 1958 |
| France | Paris | 1958 |
| UK | London | 1973 |
| Spain | Madrid | 1986 |
```
````
