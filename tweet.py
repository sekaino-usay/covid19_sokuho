import time
import threading
import subprocess

# 実行間隔を設定
def wait():
    time.sleep(600)

# 実行するファイルを設定
def cmd_exe():  # Call Python files
    subprocess.call("python osaka_tweet.py")
    print("大阪ツイート")
    print("------------------------------------------------------")

    subprocess.call("python hyogo_tweet.py")
    print("兵庫ツイート")
    print("------------------------------------------------------")

    subprocess.call("python tokyo_tweet.py")
    print("東京ツイート")
    print("------------------------------------------------------")

    subprocess.call("python hokkaido_tweet.py")
    print("北海道ツイート")
    print("------------------------------------------------------")

    subprocess.call("python fukuoka_tweet.py")
    print("福岡ツイート")
    print("------------------------------------------------------")

    subprocess.call("python aichi_tweet.py")
    print("愛知ツイート")
    print("------------------------------------------------------")

    subprocess.call("python japan_tweet.py")
    print("国内ツイート")
    print("------------------------------------------------------")

method_list = [wait, cmd_exe]
threads = []
current_time = time.time()
for i in range(1, 4320):
    for method in method_list:
        t = threading.Thread(target=method)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()