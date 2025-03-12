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
  title: tables & grids
---

+++ {"tags": []}

# tables & grids

+++

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

properly aligned in jlab and in jb2

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

same within dropdown admonitions - works fine in jlab and jb2

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

## `list-table`

this can come in handy as well; not all the options work in all envs, but that's still often better than regular `table`s  
see <https://myst-parser.readthedocs.io/en/latest/syntax/tables.html#list-tables> for more options

````{list-table}
:widths: 15 10 30
:header-rows: 1
:stub-columns: 1
:align: center

* - col1
  - col2
  - col3

* - val11
  - val12val12
  - val13val13val13

* - val21val21
  - val22val22val22val22
  - val23val23val23val23val23val23

````

+++

## grids

this unfortunately is a jlab only feature

+++ {"tags": ["gridwidth-1-3"]}

this section requires `pip install jupyterlab-gridwidth`  
at this point it works only under jlab, and **not in jbook**

see also <https://github.com/parmentelat/jupyterlab-gridwidth/issues/13>

+++ {"tags": ["gridwidth-1-2"], "slideshow": {"slide_type": ""}}

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi. Proin porttitor, orci nec nonummy molestie, enim est eleifend mi, non fermentum diam nisl sit amet erat. Duis semper. Duis arcu massa, scelerisque vitae, consequat in, pretium a, enim. Pellentesque congue. Ut in risus volutpat libero pharetra tempor. Cras vestibulum bibendum augue. Praesent egestas leo in pede. Praesent blandit odio eu enim. Pellentesque sed dui ut augue blandit sodales. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Aliquam nibh. Mauris ac mauris sed pede pellentesque fermentum. Maecenas adipiscing ante non diam sodales hendrerit.
Ut velit mauris, egestas sed, gravida nec, ornare ut, mi. Aenean ut orci vel massa suscipit pulvinar. Nulla sollicitudin. Fusce varius, ligula non tempus aliquam, nunc turpis ullamcorper nibh, in tempus sapien eros vitae ligula. Pellentesque rhoncus nunc et augue. Integer id felis. Curabitur aliquet pellentesque diam. Integer quis metus vitae elit lobortis egestas. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Morbi vel erat non mauris convallis vehicula. Nulla et sapien. Integer tortor tellus, aliquam faucibus, convallis id, congue eu, quam. Mauris ullamcorper felis vitae erat. Proin feugiat, augue non elementum posuere, metus purus iaculis lectus, et tristique ligula justo vitae magna.

Aliquam convallis sollicitudin purus. Praesent aliquam, enim at fermentum mollis, ligula massa adipiscing nisl, ac euismod nibh nisl eu lectus. Fusce vulputate sem at sapien. Vivamus leo. Aliquam euismod libero eu enim. Nulla nec felis sed leo placerat imperdiet. Aenean suscipit nulla in justo. Suspendisse cursus rutrum augue. Nulla tincidunt tincidunt mi. Curabitur iaculis, lorem vel rhoncus faucibus, felis magna fermentum augue, et ultricies lacus lorem varius purus. Curabitur eu amet.

+++ {"tags": ["gridwidth-1-2"]}

a cell with a small height

I can't find an easy way for us to be able to take adantage of the space below

+++ {"tags": ["gridwidth-1-3"]}

a cell with a small height

+++ {"tags": ["gridwidth-1-3"]}

a cell with a small height

+++ {"tags": ["gridwidth-1-3"]}

a cell with a small height

+++ {"slideshow": {"slide_type": "-"}}

License CC BY-NC-ND, Thierry Parmentelat
