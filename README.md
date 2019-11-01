# treeviz
Visualize tree structure in bash manner using python

# install

```bash
git clone git@github.com:tsupei/treeviz.git
cd treeviz
python setup.py sdist
pip install ./dist/treeviz-1.0.tar.gz
```

# Usage

Create Your tree structure

```python
from treeviz.treeviz import Node
root = Node("Jason")
child1 = Node("Mary")
child2 = Node("John")
grandson1 = Node("Kevin")
grandson2 = Node("Doris")
grandson3 = Node("James")
grandson4 = Node("Momo")
grandgrandson1 = Node("Baby")

root.add_child(child1)
root.add_child(child2)
child1.add_child(grandson1)
child1.add_child(grandson2)
child2.add_child(grandson3)
child2.add_child(grandson4)
grandson1.add_child(grandgrandson1)
root.visualize()

```

```bash
Jason
├── Mary
│   ├── Kevin
│   │   └── Baby
│   └── Doris
└── John
    ├── James
    └── Momo
```

You can also print the sub-tree structure

```python
child1.visualize()
```

```bash
Mary
├── Kevin
│   └── Baby
└── Doris
```

Two options are provided, to print in terminal or print to file
```python

# print to file
# Giving path as the first parameter
root.visualize(".")

# If path is empty, then print to terminal
root.visualize()

# Default name is treeviz.txt, if the filename already exists, a number will be appended to it.

```

# New Features

(*2019.11.1*) Adding `max_len` parameter to `visualize()`, which splits the message into multiple lines.

```python
from treeviz.treeviz import Node
root = Node("Jason is our grandfather")
child1 = Node("Mary is Kevin's mother")
child2 = Node("John is Kevin and Doris's father")
grandson1 = Node("Kevin")
grandson2 = Node("Doris")
grandson3 = Node("James")
grandson4 = Node("Momo")
grandgrandson1 = Node("Baby")

root.add_child(child1)
root.add_child(child2)
child1.add_child(grandson1)
child1.add_child(grandson2)
child2.add_child(grandson3)
child2.add_child(grandson4)
grandson1.add_child(grandgrandson1)
root.visualize(max_len=10)
```

```bash
Jason is our grandfather
├── Mary is Ke
│   vin's moth
│   er
│   ├── Kevin
│   │   └── Baby
│   └── Doris
└── John is Ke
    vin and Do
    ris's fath
    er
    ├── James
    └── Momo
```
















