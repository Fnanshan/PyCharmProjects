import asyncio

print('----------------Coroutines¶-------------')

# import asyncio
# import time
#
#
# async def say_after(delay, what):
#     await asyncio.sleep(delay)
#     print(what)
#
#
# async def main():
#     print(f"started at {time.strftime('%X')}")
#
#     await say_after(1, 'hello')
#     await say_after(2, 'world')
#
#     print(f"finished at {time.strftime('%X')}")


# 第一种调用-直接调用
# asyncio.run(say_after(1, 'hello world!'))

# 第二种调用-Awaiting on a coroutine
# asyncio.run(main())

# 第三种调用-异步并发运行
# async def main():
#     task1 = asyncio.create_task(say_after(5, 'hello'))
#     task2 = asyncio.create_task(say_after(10, 'world'))
#     print(f"started at {time.strftime('%X')}")
#     await task1
#     await task2
#     print(f"finished at {time.strftime('%X')}")
#
#
# # asyncio.run(main())

print('----------------Awaitable-----------')

print('# There are three main types of awaitable objects: coroutines, Tasks, and Futures.')
print('# coroutines')

# import asyncio
#
#
# async def nested():
#     return 42
#
#
# async def main():
#     nested()
#     print(await nested())
#
#
# # Nothing happens if we just call "nested()", RuntimeWarning: coroutine 'nested' was never awaited
# # nested()
# # if we just call print(await nested()), SyntaxError : 'await' outside function
# # print(await nested())
# asyncio.run(main())

print('# Tasks')
# import asyncio
#
#
# async def nested():
#     print('---执行nested()---')
#     return 42
#
#
# async def main():
#     print('---执行main()---')
#     task = asyncio.create_task(nested())
#     print(task)
#     await task
#     print(task)
#
#
# asyncio.run(main())

print('# Futures')

print('-------Generator-based Coroutines¶--------')

# @asyncio.coroutine
# def old_style_coroutine():
#     print('---执行old_style_coroutine()---')
#     yield from asyncio.sleep(4)
#
#
# async def main():
#     print('---执行main()---')
#     await old_style_coroutine()
#     print('---执行 await old_style_coroutine()---')
#
#
# asyncio.run(main())