# This program converts a sch kicad schematic description file into latex source code that can be compiled using the package circuitikz
# The proper kicad library must be used to obtain good results
#
#author: Vladimir Cravero - vladimircravero@gmail.com

# Generic imports
#!/usr/bin/env python

import sys

# This file contains all the supported devices classes
from devices import *

# This file contains all the constants needed around
from const import *

"""Begin of main program"""

print "This is schToTek v{0}\nOpening files...".format(VERSION)
# Opening the files:
try:
    f_in = open(INPUT_FILE_NAME, "r")
except IOError as e:
    print "IO Error opening the input file({0}): {1}\n".format(e.errno, e.strerror)
    sys.exit(-1)
except:
    print "Unexpected error({0}): {1}\n", sys.exc_info()[0]
    sys.exit(-1)

try:
    f_out = open(OUT_FILE_NAME, "w")
except IOError as e:
    print "IO Error opening the output file({0}): {1}\n".format(e.errno, e.strerror)
    sys.exit(-1)
except:
    print "Unexpected error({0}): {1}\n", sys.exc_info()[0]
    sys.exit(-1)
    
try:
    f_header = open(TEK_HEADER_FILE_NAME, "r")
except IOError as e:
    print "IO Error opening the input file({0}): {1}\n".format(e.errno, e.strerror)
    sys.exit(-1)
except:
    print "Unexpected error({0}): {1}\n", sys.exc_info()[0]
    sys.exit(-1)

# Writing the header
# WARNING: out will be erased at this point!
for line in f_header:
    f_out.write(line)

f_header.close()

print "Done. Starting parser..."

lines_parsed = 0
wires_count = 0
components_count = 0
junctions_count = 0
# Parser
for line in f_in:
    lines_parsed += 1
    if WIRE in line:
        line = f_in.next()
        lines_parsed += 1
        wires_count +=1
        f_out.write(Wire(line).to_tek())
    elif JUNCTION in line:
        f_out.write(Junction(line).to_tek())
        junctions_count += 1
    elif NO_CONNECT in line:
        f_out.write(NoConnect(line).to_tek())
    elif COMPONENT in line:
        components_count += 1
        component_block = ""
        while END_COMPONENT not in line:
            component_block = component_block + line
            line = f_in.next()
            lines_parsed += 1
        component_block = component_block + line
        c = Component(component_block)
        c.parse()
        f_out.write(c.to_tek())
           
#appending the footer            
f_out.write(TEK_FOOTER)

print "Done. Closing files..." 

# Don't forget to close all the files  
f_in.close()
f_out.close()

print "Read {0} lines".format(lines_parsed)
print "Parsed:\n{0} wire segments,\n{1} junctions,\n{2} components".format(wires_count, junctions_count, components_count)
