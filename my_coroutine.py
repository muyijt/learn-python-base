import asyncio

# 加await的判断依据
# 这行在干什么？
# ├─ 调用 async 函数？        → + await（否则不执行）
# ├─ 网络/数据库/文件/延时？   → + await（否则卡死所有协程）

# 定义协程函数
async def fetch_data():
    print("请求")
    # 定义让出点
    await asyncio.sleep(1)
    print("获取数据成功")
    return "xxx"

# 入口
async def main():
    print("主任务开始")
    # 调用协程函数(gather方式)
    # result = await asyncio.gather(fetch_data(), fetch_data())

    # 调用协程函数(create_task方式)
    result = await asyncio.create_task(fetch_data())

    print(f"收到结果: {result}")

# 创建事件循环 → 把 main() 这个协程交给循环执行 → 协程结束后关闭循环
asyncio.run(main())