# speech-audio-cleanup-pipeline

This project demonstrates a simple audio processing workflow for preparing speech recordings for voice systems, IVR prompts, and speech datasets.

The goal is to apply standard audio engineering practices (EQ, compression, loudness normalization) in a repeatable pipeline that can process multiple recordings consistently.

This type of processing is useful when preparing:

- IVR voice prompts
- speech datasets
- podcast or narration audio
- TTS training audio

## Processing Steps

The pipeline performs the following operations:

1. Normalize loudness
2. Apply EQ to improve vocal clarity
3. Apply compression to stabilize dynamics
4. Optional de-essing
5. Export processed audio

These steps help maintain consistent voice quality across recordings from different environments.

## Example Workflow

Input folder: input_audio/


Output folder: processed_audio/

Run the script: python process_audio.py

All recordings in the input folder will be processed and exported.

## Example Use Cases

Speech AI training datasets
Voice assistant recordings
Telephony / IVR systems
Podcast voice cleanup

## Tools Used

Python
FFmpeg
Basic DSP concepts from audio engineering workflows

## Motivation

In speech AI systems, small differences in recording quality can affect both model performance and user experience.

This project explores how traditional audio engineering techniques can be translated into automated pipelines that maintain consistent voice quality across large sets of recordings.
}
