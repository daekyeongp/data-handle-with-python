# <span style="color:slateblue">axis</span>

- 모든 operation function을 실행할 때, 기준이 되는 dimension 축
- <span style='color:lightcoral'>새로 생기는 것이 0이 됨</span>

> 
**1. axis=0 (index)**
- 행 방향으로 동작 ➡
- 작업 결과가 행으로 나타남

> **2. axis=1 (columns)**
- 열 방향으로 동작 ⬇
- 작업 결과가 열로 나타남


```python
import numpy as np
import pandas as pd
```


```python
test_array = np.arange(1, 13).reshape(3, 4)
test_array
```




   array([[ 1,  2,  3,  4],
           [ 5,  6,  7,  8],
           [ 9, 10, 11, 12]])



![](/images/axis1.png)


```python
df = pd.DataFrame(
    {'name': ['KIM', 'LEE', 'SMITH','BROWN', 'MILLER'],
     'age': [24, 32, 43, 24, np.nan],
     'height': [178, 168, 171, 185, 176],
     'sex': ['M', 'F', 'F', 'M', 'F']})
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>age</th>
      <th>height</th>
      <th>sex</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>KIM</td>
      <td>24.0</td>
      <td>178</td>
      <td>M</td>
    </tr>
    <tr>
      <th>1</th>
      <td>LEE</td>
      <td>32.0</td>
      <td>168</td>
      <td>F</td>
    </tr>
    <tr>
      <th>2</th>
      <td>SMITH</td>
      <td>43.0</td>
      <td>171</td>
      <td>F</td>
    </tr>
    <tr>
      <th>3</th>
      <td>BROWN</td>
      <td>24.0</td>
      <td>185</td>
      <td>M</td>
    </tr>
    <tr>
      <th>4</th>
      <td>MILLER</td>
      <td>NaN</td>
      <td>176</td>
      <td>F</td>
    </tr>
  </tbody>
</table>
</div>



<br/>

***

> **<span style="color:lightcoral">axis 1</span>을 기준으로 요소들의 합**
- 1 + 2 + 3 + 4 = 10
- 5 + 6 + 7 + 8 = 26
- 9 + 10 + 11 + 12 = 42


```python
test_array.sum(axis=1)
```




   array([10, 26, 42])


<br/>

> **<span style="color:lightcoral">axis 1</span>을 기준으로 drop**</br>


```python
df.drop(['age', 'height'], axis=1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>sex</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>KIM</td>
      <td>M</td>
    </tr>
    <tr>
      <th>1</th>
      <td>LEE</td>
      <td>F</td>
    </tr>
    <tr>
      <th>2</th>
      <td>SMITH</td>
      <td>F</td>
    </tr>
    <tr>
      <th>3</th>
      <td>BROWN</td>
      <td>M</td>
    </tr>
    <tr>
      <th>4</th>
      <td>MILLER</td>
      <td>F</td>
    </tr>
  </tbody>
</table>
</div>



<br/>

***

> **<span style="color:olivedrab">axis 0</span>을 기준으로 요소들의 합**</br>
- 1 + 5 + 9 = 15
- 2 + 6 + 10 = 18
- 3 + 7 + 11 = 21
- 4 + 8 + 12 = 24


```python
test_array.sum(axis=0)
```




   array([15, 18, 21, 24])

<br/>


> **<span style="color:olivedrab">axis 0</span>을 기준으로 drop**


```python
df.drop([1,2], axis=0)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>age</th>
      <th>height</th>
      <th>sex</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>KIM</td>
      <td>24.0</td>
      <td>178</td>
      <td>M</td>
    </tr>
    <tr>
      <th>3</th>
      <td>BROWN</td>
      <td>24.0</td>
      <td>185</td>
      <td>M</td>
    </tr>
    <tr>
      <th>4</th>
      <td>MILLER</td>
      <td>NaN</td>
      <td>176</td>
      <td>F</td>
    </tr>
  </tbody>
</table>
</div>



<br/> 

***


### third - order tensor


```python
third_order_tensor = np.array([test_array, test_array, test_array])
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



![](/images/axis2.png)


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


