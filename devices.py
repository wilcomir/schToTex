#!/usr/bin/env python

from const import *

# Simple wire connection
class Wire:
    def __init__(self, line):
        coords = Wire.parse(line)
        self.c = [MILS_TO_CM * x for x in coords]
   
    def to_tek(self):
        return "({0},{1}) to ({2},{3})\n".format(self.c[0],-self.c[1],self.c[2],-self.c[3])
    
    @staticmethod
    def parse(line):
        coords = map(int, line.strip().split(" "))
        return coords

# Filled dot that indicates a connection         
class Junction:
    def __init__(self, line):
        coords = Junction.parse(line)
        self.c = [MILS_TO_CM * x for x in coords]
    
    def to_tek(self):
        return "({0},{1}) node[circ] {{}}\n".format(self.c[0],-self.c[1])
    
    @staticmethod
    def parse(line):
        temp = line.strip().split(" ")
        temp.pop(0)
        temp.pop(0)
        coords = map(int, temp)
        return coords

# Empty dot that indicates a no connect (cross in kicad)        
class NoConnect:
    def __init__(self, line):
        coords = NoConnect.parse(line)
        self.c = [MILS_TO_CM * x for x in coords]
    
    def to_tek(self):
        return "({0},{1}) node[ocirc] {{}}\n".format(self.c[0],-self.c[1])
    
    @staticmethod
    def parse(line):
        temp = line.strip().split(" ")
        temp.pop(0)
        temp.pop(0)
        coords = map(int, temp)
        return coords

# Generic component, will call other classes methods        
class Component:

    def __init__(self, text_block):
        self.block = text_block
        self.dict = {}
    def to_tek(self):
        if self.dict["name"] in BIPOLES:
            # this component can be drawn as a bipole, the tek.lib is drawn so they can be rotated in the same manner
            # TODO I really don't like this 0.5
            
            # TODO this if is here just as a temporary workaround, better use a dictionary.
            # if self.dict["name"] == NMOS:
                # self.dict["name"] = "Tnmos"
                # H_STEP = 0.8
            # elif self.dict["name"] == PMOS:
                # self.dict["name"] = "Tpmos"
                # H_STEP = 0.8
            # elif self.dict["name"] == NPN:
                # self.dict["name"] = "Tnpn"
                # H_STEP = 0.8
            # elif self.dict["name"] == PNP:
                # self.dict["name"] = "Tpnp"
                # H_STEP = 0.8
            # else:
                # H_STEP = 0.5
            
            x_start = x_end = self.dict["x"]
            y_start = y_end = self.dict["y"]
            mirror = False
            
            if self.dict["B"] == 1:
                # left to right
                x_start -= H_STEP
                x_end += H_STEP
                if self.dict["C"] == -1:
                    mirror = True
            elif self.dict["B"] == -1:
                # right to left
                x_start += H_STEP
                x_end -= H_STEP
                if self.dict["C"] == 1:
                    mirror = True
            elif self.dict["D"] == 1:
                # up to down
                y_start += H_STEP
                y_end -= H_STEP
                if self.dict["A"] == 1:
                    mirror = True
            elif self.dict["D"] == -1:
                # down to up
                y_start -= H_STEP
                y_end += H_STEP
                if self.dict["A"] == -1:
                    mirror = True
            if mirror:
                return "({0},{1}) to [{5}, l=${2}$, mirror] ({3},{4})\n".format(x_start, y_start, self.dict["reference"], x_end, y_end, TRANSLATE[self.dict["name"]])
            else:
                return "({0},{1}) to [{5}, l=${2}$] ({3},{4})\n".format(x_start, y_start, self.dict["reference"], x_end, y_end, TRANSLATE[self.dict["name"]])
        elif self.dict["name"] == GND:
            # Assuming ground is towards down
            # TODO must handle proper orientation!
            return "({0},{1}) node[ground]{{}}".format(self.dict["x"], self.dict["y"])
        # elif self.dict["name"] == NMOS or self.dict["name"] == PMOS:
            ## this component is a MOS transistor
            # print "mos found!"
            # return "({0},{1}) node[{2}]{{}}".format(self.dict["x"], self.dict["y"], self.dict["name"].lower())
            
        else:
            print "Unsupported component found!"
            return "%Component not supported. Sorry!\n"
            
    def parse(self):
        block_iterator = iter(self.block.splitlines())
        for line in block_iterator:
            while END_COMPONENT not in line:
                line = block_iterator.next()
                if line.startswith(COMP_LABEL,0,len(COMP_LABEL)):
                    temp = line.strip().split(" ")
                    temp.pop(0)
                    self.dict["name"] = temp.pop(0)
                    self.dict["reference"] = temp.pop(0)
                elif line.startswith(COMP_TIME,0,len(COMP_TIME)):
                    temp = line.strip().split(" ")
                    temp.pop(0)
                    temp.pop(0)
                    temp.pop(0)  # Don't really know what the last two values are for
                    self.dict["time_stamp"] = temp.pop(0)
                elif line.startswith(COMP_POS,0,len(COMP_POS)):
                    # Position line. WARNING: we must change y sign since the coordinates systems are different.
                    temp = line.strip().split(" ")
                    temp.pop(0)
                    self.dict["x"] = int(temp.pop(0)) * MILS_TO_CM
                    self.dict["y"] = -int(temp.pop(0)) * MILS_TO_CM
                elif line.startswith(COMP_FIELD,0,len(COMP_FIELD)):
                    # Need to think about this
                    do_something=1
                elif line.startswith(COMP_ENDING,0,len(COMP_ENDING)):
                    # This line can be either the discontinued position line or the orientation matrix line
                    temp = line.strip().split()
                    if len(temp) == 4:
                        # That's an orientation matrix line!
                        self.dict["A"] = int(temp.pop(0))
                        self.dict["B"] = int(temp.pop(0))
                        self.dict["C"] = int(temp.pop(0))
                        self.dict["D"] = int(temp.pop(0))
                else:
                    # We should never fall down here
                    do_something=1

