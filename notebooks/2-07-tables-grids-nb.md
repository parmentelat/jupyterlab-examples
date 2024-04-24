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

# tables & grids

```{code-cell} ipython3
from IPython.display import HTML
HTML(filename="_static/style.html")
```

several variations on using tables and grids

+++

## tables

+++ {"tags": []}

### regular markdown

| country | capital | joined in |
| --- | --- | --- |
| Germany | Berlin | 1958 |
| Italy | Rome | 1958 |
| France | Paris | 1958 |
| UK | London | 1973 |
| Spain | Madrid | 1986 |

+++

### using left/right/center markers

won't work properly in Jlab

| country | capital | joined in |
| ---: | :---: | :--- |
| Germany | Berlin | 1958 |
| Italy | Rome | 1958 |
| France | Paris | 1958 |
| UK | London | 1973 |
| Spain | Madrid | 1986 |

+++

### inside admonitions (no dropdown)

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

### inside dropdown admonitions

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

### the workaround

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

+++

## grids

+++

this section requires `pip install jupyterlab-gridwidth`

see also <https://github.com/parmentelat/jupyterlab-gridwidth/issues/13>

+++ {"tags": ["gridwidth-1-2"], "slideshow": {"slide_type": ""}}

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi. Proin porttitor, orci nec nonummy molestie, enim est eleifend mi, non fermentum diam nisl sit amet erat. Duis semper. Duis arcu massa, scelerisque vitae, consequat in, pretium a, enim. Pellentesque congue. Ut in risus volutpat libero pharetra tempor. Cras vestibulum bibendum augue. Praesent egestas leo in pede. Praesent blandit odio eu enim. Pellentesque sed dui ut augue blandit sodales. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Aliquam nibh. Mauris ac mauris sed pede pellentesque fermentum. Maecenas adipiscing ante non diam sodales hendrerit.
Ut velit mauris, egestas sed, gravida nec, ornare ut, mi. Aenean ut orci vel massa suscipit pulvinar. Nulla sollicitudin. Fusce varius, ligula non tempus aliquam, nunc turpis ullamcorper nibh, in tempus sapien eros vitae ligula. Pellentesque rhoncus nunc et augue. Integer id felis. Curabitur aliquet pellentesque diam. Integer quis metus vitae elit lobortis egestas. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Morbi vel erat non mauris convallis vehicula. Nulla et sapien. Integer tortor tellus, aliquam faucibus, convallis id, congue eu, quam. Mauris ullamcorper felis vitae erat. Proin feugiat, augue non elementum posuere, metus purus iaculis lectus, et tristique ligula justo vitae magna.

Aliquam convallis sollicitudin purus. Praesent aliquam, enim at fermentum mollis, ligula massa adipiscing nisl, ac euismod nibh nisl eu lectus. Fusce vulputate sem at sapien. Vivamus leo. Aliquam euismod libero eu enim. Nulla nec felis sed leo placerat imperdiet. Aenean suscipit nulla in justo. Suspendisse cursus rutrum augue. Nulla tincidunt tincidunt mi. Curabitur iaculis, lorem vel rhoncus faucibus, felis magna fermentum augue, et ultricies lacus lorem varius purus. Curabitur eu amet.

+++ {"tags": ["gridwidth-1-2"]}

a cell with a small height

I can't find an easy way for us to be able to take adantage of the space below

+++ {"tags": ["gridwidth-1-2"]}

a cell with a small height

+++ {"tags": ["gridwidth-1-2"]}

a cell with a small height

+++ {"tags": ["gridwidth-1-2"]}

a cell with a small height
