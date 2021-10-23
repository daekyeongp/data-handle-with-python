# numpy :: Handling Shape


```python
import numpy as np
```

### reshape

- array의 shape의 크기를 변경 (element의 갯수는 동일)
- array의 size만 같다면 다차원으로 자유로이 변경 가능



```python
# ex ) 2차원 배열을 reshape해서
test_matrix = [[1,2,3,4], [1,2,5,8]]
np.array(test_matrix).shape
```




   (2, 4)




```python
# (2, 2, 2) 크기로 변경
np.array(test_matrix).reshape(2,2,2)
```




   array([[[1, 2],
            [3, 4]],
    
           [[1, 2],
            [5, 8]]])




```python
# vector로 변경
test =np.array(test_matrix).reshape(8,)
test
```




   array([1, 2, 3, 4, 1, 2, 5, 8])




```python
# -1 : size를 기반으로 row 개수 선정
test.reshape(-1, 1)
```




   array([[1],
           [2],
           [3],
           [4],
           [1],
           [2],
           [5],
           [8]])




```python
np.array(test_matrix).reshape(2,4).shape
```




   (2, 4)




```python
np.array(test_matrix).reshape(2,-1).shape
```




   (2, 4)



### flatten

- 다차원 array를 1차원 array로 변환
- reshape를 써도 되지만, 1차원으로 펴주는 유용한 함수 !
 


```python
test_matrix = [[[1,2,3,4], [1,2,5,8]], [[1,2,3,4], [1,2,5,8]]]
np.array(test_matrix).flatten()
```




   array([1, 2, 3, 4, 1, 2, 5, 8, 1, 2, 3, 4, 1, 2, 5, 8])


<br/>

***
https://www.boostcourse.org/ai222/lecture/24071