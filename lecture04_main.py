import audiorecoded
import whisper


audiorecoded.recode(10,"temp.wav")
result = whisper.transcribe("temp.wav")

#上書きがダメだったので追記するようにした
with open("output.txt", "a", encoding="utf-8") as f:
    f.write(result)
    f.write("\n")