import torchaudio

class audio_effects():
    def change_audio_frequency(self, waveform, sample_rate, value):
        new_waveform = torchaudio.transforms.Resample(sample_rate, value)(waveform[0,:].view(1, -1))
        return (new_waveform)

    def apply_flanger(self, waveform, sample_rate, delay, depth):
        new_waveform = torchaudio.functional.flanger(waveform, sample_rate, delay=delay, depth=depth)
        return (new_waveform)

    def apply_earrape(self, waveform, gain):
        new_waveform = torchaudio.functional.overdrive(waveform, gain=gain)
        return (new_waveform)

    def contrast(self, waveform, change_value):
        if (change_value >= 0 and change_value <= 100):
            new_waveform = torchaudio.functional.contrast(waveform, change_value)
        else:
            print("Contrast -> bad value: need to be a number between 0 and 100")
        return new_waveform