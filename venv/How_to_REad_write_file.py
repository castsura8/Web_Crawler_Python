
fw = open('simple.txt', 'w')
fw.write('writting some stuff in my text is cool\n')
fw.write('this is so cool to write on text')
fw.close()


r = open('simple.txt', 'r')

text = r.read()

print(text)


