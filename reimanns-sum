# Reimann's Sum

# Background: A Reimann's sum is an approximation of an integral.
# The sum is calculated by dividing the area under the curve into rectangles,
# calculating the area of each rectangle, and adding all these areas together.

# Write a function that returns a function which computes the Reimann's sum
# of a curve with limits a to b.

# Function signature:
# I(f, d) should return F(a, b) which should return the sum
# where f is the curve,
#       d is the delta (width of the rectangle)
#       a is the lower limit
#       b is the upper limit


def I(f, d):

    def F(a, b):
        sum = 0
        for i in range((b-a)/d):
            sum += d * f(a + (i*d))

        return sum

    return F
