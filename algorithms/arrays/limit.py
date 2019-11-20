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
    
    

"""



# tl:dr -- array slicing by value
def limit(arr, min_lim=None, max_lim=None):
    # 1 True if min_lim is None else (min_lim <= val) 这个三元表达的
    # 2 lambda val : 一个三元表达
    # 赋值引用下
 
    min_check = lambda val: True if min_lim is None else (min_lim <= val)
    max_check = lambda val: True if max_lim is None else (val <= max_lim)
    
    return [val for val in arr if min_check(val) and max_check(val)]
