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
if target_language == "":
    print("\nNo translation needed, captions will be generated in the original language.")
    translation_needed = False
else:
    translation_needed = True
    print("\nTranslation required. Please enter your OpenAI API key to enable translation.")
    API_KEY = input("OpenAI API Key: ")

# Función para traducir texto usando la API de OpenAI
def translate_text(text, source_language, target_language):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "gpt-4",
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
result = model.transcribe(video_path)

# Generar subtítulos y traducir si es necesario
captions = []
for segment in result['segments']:
    start = timedelta(seconds=segment['start'])
    end = timedelta(seconds=segment['end'])
    text = segment['text']
    
    # Traducir el texto si es necesario
    if translation_needed:
        text = translate_text(text, source_language, target_language)
    
    # Crear subtítulo en formato SRT
    captions.append(srt.Subtitle(index=len(captions) + 1, start=start, end=end, content=text))

# Guardar el archivo SRT
srt_file_path = "output_subtitles.srt"
with open(srt_file_path, "w") as srt_file:
    srt_file.write(srt.compose(captions))

print(f"\nSuccessfully generated {srt_file_path}.")
print("You can import it into Final Cut Pro by going to File > Import > Subtitles.")
