import os

class Node(object):
	def __init__(self, value):
		self.value = value
		self.parent = None
		self.children = [] 

	def is_valid(self):
		if not self.value:
			return False
		for child in self.children:
			if child.parent != self:
				return False
		return True

	def add_child(self, child):
		if type(child) != Node:
			return None
		self.children.append(child)
		return child

	def __visualize_child(self, value, prefix):
		return "{prefix}{value}".format(prefix=prefix, value=value)


	def __dfs(self, descendants, buff, level, prefix):
		# if descendants is empty, nothing will be excuted
		for idx, descendant in enumerate(descendants):
			cur_prefix = prefix[:]
			if idx != len(descendants)-1:
				cur_prefix.append("├── ")
				buff.append(self.__visualize_child(descendant.value, "".join(cur_prefix)))
				cur_prefix.pop()
				cur_prefix.append("│   ")
			else:
				cur_prefix.append("└── ")
				buff.append(self.__visualize_child(descendant.value, "".join(cur_prefix)))
				cur_prefix.pop()
				cur_prefix.append("    ")
			self.__dfs(descendant.children, buff, level+1, cur_prefix)

	def visualize(self, path=None):
		# visualize sub-tree
		# buffer
		buff = []
		buff.append("{}".format(self.value))
		self.__dfs(self.children, buff, 0, [])

		if not path or not os.path.exists(path):
			# Print to terminal
			for buf in buff:
				print(buf)
		else:
			filename = "treeviz.txt"
			path_to_file = "{}/{}".format(path, filename)
			version = 1

			while os.path.exists(path_to_file):
				filename = "{}_{}.{}".format(filename.rsplit(".", 1)[0], version, filename.rsplit(".", 1)[1])
				path_to_file = "{}/{}".format(path,filename)
				version += 1
			with open(path_to_file, 'w', encoding="utf-8") as f:
				for buf in buff:
					f.write(buf)
					f.write("\n")