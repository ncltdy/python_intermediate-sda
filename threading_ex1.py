import timeit
import requests
def crawl(url, dest):
    try:
        result = requests.get(url).text
        with open(dest, "a") as f:
            f.write(result)
    except requests.exceptions.RequestException:
        print("Error with URL check!")

def wo_threading():
    urls = [
        "https://jsonplaceholder.typicode.com/comments/1",
        "https://jsonplaceholder.typicode.com/comments/2",
        "https://jsonplaceholder.typicode.com/comments/3"
    ]
    for url in urls:
        crawl(url, "without_threads.txt")

def with_threading():
    import threading
    urls = [
        "https://jsonplaceholder.typicode.com/comments/1",
        "https://jsonplaceholder.typicode.com/comments/2",
        "https://jsonplaceholder.typicode.com/comments/3"
    ]

    threads = []
    for url in urls:
        th = threading.Thread(target=crawl, args=(url, "with_threads.txt"))
        th.start()
        threads.append(th)

    for th in threads:
        th.join()

if __name__ == "__main__":
    print("Without threads:", timeit.timeit(stmt=wo_threading, number=10))
    print("With threads:", timeit.timeit(stmt=with_threading,  number=10))