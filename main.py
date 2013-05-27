# This program converts a sch kicad schematic description file into latex source code that can be compiled using the package circuitikz
# The proper kicad library must be used to obtain good results
#
#author: Vladimir Cravero - vladimircravero@gmail.com

# This file contains all the supported devices classes
from devices import *

# This file contains all the constants needed around
import const
        
"""Begin of main program"""
        
# Opening the files:
try:
    f_in = open(const.__INPUT_FILE_NAME__, "r")
except IOError as e:
    print "IO Error opening the input file({0}): {1}\n".format(e.errno, e.strerror)
except:
    print "Unexpected error({0}): {1}\n", sys.exc_info()[0]

try:
    f_out = open(const.__OUT_FILE_NAME__, "w")
except IOError as e:
    print "IO Error opening the output file({0}): {1}\n".format(e.errno, e.strerror)
except:
    print "Unexpected error({0}): {1}\n", sys.exc_info()[0]
    
try:
    f_header = open(const.__TEK_HEADER_FILE_NAME__, "r")
except IOError as e:
    print "IO Error opening the input file({0}): {1}\n".format(e.errno, e.strerror)
except:
    print "Unexpected error({0}): {1}\n", sys.exc_info()[0]

# Writing the header
# WARNING: out will be erased at this point!
for line in f_header:
    f_out.write(line)

f_header.close()
f_out.close()

# We need to open f_out in append mode
try:
    f_out = open(const.__OUT_FILE_NAME__, "a")
except IOError as e:
    print "IO Error opening the output file({0}): {1}\n".format(e.errno, e.strerror)
except:
    print "Unexpected error({0}): {1}\n", sys.exc_info()[0]
    
# Parser

for line in f_in:
    if const.__WIRE__ in line:
        print "Wire found!"
        line = f_in.next()
        f_out.write(Wire(line).to_tek())
    elif const.__JUNCTION__ in line:
        print "Junction found!"
        f_out.write(Junction(line).to_tek())
    elif const.__NO_CONNECT__ in line:
        print "No connect found!"
        f_out.write(NoConnect(line).to_tek())
    elif const.__COMPONENT__ in line:
        # Now that's a challenge
        print "Component found!"
        component_block = ""
        while const.__END_COMPONENT__ not in line:
            component_block = component_block + line
            line = f_in.next()
        component_block = component_block + line
        c = Component(component_block)
        c.parse()
        f_out.write(c.to_tek())
    
            
#appending the footer            
f_out.write(const.__TEK_FOOTER__)

# Don't forget to close all the files  
f_in.close()
f_out.close()