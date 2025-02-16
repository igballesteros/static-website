import unittest
from extractimgurl import extract_markdown_images, extract_markdown_links

class TestExtractImgUrl(unittest.TestCase):

	def text_images(self):
		text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
		matches = extract_markdown_images(text)
		self.assertEqual(matches, [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])


	def test_url(self):
		text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
		matches = extract_markdown_links(text)
		self.assertEqual(matches, [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])

if __name__ == "__main__":
    unittest.main()
