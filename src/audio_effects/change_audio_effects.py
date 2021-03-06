import torchaudio

class audio_effects():
    def change_audio_frequency(self, waveform, sample_rate, frequency):
        new_waveform = torchaudio.transforms.Resample(sample_rate, frequency)(waveform[0,:].view(1, -1))
        return (new_waveform)

    def apply_flanger(self, waveform, sample_rate, delay, depth):
        if (delay < 0 or delay > 30):
            print("Delay value is incorrect")
            return (waveform)
        elif (depth < 0 or depth > 10):
            print("Depth value is incorrect")
            return (waveform)
        new_waveform = torchaudio.functional.flanger(waveform, sample_rate, delay, depth)
        return (new_waveform)

    def apply_earrape(self, waveform, gain):
        if (gain < 0 or gain > 100):
            print("Gain value is incorrect")
            return (waveform)
        new_waveform = torchaudio.functional.overdrive(waveform, gain)
        return (new_waveform)

    def apply_phaser(self, waveform, sample_rate, gain_in, gain_out, delay_ms):
        if (gain_in < 0 or gain_in > 1):
            print("Gain_in value is incorrect")
            return (waveform)
        elif (gain_out < 0 or gain_out > 1e9):
            print("Gain_out value is incorrect")
            return (waveform)
        elif (delay_ms < 0 or delay_ms > 5.0):
            print("Delay_ms value is incorrect")
            return (waveform)
        new_waveform = torchaudio.functional.phaser(waveform, sample_rate, gain_in, gain_out, delay_ms)
        return (new_waveform)

    def contrast(self, waveform, change_value):
        if (change_value >= 0 and change_value <= 100):
            new_waveform = torchaudio.functional.contrast(waveform, change_value)
            return new_waveform
        else:
            print("Contrast -> bad value: need to be a number between 0 and 100")
            return waveform