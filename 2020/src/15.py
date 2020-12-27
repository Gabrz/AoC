# https://adventofcode.com/2020/day/15

# Read the file
def readFile():
  with open("data/15.txt", "r") as fp:
    lines = [[int(x) for x in line.rstrip().split(',')] for line in fp.readlines()]
  return lines[0]


# Calculate Last Num Spoken
def getNumSpoken(data, turns):
  num_spoken = data.pop()
  num_dict = dict(map(reversed, enumerate(data)))
  turn = len(data)

  while turn < turns-1:
    if num_spoken in num_dict:
      num_new = turn - num_dict[num_spoken]
      num_dict[num_spoken] = turn
      num_spoken = num_new
    else:
      num_dict[num_spoken] = turn
      num_spoken = 0
    turn += 1
  return num_spoken


# Part One
def partOne(data):
  print(getNumSpoken(data, 2020))


# Part Two
def partTwo(data):
  print(getNumSpoken(data, 30000000))


partOne(readFile())
partTwo(readFile())
