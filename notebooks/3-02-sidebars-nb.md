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

```{code-cell} ipython3
from IPython.display import HTML
HTML(filename="_static/style.html")
```

# sidebars and similar

as per <https://jupyterbook.org/en/stable/content/layout.html>

+++

## sidebar

not supported within jupyterlab, but shows up in the book output

```{sidebar} some title
and some body within a simple sidebar
```

and below so we see how it goes

+++

### a little more complex

````{sidebar} embeddings

this one contains a code block
```python
# of course it is smaller

class Foo: pass
```
````

and below so we see how it goes

+++

### and again

not supported within jupyterlab, but shows up in the book output

```{sidebar} some title
and some body within a simple sidebar
```

and below so we see how it goes

+++

## margin

not supported within jupyterlab, but shows up in the book output

```{margin} some title
and some body within a simple margin
```

and below so we see how it goes

+++

### a little more complex

````{margin} embeddings

this one contains a code block
```python
# of course it is smaller

class Foo: pass
```
````

and below so we see how it goes

+++

### and again

not supported within jupyterlab, but shows up in the book output

```{margin} some title
and some body within a simple margin
```

and below so we see how it goes

+++ {"slideshow": {"slide_type": ""}}

## full-width

a feature to take advantage of residual space on the right hand side

of course this is targetting the jbook output

+++ {"slideshow": {"slide_type": ""}}

### full-width code

obtained with the `full-width` tag on the cell

```{code-cell} ipython3
---
slideshow:
  slide_type: ''
tags: [full-width]
---
data = """
--------------------------------------------------------------------------------------------------------------------
====================================================================================================================
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
```

### full-width text

there is a need to use a `{div}` thing; regardless, here's one example

+++

```{div} full-width
« Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi. Proin porttitor, orci nec nonummy molestie, enim est eleifend mi, non fermentum diam nisl sit amet erat. Duis semper. Duis arcu massa, scelerisque vitae, consequat in, pretium a, enim. Pellentesque congue. Ut in risus volutpat libero pharetra tempor. Cras vestibulum bibendum augue. Praesent egestas leo in pede. Praesent blandit odio eu enim. Pellentesque sed dui ut augue blandit sodales. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Aliquam nibh. Mauris ac mauris sed pede pellentesque fermentum. Maecenas adipiscing ante non diam sodales hendrerit.
Ut velit mauris, egestas sed, gravida nec, ornare ut, mi. Aenean ut orci vel massa suscipit pulvinar. Nulla sollicitudin. Fusce varius, ligula non tempus aliquam, nunc turpis ullamcorper nibh, in tempus sapien eros vitae ligula. Pellentesque rhoncus nunc et augue. Integer id felis. Curabitur aliquet pellentesque diam. Integer quis metus vitae elit lobortis egestas. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Morbi vel erat non mauris convallis vehicula. Nulla et sapien. Integer tortor tellus, aliquam faucibus, convallis id, congue eu, quam. Mauris ullamcorper felis vitae erat. Proin feugiat, augue non elementum posuere, metus purus iaculis lectus, et tristique ligula justo vitae magna.

Aliquam convallis sollicitudin purus. Praesent aliquam, enim at fermentum mollis, ligula massa adipiscing nisl, ac euismod nibh nisl eu lectus. Fusce vulputate sem at sapien. Vivamus leo. Aliquam euismod libero eu enim. Nulla nec felis sed leo placerat imperdiet. Aenean suscipit nulla in justo. Suspendisse cursus rutrum augue. Nulla tincidunt tincidunt mi. Curabitur iaculis, lorem vel rhoncus faucibus, felis magna fermentum augue, et ultricies lacus lorem varius purus. Curabitur eu amet. »
```

+++

License CC BY-NC-ND, Thierry Parmentelat
