import sys
import torchaudio

from src.audio_effects.change_audio_effects import audio_effects as audio_effect
from src.analysis.analysis import classAnalysis

ae = audio_effect()

debug = 1

def generator(name="", analyze=0, show=0):
    print("generator")

    if (analyze == 1):
        print("Appelle Analyze")
    

def modification(FilePath=None, analyze=0, contrast=-1, name=None, show=0, delay=-1, depth=-1, gain=-1, frequency=-1, gain_in=-1, gain_out=-1, delay_ms=-1):
    print("modification")
    if (FilePath != None):
        waveform, sample_rate = torchaudio.load(FilePath)
        if (analyze == 1):
            waveform_old = waveform
            sample_rate_old = sample_rate
        if (contrast != -1):
            print("contrast")
            waveform = ae.contrast(waveform, contrast)
        # if (frequency != -1):
        #    print("frequency")
        #    waveform = ae.change_audio_frequency(waveform, sample_rate, frequency)
        if (delay != -1 and depth != -1):
            print("flanger")
            waveform = ae.apply_flanger(waveform, sample_rate, delay, depth)
        if (gain != -1):
            print("gain")
            waveform = ae.apply_earrape(waveform, gain)
        if (gain_in != -1 and gain_out != -1 and delay_ms != -1):
            print("phaser")
            waveform = ae.apply_phaser(waveform, sample_rate, gain_in, gain_out, delay_ms)
        #saving file
        if (name == None):
            torchaudio.save(FilePath, waveform, sample_rate)
        else:
            torchaudio.save(name, waveform, sample_rate)
        if (analyze == 1):
            AnalyzeC = classAnalysis(waveform_old, sample_rate_old, waveform, sample_rate)
            AnalyzeC.decrypt_sound(show)

    
def analyze(FilePath=None, show=0):
    print("analyze")
    if (FilePath != None):
        waveform, sample_rate = torchaudio.load(FilePath)
        AnalyzeC = classAnalysis(None, None, waveform, sample_rate)
        AnalyzeC.decrypt_sound(show)


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
        type_arg = ["-g", "-m", "-a", "--file", "--analyze", "--contrast", "--fname", "--show", "--flanger", "--errape", "--frequency", "--phaser"]
        params = [0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1]
        need_params = 0
        y = 0
        for value in sys.argv:
            x = 0
            for arg in type_arg:
                if (arg[0] == '-' and arg[1] == '-' and arg == value
                and find_in_array(self.module, arg) == -1):
                    self.module.append(arg)
                    if (params[x] == 1):
                        self.pos_module.append(y)
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
            print(value)
            if value == "--file" or value == "--contrast" or value == "--fname" or value == "--errape" or value == "--frequency":
                if (len(sys.argv) <= self.pos_module[pos] + 1):
                    print("Lose some arg")
                    exit(84)
                self.params.append(sys.argv[self.pos_module[pos] + 1])
                pos += 1
            elif value == "--flanger":
                if (len(sys.argv) <= self.pos_module[pos] + 2):
                    print("Lose some arg")
                    exit(84)
                self.params.append(sys.argv[self.pos_module[pos] + 1])
                self.params.append(sys.argv[self.pos_module[pos] + 2])
                pos += 1
            elif value == "--phaser":
                if (len(sys.argv) <= self.pos_module[pos] + 3):
                    print("Lose some arg")
                    exit(84)
                self.params.append(sys.argv[self.pos_module[pos] + 1])
                self.params.append(sys.argv[self.pos_module[pos] + 2])
                self.params.append(sys.argv[self.pos_module[pos] + 3])
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
            elif (value == "--fname"):
                arg += "name='" + self.params[pos] + "', "
                pos += 1
            elif (value == "--show"):
                arg += "show=1, "
            elif (value == "--analyze"):
                arg += "analyze=1, "
            elif (value == "--flanger"):
                arg += "delay=" + self.params[pos] + ", depth=" + self.params[pos + 1] + ", "
                pos += 2
            elif (value == "--phaser"):
                arg += "gain_in=" + self.params[pos] + ", gain_out=" + self.params[pos + 1] + ", delay_ms=" + self.params[pos + 2] + ", "
                pos += 3
            elif (value == "--errape"):
                arg += "gain=" + self.params[pos] + ", "
                pos += 1
            elif (value == "--frequency"):
                arg += "frequency=" + self.params[pos] + ", "
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