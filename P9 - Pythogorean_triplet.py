def problem_nine():
    for a in range(2, 500):
        for b in range(a + 1, 500):
            sqr_c = a**2 + b**2
            c = sqr_c**0.5
            if has_sqr_root(sqr_c) and a + b + c == 1000:
                return int(a * b * c)
                
def has_sqr_root(sqr_c):
    for i in range(2, 500):
        if i**2 == sqr_c:
            return True
    return False
                
print problem_nine()