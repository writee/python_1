def file_load():
    #CSVファイルを取り込む

    with open('source-sheet.csv',encoding = 'utf-8') as f:

    #ファイルの読み込み、検索対象になる
    
        source = f.read()  


# 検索ツール
def search():
    word = input("検索するキャラクターを入力してください")

    # 検索のロジックをここに入力

    #1,リストにキャラクターがいなかった場合追加する
    #2,CSVファイルからリストを読み込んで登録する
    #3,キャラクターリストをCSVに書き込めるようにする

    if word in source:

        print("{}は見つかりました".format(word))
    
    else:
        print("{}は見つかりませんでしたので追加しておきます".format(word))
        
        
        with open('source-sheet.csv','a',encoding='utf-8') as f:
            f.write(','+word)

file_load()
search()



        
