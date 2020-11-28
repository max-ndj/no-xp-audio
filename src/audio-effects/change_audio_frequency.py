import torchaudio

class audio_effects():
    def decelerate_audio_frequency(self, waveform, sample_rate, new_sample_rate):
        new_waveform = torchaudio.transforms.Resample(sample_rate, new_sample_rate)(waveform[0,:].view(1, -1))
        return (new_waveform, new_sample_rate)

    def accelerate_audio_frequency(self, waveform, sample_rate, new_sample_rate):
        new_waveform = torchaudio.transforms.Resample(sample_rate, new_sample_rate)(waveform[0,:].view(1, -1))
        return (new_waveform, new_sample_rate)