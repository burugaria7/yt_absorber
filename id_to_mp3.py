from yt_dlp import YoutubeDL


def csv_to_mp3():
    import csv
    import youtube_dl

    # csvファイルを指定
    MyPath = './marasy.csv'

    # 初期設定
    ydl = YoutubeDL({'outtmpl': './mp3/%(title)s%(ext)s',
                     'postprocessors': [{
                         'key': 'FFmpegExtractAudio',
                         'preferredcodec': 'mp3',
                         'preferredquality': '192',
                     }]
                     })

    # csvファイルを読み込み
    rows = []
    i = 0
    with open(MyPath, encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if (i == 385):
                return
            rows.append(row)
            id = row[0]
            title = row[1]
            print(id + "\t" + title)

            if (i != 0 and title.find("【ピアノ】")!=-1):
                # ダウンロードする動画のURL
                url = 'https://www.youtube.com/watch?v=' + id
                try:
                    # 動画情報をダウンロードする
                    with ydl:
                        result = ydl.extract_info(
                            url,
                            download=True
                        )
                except:
                    print("例外")
            i += 1

    # print(rows)


if __name__ == "__main__":
    csv_to_mp3()
