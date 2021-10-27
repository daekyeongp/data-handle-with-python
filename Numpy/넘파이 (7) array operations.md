# numpy :: array operations


```python
import numpy as np
```

### operations b/t arrays

- numpy는 array 간의 기본적인 사칙연산을 지원


```python
test_a = np.array([[1,2,3],[4,5,6]], float)
```


```python
# Matrix + Matrix 연산
test_a + test_a 
```




   array([[ 2.,  4.,  6.],
           [ 8., 10., 12.]])




```python
# Matrix - Matrix 연산
test_a - test_a 
```




   array([[0., 0., 0.],
           [0., 0., 0.]])




```python
# Matrix내 element들 간 같은 위치에 있는 값들끼리 연산
test_a * test_a 
```




   array([[ 1.,  4.,  9.],
           [16., 25., 36.]])



### element-wise operations

- array간 shape이 같을 때 일어나는 연산


```python
matrix_a = np.arange(1,13).reshape(3,4)
matrix_a * matrix_a
```




   array([[  1,   4,   9,  16],
           [ 25,  36,  49,  64],
           [ 81, 100, 121, 144]])



### dot product

- matrix의 기본 연산
- dot 함수 사용


```python
test_a = np.arange(1,7).reshape(2,3)
test_b = np.arange(7,13).reshape(3,2)
```


```python
test_a.dot(test_b)
```




   array([[ 58,  64],
           [139, 154]])



### transpose

- transpose 또는 T attribute 사용


```python
test_a = np.arange(1,7).reshape(2,3)
test_a
```




   array([[1, 2, 3],
           [4, 5, 6]])




```python
test_a.transpose()
```




   array([[1, 4],
           [2, 5],
           [3, 6]])




```python
test_a.T
```




   array([[1, 4],
           [2, 5],
           [3, 6]])




```python
test_a.T.dot(test_a) # matrix간 곱셈
```




   array([[17, 22, 27],
           [22, 29, 36],
           [27, 36, 45]])



### broadcasting

- Shape이 다른 배열 간 연산을 지원하는 기능


```python
test_matrix = np.array([[1,2,3],[4,5,6]], float)
scalar = 3
```


```python
# Matrix - Scalar 덧셈
test_matrix + scalar 
```




   array([[4., 5., 6.],
           [7., 8., 9.]])




```python
# Matrix - Scalar 뺄셈
test_matrix - scalar
```




   array([[-2., -1.,  0.],
           [ 1.,  2.,  3.]])




```python
# Matrix - Scalar 곱셈
test_matrix * scalar
```




   array([[ 3.,  6.,  9.],
           [12., 15., 18.]])




```python
# Matrix - Scalar 나눗셈
test_matrix / 5 
```




   array([[0.2, 0.4, 0.6],
           [0.8, 1. , 1.2]])




```python
# Matrix - Scalar 몫
test_matrix // 0.2 
```




   array([[ 4.,  9., 14.],
           [19., 24., 29.]])




```python
# Matrix - Scalar 제곱
test_matrix ** 2 
```




   array([[ 1.,  4.,  9.],
           [16., 25., 36.]])




```python
# vector - Matrix 간의 연산도 지원
test_matrix = np.arange(1,13).reshape(4,3)
test_vector = np.arange(10,40,10)
test_matrix+ test_vector
```




   array([[11, 22, 33],
           [14, 25, 36],
           [17, 28, 39],
           [20, 31, 42]])



### Numpy performance 

- timeit : jupyter 환경에서 코드의 퍼포먼스를 체크하는 함수
- 일반적으로 속도는 for loop < list comprehension < numpy
- Numpy는 C로 구현되어 있어, 성능을 확보하는 대신 파이썬의 가장 큰 특징인 dynamic typing을 포기
- 대용량 계산에서는 가장 흔히 사용됨
- Concatenate처럼 계산이 아닌 할당에서는 연산 속도의 이점이 없음


```python
def sclar_vector_product(scalar, vector):
    result = []
    for value in vector:
        result.append(scalar * value)
    return result 

iternation_max = 100000000

vector = list(range(iternation_max))
scalar = 2

%timeit sclar_vector_product(scalar, vector) # for loop을 이용한 성능
```


```python
%timeit [scalar * value for value in range(iternation_max)] # list comprehension을 이용한 성능
%timeit np.arange(iternation_max) * scalar # numpy를 이용한 성능
```

<br/>

***
https://www.boostcourse.org/ai222/lecture/24071