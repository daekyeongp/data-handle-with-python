# numpy :: boolean & fancy index


```python
import numpy as np
```

### boolean index

- numpy 배열은 특정 조건에 따른 값을 배열 형태로 추출할 수 있음
- Comparison operation 함수들도 모두 사용 가능
- cf) where : index만 추출 // boolean : 값을 추출


```python
test_array = np.array([1, 4, 0, 2, 3, 8, 9, 7], float)
test_array > 3
```




   array([False,  True, False, False, False,  True,  True,  True])




```python
test_array[test_array > 3] # 조건이 True인 index의 element만 추출
```




   array([4., 8., 9., 7.])




```python
condition = test_array < 3 
test_array[condition]
```




   array([1., 0., 2.])




```python
# astype
A = np.array([
[12, 13, 14, 12, 16, 14, 11, 10,  9],
[11, 14, 12, 15, 15, 16, 10, 12, 11],
[10, 12, 12, 15, 14, 16, 10, 12, 12],
[ 9, 11, 16, 15, 14, 16, 15, 12, 10],
[12, 11, 16, 14, 10, 12, 16, 12, 13],
[10, 15, 16, 14, 14, 14, 16, 15, 12],
[13, 17, 14, 10, 14, 11, 14, 15, 10],
[10, 16, 12, 14, 11, 12, 14, 18, 11],
[10, 19, 12, 14, 11, 12, 14, 18, 10],
[14, 22, 17, 19, 16, 17, 18, 17, 13],
[10, 16, 12, 14, 11, 12, 14, 18, 11],
[10, 16, 12, 14, 11, 12, 14, 18, 11],
[10, 19, 12, 14, 11, 12, 14, 18, 10],
[14, 22, 12, 14, 11, 12, 14, 17, 13],
[10, 16, 12, 14, 11, 12, 14, 18, 11]])

B = A < 15
B.astype(np.int)
```




   array([[1, 1, 1, 1, 0, 1, 1, 1, 1],
           [1, 1, 1, 0, 0, 0, 1, 1, 1],
           [1, 1, 1, 0, 1, 0, 1, 1, 1],
           [1, 1, 0, 0, 1, 0, 0, 1, 1],
           [1, 1, 0, 1, 1, 1, 0, 1, 1],
           [1, 0, 0, 1, 1, 1, 0, 0, 1],
           [1, 0, 1, 1, 1, 1, 1, 0, 1],
           [1, 0, 1, 1, 1, 1, 1, 0, 1],
           [1, 0, 1, 1, 1, 1, 1, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 1, 1, 1, 1, 1, 0, 1],
           [1, 0, 1, 1, 1, 1, 1, 0, 1],
           [1, 0, 1, 1, 1, 1, 1, 0, 1],
           [1, 0, 1, 1, 1, 1, 1, 0, 1],
           [1, 0, 1, 1, 1, 1, 1, 0, 1]])



### fancy index

- array를 index value로 사용해서 값을 추출


```python
a = np.array([2, 4, 6, 8], float)
b = np.array([0, 0, 1, 3, 2, 1], int) # 반드시 int로 선언!!!

a[b] #bracket index, b 배열의 값을 index로 하여 a의 값들을 추출함
```




   array([2., 2., 4., 8., 6., 4.])




```python
#take 함수: bracket index와 같은 효과
a.take(b) 
```




   array([2., 2., 4., 8., 6., 4.])




```python
a = np.array([[1, 4], [9, 16]], float)
b = np.array([0, 0, 1, 1, 0], int)
c = np.array([0, 1, 1, 1, 1], int)

a[b,c] # b를 row index, c를 column index로 변환하여 표시함
```




   array([ 1.,  4., 16., 16.,  4.])




```python
a = np.array([[1, 4], [9, 16]], float)
a[b]
```




   array([[ 1.,  4.],
           [ 1.,  4.],
           [ 9., 16.],
           [ 9., 16.],
           [ 1.,  4.]])


<br/>

***
https://www.boostcourse.org/ai222/lecture/24071