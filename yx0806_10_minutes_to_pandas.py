Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
>>> import numpy as np
>>> import pandas as pd
>>> s = pd.Series([1, 3, 5, np.nan, 6,8])
>>> s
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
>>> s2 = pd.Series(np.random.randn(5),index = ['q', 'w', 'e'])
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    s2 = pd.Series(np.random.randn(5),index = ['q', 'w', 'e'])
  File "C:\Users\Yuxi\AppData\Roaming\Python\Python38\site-packages\pandas\core\series.py", line 313, in __init__
    raise ValueError(
ValueError: Length of passed values is 5, index implies 3.
>>> s2 = pd.Series(np.random.randn(5))
>>> s2
0   -1.252560
1    0.201223
2    2.506157
3   -0.753058
4   -0.541137
dtype: float64
>>> s.index
RangeIndex(start=0, stop=6, step=1)
>>> s2 = pd.Series(np.random.randn(5),index = ['a', 'b', 'c', 'd', 'e'])
>>> s2
a   -0.556117
b    1.840678
c   -0.411471
d   -0.558081
e    1.409599
dtype: float64
>>> s2.index
Index(['a', 'b', 'c', 'd', 'e'], dtype='object')
>>> datas = pd.date_range('20200517', periods = 6)
>>> datas
DatetimeIndex(['2020-05-17', '2020-05-18', '2020-05-19', '2020-05-20',
               '2020-05-21', '2020-05-22'],
              dtype='datetime64[ns]', freq='D')
>>> dates = datas
>>> df = pd.DataFrame(np.random.randn(6,4), index = dates, columns = list ('ABCD'))
>>> df
                   A         B         C         D
2020-05-17 -0.806064  0.699468  0.338983 -1.126036
2020-05-18  1.730969 -0.054287 -0.389495 -1.643036
2020-05-19 -0.611317 -0.779093  1.915488  2.016263
2020-05-20 -0.052797 -0.098746 -2.152662 -0.545372
2020-05-21  1.562959  1.005736  0.293435  0.582258
2020-05-22  0.803729  0.140965  0.159682  1.073847
>>> df.head(3)
                   A         B         C         D
2020-05-17 -0.806064  0.699468  0.338983 -1.126036
2020-05-18  1.730969 -0.054287 -0.389495 -1.643036
2020-05-19 -0.611317 -0.779093  1.915488  2.016263
>>> df.tail(3)
                   A         B         C         D
2020-05-20 -0.052797 -0.098746 -2.152662 -0.545372
2020-05-21  1.562959  1.005736  0.293435  0.582258
2020-05-22  0.803729  0.140965  0.159682  1.073847
>>> df.describe()
              A         B         C         D
count  6.000000  6.000000  6.000000  6.000000
mean   0.437913  0.152340  0.027572  0.059654
std    1.091852  0.632624  1.317323  1.400078
min   -0.806064 -0.779093 -2.152662 -1.643036
25%   -0.471687 -0.087631 -0.252201 -0.980870
50%    0.375466  0.043339  0.226559  0.018443
75%    1.373152  0.559842  0.327596  0.950949
max    1.730969  1.005736  1.915488  2.016263
>>> a = np.arange(24).reshape(6,4)
>>> a
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15],
       [16, 17, 18, 19],
       [20, 21, 22, 23]])
>>> a.shape
(6, 4)
>>> a.ndim
2
>>> type(a)
<class 'numpy.ndarray'>
>>> a.dtype
dtype('int32')
>>> b = np.array([2,3,4])
>>> b.dtype
dtype('int32')
>>> c = np.array(list['ABCD'])
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    c = np.array(list['ABCD'])
TypeError: 'type' object is not subscriptable
>>> c = np.array(list('ABCD'))
>>> C
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    C
NameError: name 'C' is not defined
>>> c
array(['A', 'B', 'C', 'D'], dtype='<U1')
>>> 