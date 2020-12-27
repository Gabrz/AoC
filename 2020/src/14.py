# https://adventofcode.com/2020/day/14


# Read the file
def readFile():
  with open("data/14.txt", "r") as fp:
    lines = [line.rstrip().split(' = ') for line in fp.readlines()]
  return lines


# Convert Decimal to Binary
def decToBin(d):
  return bin(d).replace("0b", "").rjust(36, '0')


# Format Value against the Mask
def getValue(mask, val):
  old_val = decToBin(val)
  new_val = ''
  for i in range(len(mask)):
    if mask[i] != 'X':
      new_val += mask[i]
    else:
      new_val += old_val[i]

  return int(new_val, 2)


# Format memory Ids against the Mask
def getMemories(mask, mem):
  old_mem = decToBin(mem)
  memories = ['']
  for i in range(len(mask)):
    if mask[i] == '0':
      new_char = old_mem[i]
    else:
      new_char = mask[i]

    for j, m in enumerate(reversed(memories)):
      if new_char == 'X':
        tmp_mem = memories[j]
        memories[j] += '0'
        memories.append(tmp_mem+'1')
      else:
        memories[j] += new_char

  return memories


# Part One
def partOne(data):
  mem_dict = {}
  for d in data:
    if d[0] == 'mask':
      mask = d[1]
    else:
      value = getValue(mask, int(d[1]))
      mem_dict[d[0][4:-1]] = value
  print(sum(mem_dict.values()))


# Part Two
def partTwo(data):
  mem_dict = {}
  for d in data:
    if d[0] == 'mask':
      mask = d[1]
    else:
      memories = getMemories(mask, int(d[0][4:-1]))
      for mem in memories:
        mem_dict[int(mem, 2)] = int(d[1])
  print(sum(mem_dict.values()))


partOne(readFile())
partTwo(readFile())
