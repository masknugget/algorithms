"""
Sometimes you need to limit array result to use. Such as you only need the 
 value over 10 or, you need value under than 100. By use this algorithms, you
 can limit your array to specific value

If array, Min, Max value was given, it returns array that contains values of 
 given array which was larger than Min, and lower than Max. You need to give
 'unlimit' to use only Min or Max.

ex) limit([1,2,3,4,5], None, 3) = [1,2,3]

Complexity = O(n)

这个编程方式倒是不错

def limit(text, store = ''):
    store += text
    print(store)      # 这个store不会增加
    return text      


def limit1(text, store = []):
    store.append(text)
    print(store)      # 不过这个会增加
    return text
    
store = []
def limit2(text):
    store.append(text)
    print(store)
    return text
    

def limit1(text, store = []):       # 这种方式并不像
    store.append(text)
    print(store)
    store = []
    return text
    
https://blog.csdn.net/emaste_r/article/details/47358843
当list等可变类型作为默认参数时，仅仅在定义函数的时候（也就是执行def语句）被计算一次，有且仅有这么一次
其它的时候无论调用几次函数，如果没有传参进来，就会一直用这个默认参数了

1、当list、dic等可变类型作为函数默认参数并且调用函数时没有传参的时候，要注意list、dic并不会自己清空。

2、默认参数只在def语句被执行的时候计算一次。

3、如果想要的话，把默认参数当成静态变量（也就是全局变量）也是一种抖机灵的好思路呢


def limit3(text, store=None):
    if store is None:
        store = []
    store.append(text)
    print(store)
    return text



"""



# tl:dr -- array slicing by value
def limit(arr, min_lim=None, max_lim=None):
    # 1 True if min_lim is None else (min_lim <= val) 这个三元表达的
    # 2 lambda val : 一个三元表达
    # 赋值引用下
 
    min_check = lambda val: True if min_lim is None else (min_lim <= val)
    max_check = lambda val: True if max_lim is None else (val <= max_lim)
    
    return [val for val in arr if min_check(val) and max_check(val)]
