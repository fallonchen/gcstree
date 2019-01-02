class Node:
	def __init__(self, name):
		self.name = name
		self._children = []

	def add_child(self, child_node):
		self._children.append(child_node)
		return child_node

	def add_children(self, *children):
		self._children.extend(children)

	def find_child_by_name(self, name):
		matches = [c for c in self._children if c.name == name]
		return None if not matches else matches[0]
	
	def dfs(self, level=0):
		print level * "\t" + self.name   
		if not self._children:
			return
		level += 1
		for child in self._children:
			child.dfs(level) 

	def add_from_path(self, path):
		if not path:
			raise Exception

		current_dir = path.pop(0)

		if current_node.name != current_dir:
			raise Exception

		if path:
			next_dir = current_node.find_child_by_name(path[0])
			if not next_dir:
				next_dir = current_node.add_child(Node(path[0]))

			add_to_tree(next_dir, path)
		
def test_setup():
	root = Node("a")
	b = Node("b")
	b.add_child(Node("d"))
	b.add_child(Node("f"))
	c = Node("c")
	c.add_child(Node("g"))
	e = Node("e")
	root.add_children(b, c, e)

	return root

def test(r):
	r.dfs()

def test_find_child(r):
	print r.find_child_by_name("b").name
	print r.find_child_by_name("k")


#test_find_child(test_setup())
#test(test_setup())

			
