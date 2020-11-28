import os
import torch
import torchaudio
import requests
import matplotlib.pyplot as plt

class classAnalysis():
    def __init__(self, path):
        os.remove("analysis.txt")
        self.fd = open("analysis.txt", "a")
        self.path = path

    def decrypt_sound(self):
        waveform, sample_rate = torchaudio.load(self.path)

        self.waveform = waveform
        self.sample_rate = sample_rate

        print("Shape of waveform: {}".format(waveform.size()))
        print("Sample rate of waveform: {}".format(sample_rate))

        plt.figure()
        plt.plot(waveform.t().numpy())

        self.data()
        self.fd.close()
    
    def data(self):
        self.fd.write("Shape of waveform: {}\n".format(self.waveform.size()))
        self.fd.write("Sample rate of waveform: {}\n".format(self.sample_rate))



def analysis(path):
    class_analysis = classAnalysis(path)
    
    class_analysis.decrypt_sound()

    return 0

path = "./test.wav"

analysis(path)