import os
import subprocess

INPUT_FOLDER = "input_audio"
OUTPUT_FOLDER = "processed_audio"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for file in os.listdir(INPUT_FOLDER):
    if file.endswith(".wav") or file.endswith(".mp3"):

        input_path = os.path.join(INPUT_FOLDER, file)
        output_path = os.path.join(OUTPUT_FOLDER, file)

        command = [
            "ffmpeg",
            "-i", input_path,
            "-af",
            "loudnorm,highpass=f=80,lowpass=f=15000,acompressor",
            output_path
        ]

        subprocess.run(command)

print("Processing complete.")
