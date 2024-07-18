# A string is a sequence of characters used to store and represent text.
# In Python, strings are created by enclosing text in quotes.
# You can use single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).
# Triple quotes are useful for multi-line strings or strings containing both single and double quotes.

# Example of strings:
single_quote_string = 'Hello, world!'
double_quote_string = "Hello, world!"
triple_quote_string = """This is a string
that spans multiple lines."""

print(single_quote_string)
print(double_quote_string)
print(triple_quote_string)

# Strings can contain letters, numbers, symbols, and spaces.
# You can include special characters like newlines (\n) or tabs (\t) using escape sequences.

# To define a string, follow these rules:
# 1. Enclose your text in matching quotes (single, double, or triple).

# 2. To include a quote character inside a string, use the opposite type of quote or escape it with a backslash (\).
#    For example, "She said, 'Hello!'" or 'He said, "Hello!"' or "He said, \"Hello!\""

# 3. Strings are immutable, which means you cannot change individual characters after the string is created.
#    However, you can create new strings based on existing ones.

# Example of escaping quotes:
escaped_string = 'He said, "It\'s a beautiful day!"'
# Strings are commonly used for displaying messages, handling text input/output, and processing textual data.


st = "---Aman is a good boi---"
print(len(st)) # Prints the length of string.

print(st[::])

print("st.lower()--> ",st.lower())

print("st.upper()--> ",st.upper())

print("st.count()--> ",st.count("a"))

print("st.find()--> ",st.find("b"))

print("st.strip()--> ",st.strip("-"))

print("st.lstrip()--> ",st.lstrip("-"))

print("st.rstrip()--> ",st.rstrip("-"))