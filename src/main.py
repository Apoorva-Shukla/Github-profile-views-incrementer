import threading, requests

USERNAME = 'Apoorva-Shukla'
URL = f"https://visitor-badge.glitch.me/badge?page_id={USERNAME}"
INCREASE = 300

def thread_function(name):
    requests.head(URL)
    print(name)

if __name__ == "__main__":
    threads = list()

    for index in range(INCREASE):
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()
