import torchaudio

class audio_effects():
    def change_audio_frequency(self, waveform, sample_rate, new_sample_rate):
        new_waveform = torchaudio.transforms.Resample(sample_rate, new_sample_rate)(waveform[0,:].view(1, -1))
        return (new_waveform, new_sample_rate)

    def apply_flanger(self, waveform, sample_rate, delay, depth, regen, width, speed, phase, modulation, interpolation):
        new_waveform = torchaudio.functional.flanger(waveform, sample_rate, delay, depth, regen, width, speed, phase, modulation, interpolation)
        return (new_waveform)

    def apply_earrape(self, waveform, gain, colour):
        new_waveform = torchaudio.functional.overdrive(waveform, gain, colour)
        return (new_waveform)