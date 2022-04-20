# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

three_sides_triangle = print("Enter the lengths of three side of a triangle: ")
a_side = input("a: ")
b_side = input("b: ")
c_side = input("c: ")

if a_side == b_side == c_side:
    print(f"A triangle with sides of {a_side}, {b_side}, & {c_side} is a equalateral triangle")
elif a_side != b_side != c_side:
    print(f"A triangle with sides of {a_side}, {b_side}, & {c_side} is a scalene triangle")
elif a_side == b_side != c_side:
    print(f"A triangle with sides of {a_side}, {b_side}, & {c_side} is a isoceles triangle")



# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

#equal sides in length

#scalene all three sides are unequal in length

#isosceles two sides are the same length