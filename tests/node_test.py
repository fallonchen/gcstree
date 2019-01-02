import unittest
import gcstree
from gcstree.node import Node

class TestNodeMethods(unittest.TestCase):
	def setUp(self):
		root = Node("a")
		b = Node("b")
		b.add_child(Node("d"))
		b.add_child(Node("f"))
		c = Node("c")
		c.add_child(Node("g"))
		e = Node("e")
		root.add_children(b, c, e)

		self.root = root

	#def test_dfs(self):
	#	self.root.dfs()

	def test_find_child(self):	
		self.assertEqual(self.root.find_child_by_name("b").name, "b")
		self.assertEqual(self.root.find_child_by_name("k"), None)

		


if __name__ == "__main__":
	unittest.main()
