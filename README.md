# 📝 Caption Generator and Translator

Effortlessly generate and translate video captions using OpenAI's Whisper and GPT models

**Features** • [Quick Start](#quick-start) • [Installation](#installation) • [Usage](#usage) • [Advanced](#advanced) • [How It Works](#how-it-works)

---

### 🚀 Features

- 🎯 **Transcription**: Convert audio/video content to text with high accuracy
- 🌐 **Smart Translation**: 
  - Direct English translation using Whisper (no API key needed)
  - Translation to other languages using OpenAI API
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

- **Original Language**: Enter the language code of the video (e.g., `es` for Spanish)
- **Target Language**: 
  - For English translation: Simply enter 'en' or 'english' (uses Whisper's built-in translation)
  - For other languages: Enter the desired language code and provide an OpenAI API key
  - Press Enter to skip translation
- **Whisper Model Selection**: Choose from Tiny, Small, and Turbo models to balance speed and accuracy
- **Video File Path**: Provide the full path to your video file (supported formats: `.mp4`, `.m4v`, `.mov`)

The script generates an `.srt` file named `output_subtitles.srt`, ready for import into video editing software.

---

### 📚 Advanced

- **Model Details**:
   - **Tiny**: 75 MB - Fastest, less accurate
   - **Small**: 244 MB - Moderate speed and accuracy
   - **Turbo (Large)**: 1.5 GB - Highest accuracy, longer processing

- **Translation Options**:
   - **To English**: Uses Whisper's built-in translation - fast and free
   - **To Other Languages**: Requires OpenAI API key for GPT-based translation

---

### ❓ How It Works

This script leverages OpenAI's Whisper for transcription and translation to English. For other target languages, it uses GPT models for translation. Results are saved in `.srt` format for easy integration with editing software.

---

### 📜 License

This project is licensed under the MIT License.
