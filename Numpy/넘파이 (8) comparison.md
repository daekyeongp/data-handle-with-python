# numpy :: comparison


```python
import numpy as np
```

### All & Any

- array의 데이터 전부(and) 또는 일부(or)가 조건에 만족하는지 여부 반환


```python
a = np.arange(10)
a
```




   array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])




```python
a>5
```




   array([False, False, False, False, False, False,  True,  True,  True,
            True])




```python
a<0
```




   array([False, False, False, False, False, False, False, False, False,
           False])




```python
# any : 하나라도 조건에 만족한다면 true
np.any(a>5), np.any(a<0)
```




   (True, False)




```python
# all : 모두가 조건에 만족한다면 true
np.all(a>5) , np.all(a < 10)
```




   (False, True)



### comparison operation

- numpy는 배열의 크기가 동일할 때 element간 비교의 결과를 boolean type으로 반환하여 돌려줌


```python
test_a = np.array([1, 3, 0], float)
test_b = np.array([5, 2, 1], float)
test_a > test_b
```




   array([False,  True, False])




```python
test_a == test_b
```




   array([False, False, False])




```python
(test_a > test_b).any()
```




   True




```python
a = np.array([1, 3, 0], float)
np.logical_and(a > 0, a < 3) # AND 조건의 condition
```




   array([ True, False, False])




```python
b = np.array([True, False, True], bool)
np.logical_not(b) # NOT 조건의 condition
```




   array([False,  True, False])




```python
c = np.array([False, True, False], bool)
np.logical_or(b, c) # OR 조건의 condition
```




   array([ True,  True,  True])



### np.where

- where(condition, TRUE, FALSE) 
- condition 설정하고, true일 때 그 값 반환, false일 때 그 값 반환
- np.where과 정렬하는 기법을 잘 활용하기~~ 


```python
a
```




   array([1., 3., 0.])




```python
np.where(a > 0, 3, 2) 
# a > 0 을 만족하면(true) 3을 , 만족하지 않으면(false) 2를 반환
```




   array([3, 3, 2])




```python
np.where(a>0)
```




   (array([0, 1], dtype=int64),)




```python
a = np.arange(10)
np.where(a > 5)
```




   (array([6, 7, 8, 9], dtype=int64),)




```python
a = np.array([1, np.NaN, np.Inf], float)
np.isnan(a) #is Not a Number
```




   array([False,  True, False])




```python
np.isfinite(a) # is finite number
```




   array([ True, False, False])



### argmax & argmin

- argmax : array 내 최대값의 index 반환
- argmin : array 내 최소값의 index 반환


```python
a = np.array([1,2,4,5,8,78,23,3])
np.argmax(a) , np.argmin(a)
```




   (5, 0)




```python
# axis 기반의 반환
a=np.array([[1,2,4,7],[9,88,6,45],[9,76,3,4]])
np.argmax(a, axis=1) , np.argmin(a, axis=0)
```




   (array([3, 1, 1], dtype=int64), array([0, 0, 2, 2], dtype=int64))



<br/>

***
https://www.boostcourse.org/ai222/lecture/24071