from pydub import AudioSegment
import os

INPUT_FOLDER = "input_audio"
OUTPUT_FOLDER = "processed_audio"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for filename in os.listdir(INPUT_FOLDER):
    if filename.endswith(".wav") or filename.endswith(".mp3"):

        input_path = os.path.join(INPUT_FOLDER, filename)
        output_path = os.path.join(OUTPUT_FOLDER, filename)

        audio = AudioSegment.from_file(input_path)

        # normalize loudness
        normalized_audio = audio.normalize()

        normalized_audio.export(output_path, format="wav")

print("Processing complete.")
