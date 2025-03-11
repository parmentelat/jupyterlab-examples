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
  title: miscell MyST
---

+++ {"tags": []}

# miscell MyST

```{code-cell} ipython3
from IPython.display import HTML
HTML(filename="_static/style.html")
```

## equations and dollarmath

this requires extra config, search for `dollarmath`

same for latex-math inline $\forall x\in \mathbb{C}$ like this,  
or double-dollars like that

$$
\forall x\in \mathbb{C}
$$

+++

## strikethrough

### pure markdown with double tildes

    ```
    ~~so that one can see text in strikethrough mode~~
    ```

works in jbook, but not in jlab (go figure); this requires an extra step **in the sphinx config**  
it renders : ~~so that one can see text in strikethrough mode~~

### with a MyST role

note that one can also use a MyST role 

```markdown
{strike}`so that one can see text in strikethrough mode`
```

it renders: {strike}`so that one can see text in strikethrough mode` (vanishes in jb1?)

+++ {"tags": []}

## the MyST download role

mostly we use this to create a link to download an exercise as a zip -- 
heavily used in `flotpython-exos`

```markdown
{download}`commencez par télécharger le zip<./downloadable.zip>`
```

{download}`commencez par télécharger le zip<./downloadable.zip>`

+++

## execute and insert: the eval role

looking into this to customize the README's of the 2 exos flavours  
however that won't work in jupyter book, so ...  
it does work in jlab though, in case it become useful some day (although it sometimes take 2 evaluations to show up right)

```{code-cell} ipython3
value = "Data Science"
```

+++ {"user_expressions": [{"expression": "value", "result": {"status": "ok", "data": {"text/plain": "'Data Science'"}, "metadata": {}}}]}

with this syntax
```markdown
{eval}`value`
```
we get: today we will learn {eval}`value`

```{code-cell} ipython3
# a little painful, but we can't seem to do the import inside the markdown eval
# because it only works on expressions 
import os
```

+++ {"user_expressions": [{"expression": "os.environ['USER']", "result": {"status": "ok", "data": {"text/plain": "'tparment'"}, "metadata": {}}}]}

admitting that the `USER` environment variable is set, we can also insert its value: 

### in a title{eval}: `os.environ['USER']`

+++ {"slideshow": {"slide_type": "-"}}

License CC BY-NC-ND, Thierry Parmentelat
