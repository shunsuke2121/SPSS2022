numbers = ["いとう", "さとう", "すずき", "わたなべ", "たかはし", "たなか", "いとう", "いのうえ", "やまぐち", "さいとう"]

# あいうえお順で並び替えされる
numbers.sort()

# enumerate(リスト)でリストの要素と同時にindex番号を取得できる
# index番号は0番から始まる。
for index, name in enumerate(numbers):
    # 処理
    print(f"{name}さんの出席番号は{index+1}です")