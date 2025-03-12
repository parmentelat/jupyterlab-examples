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
  title: images
---

+++ {"tags": []}

# images

```{code-cell} ipython3
# but first one code cell and its rendering

10 * 30
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

## former bugs

this now works smoothly, no longer need an extra &lt;div&gt; wrapping the image

### with a width

````{admonition} with dropdown, MyST syntax and width
:class: dropdown seealso

```{image} media/board-8x8-small.png
:width: 500px
```
````

+++

### more than an image: here some text

````{admonition} same, but adding text around the image
:class: dropdown seealso
some text before

```{image} media/board-8x8-small.png
:width: 500px
```

some text after
````

+++

### several images

`````{admonition} same, with multiple images
:class: dropdown seealso
````{div}
some text before

```{image} media/board-8x8-small.png
:width: 500px
```

some text in the middle, another image (even if it looks the same)

```{image} media/board-8x8.png
:width: 200px
```

some text after
````
`````

+++

## inline images ?

wondering if one can use an image like it was a font character
![](media/board-8x8-micro.png) and **insert it inline**; - as of 2025 march this works with jlab but causes line breaks with mystmd/jb2

in any case remember the markdown syntax does not let us set a size...

+++ {"slideshow": {"slide_type": "-"}}

License CC BY-NC-ND, Thierry Parmentelat
