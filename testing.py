#sample testing/ rough usage 
"""print("Aman")
print("Aman")
print("Aman")
print("Aman\n"*3, end="")
for i in [0,1,2]:
    print("Aman")
i=3
while i !=0:
    print("Aman")
    i=(i-1)"""
n=3
"""def meow(n):
    print("meow")"""

def main():
    print_square(3)


def print_square(size):

    # For each row in square
    for i in range(size):

        # For each brick in row
        for j in range(size):

            #  Print brick
            print("#", end="")

        # Print blank line
        print()


main()