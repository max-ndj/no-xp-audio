import torchaudio

class audio_effect():
    def contrast(self, waveform, change_value):
        waveform = torchaudio.functional.contrast(waveform, change_value)
        return waveform