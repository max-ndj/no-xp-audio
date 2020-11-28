import os
import torch
import torchaudio
import requests
import matplotlib.pyplot as plt

class classAnalysis():
    def __init__(self, path):
        if (os.path.isfile("analysis.txt")):
            os.remove("analysis.txt")
        self.fd = open("analysis.txt", "a")
        
        self.path = path

    def decrypt_sound(self, show):
        waveform, sample_rate = torchaudio.load_wav(self.path)
        #waveform, sample_rate = torchaudio.info(self.path)

        self.waveform = waveform
        self.sample_rate = sample_rate

        print("Shape of waveform: {}".format(waveform.size()))
        print("Sample rate of waveform: {}".format(sample_rate))

        #waveform.common_utils.get_sinusoid()
        #print(torchaudio.functional.detect_pitch_frequency())

        self.data()
        self.fd.close()

        if (show == 1):
            self.show_sound()

    def show_sound(self):
        plt.figure()
        plt.plot(self.waveform.t().numpy())
        plt.show()

    def data(self):
        self.fd.write("Shape of waveform: {}\n".format(self.waveform.size()))
        self.fd.write("Sample rate of waveform: {}\n".format(self.sample_rate))



def analysis(path, show):
    class_analysis = classAnalysis(path)
    
    class_analysis.decrypt_sound(show)

    return 0

path = "./daft-punk-one-more-time-official-video.wav"
show = 1

analysis(path, show)