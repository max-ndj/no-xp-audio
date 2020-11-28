import sys

def generator():
    print("generator")

def modification(FilePath=None):
    print("modification")

def analyze(FilePath=None):
    print("analyze")
    print(FilePath)


def find_in_array(array, items):
    for value in array:
        if (value == items):
            return (0)
    return (-1)

class arg():
    def __init__(self):
        self.type = -1
        self.module = []
        self.pos_module = []
        self.params = []

    def check_argument(self):
        type_arg = ["-g", "-m", "-a", "--file"]
        params = [0, 0, 0, 1]
        need_params = 0
        y = 0
        for value in sys.argv:
            x = 0
            for arg in type_arg:
                if (arg[0] == '-' and arg[1] == '-' and arg == value
                and find_in_array(self.module, arg) == -1):
                    self.module.append(arg)
                    self.pos_module.append(y)
                    if (params[x] == 1):
                        need_params = 1
                    break
                elif (self.type == -1 and arg[0] == '-' and arg == value
                and find_in_array(self.module, arg) == -1):
                    self.module.append(arg)
                    self.type = x
                    break
                x += 1
            y += 1
        return (need_params)

    def get_params(self):
        pos = 0
        for value in self.module:
            if value == "--file":
                if (len(sys.argv) <= self.pos_module[pos] + 1):
                    print("Lose some arg")
                    exit(84)
                self.params.append(sys.argv[self.pos_module[pos] + 1])
                pos += 1

    def call_function(self):
        arg = ""
        pos = 0
        for value in self.module:
            if (value == "--file"):
                arg += "FilePath='" + self.params[pos] + "', "
                pos += 1
        if (self.type == 0):
            try:
                return eval("generator(" + arg + ")")
            except:
                print("bad argument")
        elif (self.type == 1):
            try:
                return eval("modification(" + arg + ")")
            except:
                print("bad argument")
        else:
            try:
                return eval("analyze(" + arg +")")
            except:
                print("bad argument")


arg = arg()
if (arg.check_argument() == 1):
    arg.get_params()
arg.call_function()