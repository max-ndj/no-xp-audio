import torchaudio

class audio_effect():
    def contrast(self, waveform, change_value):
        if (change_value >= 0 and change_value <= 100):
            waveform = torchaudio.functional.contrast(waveform, change_value)
        else:
            print("Contrast -> bad value: need to be a number between 0 and 100")
        return waveform