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
  title: videos
---

+++ {"slideshow": {"slide_type": "-"}, "tags": []}

Licence CC BY-NC-ND, Thierry Parmentelat

+++ {"tags": []}

# videos

```{code-cell} ipython3
:tags: []

from IPython.display import HTML
HTML(filename="_static/style.html")
```

+++ {"tags": []}

(label-video-iframe)=

## youtube: use IPython IFrame()

```{code-cell} ipython3
:tags: []

from IPython.display import IFrame

# Youtube
IFrame(
    "https://www.youtube.com/embed/i_ZcP7iNw-U?rel=0&amp;controls=0&amp;showinfo=0",
    width="600",
    height="400",
    # extras='frameborder="0" allowfullscreen',
)
```

+++ {"tags": []}

## ditto with `hide-input`

the same with the input area hidden with 

- the `jupyterlab-hidecell` extension
- using the `remove-input` cell tag

```{code-cell} ipython3
:hide_input: true
:tags: [remove-input]

from IPython.display import IFrame

# Youtube
IFrame(
    "https://www.youtube.com/embed/i_ZcP7iNw-U?rel=0&amp;controls=0&amp;showinfo=0",
    width="600",
    height="400",
    # extras='frameborder="0" allowfullscreen',
)
```

+++ {"tags": []}

## local video: use ipywidgets's Video()

for a local video - source needs to be put under `_static`

```{code-cell} ipython3
:tags: []

# same as above, you can use `remove-input` to hide the code

from ipywidgets import Video
Video.from_file("_static/under-static.mp4", autoplay=False, width='800px')
```

+++ {"tags": []}

## using sphinxcontrib_video ?

mostly **not usable** for now (neither jlab nor jbook)

- jlab gives "Unknown directive"
- jbook: requires stuff under `_static` (could be ok) but also does not respect `:width:` directive...


````{admonition} a clue, but hard to read
:class: admonition-small dropdown
```{div}
trying to understand what `@chrisjewell` was meaning in
<https://github.com/executablebooks/MyST-Parser/issues/651>
which would maybe allow to refer to videos not necessarily stored under `_static`, 
but to no avail so far

as of 2023 dec, this works only

| env | vid. location | works ? | symptom/comment |
|-----|---------------|---------|-----------------|
| jlab | under `_static` | KO |  (video: unknown directive)
| jlab | outside of `_static` | KO | (likewise)
| jupyter book | under `_static` | OK | cannot be resized though
| jupyter book | outside of `_static` | KO | a video widget appears but the target file is not there
```
````

---

this one is under `_static/` - it works in jbook, except for the width `300px`  
**addendum** it looks like the width needs to be an integer in this context

```{video} _static/under-static.mp4
:width: 300
```

this one is under `media/` - it's not found

```{video} media/under-media.mp4
:width: 300
```
````

+++

## using mystmd recipe

+++

### remote - youtube 


```{iframe} https://www.youtube.com/embed/i_ZcP7iNw-U?rel=0&amp;controls=0&amp;showinfo=0
using the iframe myst directive
```

+++

### local (and not under `_static`)

```{figure} media/under-media.mp4
this works in myst, but not in jlab
```

+++

### local (and under `_static`)

```{figure} _static/under-static.mp4
this works in myst, but not in jlab
```
