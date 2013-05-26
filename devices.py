__MILS_TO_CM__ = 0.002  # This converts from mils, used in .sch, to cm, used by circuitikz

# Simple connection
class Wire:
    def __init__(self, line):
        coords = Wire.parse(line)
        self.c = [__MILS_TO_CM__ * x for x in coords]
   
    def to_tek(self):
        return "({0},{1}) to ({2},{3})\n".format(self.c[0],-self.c[1],self.c[2],-self.c[3])
    
    @staticmethod
    def parse(line):
        coords = map(int, line.strip().split(" "))
        return coords
        
class Junction:
    def __init__(self, cords):
        self.c = [__MILS_TO_CM__ * x for x in coords]
    
    def to_tek(self):
        return "({0},{1}) node[circ] {}\n".format(self.c[0],-self.c[1])