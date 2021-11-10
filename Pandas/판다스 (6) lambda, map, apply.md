# pandas :: lambda, map, apply


```python
import pandas as pd
import numpy as np
```


```python
from pandas import Series
```

### Lambda 함수

- 한 줄로 함수를 표현하는 익명 함수 기법
- Lisp 언어에서 시작된 기법으로 오늘날 현대언어에 많이 사용
- lambda argument : expression


```python
f = lambda x,y : x+y
f(1,4)
```




   5




```python
# 하나의 argument만 처리하는 lambda함수
f = lambda x : x/2
f(3)
```




   1.5




```python
f = lambda x : x**2
f(3)
```




   9




```python
# 이름을 할당하지 않는 lambda함수
(lambda x: x+1)(5)
```




   6



### map 함수

- 함수와 sequence형 데이터를 인자로 받아 각 element마다 입력받은 함수를 적용하여 list로 반환
- 일반적으로 함수를 lambda 형태로 표현함
- map(function, sequence)


```python
ex = [1, 2, 3, 4, 5]
f = lambda x : x**2
list(map(f,ex))
```




   [1, 4, 9, 16, 25]




```python
# 두 개 이상의 argument가 있을 때는 두개의 sequence형을 써야함
f = lambda x, y : x+y
list(map(f, ex, ex))
```




   [2, 4, 6, 8, 10]




```python
# 익명함수 그대로 사용할 수 있음
list(map(lambda x : x+x, ex))
```




   [2, 4, 6, 8, 10]



### map for series

- pandas의 series type 데이터에서도 map 함수 사용 가능
- function 대신 dict, sequence형 자료 등으로 대체 가능


```python
s1 = Series(np.arange(10))
s1.head(5)
```




   0    0
    1    1
    2    2
    3    3
    4    4
    dtype: int32




```python
s1.map(lambda x : x**2).head(5)
```




   0     0
    1     1
    2     4
    3     9
    4    16
    dtype: int64




```python
d1 = {1: 'A', 2: 'B', 3: 'C'}
s1.map(d1).head(5)  #dict type으로 데이터 교체 & 없는 값은 NaN
```




   0    NaN
    1      A
    2      B
    3      C
    4    NaN
    dtype: object




```python
s2 = Series(np.arange(10, 20))
s1.map(s2).head(5)  # 같은 위치의 데이터를 s2로 전환
```




   0    10
    1    11
    2    12
    3    13
    4    14
    dtype: int32



### Example - map for series


```python
df = pd.read_csv("wages.csv")
df.head()
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
      <th>earn</th>
      <th>height</th>
      <th>sex</th>
      <th>race</th>
      <th>ed</th>
      <th>age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>79571.299011</td>
      <td>73.89</td>
      <td>male</td>
      <td>white</td>
      <td>16</td>
      <td>49</td>
    </tr>
    <tr>
      <th>1</th>
      <td>96396.988643</td>
      <td>66.23</td>
      <td>female</td>
      <td>white</td>
      <td>16</td>
      <td>62</td>
    </tr>
    <tr>
      <th>2</th>
      <td>48710.666947</td>
      <td>63.77</td>
      <td>female</td>
      <td>white</td>
      <td>16</td>
      <td>33</td>
    </tr>
    <tr>
      <th>3</th>
      <td>80478.096153</td>
      <td>63.22</td>
      <td>female</td>
      <td>other</td>
      <td>16</td>
      <td>95</td>
    </tr>
    <tr>
      <th>4</th>
      <td>82089.345498</td>
      <td>63.08</td>
      <td>female</td>
      <td>white</td>
      <td>17</td>
      <td>43</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.sex.unique()
```




   array(['male', 'female'], dtype=object)




