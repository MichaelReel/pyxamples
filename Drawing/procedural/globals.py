# Colour minimum and maximum values
min = 0
max = 255

# Standard bit shifting functions
# really just to differentiate logical and arithmetic right shift
def rshift_log(val, n):
    """Logical right shift"""
    return (val % 0x100000000) >> n

def rshift_ari(val, n):
    """Arithmetic right shift"""
    return val >> n

def lshift(val, n):
    """Left shift"""
    return val << n