# coding=utf8
import asyncio
import time
# async def num(n):
#     print(f"当前的数字时：{n}")
#     await spend_time_foo(n)
#
#
# async def main():
#     tasks = [num(i) for i in range(10)]  # 协程列表
#     await asyncio.wait(tasks)  # 并发运行协程列表的协程
#
# async def spend_time_foo(n):
#     await asyncio.sleep(n)
#     print(f"等待时间：{n}")
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     try:
#         loop.run_until_complete(main())
#     finally:
#         loop.close()

# 协程调用普通函数
import functools
def callback(args, *, kwargs="defalut"):
    time.sleep(5)
    print(f"普通函数作为回调函数，获取参数：{args}, {kwargs}")

async def main(loop):
    print("注册callback")
    loop.call_soon(callback, 1)
    wrapped = functools.partial(callback, kwargs="not defalut")
    loop.call_soon(wrapped, 2)
    await asyncio.sleep(0.2)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(loop))
    finally:
        loop.close()