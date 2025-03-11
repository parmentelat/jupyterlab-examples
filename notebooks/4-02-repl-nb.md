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

# a simple REPL - MyST

using MyST syntax with triple backticks - here with `replite` we can in theory get a REPL

```{replite}
:kernel: python
:theme: JupyterLab Light
:width: 100%
:height: 500px
:prompt: click to start a replite with numpy
:prompt_color: gray

# please be patient ...

import sys
major, minor, *_ = sys.version_info
print(f"Hello from a JupyterLite console! in Python {major}.{minor}\n")

import numpy as np
print(np.arange(9).reshape((3, 3)))
```

+++

## inside dropdowns

like for images this needs to go inside a `{div}` thingy  
demo'ing pandas as well... NOTE that here `titanic.csv` is under `data/` in the git repo, but we configure `jupyterlite-sphinx` to take its contents from `data/` and eventually `titanic.csv` is in `.` inside the jlite runtime environment)


`````{admonition} a hidden repl with pandas this time
:class: dropdown

````{div}
```{replite}
:kernel: python
:theme: JupyterLab Light
:width: 100%
:height: 500px
:prompt: click for a pandas example
:prompt_color: pink

print('Hello from a JupyterLite console!')

import pandas as pd
df = pd.read_csv("titanic.csv", index_col="PassengerId")
df.head()
```
````
`````

+++

License CC BY-NC-ND, Thierry Parmentelat
