---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.0
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

Licence CC BY-NC-ND, Thierry Parmentelat

+++

# code in admonition title

it seems that not all markdown construction play well when put in an admonition title

each time we try the same admonition with backticks, and then with colons

```{code-cell} ipython3
from IPython.display import HTML
HTML(filename="_static/style.html")
```

## code in the title

+++

::::{admonition} the title has `some code`

with colons instead of backticks - this works well in jlab, but not in jbook

::::

+++

***
***

+++

the code elow breaks it very hard, I keep for next time I want to try it, but for now it is too disruptive

`````bash

````{admonition} the title has `some code`

and the admonition is made with backticks - not working in jlab, and not in jbook either

````
`````

+++

***
***

+++

## italics in the title

+++

::::{admonition} the title has *italics*

with colons instead of backticks - and same result: this works well in jlab, but not in jbook

::::

+++

***
***

+++

likewise

`````bash
````{admonition} the title has *italics*`

and the admonition is made with backticks - not working in jlab, and not in jbook either

````
`````
