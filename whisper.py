import mlx_whisper

# 音声ファイルを指定して文字起こし
def transcribe (output_file:str = "python-audio-output.wav")-> str:

    result = mlx_whisper.transcribe(
        output_file, path_or_hf_repo="whisper-base-mlx"
    )
    print(result)
    return result["text"]
