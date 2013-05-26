# This program converts a sch kicad schematic description file into latex source code that can be compiled using the package circuitikz
# The proper kicad library must be used to obtain good results
#
#author: Vladimir Cravero - vladimircravero@gmail.com

# This file contains all the supported devices classes
from devices import *

# These are the files that will be processed
__INPUT_FILE_NAME__ = "kicad/test.sch"
__OUT_FILE_NAME__ = "out.tek"

# Header and footer are necessary to generate a ready-to-compile tek file
__TEK_HEADER_FILE_NAME__ = "header.txt"
__TEK_FOOTER__ = "; \\end{circuitikz}\n\n\\end{document}"

# These strings will be used in the parser. Informations on the .sch file can be found here:
# http://en.wikibooks.org/wiki/Kicad/file_formats#Schematic_Files_Format
__WIRE__ = "Wire Wire Line"
__COMPONENT__ = "$Comp"
__END_COMPONENT__ = "$EndComp"
__JUNCTION__ = "Connection ~"
__NO_CONNECT__ = "NoConn ~"
        
        
"""Begin of main program"""
        
# Opening the files:
try:
    f_in = open(__INPUT_FILE_NAME__, "r")
except IOError as e:
    print "IO Error opening the input file({0}): {1}\n".format(e.errno, e.strerror)
except:
    print "Unexpected error({0}): {1}\n", sys.exc_info()[0]

try:
    f_out = open(__OUT_FILE_NAME__, "w")
except IOError as e:
    print "IO Error opening the output file({0}): {1}\n".format(e.errno, e.strerror)
except:
    print "Unexpected error({0}): {1}\n", sys.exc_info()[0]
    
try:
    f_header = open(__TEK_HEADER_FILE_NAME__, "r")
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
    f_out = open(__OUT_FILE_NAME__, "a")
except IOError as e:
    print "IO Error opening the output file({0}): {1}\n".format(e.errno, e.strerror)
except:
    print "Unexpected error({0}): {1}\n", sys.exc_info()[0]
    
# Parser

for line in f_in:
    if __WIRE__ in line:
        print "Wire found!"
        line = f_in.next()
        f_out.write(Wire(line).to_tek())
    elif __JUNCTION__ in line:
        print "Junction found!"
        f_out.write(Junction(line).to_tek())
    elif __NO_CONNECT__ in line:
        print "No connect found!"
        f_out.write(NoConnect(line).to_tek())
    elif __COMPONENT__ in line:
        print "Component found!"
    
            
#appending the footer            
f_out.write(__TEK_FOOTER__)

# Don't forget to close all the files  
f_in.close()
f_out.close()