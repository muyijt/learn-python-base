import threading
import time
import queue

# 生产者-消费者模式
q = queue.Queue(maxsize=10)

def produce():
    for n in range(1, 11):
        q.put(n)
        time.sleep(1)
        print(f"生产了{n}")
    q.put(None)  # 毒丸：通知消费者结束

def consume():
    while True:
        n = q.get()
        if n is None:
            break
        time.sleep(1)
        print(f"消费了{n}")

producer_thread = threading.Thread(target=produce)
consumer_thread = threading.Thread(target=consume)
producer_thread.start()
consumer_thread.start()
producer_thread.join()
consumer_thread.join()
print("全部完成")