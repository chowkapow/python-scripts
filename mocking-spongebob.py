import random

def mockingSpongeBob(word):
  msb = ''
  caps = 0
  allowed = len(word) / 2
  for c in word:
    if caps <= allowed and bool(random.getrandbits(1)):
      c = c.upper()
      caps += 1
    msb += c
  return msb

text = input('Enter text: ')

words = text.split()

wordsMSB = [mockingSpongeBob(word) for word in words]

print (" ".join(wordsMSB))
