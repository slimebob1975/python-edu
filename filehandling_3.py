myfile = './testfile.txt'
f = open(myfile, 'r')  # Öppna för endast läsning
f.close()
f = open(myfile, 'r+') # Öppna för läsning och skrivning
f.close()
f = open(myfile, 'w')  # Öppna för skrivning
f.close()
f = open(myfile, 'br') # Öppna binärfil för läsning
f.close()
f = open(myfile, 'ba+')# Öppna binär för läsning o tillägg
f.close()

