import threading, requests

USERNAME = 'Apoorva-Shukla'
URL = f"https://visitor-badge.glitch.me/badge?page_id={USERNAME}"


def thread_function(name):
    requests.head(URL)
    print(name)

if __name__ == "__main__":
    threads = list()

    for index in range(3000):
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()
        print(index)
