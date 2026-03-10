import os
import numpy as np
import soundfile as sf

INPUT_FOLDER = "input_audio"
OUTPUT_FOLDER = "processed_audio"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def highpass(audio, samplerate, cutoff=80):
    rc = 1.0 / (cutoff * 2 * np.pi)
    dt = 1.0 / samplerate
    alpha = rc / (rc + dt)

    filtered = np.zeros_like(audio)
    filtered[0] = audio[0]

    for i in range(1, len(audio)):
        filtered[i] = alpha * (filtered[i-1] + audio[i] - audio[i-1])

    return filtered


def noise_gate(audio, threshold=0.02):
    return np.where(np.abs(audio) < threshold, 0, audio)


def normalize(audio, target=0.9):
    peak = np.max(np.abs(audio))
    if peak > 0:
        audio = audio * (target / peak)
    return audio


for filename in os.listdir(INPUT_FOLDER):
    if filename.endswith(".wav"):

        input_path = os.path.join(INPUT_FOLDER, filename)
        output_path = os.path.join(OUTPUT_FOLDER, filename)

        audio, samplerate = sf.read(input_path)

        # convert stereo → mono
        if len(audio.shape) > 1:
            audio = np.mean(audio, axis=1)

        # remove low rumble
        audio = highpass(audio, samplerate)

        # reduce hiss between words
        audio = noise_gate(audio)

        # make voice louder
        audio = normalize(audio)

        sf.write(output_path, audio, samplerate)

print("Processing complete.")
