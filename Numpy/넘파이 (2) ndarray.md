# numpy :: ndarray

### numpy 모듈 호출 (import)

- numpy의 호출 방법

- 일반적으로 numpy는 np라는 별칭(alias)을 이용해서 호출함

- 특별한 이유는 없음 .. 세계적인 약속 같은 것



```python
import numpy as np
```

### array creation

- numpy는 np.array 함수를 활용하여 배열을 생성 -> ndarray (numpy dimension array)

- numpy는 하나의 데이터 타입만 배열에 넣을 수 있음

- 리스트와 가장 큰 차이점 : Dynamic typing not supported

- C의 array를 사용하여 배열 생성



```python
test_array = np.array(["1", "4", 5, 8], float)
test_array
```




   array([1., 4., 5., 8.])




```python
type(test_array[3])
```




   numpy.float64




```python
test_array = np.array([1, 4, 5, "8"], np.float32) # string type의 데이터("8")를 입력해도
test_array
```




   array([1., 4., 5., 8.], dtype=float32)




```python
type(test_array[3]) # float type으로 자동 형변환 실시
```




   numpy.float32




```python
test_array.dtype # dtype : 배열 전체의 data type을 반환
```




   dtype('float32')




```python
test_array.shape # shape : 배열의 shape을 반환함 (튜플 타입)
```




   (4,)



### array shape

- array (vector, matrix, tensor)의 크기, 형태 등에 대한 정보



```python
# array shape (vector)
test_array = np.array([1, 4, 5, "8"], float)
test_array.shape # ndarray의 shape을 반환 (튜플 타입)
```




   (4,)




```python
# array shape (matrix)
matrix = [[1, 2, 5, 8], [1, 2, 5, 8], [1, 2, 5, 8]]
np.array(matrix, int).shape # ndarray의 shape을 반환 (튜플)
```




   (3, 4)




```python
# array shape (3rd order tensor)
tensor  = [[[1,2,5,8],[1,2,5,8],[1,2,5,8]], 
           [[1,2,5,8],[1,2,5,8],[1,2,5,8]], 
           [[1,2,5,8],[1,2,5,8],[1,2,5,8]], 
           [[1,2,5,8],[1,2,5,8],[1,2,5,8]]]
np.array(tensor, int).shape # ndarray의 shape을 반환 (튜플) 
# 4 -> 깊이, 3 -> column, 4 -> row
```




   (4, 3, 4)




```python
# ndim : number of dimension
np.array(tensor, int).ndim
```




   3




```python
# size : 전체 data의 개수
np.array(tensor, int).size
```




   48



### array dtype

- ndarray의 single element가 가지는 datatype
- 각 element가 차지하는 memory의 크기가 결정됨



```python
np.array([[1, 2, 3], [4.5, 5, 6]], dtype=int) # data type을 integer로 선언
```




   array([[1, 2, 3],
           [4, 5, 6]])




```python
np.array([[1, 2, 3], [4.5, "5", "6"]], dtype=np.float32) # data type을 float로 선언
```




   array([[1. , 2. , 3. ],
           [4.5, 5. , 6. ]], dtype=float32)




```python
# nbytes : ndarray의 object의 메모리 크기를 반환

np.array([[1, 2, 3], [4.5, "5", "6"]], dtype=np.float32).nbytes 
# 6 * 32bits = 6 * 4bytes = 24bytes
```




   24




```python
np.array([[1, 2, 3], [4.5, "5", "6"]], dtype=np.int8).nbytes 
# 6 * 8bits = 6 * 1bytes = 6bytes
```




   6




```python
np.array([[1, 2, 3], [4.5, "5", "6"]], dtype=np.float64).nbytes
# 6 * 64 bits = 6 * 8bytes = 48bytes
```




   48


***
https://www.boostcourse.org/ai222/lecture/24071