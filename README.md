# NO XP AUDIO
No xp audio is a software for editing and generating audio. In the program you can get the information of the audio tracks and analyze them with diagrams.

## INSTALL

### Linux:

```
pip3 install --user torch
pip install -U matplotlib
```

### Packages:

```
python3 main.py ...
```

### Example:

```python
python3 main.py -a --file test.wav --show
python3 main.py -m --file test.wav --name bite.wav --contrast 100
python3 main.py -m --contrast 100 --accelerate 40 && python3 main.py -g -m --file *.wav
```

### Credit:

Mathias RESSORT
Nathan HOCHE
Maximilien NADJI
Nassim GHARBAOUI