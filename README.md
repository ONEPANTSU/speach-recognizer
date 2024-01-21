# Speach recognizer

The program for speach recognizing from an audio file using machine learning models.

Audio file must be WAV file and placed in `./speech` directory. Result will be appeared in `./out` directory.

### Usage 
```
python speech_recognizer.py audio_file.wav model_name\n"
```
### Supported models: 
- [x] **[Vosk models](https://alphacephei.com/vosk/models):**
  - vosk-ru-small
  - vosk-ru
  - vosk-en-small
  - vosk-en
  

- [ ] **~~Nvidia RNNT Large~~:**