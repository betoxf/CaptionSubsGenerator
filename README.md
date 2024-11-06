# CaptionSubsGenerator
Generate Captions and Subtitles (Translated captions.) immediately from your video file and use it in any video editing software SRT file

Caption Generator and Translator

Description

This project is a command-line tool that allows users to automatically generate captions for video files using OpenAI’s Whisper and optionally translate the captions to another language using the OpenAI API. The result is saved as an .srt file, compatible with video editing software like Final Cut Pro.

Features

Caption Generation: Transcribes audio from videos in .mp4, .m4v, or .mov format.
Optional Translation: Allows translation of generated captions to another language using the OpenAI API.
Whisper Model Selection: Choose from Tiny, Small, and Turbo Whisper models.
Language List: Displays supported language abbreviations when typing show in the language field.
Requirements

Python 3.7+
Python Dependencies: OpenAI Whisper, requests, and srt
Installation

Clone the repository:

git clone https://github.com/yourusername/CaptionGeneratorTranslator.git

cd CaptionGeneratorTranslator

Install dependencies:
pip install git+https://github.com/openai/whisper.git requests srt

Usage

Run the script:

python caption_translator.py


Interactive Terminal Instructions:
Original Language: Type the language code of the video (e.g., es for Spanish). Type show to see a list of available languages.
Target Language: Enter the desired language code for captions or press Enter to skip translation.
OpenAI API: If translation is required, provide the OpenAI API key.
Whisper Model: Select from Tiny, Small, and Turbo models for transcription speed and accuracy.
Video File Path: Specify the full path to the video file in .mp4, .m4v, or .mov format.
Generated Captions: The .srt file is saved as output_subtitles.srt, ready for import into Final Cut Pro.
License

This project is licensed under the MIT License.
