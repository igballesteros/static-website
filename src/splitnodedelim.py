from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
	new_nodes = []
	for node in old_nodes:
		if node.text_type != TextType.TEXT:
			new_nodes.append(node)
		else:
			text = node.text
			if text.count(delimiter) % 2 != 0:
				raise Exception("Enter valid markdown syntax")
			blocks = text.split(delimiter)
			for i in range(len(blocks)):
				if blocks[i] != "":
					if i % 2 == 1:
						node = [TextNode(blocks[i], text_type)]
						new_nodes.extend(node)
					else:
						node = [TextNode(blocks[i], TextType.TEXT)]
						new_nodes.extend(node)
	return new_nodes



# node1 = TextNode("Hello `code` world", TextType.TEXT)
# node2 = TextNode("**bold text**", TextType.BOLD)
# node3 = TextNode("Plain text no code", TextType.TEXT)
# node4 = TextNode("Start `code` middle `more code` end", TextType.TEXT)

# nodes = [node1, node2, node3, node4]

# new_nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

# for node in new_nodes:
# 	print(node)
