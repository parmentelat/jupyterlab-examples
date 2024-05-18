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

# a pruned TP

+++

to operate the nbprune workflow

the topic is for you to write a graph parser

given a file that looks like this

```
s1 10 s2
s2 20 s1
s2 30 s3
s3 20 s4
```

your code should

- open and read the file
- and return a `dict` that looks like this

```python
{'s1': [('s2', 10)], 's2': [('s1', 20), ('s3', 30)], 's3': [('s4', 20)]}
```

```{code-cell} ipython3
# prune-begin

from collections import defaultdict

def graphdict(filename):
    result = defaultdict(list)
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            src, dist, dst = line.split()
            result[src].append( (dst, int(dist)) )
    return result
            
```

```{code-cell} ipython3
with open("graphdict.txt", "w") as w:
    print("""
          s1 10 s2
          s2 20 s1
          s2 30 s3
          s3 20 s4
          """, file=w)
```

```{code-cell} ipython3
dict(graphdict("graphdict.txt"))
```

```{code-cell} ipython3
# prune-end
```

```{code-cell} ipython3
# your code here
def graphdict(filename):
    pass
```
