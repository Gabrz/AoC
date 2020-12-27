# https://adventofcode.com/2020/day/11

# import module to deepcopy an a list/Array
import copy

MAX_ROWS = 0
MAX_COLS = 0

EMP_SEAT = 0
OCC_SEAT = 1
NOT_SEAT = -1


def readFile():
  with open("data/11.txt", "r") as fp:
    # Convert line in 2D Array and convert chars to numbers
    lines = [[EMP_SEAT if l == 'L' else NOT_SEAT for l in list(line.rstrip())] for line in fp.readlines()]

  # Set Global Height and Width
  global MAX_ROWS, MAX_COLS
  MAX_ROWS = len(lines)-1
  MAX_COLS = len(lines[0])-1

  return lines


def getNeighbours1(data, row, col):
  neighbours = {0: 0, 1: 0}
  idx = [-1, 0, 1]
  for r in idx:
    for c in idx:
      rn = row+r
      cn = col+c
      # index not Smaller than 0 and larger than Max and not equal to itself
      if 0 <= rn <= MAX_ROWS and 0 <= cn <= MAX_COLS and not (rn == row and cn == col):
        neighbour = data[rn][cn]
        if neighbour != NOT_SEAT:
          # Seat found increment value
          if neighbour in neighbours:
            neighbours[neighbour] += 1

  return neighbours


def checkSeats1(data):
  new_data = copy.deepcopy(data)
  # loop Rows and Colums
  for i, row in enumerate(data):
    for j, col in enumerate(row):
      # Skip non seats
      if col != NOT_SEAT:
        nb = getNeighbours1(data, i, j)
        # Apply Rules
        if (col == EMP_SEAT and nb[OCC_SEAT] == 0) or (col == OCC_SEAT and nb[OCC_SEAT] > 3):
          # Flip values
          new_data[i][j] = abs(col-1)

  return new_data


def getNeighbours2(data, row, col):
  neighbours = {0: 0, 1: 0}
  idx = [-1, 0, 1]
  for r in idx:
    for c in idx:
      neighbour = NOT_SEAT
      rn = row+r
      cn = col+c
      while neighbour == NOT_SEAT:
        # index not Smaller than 0 and larger than Max and not equal to itself
        if 0 <= rn <= MAX_ROWS and 0 <= cn <= MAX_COLS and not (rn == row and cn == col):
          neighbour = data[rn][cn]
          if neighbour == NOT_SEAT:
            # Neighbour is not a seat
            rn = rn+r
            cn = cn+c
          else:
            # Neighbouring seat found
            neighbours[neighbour] += 1
            break
        else:
          # index out of Range, or equal to itself
          break

  return neighbours


def checkSeats2(data):
  new_data = copy.deepcopy(data)
  # loop Rows and Colums
  for i, row in enumerate(data):
    for j, col in enumerate(row):
      # Skip non seats
      if col != NOT_SEAT:
        nb = getNeighbours2(data, i, j)
        # Apply Rules
        if (col == EMP_SEAT and nb[OCC_SEAT] == 0) or (col == OCC_SEAT and nb[OCC_SEAT] > 4):
          # Flip values
          new_data[i][j] = abs(col-1)

  return new_data


def countOccSeats(data):
  total = 0
  for row in data:
    for col in row:
      if col == OCC_SEAT:
        total += 1

  return total


def partOne(data):
  prev = -1
  curr = 0
  while prev != curr:
    prev = curr
    data = checkSeats1(data)
    curr = countOccSeats(data)

  print(curr)


def partTwo(data):
  prev = -1
  curr = 0
  while prev != curr:
    prev = curr
    data = checkSeats2(data)
    curr = countOccSeats(data)

  print(curr)


partOne(readFile())
partTwo(readFile())
