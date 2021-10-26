# numpy :: operation functions


```python
import numpy as np
```

### sum

- ndarray의 element들 간의 합을 구함
- list의 sum 기능과 동일


```python
test_array = np.arange(1,11)
test_array.sum(dtype=np.float)
```




   55.0



### axis

- 모든 operation function을 실행할 때, 기준이 되는 dimension 축
- 새로 생기는 것이 0이 됨


```python
test_array = np.arange(1, 13).reshape(3,4)
# (3,4) 에서 3 -> axis=0 , 4 -> axis=1
test_array
```




   array([[ 1,  2,  3,  4],
           [ 5,  6,  7,  8],
           [ 9, 10, 11, 12]])




```python
test_array.sum(axis=1)
```




   array([10, 26, 42])




```python
test_array.sum(axis=0)
```




   array([15, 18, 21, 24])




```python
third_order_tensor = np.array([test_array,test_array,test_array])
third_order_tensor
```




   array([[[ 1,  2,  3,  4],
            [ 5,  6,  7,  8],
            [ 9, 10, 11, 12]],

   [[ 1,  2,  3,  4],
            [ 5,  6,  7,  8],
            [ 9, 10, 11, 12]],
    
   [[ 1,  2,  3,  4],
            [ 5,  6,  7,  8],
            [ 9, 10, 11, 12]]])




```python
third_order_tensor.sum(axis=2)
```




   array([[10, 26, 42],
           [10, 26, 42],
           [10, 26, 42]])




```python
third_order_tensor.sum(axis=1)
```




   array([[15, 18, 21, 24],
           [15, 18, 21, 24],
           [15, 18, 21, 24]])




```python
third_order_tensor.sum(axis=0)
```




   array([[ 3,  6,  9, 12],
           [15, 18, 21, 24],
           [27, 30, 33, 36]])



### mean & std

- ndarray의 element들 간의 평균 또는 표준편차를 반환


```python
test_array = np.arange(1,13).reshape(3,4)
test_array
```




   array([[ 1,  2,  3,  4],
           [ 5,  6,  7,  8],
           [ 9, 10, 11, 12]])




```python
#평균
test_array.mean()
```




   6.5




```python
test_array.mean(axis=0)
```




   array([5., 6., 7., 8.])




```python
# 표준편차
test_array.std()
```




   3.452052529534663




```python
test_array.std(axis=0)
```




   array([3.26598632, 3.26598632, 3.26598632, 3.26598632])



### concatenate (콘캣)

- numpy array를 합치는 함수


```python
a = np.array([1, 2, 3])
b = np.array([2, 3, 4])

np.vstack((a,b))
```




   array([[1, 2, 3],
           [2, 3, 4]])




```python
a = np.array([ [1], [2], [3]])
b = np.array([ [2], [3], [4]])

np.hstack((a,b))
```




   array([[1, 2],
           [2, 3],
           [3, 4]])




```python
a = np.array([[1, 2, 3]])
b = np.array([[2, 3, 4]])

np.concatenate( (a,b) ,axis=0)
```




   array([[1, 2, 3],
           [2, 3, 4]])




```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])

np.concatenate( (a,b.T) ,axis=1)
```




   array([[1, 2, 5],
           [3, 4, 6]])




```python
# array를 list로 변환

a.tolist()
```




   [[1, 2], [3, 4]]


<br/>

***
https://www.boostcourse.org/ai222/lecture/24071