import sys

with open(sys.argv[1]) as csvfile:
    for line in csvfile:
        print("\t".join(line.strip().split(',')))
