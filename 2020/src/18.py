# https://adventofcode.com/2020/day/18


OPERATORS = ['+', '*']


# Read the file
def readFile():
  with open("data/18.txt", "r") as fp:
    lines = [line.rstrip().replace(' ', '') for line in fp.readlines()]
  return lines


# Keep track of Parentheses
def countParenth(c):
  if c == '(':
    return 1
  elif c == ')':
    return -1
  else:
    return 0


# Determine the next Operator
def getNextOper(value):
  no_of_parenth = 0

  # Find the next operator (outside parentheses)
  for v in value:
    no_of_parenth += countParenth(v)
    if no_of_parenth == 0 and v in OPERATORS:
      return v


# Calculate result
def calcResult(input, mode):
  result = 0
  operator = '+'
  value = ''
  no_of_parenth = 0

  for i, char in enumerate(input):
    # Keep Track of Patentheses
    no_of_parenth += countParenth(char)

    if no_of_parenth > 0:
      # If we are inside parentheses, just keep adding chars
      value = value + char
    else:
      if char in OPERATORS:
        # Char is an operator, reset value
        operator = char
        value = ''
        # Part two, determine next operator
        if mode == 2 and char == '*' and getNextOper(input[i+1:]) == '+':
          # Recursive call to force addition to go first
          value = str(calcResult(input[i+1:], mode))
          result = eval(str(result) + operator + value)
          break

      else:
        value = value + char
        if len(value) > 1:
          # Recusive call to solve inside Parenteses
          value = str(calcResult(value[1:-1], mode))
        result = eval(str(result) + operator + value)

  return result


# Part One
def partOne(data):
  total = 0
  for d in data:
    total += calcResult(d, 1)
  print(total)


# Part Two
def partTwo(data):

  total = 0
  for d in data:
    total += calcResult(d, 2)
  print(total)


partOne(readFile())
partTwo(readFile())


# Test functions
def test(data, mode):
  print(str(10 if mode == 1 else 14), calcResult('2*3+4', mode))
  print(str(16 if mode == 1 else 20), calcResult('(2*3+4)+(2*3)', mode))
  print(str(26 if mode == 1 else 40), calcResult('2*(2*3+4)+(2*3)', mode))
  print(str(71 if mode == 1 else 231), calcResult('1+2*3+4*5+6', mode))
  print(str(51 if mode == 1 else 51), calcResult('1+(2*3)+(4*(5+6))', mode))
  print(str(26 if mode == 1 else 46), calcResult('2*3+(4*5)', mode))
  print(str(437 if mode == 1 else 1445), calcResult('5+(8*3+9+3*4*3)', mode))
  print(str(12240 if mode == 1 else 669060), calcResult('5*9*(7*3*3+9*3+(8+6*4))', mode))
  print(str(13632 if mode == 1 else 23340), calcResult('((2+4*9)*(6+9*8+6)+6)+2+4*2', mode))


# print('---')
# test(readFile(), 1)
# print('---')
# test(readFile(), 2)
