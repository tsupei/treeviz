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
root.visualize(line_space=2)

