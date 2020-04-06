'''
主题一：迭代器和可迭代对象的区别及最佳实践
-------------------------------------
# L是可迭代对象但不是迭代器
L = [1,2,3]
next(L)
TypeError: 'list' object is not an iterator
--------------------------------------
# 将L转换为迭代器之后才能使用next方法
# 迭代器也可以使用for循环对其遍历，但是不支持重复遍历。
I = iter(L)
next(I)
Out[11]: 1
next(I)
Out[12]: 2
next(I)
Out[13]: 3
next(I)
Traceback (most recent call last):
  File "C:\ProgramData\Anaconda3\lib\site-packages\IPython\core\interactiveshell.py", line 2910, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-14-ebc5a6f5e444>", line 1, in <module>
    next(I)
StopIteration
--------------------------------------
迭代协议：这个迭代协议被python中所有的迭代工具使用，并广泛的被许多对象所支持。该协议基于分别用在不同的，两个步骤中的两种对象。
可迭代对象（iterable）：迭代的被调对象，其__iter__方法被iter函数所调用。（遍历可迭代对象时，需要使用iter函数将其转换成迭代器，才能进行遍历）
迭代器对象(iterator)：可迭代对象的返回结果，在迭代过程中实际提供值的对象。它的__next__方法被next()运行，并在结束时触发StopIteration异常（迭代器对象只能遍历一次。）
可迭代对象和迭代器的区别：可迭代对象是支持迭代协议的对象，数据全部保存在内存当中。迭代器只在执行next()的时候一次返回一行数据。可迭代对象支持重复遍历，分片，索引的操作，迭代器不支持。
参考：python学习手册；知乎：https://zhuanlan.zhihu.com/p/49077450
-----------------------------------------
主题二：迭代器的作用
在面向对象的编程中，迭代器模式是一种设计模式，其中迭代器用于遍历容器并访问容器的元素。迭代器模式将算法与容器分离。
有许多种方法可以把对象组成一个集合。底层的容器可以是数组，堆栈，链表，散列表等。当用户希望遍历这些对象的时候，我们不希望用户需要看到底层容器的实现。迭代器模式就是用来处理这种情况的。
参考：掘金博客链接：https://juejin.im/post/5d80bcafe51d453bb13b66dd
迭代器更像一种算法，每执行一次__next__()方法，得到一次结果，并记录运行到第几次，下次在使用的时候接着上一次停下的地方继续执行，适合需要基于上一次运算结果得到当前结果的算法。
参考：知乎https://www.zhihu.com/question/20829330
'''

# L = [1, 2, 3]
# def get_interator(L):
#     for num in L:
#         yield num
#
# iterator = get_interator(L)
#
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(type(iterator))

# 用迭代器实现一个斐波那契数列
# class Fib:
#
#     def __init__(self, n):
#         self.prev = 0
#         self.cur = 1
#         self.n = n
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.n > 0:
#             value = self.cur
#             self.cur = self.cur + self.prev
#             self.prev = value
#             self.n -= 1
#             return value
#         else:
#             raise StopIteration
#
# f = Fib(10)
#
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))

# 模拟一个最简单的生成器
# class IteratorImitate():
#     def __init__(self, n):
#         self.init_num = n
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.init_num > 100:
#             raise StopIteration
#         self.init_num += 1
#         return self.init_num
#
# imitate = IteratorImitate(20)
# print(next(imitate))
# print(next(imitate))
# print(next(imitate))
# print(next(imitate))
# print(next(imitate))
# print(next(imitate))
# print(next(imitate))
# print(next(imitate))
# print([num for num in imitate])

# 模拟一个列表生成器
class ListIteratorImitate():
    def __init__(self, L):
        self.L = L
        self.index = 0
        self.max_index = len(L)

    def __iter__(self):
        '''必须实现这个方法才能算iterable对象，不然使用for循环会报错'''
        return self

    def __next__(self):
        if self.index >= self.max_index:
            raise StopIteration
        value = self.L[self.index]
        self.index += 1
        return value

LII = ListIteratorImitate([1, 2, 3, 4])
for num in LII:
    print(num)
# print(next(LII))
# print(next(LII))
# print(next(LII))
# print(next(LII))
# print(next(LII))