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

## `{code-block}`

prefer to use the `code-block` directive  
more details here <https://mystmd.org/guide/code>

+++

# code blocks

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

### plain inclusion of separate file in the repo

apparently this is **hopeless with jlab**; works fine in jb2 though..

```{literalinclude} Makefile
```

+++

### partial

same between `prune` (inclusive) and `toc` (exclusive)

```{literalinclude} Makefile
:start-at: prune
:end-before: toc
```

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

+++

### the file name

```{literalinclude} Makefile
:filename: my-fake-name

```

+++

License CC BY-NC-ND, Thierry Parmentelat
