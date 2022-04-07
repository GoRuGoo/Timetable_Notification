from multiprocessing.spawn import import_main_path
import os
from datetime import datetime
import environ
import requests

def send_message(message):
    url = "https://notify-api.line.me/api/notify"
    token = environ.TIMETABLE_TOKEN
    headers = {"Authorization" : "Bearer "+ token}
    payload = {"message" :  message}

    r = requests.post(url ,headers = headers ,params=payload)


def judge_subject():
    now = datetime.today().weekday()
    send_message = ''
    if now == 6:
        send_message = "月曜\n1限:ディジタル回路 基礎からわかる論理回路\n2限:保健体育 ステップアップ高校スポーツ 現代高等保健体育\n3限:英語表現 ヒビスピ 読書記録手帳"
        return send_message
    elif now == 0:
        send_message = "火曜\n1限:プログラミング 授業プリント\n2限:英語講読 NEW FLAG NEW FLAGノート\n3限:線形数学 高専の数学2 問題集\n4限:国語 精選現代文B 国語総合 パスワード漢字 常用国語便覧"
        return send_message
    elif now == 1:
        send_message = "水曜\n1限:物理 高専テキストシリーズ上下 高専の物理問題集 リードαⅠⅡ\n2限:化学 化学基礎 化学 リードα化学基礎＋化学 フォトサイエンス化学図録\n3限:基礎解析 高専の数学2 高専の数学2問題集 ノート"
        return send_message
    elif now == 2:
        send_message = "木曜\n1限:プログラミング 授業プリント\n2限:基礎解析 高専の数学2 高専の数学2問題集 ノート\n3限:歴史 高校世界史B 高校日本史B 最新世界史図説タペストリ プリント"
        return send_message
    elif now == 3:
        send_message = "金曜\n1限:回路理論 エッセンシャル電気回路 プリント\n2,3限:工学実験 工学実験Ⅰ指導書 基本からわかる電気回路"
        return send_message
    else:
        pass



if __name__ == '__main__':
    send_message(judge_subject())