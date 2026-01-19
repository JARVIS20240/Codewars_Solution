"""
Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep count in the array (true means count).

For example,

[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
"""

sheep = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]

# Way-1
# def count_sheeps(sheep):
#   # TODO May the force be with you
#   count = 0
#   for s in sheep:
#     if s == True :
#       count+= s
#   return count

# print(count_sheeps(sheep))

# Way-2
# def sheep_count(sheep):
#     return sum(sheep)

# print(sheep_count(sheep))

# Way-3
def count_sheeps(arrayOfSheeps):
  return arrayOfSheeps.count(True)
print(count_sheeps(sheep))