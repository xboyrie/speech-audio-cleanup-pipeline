import os
import numpy as np
import soundfile as sf

INPUT_FOLDER = "input_audio"
OUTPUT_FOLDER = "processed_audio"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for filename in os.listdir(INPUT_FOLDER):
    if filename.endswith(".wav"):

        input_path = os.path.join(INPUT_FOLDER, filename)
        output_path = os.path.join(OUTPUT_FOLDER, filename)

        audio, samplerate = sf.read(input_path)

        # normalize audio
        max_val = np.max(np.abs(audio))
        if max_val > 0:
            audio = audio / max_val

        sf.write(output_path, audio, samplerate)

print("Processing complete.")
