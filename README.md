# oop2-2025-04-G21

## audiorecoded.py
10秒間録音し、python-audio-output.wavという名前で保存される。
エラーが出たら、エラーメッセージを表示してプログラムが終了する。

## StringGeneration
録音した音声ファイルをテキストに変換して返す。

## whisper.py
文字起こししたテキストを保存する。

### 保存形式
 
文字起こしされたテキストは、プログラムの実行フォルダに transcription_result.txt というファイル名で保存されます。
 
#### 仕様:
 
保存形式は (元のファイル名): (文字起こし結果) となります。
 
#### 出力例 (transcription_result.txt)
 
<pre>
audio-output-before.wav: （ここにaudio-output-before.wavの文字起こし結果が入ります）
audio-output-after.wav: （ここにaudio-output-after.wavの文字起こし結果が入ります）
</pre>
