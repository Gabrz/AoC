# https://adventofcode.com/2020/day/10

# Read the file
def readFile():
  with open("data/10.txt", "r") as fp:
    lines = [int(line.rstrip()) for line in fp.readlines()]
  # Append Min and Max and return sorted data
  lines.append(0)
  lines.append(max(lines)+3)
  return sorted(lines)


def partOne(data):
  sol = {}
  prev = data[0]
  for i, curr in enumerate(data, start=1):
    # Calculate difference and increment counter in Object
    diff = curr - prev
    if diff in sol:
      sol[diff] += 1
    else:
      sol[diff] = 1
    prev = curr

  # return product
  print(sol[1] * sol[3])


def partTwo(data):
  # Create object with first item from list, set amount to 1
  sol = {data.pop(0): 1}
  for d in data:
    # Add placeholder for current item in Object
    sol[d] = 0
    # Check if previous values exist and add their amount to current item
    if d-1 in sol:
      sol[d] += sol[d-1]
    if d-2 in sol:
      sol[d] += sol[d-2]
    if d-3 in sol:
      sol[d] += sol[d-3]

  # return the amount of max(data)
  print(sol[max(data)])


partOne(readFile())
partTwo(readFile())
