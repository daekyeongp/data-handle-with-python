# numpy :: creation function


```python
import numpy as np
```

### arange

- array의 범위를 지정하여, 값의 list를 생성하는 명령어


```python
np.arange(30) # arange : list의 range와 같은 효과, integer로 0부터 29까지 배열 추출
```




   array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
           17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29])




```python
np.arange(0, 5, 0.5) # (시작, 끝, step) & floating point 표시 가능
```




   array([0. , 0.5, 1. , 1.5, 2. , 2.5, 3. , 3.5, 4. , 4.5])




```python
np.arange(30).reshape(5, 6)
```




   array([[ 0,  1,  2,  3,  4,  5],
           [ 6,  7,  8,  9, 10, 11],
           [12, 13, 14, 15, 16, 17],
           [18, 19, 20, 21, 22, 23],
           [24, 25, 26, 27, 28, 29]])



### zeros

- 0으로 가득찬 ndarray 생성
- np.zeros(shape, dtype, order)



```python
np.zeros(shape=(10,), dtype=np.int8) # 10 - zero vector 생성
```




   array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=int8)




```python
np.zeros((2, 5)) # 2 by 5 - zero matrix 생성
```




   array([[0., 0., 0., 0., 0.],
           [0., 0., 0., 0., 0.]])



### ones 

- 1로 가득찬 ndarray 생성
- np.ones(shape, dtype, order)


```python
np.ones(shape=(10,), dtype=np.int8)
```




   array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], dtype=int8)




```python
np.ones((2,5))
```




   array([[1., 1., 1., 1., 1.],
           [1., 1., 1., 1., 1.]])



### empty

- shape만 주어지고 비어있는 ndarray 생성
- memory initialization이 되지 않음
- 메모리 공간만 잡아주는 것


```python
np.empty(shape=(10,), dtype=np.int8)
```




   array([110,   0,  32,   0,  70,   0, 105,   0, 108,   0], dtype=int8)




```python
np.empty((3,5))
```




   array([[0., 0., 0., 0., 0.],
           [0., 0., 0., 0., 0.],
           [0., 0., 0., 0., 0.]])



### something_like

- 기존 ndarray의 shape의 크기만큼 1, 0 또는 empty array 리턴


```python
test_matrix = np.arange(30).reshape(5, 6)
np.ones_like(test_matrix)
```




   array([[1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1]])




```python
np.zeros_like(test_matrix)
```




   array([[0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0]])



### identity

- 단위 행렬 (정방행렬) 생성


```python
np.identity(n=3, dtype=np.int8) # n : number of rows
```




   array([[1, 0, 0],
           [0, 1, 0],
           [0, 0, 1]], dtype=int8)




```python
np.identity(5)
```




   array([[1., 0., 0., 0., 0.],
           [0., 1., 0., 0., 0.],
           [0., 0., 1., 0., 0.],
           [0., 0., 0., 1., 0.],
           [0., 0., 0., 0., 1.]])



### eye

- 대각선이 1인 행렬, k값의 시작 index의 변경이 가능


```python
np.eye(N=3, M=5, dtype = np.int8)
```




   array([[1, 0, 0, 0, 0],
           [0, 1, 0, 0, 0],
           [0, 0, 1, 0, 0]], dtype=int8)




```python
np.eye(3)
```




   array([[1., 0., 0.],
           [0., 1., 0.],
           [0., 0., 1.]])




```python
np.eye(3, 5, k=2) # k : start index
```




   array([[0., 0., 1., 0., 0.],
           [0., 0., 0., 1., 0.],
           [0., 0., 0., 0., 1.]])



### diag

- 대각 행렬의 값을 추출함


```python
matrix = np.arange(9).reshape(3,3)
np.diag(matrix)
```




   array([0, 4, 8])




```python
np.diag(matrix, k=1) # k : start index
```




   array([1, 5])



### random sampling

- 데이터 분포에 따른 sampling으로 array 생성


```python
np.random.uniform(0,1,10).reshape(2,5) # 균등분포
```




   array([[0.39687944, 0.14559092, 0.62898727, 0.26847138, 0.60052723],
           [0.69149895, 0.40151342, 0.02206676, 0.7171968 , 0.81369266]])




```python
np.random.normal(0,1,10).reshape(2,5) # 정규분포
```




   array([[-0.04325594, -0.50706879, -0.37899264, -0.35053484,  0.18610277],
           [-1.0736414 ,  0.34261525,  1.18722716, -1.84160466,  0.75003724]])

<br/>

***
https://www.boostcourse.org/ai222/lecture/24071
