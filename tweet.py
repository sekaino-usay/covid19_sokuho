import time
import threading
import subprocess

# 実行間隔を設定
def wait():
    time.sleep(600)

# 実行するファイルを設定
def cmd_exe():  # Call Python files
    subprocess.call("python osaka_tweet.py")
    subprocess.call("python hyogo_tweet.py")
    subprocess.call("python tokyo_tweet.py")
    subprocess.call("python hokkaido_tweet.py")
    print("------------------------------------------------------")

method_list = [wait, cmd_exe]
threads = []
current_time = time.time()

# 実行回数を指定（1, 回数）
for i in range(1, 4320):
    for method in method_list:
        t = threading.Thread(target=method)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()