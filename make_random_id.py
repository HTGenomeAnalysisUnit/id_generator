#!/usr/bin/env python3

import random
import string
import sys
import argparse

ALLOWED_TYPES = ["LUP", "LLOW", "L", "D", "LD"]

# Generate random string of given length and type
def get_random_string(length, type="LUP"):
    # choose from all uppercase letter
    if type == "LUP":
        items = string.ascii_uppercase
    elif type == "LLOW":
        items = string.ascii_lowercase
    elif type == "L":
        items = string.ascii_letters
    elif type == "D":
        items = string.digits
    elif type == "LD":
        items = string.ascii_uppercase + string.digits

    result_str = ''.join(random.choice(items) for i in range(length))
    return result_str

# Generate random id based on pattern (list of elements)
def get_id(pattern):
    id_toks = []
    for x in pattern:
        if x.startswith("@"):
            toks = x.strip("@").split("x")
            id_toks.append(get_random_string(int(toks[0]), toks[1]))
        else:
            id_toks.append(x)
    return "".join(id_toks)

# Parse pattern string into list of elements
def parse_pattern(pattern_string):
    elements = []
    e = ""
    for x in pattern_string:
        if x == "@":
            if e != "":
                elements.append(e)
                e = "" if e.startswith("@") else "@" # reset
            else:
                e += x
        else:
            e += x
    if e != "":
        elements.append(e)
    return elements

# Check if elements in the pattern are correct
def check_pattern(pattern):
    print(f"Parsed elements: {pattern}")
    for x in pattern:
        if x.startswith("@"):
            toks = x.strip("@").split("x")
            if len(toks) < 2:
                print(f"Error: element {x} is not correct")
                sys.exit(1)
            if toks[1] not in ALLOWED_TYPES:
                print(f"Error: type {toks[1]} for element {x} is not correct")
                print(f"Allowed types are {ALLOWED_TYPES}")
                sys.exit(1)
        else:
            if len(x) < 1:
                print(f"Error: element {x} is not correct")
                sys.exit(1)

# Parse arguments and set vars
parser = argparse.ArgumentParser(description='Make random id')
inputs = parser.add_mutually_exclusive_group()
inputs.add_argument('-i', '--input', help='Input file. One random id will be generated per line')
inputs.add_argument('-n', '--number', help='Number of random id to create', type=int)

parser.add_argument('-o', '--output', help='Output file', required=True)
parser.add_argument('-p', '--pattern', help='Pattern, like "AA_@3xLU@-@2xD@"', required=True)
parser.add_argument('--no_head', action="store_false", help='Input file has no header and no header in output')
args = parser.parse_args()

inputfile=args.input
outfile=args.output
pattern=args.pattern
n_ids=args.number

# Initial logging
print("=== ARGUMENTS ===")
print("Input file is ", inputfile)
print("Output file is ", outfile)
print("Pattern is ", pattern)
print("Number of ids to generate is ", n_ids)
print("=================")

# Parse pattern and check if it is correct
pattern = parse_pattern(pattern)
check_pattern(pattern)

outf = open(outfile, "w")

print("Generating random ids...")
# Input is a file
if inputfile:
    # Check if input file exists, raise error otherwise
    try:
        f = open(inputfile)
        f.close()
    except IOError:
        print(f"Error: {inputfile} does not exist")
        sys.exit(1)

    # Read input file and generate random ids
    is_header = args.no_head
    with open(inputfile) as f:
        for line in f:
            line = line.rstrip("\n")
            if is_header:
                outf.write(f"{line}\trandom_id\n")
                is_header = False
            else:
                rnd_id = get_id(pattern)
                outf.write(f"{line}\t{rnd_id}\n")
else:
# Input is a number of ids to generate
    if n_ids < 1:
        print(f"Error: number of random ids {n_ids} is not correct")
        sys.exit(1)
    if args.no_head:
        outf.write("random_id\n")
    for i in range(n_ids):
        rnd_id = get_id(pattern)
        outf.write(f"{rnd_id}\n")

outf.close()

print("Done")