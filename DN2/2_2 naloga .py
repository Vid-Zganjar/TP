our_list = [1,2,3,4,5,6,7]
our_dict = {
    "a": 2,
    "b": 5,
    "c": 8,
    "d": 12,
    "e": 357,
    "f": 12
}
our_tuple = (357, 12, 12, 8, 5, 2, 2)

d=our_list[4]
nov_tuple=[]
for key, x in our_dict.items():
    nov_tuple.append(x)
print(nov_tuple)
print(our_tuple)
print("Ali sta tabeli isti:",our_tuple==nov_tuple)
