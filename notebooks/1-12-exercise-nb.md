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
---

+++ {"slideshow": {"slide_type": "-"}}

Licence CC BY-NC-ND, Thierry Parmentelat

+++

# exercises

```{code-cell} ipython3
from IPython.display import HTML
HTML(filename="_static/style.html")
```

````{warning}
this requires to have

* ```bash
  pip install sphinx-exercise
  ```

* **and** `sphinx_exercise` in `_config.yml` like so
  ```yaml
  sphinx:
    extra_extensions:
      sphinx_exercise
  ```
````

+++

see all options in <https://mystmd.org/guide/exercises>  
as well as <https://ebp-sphinx-exercise.readthedocs.io/en/latest/syntax.html>

in particular there is a `hidden` attribute that may come in handy but I have not explored in depth yet

+++

## native MyST exercise

+++

here's a sample

````{exercise} the header
:label: exo-label

the question; the dropdown class works too if needed
```{code-block}
# of course one can insert code in the body
class Foo:
    pass
```
````

+++

``````{admonition} the code for this output
:class: dropdown

`````{code-block}
````{exercise} the header
:label: exo-label

the question; the dropdown class works too if needed
```{code-block}
# of course one can insert code in the body
class Foo:
    pass
```
`````
``````

+++

## native MyST solution

here's a sample solution for the above exercise

+++

````{solution} exo-label
:class: dropdown
:label: sol-label

the solution
```{code-block} python
one can use ```{code-block} to insert code
def fact(n):
    pass
```
````

+++

``````{admonition} the code for this output
:class: dropdown

`````{code-block}
````{solution} exo-label
:class: dropdown
:label: sol-label

the solution
```{code-block} python
one can use ```{code-block} to insert code
def fact(n):
    pass
```
````
`````
``````

+++

````{warning}
the argument to the `solution` directive is the label of the exercise
````

+++

````{admonition} autre syntaxe
:class: seealso

see also an alternative syntax based on `solution-start` / `solution-end` in  
<https://ebp-sphinx-exercise.readthedocs.io/en/latest/syntax.html#basic-syntax>
````

+++

## without this feature

before that we have used an admonition with a `seealso` class

```{admonition} exercise: the topic
:class: seealso

the question blabla  
note that the whole business might come with a `:class: dropdown` thingy
```

I don't have a very stable way to present solutions, here's one suboptimal way to do it with a 
`:class: dropdown warning` directive

```{admonition} solution
:class: dropdown warning

the solution
````
