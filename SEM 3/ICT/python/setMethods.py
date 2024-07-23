# method 1 to create set 
dogs = {"pitbull", "husky"}

# method 2 to create set
cats = set({"tiger", "lion"})

dogs.add("golden")
print(dogs)
print(len(dogs))

print(dogs.pop())

newSet = dogs.union(dogs,cats)
print(newSet)

dogs.remove("golden")
print(dogs)

dogs.clear()
print(dogs)