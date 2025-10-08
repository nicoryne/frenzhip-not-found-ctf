import sys
import ast

# the intuitive way to solve this would be
# to reverse the operations
# but looking at the pattern
# we can see that if we were to just
# ignore nested lists, we can actually
# flatten the whole thing and get the 
# hex flag

def exit():
  sys.exit(0)

# flatten one outer layer
# flatten_one_level([1, 2], [3, 4], 5]) =>
# [1, 2, 3, 4, 5]

def flatten_one_level(L):
  flat = []
  for item in L:
    if isinstance(item, list):
      flat.extend(item)
    else:
      flat.append(item)
  return flat


def descramble(L):
  A = L

  # for each sublist in our list
  for sublist in A:
    # we iterate over each element in
    # the sublist
    for index, element in enumerate(sublist):
      # if that element is also a list
      # we just pop it
      if isinstance(element, list):
        sublist.pop(index)
  # flatten everything to get the
  # clean list of hex
  return list(flatten_one_level(A))
  

def get_cipher():
  with open('ciphered_flag.txt', 'r') as f:
    c = f.read().strip()
  return ast.literal_eval(c) # converts our text to list

def main():
  cipher = get_cipher()
  hex_flag = descramble(cipher)
  # convert hex into character list
  list_flag = [chr(int(x,16)) for x in hex_flag]
  # standard join 
  flag = ''.join(list_flag)
  print(flag)

if __name__ == '__main__':
  main()
