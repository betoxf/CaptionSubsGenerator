import whisper
import requests
import srt
import os
from datetime import timedelta

# Mensaje de bienvenida
print("Welcome to the Caption Generator and Translator!")
print("In this tool, you can generate captions for your video and optionally translate them to another language.\n")

# Solicitar el idioma original
source_language = input("Please enter the original language of the video (e.g., 'es' for Spanish, 'en' for English): ")

# Solicitar el idioma deseado
target_language = input("Enter the desired language for captions (press Enter to keep the same language): ")

translation_needed = False
use_whisper_translation = False
API_KEY = None

if target_language:
    if target_language.lower() == 'en' or target_language.lower() == 'english':
        print("\nWhisper will handle the translation to English directly - no API key needed.")
        use_whisper_translation = True
    else:
        translation_needed = True
        print("\nTranslation to languages other than English requires OpenAI's API.")
        print("To get an API key:")
        print("1. Go to https://platform.openai.com/api-keys")
        print("2. Sign up or log in")
        print("3. Create a new API key")
        API_KEY = input("\nPlease enter your OpenAI API key: ")

# Función para traducir texto usando la API de OpenAI
def translate_text(text, source_language, target_language):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": f"Translate the following text from {source_language} to {target_language}."},
            {"role": "user", "content": text}
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()['choices'][0]['message']['content']

# Elegir modelo de Whisper
print("\nPlease select the Whisper model you'd like to use:")
print("1. Tiny (75 MB - fastest)")
print("2. Small (244 MB - moderate)")
print("3. Turbo (Large, 1.5 GB - highest accuracy)")
model_choice = input("Enter 1, 2, or 3: ")

model_map = {
    "1": "tiny",
    "2": "small",
    "3": "large"
}
model_name = model_map.get(model_choice, "tiny")  # Default to "tiny" if an invalid option is given
print(f"Selected Whisper model: {model_name} - please wait while the model downloads if it's not already cached.")

# Cargar el modelo de Whisper
model = whisper.load_model(model_name)

# Solicitar la ruta al archivo de video con ejemplo y tipos aceptados
print("\nPlease enter the path to your video file.")
print("Example for macOS: /Users/YourUsername/Downloads/YourVideo.mp4")
print("Accepted formats: .mp4, .m4v, .mov\n")
video_path = input("Path to your video file: ")

# Verificar si el formato es válido
accepted_formats = (".mp4", ".m4v", ".mov")
if not video_path.lower().endswith(accepted_formats):
    print("Error: Unsupported file format. Please use a .mp4, .m4v, or .mov file.")
    exit()

# Procesar el video
print("\nProcessing the video...")
if use_whisper_translation:
    # Use Whisper's built-in translation
    result = model.transcribe(video_path, task="translate")
else:
    result = model.transcribe(video_path)

# Generar subtítulos y traducir si es necesario
captions = []
for segment in result['segments']:
    start = timedelta(seconds=segment['start'])
    end = timedelta(seconds=segment['end'])
    text = segment['text']
    
    # Traducir el texto solo si es necesario y no es una traducción de Whisper
    if translation_needed and not use_whisper_translation:
        text = translate_text(text, source_language, target_language)
    
    # Crear subtítulo en formato SRT
    captions.append(srt.Subtitle(index=len(captions) + 1, start=start, end=end, content=text))

# Guardar el archivo SRT
srt_file_path = "output_subtitles.srt"
with open(srt_file_path, "w") as srt_file:
    srt_file.write(srt.compose(captions))

print(f"\nSuccessfully generated {srt_file_path}.")
print("You can import it into Final Cut Pro by going to File > Import > Subtitles.")
