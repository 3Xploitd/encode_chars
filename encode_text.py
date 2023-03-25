import sys

def encode_text(string):
    text = []
    for line in string:
        line = hex(ord(line))
        text.append(f'chr({line})')
    print("+".join(text))
    
    
encode_text(sys.argv[1])
