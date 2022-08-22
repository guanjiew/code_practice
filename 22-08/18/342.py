def isPowerOfFour(num):
    # power of 4 must be a power of 2
    # and the only one bit must be in the even position
    # Create a mask with every even bit set to 1 and every odd bit set to 0
    # And the number with the mask, the result should be 0 if 1 only appears in the even position
    return num > 0 and (num & (num - 1)) == 0 and (num & 0xAAAAAAAA) == 0

