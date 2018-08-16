# Evenly Spaced

# Given three ints, a b c, one of them is small, one is medium and one is large. 
# Return true if the three values are evenly spaced, so the difference between 
# small and medium is the same as the difference between medium and large.


# evenlySpaced(2, 4, 6) → true
# evenlySpaced(4, 6, 2) → true
# evenlySpaced(4, 6, 3) → false

def evenlySpaced(a,b,c):

    nums = [a, b, c]
    nums.sort()

    diff1 = nums[1] - nums[0]
    diff2 = nums[2] - nums[1]

    if diff1 == diff2:
        return True
    else:
        return False
