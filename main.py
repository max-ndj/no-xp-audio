import sys
import torchaudio

from contrast import audio_effect as contrast

cn = contrast()

debug = 1

def generator(name=""):
    print("generator")

def modification(FilePath=None, contrast=-1, name=""):
    print("modification")
    if (FilePath != None):
        waveform, sample_rate = torchaudio.load(FilePath)
        if (contrast != -1):
            waveform = cn.contrast(waveform, contrast)

        #saving file
        if (name == ""):
            torchaudio.save(FilePath, waveform, sample_rate)
        else:
            torchaudio.save(name, waveform, sample_rate)

def analyze(FilePath=None, show=0):
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
        type_arg = ["-g", "-m", "-a", "--file", "--contrast", "--name", "--show"]
        params = [0, 0, 0, 1, 1, 1, 1]
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
            if value == "--file" or value == "--contrast" or value == "--name" or value == "--show":
                if (len(sys.argv) <= self.pos_module[pos] + 1):
                    print("Lose some arg")
                    exit(84)
                self.params.append(sys.argv[self.pos_module[pos] + 1])
                pos += 1

    def call_function(self):
        global debug
        arg = ""
        pos = 0
        for value in self.module:
            if (value == "--file"):
                arg += "FilePath='" + self.params[pos] + "', "
                pos += 1
            elif (value == "--contrast"):
                arg += "contrast=" + self.params[pos] + ", "
                pos += 1
            elif (value == "--name"):
                arg += "name='" + self.params[pos] + "', "
                pos += 1
            elif (value == "--show"):
                arg += "show='" + self.params[pos] + "', "
                pos += 1
        if (self.type == 0 and debug == 0):
            try:
                return eval("generator(" + arg + ")")
            except:
                print("bad argument")
        elif (self.type == 1 and debug == 0):
            try:
                return eval("modification(" + arg + ")")
            except:
                print("bad argument")
        elif (debug == 0):
            try:
                return eval("analyze(" + arg +")")
            except:
                print("bad argument")
        elif (self.type == 0 and debug == 1):
            return eval("generator(" + arg + ")")
        elif (self.type == 1 and debug == 1):
            return eval("modification(" + arg + ")")
        else:
            return eval("analyze(" + arg +")")


arg = arg()
if (arg.check_argument() == 1):
    arg.get_params()
arg.call_function()