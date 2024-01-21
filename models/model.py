from abc import abstractmethod, ABC

from pydub import AudioSegment


class AbstractModel(ABC):
    def __init__(self):
        self.model = None

    @abstractmethod
    def recognize_audio(self, audio_path):
        raise NotImplementedError

    @staticmethod
    def convert_audio(audiofile):
        audio_path = f"./speech/{audiofile}"
        audio = AudioSegment.from_wav(audio_path)
        audio = audio.set_channels(1)
        audio = audio.set_frame_rate(16000)
        audio = audio.set_sample_width(2)
        new_filename = audiofile.split(".")[0] + "_temp.wav"
        audio_path = f"./speech/{new_filename}"
        audio.export(audio_path, format="wav")
        return audio_path

    @staticmethod
    def create_file(text, filename):
        with open(f"./out/{filename}", "w") as file:
            file.write(text)
