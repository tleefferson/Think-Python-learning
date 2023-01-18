def print_lyrics():  
  print("some lyrics") 
  print("some more lyrics")

def print_twice(bruce):
  print(bruce)
  print(bruce)
  
def cat_twice(part1, part2):
  cat = part1 + part2
  print_twice(cat)
  
line1 = "bing tiddle "
line2 = "tiddle bang "
cat_twice(line1, line2)
  
## Excercise 1
def right_justify(s):
  spaces = 70 - len(s)
  print(" " * spaces + s)

## Excercise 2

def do_twice(f):
  f()
  f()
  
def print_spam():
  print('spam')

def do_four(f):
  do_twice(f)
  do_twice(f)
  
## Excercise 3

def plus_row():
  print("+ - - - - + - - - - +")
  
def line_row():
  print("/         /         /")
  
def print_2x2():
  plus_row()
  do_four(line_row)
  plus_row()
  do_four(line_row)
  plus_row()
  


  
