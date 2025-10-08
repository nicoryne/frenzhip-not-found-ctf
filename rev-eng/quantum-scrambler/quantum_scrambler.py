import sys

def exit():
  sys.exit(0)

# How it works
def scramble(L):
  # assign flag reference
  A = L
  # Start at index 2
  i = 2
  
  # iterate 
  while (i < len(A)):
    # for better visualization, imagine we have
    # list of lists where 
    # list = [['a'], ['b'], ['c'], ['d']]
    # i = 2
    # attach i - 2th letter with i - 1th letter then
    # pop i - 1th position
    # list becomes [['a', 'b'], ['c'], ['d']]
    A[i-2] += A.pop(i-1)
    # append a slice of all earlier lists
    # to the i - 1th list
    # starting from position 0 all the way 
    # to i - 2th position, not including 
    # i - 2th
    # list becomes
    # [['a', 'b'], ['c', [['a', 'b']]], ['d']]
    A[i-1].append(A[:i-2])
    # iterate over
    i += 1
    
  return L


def get_flag():
  flag = open('flag.txt', 'r').read()
  flag = flag.strip()
  hex_flag = []
  for c in flag:
    hex_flag.append([str(hex(ord(c)))])

  return hex_flag

def main():
  flag = get_flag()
  cypher = scramble(flag)
  print(cypher)

if __name__ == '__main__':
  main()
