# functions and behavior of non-primetive data-types

# list - functions & behaviour

# declaration synatx
ls = [1, 2, 3, 4, 5, 0, 2, 1, 4]
ls2 = [9, 8, 7, 6]

# add-new items into the list - append()
ls.append(6)
print(ls)

# delete the item - pop()
ls.pop()
print(ls)

# count the no.of items in the list - len()
print(len(ls))

# sorting the list - sorted()
print(sorted(ls)) # ascending order is the default
print(sorted(ls, reverse=True)) # descending order

# count the occurance of an item - count()
print(ls.count(4))

# merge 2 or more lists into a single list - extend()
ls.extend(ls2)
print(ls)

# interview - based question
ls.append(ls2) # [1, 2, 3, 4, 5, 0, 2, 1, 4, [9, 8, 7, 6]]
ls.extend(ls2) # [1, 2, 3, 4, 5, 0, 2, 1, 4, 9, 8, 7, 6]
print(ls)


# tuple - functions & behaviour (immutable)

# declaration
tup = (1, 2, 3, 4, 5, 1, 1, 1, 1)

# len()
print(len(tup))

# count()
print(tup.count(1))

# index - tbd

# type - convertion

ls_tup = list(tup)
print(ls_tup)

tup3 = tuple(ls2)
print(tup3)
