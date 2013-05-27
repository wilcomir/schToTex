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
        if self.dict["name"] == const.__RESISTOR__:
            # We must draw a resistor! I'm assuming it is horizontal now.
            return "({0},{1}) to [R, l=${2}$] ({3},{4})\n".format(self.dict["x"]-0.5, self.dict["y"], self.dict["reference"], self.dict["x"]+0.5, self.dict["y"])
        else:
            return "%Component not supported. Sorry!\n"
            
    def parse(self):
        block_iterator = iter(self.block.splitlines())
        for line in block_iterator:
            while const.__END_COMPONENT__ not in line:
                line = block_iterator.next()
                print line
                if line.startswith(const.__COMP_LABEL__,0,1):
                    temp = line.strip().split(" ")
                    temp.pop(0)
                    self.dict["name"] = temp.pop(0)
                    self.dict["reference"] = temp.pop(0)
                elif line.startswith(const.__COMP_TIME__,0,1):
                    temp = line.strip().split(" ")
                    temp.pop(0)
                    temp.pop(0)
                    temp.pop(0)  # Don't really know what the last two values are for
                    self.dict["time_stamp"] = temp.pop(0)
                elif line.startswith(const.__COMP_POS__,0,1):
                    temp = line.strip().split(" ")
                    temp.pop(0)
                    self.dict["x"] = int(temp.pop(0)) * const.__MILS_TO_CM__
                    self.dict["y"] = -int(temp.pop(0)) * const.__MILS_TO_CM__
                elif line.startswith(const.__COMP_FIELD__,0,1):
                    # Need to think about this
                    do_something=1
                elif line.startswith(const.__COMP_ALT_POS__,0,1):
                    # This should never be used because it is discontinued
                    do_something=1
                else:
                    # Should really check this out
                    do_something=1

