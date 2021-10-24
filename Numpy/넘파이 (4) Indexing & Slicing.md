# numpy :: indexing & slicing


```python
import numpy as np
```

### indexing

- list와 달리 2차원 배열에서 [0,0]과 같은 표기법을 제공
- matrix일 경우 앞은 row, 뒤는 column을 의미



```python
test_example = np.array([[1, 2, 3], [4.5, 5, 6]], int)
test_example
```




   array([[1, 2, 3],
           [4, 5, 6]])




```python
test_example[0][0]
```




   1




```python
test_example[0,0]
```




   1




```python
test_example[0,0] = 12 # matrix 0,0에 12 할당
test_example
```




   array([[12,  2,  3],
           [ 4,  5,  6]])




```python
test_example[0][0] = 5 # matrix 0,0에 5 할당
test_example[0,0]
```




   5



### slicing

- list와 달리 행과 열 부분을 나눠서 slicing이 가능 (for문 필요 없게 함)
- matrix의 부분 집합을 추출할 때 유용



```python
test_exmaple = np.array([
    [1, 2, 5,8], [1, 2, 5,8],[1, 2, 5,8],[1, 2, 5,8]], int)
test_exmaple[:2,:]
```




   array([[1, 2, 5, 8],
           [1, 2, 5, 8]])




```python
test_exmaple[:,1:3] 
```




   array([[2, 5],
           [2, 5],
           [2, 5],
           [2, 5]])




```python
test_exmaple[1,:2]
```




   array([1, 2])




```python
test_exmaple = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], int)
test_exmaple[:,2:] # 전체 Row의 2열 이상
```




   array([[ 3,  4,  5],
           [ 8,  9, 10]])




```python
test_exmaple[1:3] # 1 Row ~ 2 Row의 전체
```




   array([[ 6,  7,  8,  9, 10]])




```python
a = np.arange(100).reshape(10,10)
a[:, -1].reshape(-1,1)
```




   array([[ 9],
           [19],
           [29],
           [39],
           [49],
           [59],
           [69],
           [79],
           [89],
           [99]])

<br/>

***
https://www.boostcourse.org/ai222/lecture/24071
