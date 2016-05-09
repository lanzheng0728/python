
In [43]: c
Out[43]: array([[1, 2, 3, 4], [4, 5, 6, 7], [6, 7, 8, 9]], dtype=object)

In [44]: c.len
Traceback (most recent call last):

  File "<ipython-input-44-a8d9383261fe>", line 1, in <module>
    c.len

AttributeError: 'numpy.ndarray' object has no attribute 'len'


In [45]: c.shape = 2.-1
D:\Anaconda3\lib\site-packages\spyderlib\widgets\externalshell\start_ipython_kernel.py:1: DeprecationWarning: using a non-integer number instead of an integer will result in an error in the future
  # -*- coding: utf-8 -*-
Traceback (most recent call last):

  File "<ipython-input-45-08fe31afab89>", line 1, in <module>
    c.shape = 2.-1

ValueError: total size of new array must be unchanged


In [46]: c
Out[46]: array([[1, 2, 3, 4], [4, 5, 6, 7], [6, 7, 8, 9]], dtype=object)

In [47]: c[1]
Out[47]: [4, 5, 6, 7]

In [48]: c[1:3]
Out[48]: array([[4, 5, 6, 7], [6, 7, 8, 9]], dtype=object)

In [49]: c[0:2]
Out[49]: array([[1, 2, 3, 4], [4, 5, 6, 7]], dtype=object)

In [49]: 

In [50]: c[0:2]
Out[50]: array([[1, 2, 3, 4], [4, 5, 6, 7]], dtype=object)

In [51]: c[0:3]
Out[51]: array([[1, 2, 3, 4], [4, 5, 6, 7], [6, 7, 8, 9]], dtype=object)

In [52]: b=np.array((5,6,7,8))

In [53]: b.shape
Out[53]: (4,)

In [54]: a=np.array([5,6,7,8])

In [55]: a.shape
Out[55]: (4,)

In [56]: c=np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])

In [57]: c.shape
Out[57]: (3, 4)

In [58]: c.shape=3,4

In [59]: c.shape=4,3

In [60]: c
Out[60]: 
array([[ 1,  2,  3],
       [ 4,  4,  5],
       [ 6,  7,  7],
       [ 8,  9, 10]])

In [61]: c.shape=2,-1

In [62]: c
Out[62]: 
array([[ 1,  2,  3,  4,  4,  5],
       [ 6,  7,  7,  8,  9, 10]])
In [63]: d=a.reshape((2,2))

In [64]: d
Out[64]: 
array([[5, 6],
       [7, 8]])
In [65]: a
Out[65]: array([5, 6, 7, 8])

In [66]: a[1]
Out[66]: 6

In [67]: a[1]=100

In [68]: a
Out[68]: array([  5, 100,   7,   8])

In [69]: d
Out[69]: 
array([[  5, 100],
       [  7,   8]])

In [70]: np.arange(0,1,0.1)
Out[70]: array([ 0. ,  0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7,  0.8,  0.9])
In [71]: np.linspace(0,1,12)
Out[71]: 
array([ 0.        ,  0.09090909,  0.18181818,  0.27272727,  0.36363636,
        0.45454545,  0.54545455,  0.63636364,  0.72727273,  0.81818182,
        0.90909091,  1.        ])
In [72]: help(linspace)
Help on function linspace in module numpy.core.function_base:

linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
    Return evenly spaced numbers over a specified interval.
    
    Returns `num` evenly spaced samples, calculated over the
    interval [`start`, `stop`].
    
    The endpoint of the interval can optionally be excluded.
    
    Parameters
    ----------
    start : scalar
        The starting value of the sequence.
    stop : scalar
        The end value of the sequence, unless `endpoint` is set to False.
        In that case, the sequence consists of all but the last of ``num + 1``
        evenly spaced samples, so that `stop` is excluded.  Note that the step
        size changes when `endpoint` is False.
    num : int, optional
        Number of samples to generate. Default is 50. Must be non-negative.
    endpoint : bool, optional
        If True, `stop` is the last sample. Otherwise, it is not included.
        Default is True.
    retstep : bool, optional
        If True, return (`samples`, `step`), where `step` is the spacing
        between samples.
    dtype : dtype, optional
        The type of the output array.  If `dtype` is not given, infer the data
        type from the other input arguments.
    
        .. versionadded:: 1.9.0
    
    Returns
    -------
    samples : ndarray
        There are `num` equally spaced samples in the closed interval
        ``[start, stop]`` or the half-open interval ``[start, stop)``
        (depending on whether `endpoint` is True or False).
    step : float
        Only returned if `retstep` is True
    
        Size of spacing between samples.
    
    
    See Also
    --------
    arange : Similar to `linspace`, but uses a step size (instead of the
             number of samples).
    logspace : Samples uniformly distributed in log space.
    
    Examples
    --------
    >>> np.linspace(2.0, 3.0, num=5)
        array([ 2.  ,  2.25,  2.5 ,  2.75,  3.  ])
    >>> np.linspace(2.0, 3.0, num=5, endpoint=False)
        array([ 2. ,  2.2,  2.4,  2.6,  2.8])
    >>> np.linspace(2.0, 3.0, num=5, retstep=True)
        (array([ 2.  ,  2.25,  2.5 ,  2.75,  3.  ]), 0.25)
    
    Graphical illustration:
    
    >>> import matplotlib.pyplot as plt
    >>> N = 8
    >>> y = np.zeros(N)
    >>> x1 = np.linspace(0, 10, N, endpoint=True)
    >>> x2 = np.linspace(0, 10, N, endpoint=False)
    >>> plt.plot(x1, y, 'o')
    [<matplotlib.lines.Line2D object at 0x...>]
    >>> plt.plot(x2, y + 0.5, 'o')
    [<matplotlib.lines.Line2D object at 0x...>]
    >>> plt.ylim([-0.5, 1])
    (-0.5, 1)
    >>> plt.show()


In [73]: logspace(0,2,20)
Out[73]: 
array([   1.        ,    1.27427499,    1.62377674,    2.06913808,
          2.6366509 ,    3.35981829,    4.2813324 ,    5.45559478,
          6.95192796,    8.8586679 ,   11.28837892,   14.38449888,
         18.32980711,   23.35721469,   29.76351442,   37.92690191,
         48.32930239,   61.58482111,   78.47599704,  100.        ])

In [74]: s="abcdefgh"

In [75]: fromstring(s,dtype=np.int8)
Out[75]: array([ 97,  98,  99, 100, 101, 102, 103, 104], dtype=int8)

In [76]: help(fromstring)
Help on built-in function fromstring in module numpy.core.multiarray:

fromstring(...)
    fromstring(string, dtype=float, count=-1, sep='')
    
    A new 1-D array initialized from raw binary or text data in a string.
    
    Parameters
    ----------
    string : str
        A string containing the data.
    dtype : data-type, optional
        The data type of the array; default: float.  For binary input data,
        the data must be in exactly this format.
    count : int, optional
        Read this number of `dtype` elements from the data.  If this is
        negative (the default), the count will be determined from the
        length of the data.
    sep : str, optional
        If not provided or, equivalently, the empty string, the data will
        be interpreted as binary data; otherwise, as ASCII text with
        decimal numbers.  Also in this latter case, this argument is
        interpreted as the string separating numbers in the data; extra
        whitespace between elements is also ignored.
    
    Returns
    -------
    arr : ndarray
        The constructed array.
    
    Raises
    ------
    ValueError
        If the string is not the correct size to satisfy the requested
        `dtype` and `count`.
    
    See Also
    --------
    frombuffer, fromfile, fromiter
    
    Examples
    --------
    >>> np.fromstring('\x01\x02', dtype=np.uint8)
    array([1, 2], dtype=uint8)
    >>> np.fromstring('1 2', dtype=int, sep=' ')
    array([1, 2])
    >>> np.fromstring('1, 2', dtype=int, sep=',')
    array([1, 2])
    >>> np.fromstring('\x01\x02\x03\x04\x05', dtype=np.uint8, count=3)
    array([1, 2, 3], dtype=uint8)


In [77]: np.fromstring(s,dtype=np.int16)
Out[77]: array([25185, 25699, 26213, 26727], dtype=int16)

In [78]: x=arange(10,1,-1)

In [79]: x
Out[79]: array([10,  9,  8,  7,  6,  5,  4,  3,  2])
In [80]: b=x[[1,2,3,4]]

In [81]: b
Out[81]: array([9, 8, 7, 6])
In [82]: b[1]=100

In [83]: b
Out[83]: array([  9, 100,   7,   6])

In [84]: x
Out[84]: array([10,  9,  8,  7,  6,  5,  4,  3,  2])

