# Use string indexing and string concatenation
# to write the sentence "we see trees" only by picking
# the necessary letters from the given string.

word = "tweezers "

we = word[1:3]
see = word[-2] + word[2:4]
trees = word[0] + word[-3] + word[2:4] + word[-2] 

print(we + ' ' + see + ' ' + trees)
