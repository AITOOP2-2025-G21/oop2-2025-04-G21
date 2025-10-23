import audiorecoded
import StringGeneration
import whisper

audio = audiorecoded()
audio.recode()
audioString = StringGeneration()
whisp = whisper()
audioString.getString()