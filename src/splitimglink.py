from textnode import TextType, TextNode
from extractimgurl import extract_markdown_images, extract_markdown_links


def split_nodes_image(old_nodes):
	new_nodes = []
	for node in old_nodes:
		print(node)
		if node.text_type != TextType.TEXT:
			new_nodes.append(node)
		else:
			text = node.text
			matches = extract_markdown_images(text)
			for match in matches:
				text = text.replace(match[0], "")
				text = text.replace(match[1], "")
				text = text.translate({ord(i): None for i in "[]()"})
				print(text)


def split_nodes_link(old_nodes):
	pass


node = TextNode(
    "This is text with an image ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
)
new_nodes = split_nodes_image([node])