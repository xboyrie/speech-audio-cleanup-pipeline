import os
import numpy as np
import soundfile as sf

INPUT_FOLDER = "input_audio"
OUTPUT_FOLDER = "processed_audio"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def remove_dc(audio):
    return audio - np.mean(audio)


def highpass(audio, samplerate, cutoff=100):
    rc = 1.0 / (2 * np.pi * cutoff)
    dt = 1.0 / samplerate
    alpha = rc / (rc + dt)

    filtered = np.zeros_like(audio)
    filtered[0] = audio[0]

    for i in range(1, len(audio)):
        filtered[i] = alpha * (filtered[i-1] + audio[i] - audio[i-1])

    return filtered


def rms_normalize(audio, target_db=-16):
    rms = np.sqrt(np.mean(audio**2))
    if rms == 0:
        return audio

    current_db = 20 * np.log10(rms)
    gain = 10 ** ((target_db - current_db) / 20)

    return audio * gain


def lowpass(audio, samplerate, cutoff=5000):
    rc = 1.0 / (2 * np.pi * cutoff)
    dt = 1.0 / samplerate
    alpha = dt / (rc + dt)

    filtered = np.zeros_like(audio)
    filtered[0] = audio[0]

    for i in range(1, len(audio)):
        filtered[i] = filtered[i-1] + alpha * (audio[i] - filtered[i-1])

    return filtered


for filename in os.listdir(INPUT_FOLDER):

    if filename.endswith(".wav"):

        input_path = os.path.join(INPUT_FOLDER, filename)
        output_path = os.path.join(OUTPUT_FOLDER, filename)

        audio, samplerate = sf.read(input_path)

        # convert stereo to mono
        if len(audio.shape) > 1:
            audio = np.mean(audio, axis=1)

        # remove DC offset
        audio = remove_dc(audio)

        # remove rumble
        audio = highpass(audio, samplerate, cutoff=100)

        # normalize loudness
        audio = rms_normalize(audio)

        # prevent clipping
        peak = np.max(np.abs(audio))
        if peak > 1:
            audio = audio / peak

        # remove hiss (final stage)
        audio = lowpass(audio, samplerate, cutoff=5000)

        sf.write(output_path, audio, samplerate)


print("Processing complete.")
