#accepting arguments
# we are going to use SYS module

# import sys

# print("hello Caliber")
# name = sys.argv[1]
# print("Hello " + name)



import argparse
parser = argparse.ArgumentParser(
    description = "This program prints the name of my dogs"
)

# parser.add_argument('-c','--color', metavar='color',required=True, help='the color to search for')
parser.add_argument('-c','--color', metavar='color',required=True, choices={'red','yellow','blue'}, help='the color to search for')


args = parser.parse_args()

print(args.color)