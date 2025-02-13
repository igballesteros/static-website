from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
	def __init__(self, tag, children, props=None):
		super().__init__(tag, None, children, props)


	def to_html(self):
		if self.tag == None:
			raise ValueError("Tag not set to a value")
		if self.children == None:
			raise ValueError("Children not set to a value")

		parent_tag = self.tag
		final_string = f"<{parent_tag}>"

		for child in self.children:
			final_string += f"{child.to_html()}"
		
		final_string += f"</{parent_tag}>"
		return final_string

	def __repr__(self):
		return f"ParentNode({self.tag}, children: {self.children}, {self.props})"






node = ParentNode(
	"p",
	[
		LeafNode("b", "Bold text"),
		LeafNode(None, "Normal Text"),
		LeafNode("i", "italic text"),
		LeafNode(None, "normal text"),
	],
)
print(node.to_html())