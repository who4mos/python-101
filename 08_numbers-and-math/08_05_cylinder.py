# Write the necessary code calculate the volume and surface area
# of a cylinder with a radius of 3.14 and a height of 5.
# Print out the result.

pi = 3.14
radius = 3.14
height = 5

volume = pi * radius ** 2 * height
surface =  2 * pi * radius * (height + radius)

print("Volume: " + str(volume))
print("Surface area: " + str(surface))
