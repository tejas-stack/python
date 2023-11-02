my_set={1,2,3,4}
my_set.add(5)
print(my_set)
my_set.remove(1)
my_set.discard(2)
print(my_set)
#operations in set 
'''union=union()
intersection=intersection()
difference=difference()
symmetric difference=symmetric_difference()'''
my_set2={1,5,7,8,9}
intersection=my_set.intersection(my_set2)
print(intersection)

myset1 = (1,2,3)
myset={4,5}
a = myset.union(myset1)
print(a)
#intersection 
#difference 
#symmetric difference
set1 = {1,2,3,4}
set2 = {4,5,6}

union_set = set1.union(set2)
print(union_set)
intersection_set = set1.intersection(set2)
print(intersection_set)
difference_set = set1.difference(set2)
print(difference_set)
systemati_difference = set1.symmetric_difference(set2)
print(systemati_difference)

gym_members=['april','john','corey']
developers=['judy','corey','steven','jane','april']
result=set(gym_members).intersection(developers)
print(result)




