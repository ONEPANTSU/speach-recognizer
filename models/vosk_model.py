import enum
import json
import os

from models.model import AbstractModel
import vosk
import wave


class VoskModel(AbstractModel):
    class Names(enum.Enum):
        RU_SMALL = "vosk-model-small-ru-0.22"
        RU = "vosk-model-ru-0.42"
        EN_SMALL = "vosk-model-small-en-us-0.15"
        EN = "vosk-model-en-us-0.22"

    def __init__(self, model_name=Names.RU):
        super().__init__()
        self.model_name = model_name.value
        self.model = vosk.Model(model_name=self.model_name)

    def recognize_audio(self, audiofile):
        audio_path = self.convert_audio(audiofile)
        wf = wave.open(audio_path, "rb")
        text = ""
        if self.check_audiofile(wf):
            rec = vosk.KaldiRecognizer(self.model, wf.getframerate())

            while True:
                data = wf.readframes(4000)
                if len(data) == 0:
                    break
                if rec.AcceptWaveform(data):
                    text += self.get_text_from_result(rec.Result()) + "\n"

            text += self.get_text_from_result(rec.FinalResult()) + "\n"
        wf.close()
        os.remove(audio_path)

        self.create_file(text, filename=audiofile.split(".")[0] + "_out.txt")

    @staticmethod
    def check_audiofile(wavefile):
        if wavefile.getsampwidth() != 2:
            print("Audio file must be 16-bit PCM mono WAV file")
            return False

        if wavefile.getnchannels() != 1:
            print("Audio file must be mono")
            return False

        if wavefile.getframerate() != 16000:
            print("Audio file must have 16 kHz sample rate")
            return False

        return True

    @staticmethod
    def get_text_from_result(text):
        data = json.loads(text)
        text_content = data.get("text", "")
        return text_content


class VoskModelRuSmall(VoskModel):
    def __init__(self):
        super().__init__(model_name=self.Names.RU_SMALL)


class VoskModelRu(VoskModel):
    def __init__(self):
        super().__init__(model_name=self.Names.RU)


class VoskModelEn(VoskModel):
    def __init__(self):
        super().__init__(model_name=self.Names.EN)


class VoskModelEnSmall(VoskModel):
    def __init__(self):
        super().__init__(model_name=self.Names.EN_SMALL)
