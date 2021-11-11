# pandas :: Pandas Built-in functions


```python
import pandas as pd
from pandas import Series
from pandas import DataFrame

import numpy as np
```

### describe

- Numeric type 데이터의 요약 정보를 보여줌


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
df.describe()
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
      <th>ed</th>
      <th>age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>1379.000000</td>
      <td>1379.000000</td>
      <td>1379.000000</td>
      <td>1379.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>32446.292622</td>
      <td>66.592640</td>
      <td>13.354605</td>
      <td>45.328499</td>
    </tr>
    <tr>
      <th>std</th>
      <td>31257.070006</td>
      <td>3.818108</td>
      <td>2.438741</td>
      <td>15.789715</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-98.580489</td>
      <td>57.340000</td>
      <td>3.000000</td>
      <td>22.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>10538.790721</td>
      <td>63.720000</td>
      <td>12.000000</td>
      <td>33.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>26877.870178</td>
      <td>66.050000</td>
      <td>13.000000</td>
      <td>42.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>44506.215336</td>
      <td>69.315000</td>
      <td>15.000000</td>
      <td>55.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>317949.127955</td>
      <td>77.210000</td>
      <td>18.000000</td>
      <td>95.000000</td>
    </tr>
  </tbody>
</table>
</div>



### unique

- series data의 유일한 값을 list로 반환


```python
# 유일한 인종의 값 list
df.race.unique()
```




   array(['white', 'other', 'hispanic', 'black'], dtype=object)




```python
# dict type으로 index
np.array(dict(enumerate(df["race"].unique())))
```




   array({0: 'white', 1: 'other', 2: 'hispanic', 3: 'black'}, dtype=object)




```python
# label index 값과 label값 각각 추출
value = list(map(int, np.array(list(enumerate(df["race"].unique())))[:, 0].tolist()))
key = np.array(list(enumerate(df["race"].unique())), dtype=str)[:, 1].tolist()

value, key
```




   ([0, 1, 2, 3], ['white', 'other', 'hispanic', 'black'])




```python
# label str -> index 값으로 변환
df["race"].replace(to_replace=key, value=value, inplace=True) 
df["race"]
```




   0       0
    1       0
    2       0
    3       1
    4       0
           ..
    1374    0
    1375    0
    1376    0
    1377    0
    1378    0
    Name: race, Length: 1379, dtype: int64




```python
# 성별에 대해서도 동일하게 적용
value = list(map(int, np.array(list(enumerate(df["sex"].unique())))[:, 0].tolist()))
key = np.array(list(enumerate(df["sex"].unique())), dtype=str)[:, 1].tolist()

value, key
```




   ([0, 1], ['male', 'female'])




```python
df["sex"].replace(to_replace=key, value=value, inplace=True)
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>79571.299011</td>
      <td>73.89</td>
      <td>0</td>
      <td>0</td>
      <td>16</td>
      <td>49</td>
    </tr>
    <tr>
      <th>1</th>
      <td>96396.988643</td>
      <td>66.23</td>
      <td>1</td>
      <td>0</td>
      <td>16</td>
      <td>62</td>
    </tr>
    <tr>
      <th>2</th>
      <td>48710.666947</td>
      <td>63.77</td>
      <td>1</td>
      <td>0</td>
      <td>16</td>
      <td>33</td>
    </tr>
    <tr>
      <th>3</th>
      <td>80478.096153</td>
      <td>63.22</td>
      <td>1</td>
      <td>1</td>
      <td>16</td>
      <td>95</td>
    </tr>
    <tr>
      <th>4</th>
      <td>82089.345498</td>
      <td>63.08</td>
      <td>1</td>
      <td>0</td>
      <td>17</td>
      <td>43</td>
    </tr>
  </tbody>
</table>
</div>



### sum

- 기본적인 column 또는 row 값의 연산을 지원
- sub, mean, min, max, count, median, mad, var 등


```python
df.sum(axis=0)  #column별
```




   earn      4.474344e+07
    height    9.183125e+04
    sex       8.590000e+02
    race      5.610000e+02
    ed        1.841600e+04
    age       6.250800e+04
    dtype: float64




```python
df.sum(axis=1)  #row별
```




   0       79710.189011
    1       96542.218643
    2       48824.436947
    3       80654.316153
    4       82213.425498
                ...     
    1374    30290.060363
    1375    25019.829514
    1376    13824.311312
    1377    95563.664410
    1378     9686.681857
    Length: 1379, dtype: float64



### isnull

- column 또는 row 값의 NaN (null) 값의 index를 반환함


```python
df.isnull()
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
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1374</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1375</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1376</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1377</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1378</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
<p>1379 rows × 6 columns</p>
</div>