```python
df["sex_code"] = df.sex.map({"male" : 0, "female" : 1})  #성별 str -> 성별 code
df.head(5)
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
      <th>earn</th>
      <th>height</th>
      <th>sex</th>
      <th>race</th>
      <th>ed</th>
      <th>age</th>
      <th>sex_code</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>79571.299011</td>
      <td>73.89</td>
      <td>male</td>
      <td>white</td>
      <td>16</td>
      <td>49</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>96396.988643</td>
      <td>66.23</td>
      <td>female</td>
      <td>white</td>
      <td>16</td>
      <td>62</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>48710.666947</td>
      <td>63.77</td>
      <td>female</td>
      <td>white</td>
      <td>16</td>
      <td>33</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>80478.096153</td>
      <td>63.22</td>
      <td>female</td>
      <td>other</td>
      <td>16</td>
      <td>95</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>82089.345498</td>
      <td>63.08</td>
      <td>female</td>
      <td>white</td>
      <td>17</td>
      <td>43</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



### ✨ Replace function

- map 함수의 기능 중 데이터 변환 기능만 담당
- 데이터 변환시 많이 사용하는 함수


```python
df. sex.replace({"male": 0, "female" : 1}).head()  # dict type 적용
```




   0    0
    1    1
    2    1
    3    1
    4    1
    Name: sex, dtype: int64




```python
df.sex.replace(["male", "female"], [0,1], inplace=True)
df.head(5)
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
      <th>earn</th>
      <th>height</th>
      <th>sex</th>
      <th>race</th>
      <th>ed</th>
      <th>age</th>
      <th>sex_code</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>79571.299011</td>
      <td>73.89</td>
      <td>0</td>
      <td>white</td>
      <td>16</td>
      <td>49</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>96396.988643</td>
      <td>66.23</td>
      <td>1</td>
      <td>white</td>
      <td>16</td>
      <td>62</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>48710.666947</td>
      <td>63.77</td>
      <td>1</td>
      <td>white</td>
      <td>16</td>
      <td>33</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>80478.096153</td>
      <td>63.22</td>
      <td>1</td>
      <td>other</td>
      <td>16</td>
      <td>95</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>82089.345498</td>
      <td>63.08</td>
      <td>1</td>
      <td>white</td>
      <td>17</td>
      <td>43</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



### apply for dataframe

- map과 달리, series 전체(column)에 해당 함수를 적용
- 입력값이 series 데이터로 입력받아 handling 가능


```python
df_info = df[["earn", "height", "age"]]
df_info.head()
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
      <th>earn</th>
      <th>height</th>
      <th>age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>79571.299011</td>
      <td>73.89</td>
      <td>49</td>
    </tr>
    <tr>
      <th>1</th>
      <td>96396.988643</td>
      <td>66.23</td>
      <td>62</td>
    </tr>
    <tr>
      <th>2</th>
      <td>48710.666947</td>
      <td>63.77</td>
      <td>33</td>
    </tr>
    <tr>
      <th>3</th>
      <td>80478.096153</td>
      <td>63.22</td>
      <td>95</td>
    </tr>
    <tr>
      <th>4</th>
      <td>82089.345498</td>
      <td>63.08</td>
      <td>43</td>
    </tr>
  </tbody>
</table>
</div>




```python
f = lambda x : x.max() - x.min()
df_info.apply(f)  #각 column 별로 결과값 반환
```




   earn      318047.708444
    height        19.870000
    age           73.000000
    dtype: float64



- 내장 연산 함수를 사용할 때도 똑같은 효과
- mean, std 등 사용 가능


```python
df_info.sum()
```




   earn      4.474344e+07
    height    9.183125e+04
    age       6.250800e+04
    dtype: float64




```python
df_info.apply(sum)
```




   earn      4.474344e+07
    height    9.183125e+04
    age       6.250800e+04
    dtype: float64



- scalar 값 이외에 series값의 반환도 가능


```python
def f(x):
    return Series([x.min(), x.max()], index=["min", "max"])
df_info.apply(f)
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
      <th>earn</th>
      <th>height</th>
      <th>age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>min</th>
      <td>-98.580489</td>
      <td>57.34</td>
      <td>22</td>
    </tr>
    <tr>
      <th>max</th>
      <td>317949.127955</td>
      <td>77.21</td>
      <td>95</td>
    </tr>
  </tbody>
</table>
</div>



### applymap for dataframe

- series 단위가 아닌 element단위로 함수 적용
- series 단위에 apply를 적용시킬 때와 같은 효과


```python
f = lambda x: -x
df_info.applymap(f).head(5)
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
      <th>earn</th>
      <th>height</th>
      <th>age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-79571.299011</td>
      <td>-73.89</td>
      <td>-49</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-96396.988643</td>
      <td>-66.23</td>
      <td>-62</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-48710.666947</td>
      <td>-63.77</td>
      <td>-33</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-80478.096153</td>
      <td>-63.22</td>
      <td>-95</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-82089.345498</td>
      <td>-63.08</td>
      <td>-43</td>
    </tr>
  </tbody>
</table>
</div>




```python
f = lambda x: -x
df_info["earn"].apply(f).head(5)
```




   0   -79571.299011
    1   -96396.988643
    2   -48710.666947
    3   -80478.096153
    4   -82089.345498
    Name: earn, dtype: float64



</br>

***
https://www.boostcourse.org/ai222/lecture/23822