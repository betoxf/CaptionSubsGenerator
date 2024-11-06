
# 📝 Caption Generator and Translator

Effortlessly generate and translate video captions using OpenAI’s Whisper and GPT models

**Features** • [Quick Start](#quick-start) • [Installation](#installation) • [Usage](#usage) • [Advanced](#advanced) • [How It Works](#how-it-works)

---

### 🚀 Features

- 🎯 **Transcription**: Convert audio/video content to text with high accuracy
- 🌐 **Optional Translation**: Translate generated captions to various languages using the OpenAI API
- 🛠️ **Whisper Model Selection**: Choose from Whisper Tiny, Small, and Turbo models for different processing speeds and accuracies
- 📊 **Language Abbreviation Display**: Shows supported language abbreviations for ease of selection
- 🔍 **Flexible Output**: Generates `.srt` files for easy import into Final Cut Pro and other editing software

---

### 📖 Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/CaptionGeneratorTranslator.git
   cd CaptionGeneratorTranslator
   ```
2. Install dependencies:
   ```bash
   pip install git+https://github.com/openai/whisper.git requests srt
   ```
3. Run the script:
   ```bash
   python caption_translator.py
   ```

---

### ⚙️ Installation

1. Ensure Python 3.7+ is installed.
2. Install required libraries with:
   ```bash
   pip install git+https://github.com/openai/whisper.git requests srt
   ```

---

### 🎬 Usage

- **Original Language**: Enter the language code of the video (e.g., `es` for Spanish). Type `show` to see a list of available language options.
- **Target Language**: Enter the desired language code for captions, or press Enter to skip translation.
- **OpenAI API Key**: If translation is selected, provide the OpenAI API key.
- **Whisper Model Selection**: Choose from Tiny, Small, and Turbo models to balance speed and accuracy.
- **Video File Path**: Provide the full path to your video file (supported formats: `.mp4`, `.m4v`, `.mov`).

   The script generates an `.srt` file named `output_subtitles.srt`, ready for import into video editing software.

---

### 📚 Advanced

- **Model Details**:
   - **Tiny**: 75 MB - Fastest, less accurate
   - **Small**: 244 MB - Moderate speed and accuracy
   - **Turbo (Large)**: 1.5 GB - Highest accuracy, longer processing

- **Supported Languages**: To see all available language abbreviations, type `show` when prompted for language input.

---

### ❓ How It Works

This script uses OpenAI’s Whisper for transcription and GPT models for optional translation, saving results in `.srt` format for easy integration with editing software.

---

### 📜 License

This project is licensed under the MIT License.
