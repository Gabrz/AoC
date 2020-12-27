# https://adventofcode.com/2020/day/17

# import module to deepcopy an a list/Array
import copy


# Global variables
cubes = {}


# Get Indexes of Neighbouring Cubes
def getNeighbours(c):
  idx = [-1, 0, 1]
  if len(c) == 3:
    neighbours = [(c[0]+x, c[1]+y, c[2]+z)
                  for x in idx for y in idx for z in idx
                  if not (x == 0 and y == 0 and z == 0)]
  elif len(c) == 4:
    neighbours = [(c[0]+x, c[1]+y, c[2]+z, c[3]+w)
                  for x in idx for y in idx for z in idx for w in idx
                  if not (x == 0 and y == 0 and z == 0 and w == 0)]
  return neighbours


# Count Active Neighbours
def countNeighbours(neighbours, tcubes):
  return sum([tcubes[nb] for nb in neighbours if nb in tcubes])


# check status of a Cube
def checkCube(cube, value, tcubes, neighbours):
  active = countNeighbours(neighbours, tcubes)
  if value == 1:
    if active not in [2, 3]:
      cubes[cube] = 0
  else:
    if active == 3:
      cubes[cube] = 1


# Cycle the cubes
def cycleCubes():
  # Store the old state in temp_cubes
  temp_cubes = copy.deepcopy(cubes)
  for cube in temp_cubes:
    # Check a cube against its neighbours
    value = cubes[cube]
    neighbours = getNeighbours(cube)
    checkCube(cube, value, temp_cubes, neighbours)

    if value == 1:
      # Add neighbours that not yet exist to cubes
      for n in neighbours:
        if n not in temp_cubes:
          # Get neighbours of neighbours and determine their state
          neighbours = getNeighbours(n)
          checkCube(n, 0, temp_cubes, neighbours)


# Part One
def partOne():
  with open("data/17.txt", "r") as fp:
    lines = [line.rstrip() for line in fp.readlines()]

  # Read lines into cubes dict, replace chars with 1 or 0
  global cubes
  cubes = {}
  for y in range(len(lines)):
    for x in range(len(lines[0])):
      cubes[(x, y, 0)] = 1 if lines[y][x] == '#' else 0

  for i in range(6):
    cycleCubes()

  print(sum(cubes.values()))


# Part Two
def partTwo():
  with open("data/17.txt", "r") as fp:
    lines = [line.rstrip() for line in fp.readlines()]

  # Read lines into cubes dict, replace chars with 1 or 0
  global cubes
  cubes = {}
  for y in range(len(lines)):
    for x in range(len(lines[0])):
      cubes[(x, y, 0, 0)] = 1 if lines[y][x] == '#' else 0

  for i in range(6):
    cycleCubes()

  print(sum(cubes.values()))


partOne()
partTwo()
