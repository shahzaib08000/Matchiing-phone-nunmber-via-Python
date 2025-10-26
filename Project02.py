import re
Text = "Contact me on John123@gamil.com or visit my website at http://example.com for more info."
# Regular expression pattern for matching email addresses
pattern = r"[a-zA-Z0-9.-_%+]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
# Find all email addresses in the text
emails = re.findall(pattern, Text)
print("Extracted Email addresses:", emails)