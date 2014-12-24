def find_message(text):
    return "".join(c for c in text if c.isupper())

print find_message("How are you? Eh, ok. Low or Lower? Ohhh.") 
print find_message("hello world!")
print find_message("HELLO WORLD!!!")