```python
df.isnull().sum()  #null인 값의 합
```




   earn      0
    height    0
    sex       0
    race      0
    ed        0
    age       0
    dtype: int64



### sort_values

- column값을 기준으로 데이터를 sorting


```python
df.sort_values(["age", "earn"], ascending=True).head(10)
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
      <th>1038</th>
      <td>-56.321979</td>
      <td>67.81</td>
      <td>0</td>
      <td>2</td>
      <td>10</td>
      <td>22</td>
    </tr>
    <tr>
      <th>800</th>
      <td>-27.876819</td>
      <td>72.29</td>
      <td>0</td>
      <td>0</td>
      <td>12</td>
      <td>22</td>
    </tr>
    <tr>
      <th>963</th>
      <td>-25.655260</td>
      <td>68.90</td>
      <td>0</td>
      <td>0</td>
      <td>12</td>
      <td>22</td>
    </tr>
    <tr>
      <th>1105</th>
      <td>988.565070</td>
      <td>64.71</td>
      <td>1</td>
      <td>0</td>
      <td>12</td>
      <td>22</td>
    </tr>
    <tr>
      <th>801</th>
      <td>1000.221504</td>
      <td>64.09</td>
      <td>1</td>
      <td>0</td>
      <td>12</td>
      <td>22</td>
    </tr>
    <tr>
      <th>862</th>
      <td>1002.023843</td>
      <td>66.59</td>
      <td>1</td>
      <td>0</td>
      <td>12</td>
      <td>22</td>
    </tr>
    <tr>
      <th>933</th>
      <td>1007.994941</td>
      <td>68.26</td>
      <td>1</td>
      <td>0</td>
      <td>12</td>
      <td>22</td>
    </tr>
    <tr>
      <th>988</th>
      <td>1578.542814</td>
      <td>64.53</td>
      <td>0</td>
      <td>0</td>
      <td>12</td>
      <td>22</td>
    </tr>
    <tr>
      <th>522</th>
      <td>1955.168187</td>
      <td>69.87</td>
      <td>1</td>
      <td>3</td>
      <td>12</td>
      <td>22</td>
    </tr>
    <tr>
      <th>765</th>
      <td>2581.870402</td>
      <td>64.79</td>
      <td>1</td>
      <td>0</td>
      <td>12</td>
      <td>22</td>
    </tr>
  </tbody>
</table>
</div>



### Correlation & Covatiance

- 상관계수와 공분산을 구하는 함수
- corr, cov, corrwith


```python
df.age.corr(df.earn)
```




   0.07400349177836055




```python
df.age.cov(df.earn)
```




   36523.6992104089




```python
df.corrwith(df.earn)
```




   earn      1.000000
    height    0.291600
    sex      -0.337328
    race     -0.063977
    ed        0.350374
    age       0.074003
    dtype: float64




```python
df.corr()
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
      <th>earn</th>
      <td>1.000000</td>
      <td>0.291600</td>
      <td>-0.337328</td>
      <td>-0.063977</td>
      <td>0.350374</td>
      <td>0.074003</td>
    </tr>
    <tr>
      <th>height</th>
      <td>0.291600</td>
      <td>1.000000</td>
      <td>-0.703672</td>
      <td>-0.045974</td>
      <td>0.114047</td>
      <td>-0.133727</td>
    </tr>
    <tr>
      <th>sex</th>
      <td>-0.337328</td>
      <td>-0.703672</td>
      <td>1.000000</td>
      <td>0.000858</td>
      <td>-0.061747</td>
      <td>0.070036</td>
    </tr>
    <tr>
      <th>race</th>
      <td>-0.063977</td>
      <td>-0.045974</td>
      <td>0.000858</td>
      <td>1.000000</td>
      <td>-0.049487</td>
      <td>-0.056879</td>
    </tr>
    <tr>
      <th>ed</th>
      <td>0.350374</td>
      <td>0.114047</td>
      <td>-0.061747</td>
      <td>-0.049487</td>
      <td>1.000000</td>
      <td>-0.129802</td>
    </tr>
    <tr>
      <th>age</th>
      <td>0.074003</td>
      <td>-0.133727</td>
      <td>0.070036</td>
      <td>-0.056879</td>
      <td>-0.129802</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>


</br>

***

https://www.boostcourse.org/ai222/lecture/23822/