In [85]: x[[2,3]]=100,101

In [86]: x
Out[86]: array([ 10,   9, 100, 101,   6,   5,   4,   3,   2])
In [87]: x[2,3]=100,102
Traceback (most recent call last):

  File "<ipython-input-87-483bce41aafb>", line 1, in <module>
    x[2,3]=100,102

IndexError: too many indices for array


In [88]: c=x[[2,3]]

In [89]: c
Out[89]: array([100, 101])
In [90]: c[[0,1]]=1000,1200

In [91]: c
Out[91]: array([1000, 1200])

In [92]: x
Out[92]: array([ 10,   9, 100, 101,   6,   5,   4,   3,   2])

In [93]: x[[T,F,F,T]]
Traceback (most recent call last):

  File "<ipython-input-93-4e4807da4b49>", line 1, in <module>
    x[[T,F,F,T]]

NameError: name 'T' is not defined


In [94]: x[[True,False,False,True]]
D:\Anaconda3\lib\site-packages\spyderlib\widgets\externalshell\start_ipython_kernel.py:1: FutureWarning: in the future, boolean array-likes will be handled as a boolean array index
  # -*- coding: utf-8 -*-
Out[94]: array([ 9, 10, 10,  9])

In [95]: x=arange(1,5,1)

In [96]: x
Out[96]: array([1, 2, 3, 4])

In [97]: x=arange(0,5,1)

In [98]: x
Out[98]: array([0, 1, 2, 3, 4])

In [99]: x[[True,False,False,True,True]]
D:\Anaconda3\lib\site-packages\spyderlib\widgets\externalshell\start_ipython_kernel.py:1: FutureWarning: in the future, boolean array-likes will be handled as a boolean array index
  # -*- coding: utf-8 -*-
Out[99]: array([1, 0, 0, 1, 1])

In [100]: x[array([True,False,False,True,True])]
Out[100]: array([0, 3, 4])

In [101]: x[array([True])]
D:\Anaconda3\lib\site-packages\spyderlib\widgets\externalshell\start_ipython_kernel.py:1: VisibleDeprecationWarning: boolean index did not match indexed array along dimension 0; dimension is 5 but corresponding boolean dimension is 1
  # -*- coding: utf-8 -*-
Out[101]: array([0])

In [102]: x[array([True,False])]
D:\Anaconda3\lib\site-packages\spyderlib\widgets\externalshell\start_ipython_kernel.py:1: VisibleDeprecationWarning: boolean index did not match indexed array along dimension 0; dimension is 5 but corresponding boolean dimension is 2
  # -*- coding: utf-8 -*-
Out[102]: array([0])

In [103]: x[np.array([True,False])]
D:\Anaconda3\lib\site-packages\spyderlib\widgets\externalshell\start_ipython_kernel.py:1: VisibleDeprecationWarning: boolean index did not match indexed array along dimension 0; dimension is 5 but corresponding boolean dimension is 2
  # -*- coding: utf-8 -*-
Out[103]: array([0])

In [104]: x
Out[104]: array([0, 1, 2, 3, 4])

In [105]: x[np.array([True,False])]
D:\Anaconda3\lib\site-packages\spyderlib\widgets\externalshell\start_ipython_kernel.py:1: VisibleDeprecationWarning: boolean index did not match indexed array along dimension 0; dimension is 5 but corresponding boolean dimension is 2
  # -*- coding: utf-8 -*-
Out[105]: array([0])

In [106]: x[np.array([True,False,False,False,False])]
Out[106]: array([0])

In [107]: x[np.array([True,True])]
D:\Anaconda3\lib\site-packages\spyderlib\widgets\externalshell\start_ipython_kernel.py:1: VisibleDeprecationWarning: boolean index did not match indexed array along dimension 0; dimension is 5 but corresponding boolean dimension is 2
  # -*- coding: utf-8 -*-
Out[107]: array([0, 1])

In [108]: x=np.random.rand(10)

In [109]: x
Out[109]: 
array([ 0.43690701,  0.33819548,  0.04550784,  0.47002394,  0.93635745,
        0.67030661,  0.60716703,  0.69829529,  0.51176957,  0.91308271])

In [110]: x>0.5
Out[110]: array([False, False, False, False,  True,  True,  True,  True,  True,  True], dtype=bool)

