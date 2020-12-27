# https://adventofcode.com/2020/day/12

# import module to deepcopy an a list/Array
import copy


def readFile():

  with open("data/12.txt", "r") as fp:
    # Convert line in 2D Array
    lines = [[line[0], line[1:]] for line in fp.readlines()]
  return lines


# Directions lookup by index.
# Angles are devided by 90 to get index
# i.e. N=0  --> 180/90=2=S
DIRECTIONS = ['N', 'E', 'S', 'W']
POS_SHIP = [0, 0, 0, 0]
POS_WAYP = [1, 10, 0, 0]


def rotate(heading, direction, angle):
  # Get current Angle
  cur_ang = DIRECTIONS.index(heading)
  # Caculate new Angle
  ang = angle if direction == 'R' else -angle
  ang = int(ang / 90)  # Divide by 90 to get Index value
  new_ang = (cur_ang + ang) % len(DIRECTIONS)
  # return new Heading
  return DIRECTIONS[new_ang]


def rotateWayPoint(direction, angle):
  tmp_wayp = copy.deepcopy(POS_WAYP)

  for i, pos in enumerate(tmp_wayp):
    # Get heading based on i(ndex)
    head = DIRECTIONS[i]
    # Rotate the heading
    new_head = rotate(head, direction, angle)
    # Get new (rotated) index
    new_i = DIRECTIONS.index(new_head)
    # Update the value of the new index
    POS_WAYP[new_i] = pos


def move(object, heading, units):
  # Get Index based on Heading
  i = DIRECTIONS.index(heading)
  # Update object with value
  object[i] += units


def moveShip(times):
  # Get position of WayPoint
  pos_wayp = getPos(POS_WAYP)
  # Move ship along the longitude (N,S)
  i_lon = 1 + (-1 if pos_wayp['lon'] > 0 else 1)
  move(POS_SHIP, DIRECTIONS[i_lon], times * abs(pos_wayp['lon']))
  # Move ship along the lattitude (E,W)
  i_lat = 2 + (-1 if pos_wayp['lat'] > 0 else 1)
  move(POS_SHIP, DIRECTIONS[i_lat], times * abs(pos_wayp['lat']))


def moveWayPoint(heading, units):
  move(POS_WAYP, heading, units)


def getPos(object):
  pos = {}
  # Longitude is North minus South
  pos['lon'] = object[0] - object[2]
  # Lattitude is East minus West
  pos['lat'] = object[1] - object[3]

  return pos


# Part One
def partOne(data):
  # Set current heading
  heading = 'E'
  for d in data:
    action = d[0]
    units = int(d[1])
    if action in ['L', 'R']:
      heading = rotate(heading, action, units)
    elif action == 'F':
      move(POS_SHIP, heading, units)
    else:
      move(POS_SHIP, action, units)

  # Get position of Ship
  pos_ship = getPos(POS_SHIP)
  print(abs(pos_ship['lon'] - abs(pos_ship['lat'])))


# Part Two
def partTwo(data):
  # Reset Postition of ship
  global POS_SHIP
  POS_SHIP = [0, 0, 0, 0]
  for d in data:
    action = d[0]
    units = int(d[1])
    if action in ['L', 'R']:
      rotateWayPoint(action, units)
    elif action == 'F':
      moveShip(units)
    else:
      moveWayPoint(action, units)

  # Get position of Ship
  pos_ship = getPos(POS_SHIP)
  print(abs(pos_ship['lon'] - abs(pos_ship['lat'])))


partOne(readFile())
partTwo(readFile())
