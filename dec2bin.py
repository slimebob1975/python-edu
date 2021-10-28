def dec2bin(x):
    if x > 0:
        if x % 2 == 0:
            return (dec2bin(x // 2) + "0").lstrip("0")
        else:
            return (dec2bin(x // 2) + "1").lstrip("0")
    else:
        return "0"
print(dec2bin(128))
        
