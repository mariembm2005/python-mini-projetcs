import re
pattern = "[A-Za-z0-9]+@[A-Za-z0-9]+.(com|org|net)"
if re.search(pattern,input()):
    print("valid email")
else:
    print("invalid email")