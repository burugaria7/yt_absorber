# ライブラリの読み込み
from yt_dlp import YoutubeDL
import os
from pathlib import Path

# 初期設定
ydl = YoutubeDL({'outtmpl': './mp3/%(id)s%(ext)s',
                                    'postprocessors': [{
                                        'key': 'FFmpegExtractAudio',
                                        'preferredcodec': 'mp3',
                                        'preferredquality': '192',
                                    }]
                                    })

# ダウンロードする動画のURL
url = 'https://www.youtube.com/watch?v=n1M5MyYB04U'
# 動画情報をダウンロードする
with ydl:
    result = ydl.extract_info(
        url,
        download=True
    )

# ファイル名を変更
# filename_before1 = url[32:] + 'mp4' + '.mp3'
# filename_after1 = url[32:] + '.mp3'
# os.rename(filename_before1, filename_after1)
print('処理が完了しました')