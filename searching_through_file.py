fhand =open ("read_file.2.py")
for line in fhand:
    if line.startswith("x"):
        print(line)