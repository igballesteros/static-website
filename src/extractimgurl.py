
import re

def extract_markdown_images(text):
	text_copy = text
	regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
	matches = re.findall(regex, text_copy)
	return matches

def extract_markdown_links(text):
	text_copy = text
	regex = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
	matches = re.findall(regex, text_copy)
	return matches

