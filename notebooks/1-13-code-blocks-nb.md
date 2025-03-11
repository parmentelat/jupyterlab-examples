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

# code blocks

+++

## `{code-block}`

prefer to use the `code-block` directive  
more details here <https://mystmd.org/guide/code>

+++

### `:linenos:`

+++

```{code-block}
:linenos:

one
two
three
four
five
six
seven
```

+++

### `:emphasize-lines:`

**must** use linenos too, otherwise it won't trigger

+++

```{code-block}
:linenos:
:emphasize-lines: 2, 4,5,6

one
two
three
four
five
six
seven
```

+++

### filename

+++

```{code-block}
:filename: my-numbers.txt

one
two
three
four
five
six
seven
```

+++

## `{literalinclude}`

to show stuff - possible an extract - from a local file
(not working in jlab)

+++

### plain inclusion of Makefile

```{literalinclude} Makefile
```

+++

### partial

same between `prune` (inclusive) and `toc` (exclusive)

```{list-table}
:header-rows: 1

* - directive
  - how it works

* - `start-at`
  - inclusive

* - `start-after`
  - exclusive

* - `end-at`
  - inclusive

* - `end-before`
  - exclusive
```

```{literalinclude} Makefile
:start-at: prune
:end-before: toc
```

+++

### the file name

apparently this is hopeless with jbook..

```{literalinclude} Makefile
:filename: Makefile

```

+++

License CC BY-NC-ND, Thierry Parmentelat
