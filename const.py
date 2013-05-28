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

# Strictly component related constants
__COMP_LABEL__ = "L"
__COMP_TIME__ = "U"
__COMP_POS__ = "P"
__COMP_FIELD__ = "F"
__COMP_ENDING__ = "\t"

# Components names
__RESISTOR__ = "R"
__CAPACITOR__ = "C"
__INDUCTOR__ = "L"
__NMOS__ = "NMOS"
__PMOS__ = "PMOS"
__GND__ = "GND"
# This converts from mils, used in .sch, to cm, used by circuitikz
__MILS_TO_CM__ = 0.002  

# Fuffa
__VERSION__ = "0.1"