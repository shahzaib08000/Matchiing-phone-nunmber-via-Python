import re
Text = "Please contact me at +1 (123) 456-7890 ot at my email john@gmail.com or at my office number +1-987-654-3210. Thank you!"
# Regular expression pattern for phone numbers
pattern = r"\+?\d{1,3}[-.\s]?\(/?\d{1,3}\)?[-.\s]?\d{1,3}[-.\s]?\d{1,4}"
# Find all phone numbers in the text

phone_number = re.findall(pattern, Text)

print(phone_number)

