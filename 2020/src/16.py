# https://adventofcode.com/2020/day/16

field_ranges = []
field_positions = {}
tickets = []


# Read the file
def readFile():
  global field_ranges, tickets
  field_ranges = []
  tickets = []
  with open("data/16.txt", "r") as fp:
    your_ticket = False
    othr_ticket = False
    for line in fp.readlines():
      line = line.rstrip()
      if len(line) == 0:
        continue
      if your_ticket or othr_ticket:
        tickets.append([int(l) for l in line.split(',')])
        your_ticket = False
        continue
      if 'your ticket' in line:
        your_ticket = True
        continue
      if 'nearby tickets' in line:
        othr_ticket = True
        continue
      line = line.replace('or ', '').split(': ')
      field_ranges.append([line[0], [int(l) for l in line[1].replace(' ', '-').split('-')]])


# Part One
def partOne(data):
  error_rate = 0

  for ticket in tickets[1:]:
    for number in ticket:
      is_number_valid = False
      for f_range in field_ranges:
        if f_range[1][0] <= number <= f_range[1][1] or f_range[1][2] <= number <= f_range[1][3]:
          is_number_valid = True
        if is_number_valid:
          break
      if not is_number_valid:
        error_rate += number

  print(error_rate)


# Part Two
def partTwo(data):
  # Remove invalid tickets
  for ticket in tickets[1:]:
    for number in ticket:
      is_number_valid = False
      for f_range in field_ranges:
        if f_range[1][0] <= number <= f_range[1][1] or f_range[1][2] <= number <= f_range[1][3]:
          is_number_valid = True
        if is_number_valid:
          break
      if not is_number_valid:
        break
    if not is_number_valid:
      tickets.remove(ticket)

  # Calculate Invalid Field positions
  field_positions = {i: [ran[0] for ran in field_ranges] for i in range(len(tickets[0]))}
  for ticket in tickets[1:]:
    for i, number in enumerate(ticket):
      for f_range in field_ranges:
        if not (f_range[1][0] <= number <= f_range[1][1] or f_range[1][2] <= number <= f_range[1][3]):
          field_positions[i].remove(f_range[0])

  prev_pos = []
  total = 1
  for i in sorted(field_positions, key=lambda t: len(field_positions[t])):
    field = [f for f in field_positions[i] if f not in prev_pos]
    if field[0].startswith('departure'):
      total *= tickets[0][i]
    prev_pos = field_positions[i]

  print(total)


partOne(readFile())
partTwo(readFile())
