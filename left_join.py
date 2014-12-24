#Elementary
#Right to Left
#Created at: Decemeber 14th 2014

def left_join(phrase):
  for i in range(0,len(phrase)):

    if phrase[i].find("right"):
      phrase[i] = "right"

  return phrase

print left_join(("left","right"))

