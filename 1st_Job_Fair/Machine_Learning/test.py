# colors = ["red", "blue", "green", "yellow"]
# results = ""
# for s in colors:
#     results += s
# print(results)

# answer = "".join(colors)
# print(answer)
# items = 'zero one two three'.split()	# 빈칸을 기준으로 문자열 나누기
# print(items)

# ['zero', 'one', 'two', 'three']

# example = 'python, jquery, javascript'	# ","을 기준으로 무나열 나누기
# example.split(",")

# ['python', 'jquery', 'javascript']

# a, b, c = example.split(",")
# # 리스트에 있는 각 값을 a, b, c 변수로 unpacking

# example = 'cs50.gachon.edu'
# subdomain, domain, tld = example.split('.')
# # ","을 기준으로 문자열 나누기 -> Unpacking

# word_1 = "Hello"
# word_2 = "World"
# result = [i+j for i in word_1 for j in word_2]
# print(result)

# case_1 = ["A", "B", "C"]
# case_2 = ["D", "E", "A"]
# result = [i + j for i in case_1 for j in case_2]
# print(result)

# result = [[i + j for i in case_1] for j in case_2]
# print(result)

# result = [i + j for i in case_1 for j in case_2 if not(i==j)]
# print(result)
# result.sort()
# print(result)

# words = 'The quick brown fox jumps over lazy dog'.split()
# # 문장을 빈칸 기준으로 나눠 List로 변환
# print(words)
# ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'lazy', 'dog']

# stuff = [[w.upper(), w.lower(), len(w)] for w in words]
# # List의 각 elemente들을 대문자, 소문자, 길이로 변환하여 two dimensional List로 변환
# for i in stuff:
#     print(i)

# for i, v in enumerate(['tic', 'tac', 'toe']):
# # List에 있는 index와 값을 unpacking
# 	print(i, v)

# mylist = ["a", "b", "c", "d"]
# list (enumerate(mylist))	# list에 있는 index와 값을 unpacking하여 list로 저장
# print(mylist)

# alist = ['a1', 'a2', 'a3']
# blist = ['b1', 'b2', 'b3']
# for a, b in zip(alist, blist):	# 병렬적으로 값을 추출
#     print(a, b)

# a, b, c = zip((1, 2, 3), (10, 20, 30), (100, 200, 300))	# 각 tuple의 같은 index끼리 묶음
# print(a, b, c)

# x = 0
# [sum(x) for x in zip((1, 2, 3), (10, 20, 30), (100, 200, 300))]
# # 각 tuple의 같은 index를 묶어 합을 list로 변환

# alist = ['a1', 'a2', 'a3']
# blist = ['b1', 'b2', 'b3']

# for i, (a, b) in enumerate (zip(alist, blist)):
#     print(i, a, b)	# index alist [index] blist [index] 표시

# print((lambda x: x + 1)(5))

# ex = [1, 2, 3, 4, 5]
# f = lambda x: x ** 2
# print(list(map(f, ex)))

# f = lambda x, y : x + y
# print(list(map(f, ex, ex)))

# x = [value ** 2 for value in ex]
# print(x)

# from functools import reduce
# # print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))

# def factorial(n):
#     return reduce(lambda x, y: x*y, range(1, n+1))

# print(factorial(5))

# def asterisk_test(a, *args):
#     print(a, args)
#     print(type(args))
    
# asterisk_test(1, 2, 3, 4, 5, 6)

# def asterisk_test(a, **kargs):
#     print(a, kargs)
#     print(type(kargs))
    
# asterisk_test(1, b=2, c=3, d=4, e=5, f=6)

# def asterisk_test(a, *args):
#     print(a, args)
#     print(type(args))

# asterisk_test(1, *(2, 3, 4, 5, 6))

# def asterisk_test(a, *args):
#     print(a, *args)
#     print(type(args))
    
# asterisk_test(1, (2, 3, 4, 5, 6))

# def asterisk_test(a, *args):
#     print(a, args)
#     print(type(args))

# asterisk_test(1, (2, 3, 4, 5, 6))

# def asterisk_test(a, *args):
#     print(a, args[0][0])
#     print(type(args))

# asterisk_test(1, (2, 3, 4, 5, 6))

# a, b, c = ([1, 2], [3, 4], [5, 6])
# print(a, b, c)

# data = ([1, 2], [3, 4], [5, 6])
# print(*data)

# def asterisk_test(a, b, c, d,):
#     print(a, b, c, d)
    
# data = {"b":1, "c":2, "d":3}
# asterisk_test(10, **data)

# for data in zip(*([1, 2], [3, 4], [5, 6])):
#     print(data)
#     print(sum(data))

# def asterisk_test(a, b, c, d, e=0):
#     print(a, b, c, d, e)
    
# data = {"d":1, "c":2, "b":3, "e":56}
# asterisk_test(10, **data)

# from collections import deque

# deque_list = deque()
# for i in range(5):
#     deque_list.append(i)
# print(deque_list)

# deque_list.appendleft(10)
# print(deque_list)

# d = {}
# d['x'] = 100
# d['y'] = 200
# d['z'] = 300
# d['l'] = 500

# for k, v in d.items():
#     print(k, v)

# from collections import OrderedDict

# d = OrderedDict()
# d['x'] = 100
# d['y'] = 200
# d['z'] = 300
# d['l'] = 500

# for k, v in d.items():
#     print(k, v)    

# from collections import OrderedDict

# d = OrderedDict()
# d['x'] = 100
# d['y'] = 200
# d['z'] = 300
# d['l'] = 500

# for k, v in d.items():
#     print(k, v)
    
# Dict type의 값을, value 또는 key 값으로 정렬
# for k, v in OrderedDict(sorted(d.items(), key=lambda t: t[0])).items():
#     print(k, v)
# for k, v in OrderedDict(sorted(d.items(), key=lambda t: t[1])).items():
# 	print(k, v)

# d = dict()
# print(d["first"])

# from collections import defaultdict

# d = defaultdict(object)		# Default dictionary를 생성
# d = defaultdict(lambda: 0)		# Default 값을 0으로 설정함

# print(d["first"])

# from collections import OrderedDict
# from collections import defaultdict

# text = """A press release is the quickest and easiest way to get free publicity. """.lower().split()

# word_count = {}
# for word in text:
#     if word in word_count.keys():
# 	    word_count[word] += 1
#     else:
#         word_count[word] = 1
# # print(word_count)

# word_count = defaultdict(object)		# Default dictionary를 생성
# word_count = defaultdict(lambda: 0)		# Default 값을 0으로 설정함

# for word in text:
#     word_count[word] += 1
# for i, v in OrderedDict(sorted(word_count.items(), key=lambda t: t[1], reverse=True)).items():
# 	print(i, v)

# from collections import Counter

# c = Counter()				# a new, empty counter
# c = Counter('gallahad')		# a new counter from aniterable
# print(c)

# from collections import Counter
# c = Counter({'red':4, 'blue':2})	# a new counter from a mapping
# print(c)
# print(list(c.elements()))

# c = Counter(cats=4, dogs=8)			# a new counter fom keyword args
# print(c)
# print(list(c.elements()))

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y = 22)
# print(p[0] + p[1])

x, y = p
print(x, y)
print(p.x + p.y)
print(Point(x = 11, y = 22))