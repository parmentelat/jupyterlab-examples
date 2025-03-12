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
  title: iframes
---

+++ {"tags": []}

# iframes

+++

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

## tl - dr

- remote URLs are OK
- for locally shipped htmls (e.g. folium-produced maps), as of 2025 march:
  - jlab is mostly OK
  - jb2: I can't find the URL to retrieve them - whether we put them in `_static` or in `media`...

+++

## use IPython's IFrame instead

it works [with remote URLs, like we'ne seen about videos](label-video-iframe)

with local URLs though, it's an issue

here's an example with an HTML produced with folium, and stored in `_static`

apparently this won't work at all in mystmd;
it does work in jlab

```{code-cell} ipython3
from IPython.display import IFrame

IFrame("_static/addresses-final.html", "500px", "400px")
```

```{code-cell} ipython3
from IPython.display import IFrame

IFrame("media/addresses-final.html", "500px", "400px")
```

## mystmd iframe

### a local URL in `static`: not working ?

this is not working as of 2025 march

    ```{iframe} _static/addresses-final.html
    ```
    
```{iframe} _static/addresses-final.html
:width: 400px
:height: 300px
:align: center
```

+++

### a local URL in `media`: not working ?

this is not working as of 2025 march

    ```{iframe} media/addresses-final.html
    ```

```{iframe} media/addresses-final.html
:width: 400px
height: 300px
:align: center
```

+++

### a remote URL

using remote URLS is OK - can't seem to set the heiht though

    ```{iframe} https://ue12-p25.github.io/intro/
    ```

```{iframe} https://ue12-p25.github.io/intro/
:width: 500px
:height: 400px
:align: center
```

+++

License CC BY-NC-ND, Thierry Parmentelat
