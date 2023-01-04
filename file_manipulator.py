import sys

print(sys.argv)
l = len(sys.argv) # 引数の数を取得
print(f'len: {l}')
command = sys.argv[1] # 関数名の取得
print(f'command name: {command}')

# reverse inputpath outputpath: inputpath にあるファイルを受け取り、outputpath に inputpath の内容を逆にした新しいファイルを作成します。引数3つ
if command == 'reverse':
    if l != 4:
        print("入力に不備があります")
        sys.exit()
    try:
        inputpath = sys.argv[2]
        outputpath = sys.argv[3]
        with open(inputpath) as f:
            original_str = f.read()
            print(original_str)
            reversed_str = original_str[::-1]
            print(reversed_str)
        # 書き込みモードwでファイルオープン ファイルが存在したら上書き
        with open(outputpath, mode='w') as f: 
            f.write(reversed_str)
    except FileNotFoundError as e:
        print('ファイルが存在しません')
    
# copy inputpath outputpath: inputpath にあるファイルのコピーを作成し、outputpath として保存します。
elif command == 'copy':
    if l != 4:
        print("入力に不備があります")
        sys.exit()
    try:
        inputpath = sys.argv[2]
        outputpath = sys.argv[3]
        with open(inputpath) as f:
            original_str = f.read()
            print(original_str)
        # 書き込みモードxでファイルオープン ファイルが存在したらエラー
        with open(outputpath, mode='x') as f: 
            f.write(original_str)
    except FileNotFoundError as e:
        print('ファイルが存在しません')

# duplicate-contents inputpath n: inputpath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputpath に n 回複製します。
elif command == 'duplicate-contents':
        if l != 4:
            print("入力に不備があります")
            sys.exit()
        try:
            inputpath = sys.argv[2]
            n = int(sys.argv[3]) # intに変換できなかったらValueError
            with open(inputpath) as f:
                original_str = f.read()
                print(original_str)
            # 書き込みモードaでファイルオープン ファイルがなかったらエラー
            with open(inputpath, mode='a') as f: 
                for i in range(n):
                    f.write(original_str)
        except FileNotFoundError as e:
            print('ファイルが存在しません')
        except ValueError:
            print('数値を入力してください')
# replace-string inputpath needle newstring: inputpath' にあるファイルの内容から文字列 'needle' を検索し、'needle' の全てを 'newstring' に置き換えます。
elif command == 'replace-string':
        if l != 5:
            print("入力に不備があります")
            sys.exit()
        try:
            inputpath = sys.argv[2]
            needle = sys.argv[3]
            newstring = sys.argv[4]
            with open(inputpath) as f:
                original_str = f.read()
                replace_str = original_str.replace(needle, newstring)
                print(original_str)
            # 書き込みモードwでファイルオープン ファイルがなかったらエラー
            with open(inputpath, mode='w') as f: 
                f.write(replace_str)
        except FileNotFoundError as e:
            print('ファイルが存在しません')
else:
    print("正しいコマンドを入力してください")
