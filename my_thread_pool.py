import random
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def square(n):
    time.sleep(random.uniform(0, 1))
    return n*n

# 线程池--submit提交
with ThreadPoolExecutor(max_workers=10) as executor:
    future1 = executor.submit(square, 1)
    future2 = executor.submit(square, 6)
    print(future1.result())
    print(future2.result())
print("结束")

# 线程池--submit提交，as_completed()获取结果。
# 批量提交一批任务，谁先执行完谁先返回结果
with ThreadPoolExecutor(max_workers=10) as executor:
    task_map = {executor.submit(square, n):n for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]}
    future_iterator = as_completed(task_map)
    for future in future_iterator:
        print(task_map.get(future), future.result())
print("结束")

# 线程池--map提交
# 批量提交一堆任务，按任务提交顺序返回结果
with ThreadPoolExecutor(max_workers=10) as executor:
    temp_iterator = executor.map(square, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    for item in temp_iterator:
        print(item)
print("结束")

