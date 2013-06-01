# These are the files that will be processed
INPUT_FILE_NAME = "kicad/test.sch"
OUT_FILE_NAME = "out.tek"

# Header and footer are necessary to generate a ready-to-compile tek file
TEK_HEADER_FILE_NAME = "header.txt"
TEK_FOOTER = "; \\end{circuitikz}\n\n\\end{document}"

# These strings will be used in the parser. Informations on the .sch file can be found here:
# http://en.wikibooks.org/wiki/Kicad/file_formats#Schematic_Files_Format
WIRE = "Wire Wire Line"
COMPONENT = "$Comp"
END_COMPONENT = "$EndComp"
JUNCTION = "Connection ~"
NO_CONNECT = "NoConn ~"

# Strictly component related constants
COMP_LABEL = "L"
COMP_TIME = "U"
COMP_POS = "P"
COMP_FIELD = "F"
COMP_ENDING = "\t"

# Components names
RESISTOR = "R"
CAPACITOR = "C"
INDUCTOR = "L"
NMOS = "NMOS"
PMOS = "PMOS"
NPN = "NPN"
PNP = "PNP"
GND = "GND"

# Translation dictionary, from kicad name to circuitikz name

TRANSLATE = {
    RESISTOR : "R",
    CAPACITOR : "C",
    INDUCTOR : "L",
    NMOS : "Tnmos",
    PMOS : "Tpmos",
    NPN : "Tnpn",
    PNP : "Tpnp",
    GND : "GND",
}

# Bipoles set. This are not bipoles actually but they can be drawn in the same way.
BIPOLES = {RESISTOR, CAPACITOR, INDUCTOR, NMOS, PMOS, NPN, PNP}
# This converts from mils, used in .sch, to cm, used by circuitikz
MILS_TO_CM = 0.002
# This is used to calculate start and stop position for from..to syntax (half step)
# TODO this must change, it is not constant through all the components.
H_STEP = 0.5

# Fuffa
VERSION = "0.1"