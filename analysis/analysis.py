import os
import torch
import torchaudio
import requests
import matplotlib.pyplot as plt

class classAnalysis():
    def __init__(self, waveform_old, sample_rate_old, waveform_new, sample_rate_new):
        if (os.path.isfile("analysis.txt")):
            os.remove("analysis.txt")
        self.fd = open("analysis.txt", "a")

        if (sample_rate_old != None):
            self.two_wave = 1
            self.waveform_old = waveform_old
            self.sample_rate_old = sample_rate_old
        else:
            self.two_wave = 0

        self.waveform_new = waveform_new
        self.sample_rate_new = sample_rate_new

    def decrypt_sound(self, show):
        #waveform = torchaudio.functional.detect_pitch_frequency(waveform, sample_rate)
        #print(waveform)

        #waveform.common_utils.get_sinusoid()
        #print(torchaudio.functional.detect_pitch_frequency())

        self.data()
        self.fd.close()

        if (show == 1):
            self.show_sound()

    def show_sound(self):
        if (self.two_wave == 1):
            plt.figure()
            plt.plot(self.waveform_old.t().numpy())

        plt.figure()
        plt.plot(self.waveform_new.t().numpy())
        plt.show()

    def data(self):
        if (self.two_wave == 1):
            print("<-------------------->")
            print("Shape of waveform: {}".format(self.waveform_old.size()))
            print("Sample rate of waveform: {}".format(self.sample_rate_old))
            self.fd.write("Shape of waveform: {}\n".format(self.waveform_old.size()))
            self.fd.write("Sample rate of waveform: {}\n".format(self.sample_rate_old))

        print("<-------------------->")
        print("Shape of waveform: {}".format(self.waveform_new.size()))
        print("Sample rate of waveform: {}".format(self.sample_rate_new))
        self.fd.write("Shape of waveform: {}\n".format(self.waveform_new.size()))
        self.fd.write("Sample rate of waveform: {}\n".format(self.sample_rate_new))


def analysis(waveform_new, sample_rate_new, show, waveform_old=None, sample_rate_old=None):
    class_analysis = classAnalysis(waveform_old, sample_rate_old, waveform_new, sample_rate_new)
    
    class_analysis.decrypt_sound(show)
    return 0

path = "./daft-punk-one-more-time-official-video.wav"
waveform_old, sample_rate_old = torchaudio.load(path)
waveform_new, sample_rate_new = torchaudio.load("test.wav")
show = 1

analysis(waveform_new, sample_rate_new, show, waveform_old=waveform_old, sample_rate_old=sample_rate_old)