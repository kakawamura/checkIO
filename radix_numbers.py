def checkio(str_number, radix):
  sum = 0
  for i, exp in enumerate(range(len(str_number)-1, -1, -1)):
    if str_number[i].isdigit():
      sum += int(str_number[i]) * radix ** exp 
      if int(str_number[i]) >= radix:
        return -1
    else:
      sum += (ord(str_number[i]) - 55) * radix ** exp
      if (ord(str_number[i]) - 55) >= radix:
        return -1

  return sum

def solution(str_number, radix):
  try:
    return int(str_number, radix)
  except ValueError :
    return -1



print solution('AF', 16)
print solution('101', 2)
print solution('101', 5)
print solution('Z', 36)
print solution('AB', 10)

