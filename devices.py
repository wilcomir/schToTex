import const

# Simple wire connection
class Wire:
    def __init__(self, line):
        coords = Wire.parse(line)
        self.c = [const.__MILS_TO_CM__ * x for x in coords]
   
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
        self.c = [const.__MILS_TO_CM__ * x for x in coords]
    
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
        self.c = [const.__MILS_TO_CM__ * x for x in coords]
    
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
        if self.dict["name"] == const.__RESISTOR__ or self.dict["name"] == const.__CAPACITOR__ or self.dict["name"] == const.__INDUCTOR__:
            # this component is a bilpole, the tek.lib is drawn so they can be rotated in the same manner
            x_start = x_end = self.dict["x"]
            y_start = y_end = self.dict["y"]
            if self.dict["o_01"] == -1:
                # left to right
                x_start -= 0.5
                x_end += 0.5
            elif self.dict["o_01"] == 1:
                # right to left
                x_start += 0.5
                x_end -= 0.5
            elif self.dict["o_00"] == -1:
                # down to up
                y_start -= 0.5
                y_end += 0.5
            elif self.dict["o_00"] == 1:
                # up to down
                y_start += 0.5
                y_end -= 0.5
            return "({0},{1}) to [{5}, l=${2}$] ({3},{4})\n".format(x_start, y_start, self.dict["reference"], x_end, y_end, self.dict["name"])
        else:
            return "%Component not supported. Sorry!\n"
            
    def parse(self):
        block_iterator = iter(self.block.splitlines())
        for line in block_iterator:
            while const.__END_COMPONENT__ not in line:
                line = block_iterator.next()
                if line.startswith(const.__COMP_LABEL__,0,len(const.__COMP_LABEL__)):
                    temp = line.strip().split(" ")
                    temp.pop(0)
                    self.dict["name"] = temp.pop(0)
                    self.dict["reference"] = temp.pop(0)
                elif line.startswith(const.__COMP_TIME__,0,len(const.__COMP_TIME__)):
                    temp = line.strip().split(" ")
                    temp.pop(0)
                    temp.pop(0)
                    temp.pop(0)  # Don't really know what the last two values are for
                    self.dict["time_stamp"] = temp.pop(0)
                elif line.startswith(const.__COMP_POS__,0,len(const.__COMP_POS__)):
                    temp = line.strip().split(" ")
                    temp.pop(0)
                    self.dict["x"] = int(temp.pop(0)) * const.__MILS_TO_CM__
                    self.dict["y"] = -int(temp.pop(0)) * const.__MILS_TO_CM__
                elif line.startswith(const.__COMP_FIELD__,0,len(const.__COMP_FIELD__)):
                    # Need to think about this
                    do_something=1
                elif line.startswith(const.__COMP_ENDING__,0,len(const.__COMP_ENDING__)):
                    # This line can be either the discontinued position line or the orientation matrix line
                    temp = line.strip().split()
                    if len(temp) == 4:
                        # That's an orientation matrix line!
                        self.dict["o_00"] = int(temp.pop(0))
                        self.dict["o_10"] = int(temp.pop(0))
                        self.dict["o_01"] = int(temp.pop(0))
                        self.dict["o_11"] = int(temp.pop(0))
                else:
                    # We should never fall down here
                    do_something=1

