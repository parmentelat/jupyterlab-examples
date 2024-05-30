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

# cards and tabs

+++

from <https://mystmd.org/guide/dropdowns-cards-and-tabs>

+++

## grid of cards

primarily to check that it works under jb1 too

````{grid} 1 1 2 3

```{card}
:header: Text content ✏️
Structure books with text files and Jupyter Notebooks with minimal configuration.
```

```{card}
:header: MyST Markdown ✨
Write MyST Markdown to create enriched documents with publication-quality features.
```

```{card}
:header: Executable content 🔁
Execute notebook cells, store results, and insert outputs across pages.
```
````

+++

## tabs

### as-is from the doc

````{tab-set}
```{tab-item} Tab 1
:sync: tab1
Tab one
```
```{tab-item} Tab 2
:sync: tab2
Tab two
```
````

+++

### going deeper

``````{tab-set}
`````{tab-item} Windows

````{admonition} prep
:class: 

```{image} media/windows.png
:width: 300px
```
````

````{admonition} download
:class: dropdown

the text
````

````{admonition} install
:class: dropdown

the text
````
`````


`````{tab-item} MacOS
````{admonition} prep
:class: 

```{image} media/board-8x8.png
:width: 300px
```
````
````{admonition} download
:class: dropdown

the text
````
````{admonition} install
:class: dropdown

the text
````
`````


`````{tab-item} Linux
````{admonition} prep
:class: 

```{image} media/linux.png
:width: 300px
```
````
````{admonition} download
:class: dropdown

the text
````
````{admonition} install
:class: dropdown

the text
````
`````
``````
