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

# `notebooklite`

each comes in two flavours, with or without a notebook name

+++

## nb no args


```{notebooklite}
:theme: JupyterLab Light
:width: 100%
:height: 500px
:prompt: notebooklite no args
:prompt_color: red
```

+++

## nb on hello-world.ipynb

omitting the theme

```{notebooklite} hello-world.ipynb
:width: 100%
:height: 500px
:prompt: notebooklite on one notebook
:prompt_color: orange
```

+++

## same inside a dropdown

probably the way to go; a few caveats:

- needs 2 clicks to open
- cannot change the size

`````{admonition} same inside a dropdown
:class: dropdown

````{div}
```{notebooklite} hello-world.ipynb
:width: 100%
:height: 500px
:prompt: notebooklite on one notebook within a dropdown
:prompt_color: orange
```
````
`````

+++

License CC BY-NC-ND, Thierry Parmentelat
