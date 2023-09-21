import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))

"""$ python prog.py -h
usage: prog.py [-h] [--sum] N [N ...]

Process some integers.

positional arguments:
 N           an integer for the accumulator

options:
 -h, --help  show this help message and exit
 --sum       sum the integers (default: find the max)"""

"""$ python prog.py 1 2 3 4
4

$ python prog.py 1 2 3 4 --sum
10"""

"""$ python prog.py a b c
usage: prog.py [-h] [--sum] N [N ...]
prog.py: error: argument N: invalid int value: 'a'"""

# How this all stuff work...
# The first step in using the argparse is creating an ArgumentParser object:

parser = argparse.ArgumentParser(description='Process some integers.')  # just like this
# but what will this actually do?
# Well... The ArgumentParser object will hold all the information necessary to parse the command line into Python data types.

"""Filling an ArgumentParser with information about program arguments is done by making calls 
to the add_argument() method. Generally, these calls tell the ArgumentParser how 
to take the strings on the command line and turn them into objects.
 This information is stored and used when parse_args() is called. For example:"""



parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')

parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

"""Later, calling parse_args() will return an object with two attributes, integers and accumulate.
 The integers attribute will be a list of one or more integers,
  and the accumulate attribute will be either the sum() function,
 if --sum was specified at the command line, or the max() function if it was not."""


'''ArgumentParser parses arguments through the parse_args() method. This will inspect the command line, convert 
each argument to the appropriate type and then invoke the appropriate action. In most cases, this means a simple
 Namespace object will be built up from attributes parsed out of the command line:

##########################
 parser.parse_args(['--sum', '7', '-1', '42'])
##########################
Namespace(accumulate=<built-in function sum>, integers=[7, -1, 42])


In a script, parse_args() will typically be called with no arguments, and the 
ArgumentParser will automatically determine the command-line arguments from sys.argv.
'''
