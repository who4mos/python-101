# If a runner runs 10 miles in 30 minutes and 30 seconds,
# What is their average speed in kilometers per hour?
# (Tip: 1 mile = 1.6 km)

miles = 10
time = 30.5

# finds how many miles the runner runned in 1 minute
miles_per_minute = miles / time

miles_per_hour =  miles_per_minute * 60
kms_per_hour = miles_per_hour * 1.6

print("KMs/h: " + str(kms_per_hour))
