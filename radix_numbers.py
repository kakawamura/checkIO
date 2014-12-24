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



print checkio('AF', 16)
print checkio('101', 2)
print checkio('101', 5)
print checkio('Z', 36)
print checkio('AB', 10)

