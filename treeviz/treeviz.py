import os
import logging


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
		# child cannot be any ancestor
		cur = self
		while cur:
			if cur == child:
				raise ValueError("child should not be any of the ancestor")
			cur = cur.parent
		child.parent = self
		self.children.append(child)

		return child

	def __pack(self, value, prefix):
		return "{prefix}{value}".format(prefix="".join(prefix), value=value)

	def __dfs(self, descendants, buff, level, prefix, max_len, line_space):
		"""
		Using dfs to draw the tree
		args:
			descendants: all children nodes in current level
			buff (list): all lines going to print or save to file
			level:
			prefix:
			max_len: maximum length of per line
			line_space: space between lines
		"""
		# if descendants is empty, nothing will be executed
		for idx, descendant in enumerate(descendants):
			is_leaf = True if descendant.children else False
			cur_prefix = prefix[:]
			if idx != len(descendants)-1:
				end = len(descendant.value) // max_len + 1
				# split into multi-lines
				for i in range(0, end):
					if i == 0:
						buff.append(self.__pack(descendant.value[i*max_len:(i+1)*max_len], cur_prefix + ["├── "]))
					else:
						buff.append(self.__pack(descendant.value[i*max_len:(i+1)*max_len], cur_prefix + ["│   "]))
				# line space
				for i in range(0, line_space):
					if is_leaf:
						buff.append(self.__pack("│   ", cur_prefix + ["│   "]))
					else:
						buff.append(self.__pack("    ", cur_prefix + ["│   "]))
				cur_prefix.append("│   ")
			else:
				end = len(descendant.value) // max_len + 1
				# split into multi-lines
				for i in range(0, end):
					if i == 0:
						buff.append(self.__pack(descendant.value[i*max_len:(i+1)*max_len], cur_prefix + ["└── "]))
					else:
						buff.append(self.__pack(descendant.value[i*max_len:(i+1)*max_len], cur_prefix + ["    "]))
				# line space
				for i in range(0, line_space):
					if is_leaf:
						buff.append(self.__pack("│   ", cur_prefix + ["    "]))
					else:
						buff.append(self.__pack("    ", cur_prefix + ["    "]))
				cur_prefix.append("    ")
			self.__dfs(descendant.children, buff, level+1, cur_prefix, max_len, line_space)

	def visualize(self, path=None, filename=None, max_len=50, line_space=0):
		"""
		Visualize the tree using current node as root
		args:
			path: directory to save file
			filename: specified filename
			max_len: maximum length of per line
			line_space: space between lines
		"""
		buff = list()
		buff.append("{}".format(self.value))
		self.__dfs(self.children, buff, 0, [], max_len, line_space)

		if not path or not os.path.exists(path):
			# Print to terminal
			for buf in buff:
				print(buf)
		else:
			if not filename:
				filename = "treeviz.txt"
				logging.info("Default filename: {}".format(filename))
			filename_components = filename.rsplit(".", 1)
			if len(filename_components) != 2:
				filename = "treeviz.txt"
				logging.warning("filename should be .txt file")
				logging.info("Default filename: {}".format(filename))
			if filename_components[1] != 'txt':
				filename = "treeviz.txt"
				logging.warning("filename should be .txt file")
				logging.info("Default filename: {}".format(filename))
			path_to_file = "{}/{}".format(path, filename)
			version = 1

			while os.path.exists(path_to_file):
				new_filename = "{}_{}.{}".format(filename.rsplit(".", 1)[0], version, filename.rsplit(".", 1)[1])
				path_to_file = "{}/{}".format(path, new_filename)
				version += 1
			logging.info("file is saved to {}".format(path_to_file))
			with open(path_to_file, 'w', encoding="utf-8") as f:
				for buf in buff:
					f.write(buf)
					f.write("\n")
