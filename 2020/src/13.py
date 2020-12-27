# https://adventofcode.com/2020/day/13


# Read the file
def readFile():
  with open("data/13.txt", "r") as fp:
    lines = [line for line in fp.readlines()]

  lines[0] = int(lines[0])
  lines[1] = ['x' if l == 'x' else int(l) for l in lines[1].split(',')]

  return lines


# Part One
def partOne(data):
  dep_time = data[0]
  busses = [d for d in data[1] if d != 'x']
  time_table = dict({bus: 0 for bus in busses})

  while len(busses) > 0:
    for bus in busses:
      time = time_table[bus]+bus
      time_table[bus] = time
      if time > dep_time:
        busses.remove(bus)

  min_bus = min(time_table, key=time_table.get)
  print((time_table[min_bus]-dep_time)*min_bus)


# Part two with chinese remainder theory
# def partTwo(data):
#   busses = dict({bus: -i % bus for i, bus in enumerate(data[1]) if bus != 'x'})
#   vals = list(reversed(sorted(busses)))
#   r = vals[0]
#   val = busses[r]

#   for b in vals[1:]:
#     while val % b != busses[b]:
#       val += r
#     r *= b
#   print(val)

def partTwo(data):
  busses = [[bus, i] for i, bus in enumerate(data[1]) if bus != 'x']

  lcm = 1
  tme = 0
  for i in range(len(busses)-1):
    bus = busses[i+1]
    lcm *= busses[i][0]
    while (tme+bus[1]) % bus[0] != 0:
      tme += lcm
  print(tme)


partOne(readFile())
partTwo(readFile())
