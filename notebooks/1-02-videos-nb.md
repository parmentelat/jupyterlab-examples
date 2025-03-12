---
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
---

# videos

+++

(label-video-iframe)=

## youtube: use IPython IFrame()

```{code-cell} ipython3
from IPython.display import IFrame

# Youtube
IFrame(
    "https://www.youtube.com/embed/i_ZcP7iNw-U?rel=0&amp;controls=0&amp;showinfo=0",
    width="600",
    height="400",
    # extras='frameborder="0" allowfullscreen',
)
```

## ditto with `hide-input`

the same with the input area hidden with 

- the `jupyterlab-hidecell` extension
- using the `remove-input` cell tag

```{code-cell} ipython3
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

## local video: use ipywidgets's Video()

for a local video - source needs to be put under `_static`

```{code-cell} ipython3
# same as above, you can use `remove-input` to hide the code

from ipywidgets import Video
Video.from_file("_static/under-static.mp4", autoplay=False, width='800px')
```

## using mystmd recipe

+++

### remote - youtube

using the `iframe` myst directive

```{iframe} https://www.youtube.com/embed/i_ZcP7iNw-U?rel=0&amp;controls=0&amp;showinfo=0

works in both jlab and jb2
```

+++

### local (and not under `_static`)

using the `figure` myst directive

```{figure} media/under-media.mp4
this works in mystmd/jb2, but not in jlab
```

+++

### local (and under `_static`)

using the `figure` myst directive again

```{figure} _static/under-static.mp4
this works in mystmd/jb2, but not in jlab
```

+++

License CC BY-NC-ND, Thierry Parmentelat
