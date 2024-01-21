import sys

from models.vosk_model import *

MODELS = {
    "vosk-ru-small": VoskModelRuSmall,
    "vosk-ru": VoskModelRu,
    "vosk-en-small": VoskModelEnSmall,
    "vosk-en": VoskModelEn,
}


def check_audiofile(audiofile):
    if not audiofile.endswith(".wav"):
        print("Unsupported audio format (Audio file must be WAV file)")
        return False

    if len(audiofile.split(".")) > 2:
        print("Specify only the name of the file (File must be placed in ./speech directory)")
        return False

    return True


def main():
    if len(sys.argv) != 3:
        print(
            "Usage: python speech_recognizer.py audio_file.wav model_name\n"
            "Supported model names: vosk-ru-small,  vosk-ru,  vosk-en-small,  vosk-en"
            "Audio file must be WAV file and placed in ./speech directory"
        )
        sys.exit(1)

    audiofile = sys.argv[1]
    model_name = sys.argv[2]

    if check_audiofile(audiofile):
        if MODELS.get(model_name, None):
            model = MODELS[model_name]()
            model.recognize_audio(audiofile)
        else:
            print("Unsupported model name")


if __name__ == "__main__":
    main()
