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
nbhosting:
  title: React apps basics
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

## youtube: use IPython IFrame() instead

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

the same with the input area hidden with `jupyterlab-hidecell` using `remove-input`

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

for a local video:

```{code-cell} ipython3
:tags: []

# same as above, you can use `remove-input` to hide the code

from ipywidgets import Video
Video.from_file("_static/under-static.mp4", autoplay=False)
```

+++ {"tags": []}

## using sphinxcontrib_video ?

trying to understand what @chirsjewell was meaning in 
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

---

this one is under `_static/`

```{video} _static/under-static.mp4
:width: 300px
```

this one is under `media/`

```{video} media/under-media.mp4
```
