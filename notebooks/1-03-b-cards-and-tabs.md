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

### texts, from the doc

primarily to check that it works under jb1 too - **note** that the headers don't make it to jb1's output

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

### 2 images, no size specified

`````{grid} 1 1 2 2

````{card}
:header: Image content twice
```{image} media/board-8x8.png
```
````
````{card}
:header: Image content twice
```{image} media/board-8x8.png
```
````

`````

+++

### 3 images, with sizes

`````{grid} 1 1 2 3

````{card}
:header: Image content twice
```{image} media/board-8x8.png
:width: 400px
```
````
````{card}
:header: Image content twice
```{image} media/board-8x8.png
:width: 400px
```
````
````{card}
:header: Image content twice
```{image} media/board-8x8.png
:width: 400px
```
````

`````

+++

## tabs

### almosas-is from the doc
 
`````{tab-set}
````{tab-item} Tab 1
:sync: tab1
Tab one
```{image} media/board-8x8.png
:width: 200px
:align: center
```
````
````{tab-item} Tab 2
:sync: tab2
Tab two
````
`````

+++

### going deeper

``````{tab-set}
`````{tab-item} Windows

```{image} media/windows.png
:width: 80px
```

````{admonition} prep
:class: seealso

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
```{image} media/apple.png
:width: 80px
```
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
```{image} media/linux.png
:width: 80px
```
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

+++

### synced tabs

using the same names here to check for synchronized selection

``````{tab-set}
`````{tab-item} Windows
replica

```{image} media/windows.png
:width: 80px
```
`````


`````{tab-item} MacOS
replica
```{image} media/apple.png
:width: 80px
```
`````


`````{tab-item} Linux
replica
```{image} media/linux.png
:width: 80px
```
`````
``````