In [111]: x[x>0.5]
Out[111]: 
array([ 0.93635745,  0.67030661,  0.60716703,  0.69829529,  0.51176957,
        0.91308271])

In [112]: 10,11==11,10
Out[112]: (10, True, 10)

In [113]: (10,11)==(11,10)
Out[113]: False

In [114]: 10
Out[114]: 10

In [115]: ls
 驱动器 C 中的卷是 win7
 卷的序列号是 CC7B-2D54

 C:\Users\Administrator\Documents\Python Scripts 的目录

2016/03/07  12:05    <DIR>          .
2016/03/07  12:05    <DIR>          ..
               0 个文件              0 字节
               2 个目录  1,241,939,968 可用字节

In [116]: pwd
Out[116]: 'C:\\Users\\Administrator\\Documents\\Python Scripts'

In [117]: x=np.arange(0,60,10)

In [118]: x
Out[118]: array([ 0, 10, 20, 30, 40, 50])

In [119]: x=x.reshape(-1,1)

In [120]: x
Out[120]: 
array([[ 0],
       [10],
       [20],
       [30],
       [40],
       [50]])

In [121]: y=np.arange(0,6)

In [122]: y
Out[122]: array([0, 1, 2, 3, 4, 5])

In [123]: x+y
Out[123]: 
array([[ 0,  1,  2,  3,  4,  5],
       [10, 11, 12, 13, 14, 15],
       [20, 21, 22, 23, 24, 25],
       [30, 31, 32, 33, 34, 35],
       [40, 41, 42, 43, 44, 45],
       [50, 51, 52, 53, 54, 55]])

In [124]: (x+y)[1,]
Out[124]: array([10, 11, 12, 13, 14, 15])

In [125]: (x+y)[1,3:5]
Out[125]: array([13, 14])

In [126]: (x+y)[0,3:5]
Out[126]: array([3, 4])

In [127]: (x+y)[5:,5:]
Out[127]: array([[55]])

In [128]: (x+y)[4:,4:]
Out[128]: 
array([[44, 45],
       [54, 55]])

In [129]: (x+y)[2,:]
Out[129]: array([20, 21, 22, 23, 24, 25])

In [130]: (x+y)[:,2]

In [130]: array([ 2, 12, 22, 32, 42, 52])In [131]: 

In [131]: (x+y)[2::2,::2]
Out[131]: 
array([[20, 22, 24],
       [40, 42, 44]])

In [132]: (x+y)[(0,1,2,3,4),(1,2,3,4,5)]
Out[132]: array([ 1, 12, 23, 34, 45])

In [133]: (x+y)[np.array([1,0,0,1,1,1],dtype=np.bool),]
Out[133]: 
array([[ 0,  1,  2,  3,  4,  5],
       [30, 31, 32, 33, 34, 35],
       [40, 41, 42, 43, 44, 45],
       [50, 51, 52, 53, 54, 55]])

In [134]: persntype=np.dtype({})

In [135]: persntype=np.dtype({'name':['name','age','weight'],'formats':['S32','i','f']})
Traceback (most recent call last):

  File "<ipython-input-135-5c39530f511d>", line 1, in <module>
    persntype=np.dtype({'name':['name','age','weight'],'formats':['S32','i','f']})

  File "D:\Anaconda3\lib\site-packages\numpy\core\_internal.py", line 61, in _usefields
    names, formats, offsets, titles = _makenames_list(adict, align)

  File "D:\Anaconda3\lib\site-packages\numpy\core\_internal.py", line 29, in _makenames_list
    raise ValueError("entry not a 2- or 3- tuple")

ValueError: entry not a 2- or 3- tuple


In [136]: persntype=np.dtype({'names':['name','age','weight'],'formats':['S32','i','f']})

In [137]: a=np.array([("zhang",32,75.7),("wang",18,50.8)],dtype=persntype)

In [138]: a
Out[138]: 
array([(b'zhang', 32, 75.69999694824219), (b'wang', 18, 50.79999923706055)], 
      dtype=[('name', 'S32'), ('age', '<i4'), ('weight', '<f4')])

In [139]: a[1]
Out[139]: (b'wang', 18, 50.79999923706055)

In [140]: a[0]

In [140]: Out[140]: (b'zhang', 32, 75.69999694824219)

In [141]: a.dtype
Out[141]: dtype([('name', 'S32'), ('age', '<i4'), ('weight', '<f4')])

In [142]: 