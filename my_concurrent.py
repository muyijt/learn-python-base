# 并发编程
import threading
import time

num = 0

# 获取锁对象
lock = threading.RLock()

# 加1的函数
def add_conc(count):
    # 使用锁对象来保证代码代码原子性（加锁）
    with lock:
        global num
        for i in range(count):
            temp = num
            temp += 1
            # sleep会使cpu不再执行当前线程，执行其他线程，方便测试是否有并发问题
            time.sleep(0)
            num = temp

# 减1的函数
def sub_conc(count):
    with lock:
        global num
        for i in range(count):
            temp = num
            temp -= 1
            time.sleep(0)
            num = temp

# 创建线程target指定线程要执行的方法, args是线程执行的那个方法的参数
add_thread = threading.Thread(target=add_conc, args=(10000000,))
sub_thread = threading.Thread(target=sub_conc, args=(10000000,))
# 告诉cpu线程可以被执行，cpu调度到后线程就会执行
add_thread.start()
sub_thread.start()
add_thread.join()
sub_thread.join()
print(f"总数:{num}")
