import mlx_whisper
from pydub import AudioSegment
import numpy as np
import os

# 音声ファイルを指定して文字起こし
audio_file_path = "python-audio-output.wav"

result = mlx_whisper.transcribe(
  audio_file_path, path_or_hf_repo="whisper-base-mlx"
)

# 音声データを指定して文字起こし
def preprocess_audio(sound):
    if sound.frame_rate != 16000:
        sound = sound.set_frame_rate(16000)
    if sound.sample_width != 2:
        sound = sound.set_sample_width(2)
    if sound.channels != 1:
        sound = sound.set_channels(1)
    return sound

audio_data = []

def save_text_to_file(text, filename="transcription_result.txt"):
    """
    認識結果を .txt ファイルに保存する関数
    """
    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(text + "\n")
        print(f"{filename} に結果を保存しました。")
    except Exception as e:
        print("保存中にエラーが発生しました:", e)


# -------------------------------
# 音声データ読み込み
# -------------------------------
audio_data = []
audio_data.append(("audio-output-before.wav", AudioSegment.from_file("audio-output-before.wav", format="wav")))
audio_data.append(("audio-output-after.wav", AudioSegment.from_file("audio-output-after.wav", format="wav")))


# -------------------------------
# 音声→テキスト変換 ＋ 保存
# -------------------------------
output_txt = "transcription_result.txt"

# 前回の結果を消す（上書き保存）
if os.path.exists(output_txt):
    os.remove(output_txt)

for file_name, data in audio_data:
    print(f"\n▶ {file_name} を処理中...")

    # 前処理
    sound = preprocess_audio(data)

    # NumPy配列に変換（Whisperが扱える形式）
    arr = np.array(sound.get_array_of_samples()).astype(np.float32) / 32768.0

    # Whisperによる文字起こし
    result = mlx_whisper.transcribe(arr, path_or_hf_repo="whisper-base-mlx")
    text = result["text"].strip()

    # コンソール出力
    print("文字起こし結果:", text)

    # テキストファイルに保存
    save_text_to_file(output_txt, f"{file_name}: {text}")

print("\nすべての音声ファイルの文字起こし結果を保存しました！")