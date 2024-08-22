# import csv


# TODO: お題を決める
def choose_subject():
    # 内部or外部のcsvファイルを読み込む
    # 読み込んだファイルのランダムな行を取得し、お題テキストと画像ナンバーを返す
    subject = {"text":"", "img":""}
    subject["text"] = "XXX"
    subject["img"] = "quest_cave"
    return subject

# TODO: 手札をhand_num枚数選ぶ
def choose_hand(hand_num):
    # 内部or外部のcsvファイルを読み込む
    # 読み込んだファイルのランダムな行を取得し、手札テキストと画像ナンバーを返す
    # TODO: 同じカードが2枚選ばれないような工夫
    hand_list = []
    for n in range(hand_num):
        hand_list.append({"nth":n+1, "text":"AAA", "img":"B_"})
    return hand_list

# String型からint型に変換可能か判定
def isInt(s):
    try:
        int(s)
    except ValueError:
        return False  # 例外が発生する=変換できない
    else:
        return True  # 例外が発生しない=変換できる
