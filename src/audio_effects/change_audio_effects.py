import torchaudio

class audio_effects():
    def change_audio_frequency(self, waveform, sample_rate, new_sample_rate):
        new_waveform = torchaudio.transforms.Resample(sample_rate, new_sample_rate)(waveform[0,:].view(1, -1))
        return (new_waveform, new_sample_rate)

    def apply_flanger(self, waveform, sample_rate, delay, depth):
        new_waveform = torchaudio.functional.flanger(waveform, sample_rate, delay, depth)
        return (new_waveform)

    def apply_earrape(self, waveform, gain):
        new_waveform = torchaudio.functional.overdrive(waveform, gain)
        return (new_waveform)

    def apply_phaser(self, waveform, sample_rate, gain_in, gain_out, delay_ms):
        new_waveform = torchaudio.functional.phaser(waveform, sample_rate, gain_in, gain_out, delay_ms)
        return (new_waveform)