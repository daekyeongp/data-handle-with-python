# pandas :: dataframe

![](/images/dataframe.png)
![](/images/dataframe2.png)

https://www.slideshare.net/wesm/pandas-powerful-data-analysis-tools-for-python

### DataFrame

- Series를 모아서 만든 Data Table = 기본 2차원


```python
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
```


```python
# Example from - https://chrisalbon.com/python/pandas_map_values_to_values.html
raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
        'age': [42, 52, 36, 24, 73],
        'city': ['San Francisco', 'Baltimore', 'Miami', 'Douglas', 'Boston']}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'city'])
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
      <th>first_name</th>
      <th>last_name</th>
      <th>age</th>
      <th>city</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jason</td>
      <td>Miller</td>
      <td>42</td>
      <td>San Francisco</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Molly</td>
      <td>Jacobson</td>
      <td>52</td>
      <td>Baltimore</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tina</td>
      <td>Ali</td>
      <td>36</td>
      <td>Miami</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jake</td>
      <td>Milner</td>
      <td>24</td>
      <td>Douglas</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Amy</td>
      <td>Cooze</td>
      <td>73</td>
      <td>Boston</td>
    </tr>
  </tbody>
</table>
</div>




```python
# column 선택
DataFrame(raw_data, columns = ["age", "city"])
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
      <th>age</th>
      <th>city</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>42</td>
      <td>San Francisco</td>
    </tr>
    <tr>
      <th>1</th>
      <td>52</td>
      <td>Baltimore</td>
    </tr>
    <tr>
      <th>2</th>
      <td>36</td>
      <td>Miami</td>
    </tr>
    <tr>
      <th>3</th>
      <td>24</td>
      <td>Douglas</td>
    </tr>
    <tr>
      <th>4</th>
      <td>73</td>
      <td>Boston</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 새로운 column (debt) 추가
DataFrame(raw_data, 
          columns = ["first_name","last_name","age", "city", "debt"]
         )
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
      <th>first_name</th>
      <th>last_name</th>
      <th>age</th>
      <th>city</th>
      <th>debt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jason</td>
      <td>Miller</td>
      <td>42</td>
      <td>San Francisco</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Molly</td>
      <td>Jacobson</td>
      <td>52</td>
      <td>Baltimore</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tina</td>
      <td>Ali</td>
      <td>36</td>
      <td>Miami</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jake</td>
      <td>Milner</td>
      <td>24</td>
      <td>Douglas</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Amy</td>
      <td>Cooze</td>
      <td>73</td>
      <td>Boston</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
# column 선택 - series 추출 : 방법 1
df = DataFrame(raw_data, columns = ["first_name","last_name","age", "city", "debt"])
df.first_name
```




   0    Jason
    1    Molly
    2     Tina
    3     Jake
    4      Amy
    Name: first_name, dtype: object




```python
# column 선택 - series 추출 : 방법 2
df["first_name"]
```




   0    Jason
    1    Molly
    2     Tina
    3     Jake
    4      Amy
    Name: first_name, dtype: object




```python
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
      <th>first_name</th>
      <th>last_name</th>
      <th>age</th>
      <th>city</th>
      <th>debt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jason</td>
      <td>Miller</td>
      <td>42</td>
      <td>San Francisco</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Molly</td>
      <td>Jacobson</td>
      <td>52</td>
      <td>Baltimore</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tina</td>
      <td>Ali</td>
      <td>36</td>
      <td>Miami</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jake</td>
      <td>Milner</td>
      <td>24</td>
      <td>Douglas</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Amy</td>
      <td>Cooze</td>
      <td>73</td>
      <td>Boston</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
# loc : index location
df.loc[1]
```




   first_name        Molly
    last_name      Jacobson
    age                  52
    city          Baltimore
    debt                NaN
    Name: 1, dtype: object




```python
# iloc : index position
df["age"].iloc[1:]
```




   1    52
    2    36
    3    24
    4    73
    Name: age, dtype: int64




```python
# loc은 index 이름, iloc은 index number
```


```python
# Example from - https://stackoverflow.com/questions/31593201/pandas-iloc-vs-ix-vs-loc-explanation
s = pd.Series(np.nan, index=[49,48,47,46,45, 1, 2, 3, 4, 5])
s.loc[:3]  # 3이라는 index까지
```




   49   NaN
    48   NaN
    47   NaN
    46   NaN
    45   NaN
    1    NaN
    2    NaN
    3    NaN
    dtype: float64




```python
s.iloc[:3]  # 처음부터 3개
```




   49   NaN
    48   NaN
    47   NaN
    dtype: float64




```python
df.age > 40
```




   0     True
    1     True
    2    False
    3    False
    4     True
    Name: age, dtype: bool




```python
# column에 새로운 데이터 할당
df.debt = df.age > 40
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
      <th>first_name</th>
      <th>last_name</th>
      <th>age</th>
      <th>city</th>
      <th>debt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jason</td>
      <td>Miller</td>
      <td>42</td>
      <td>San Francisco</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Molly</td>
      <td>Jacobson</td>
      <td>52</td>
      <td>Baltimore</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tina</td>
      <td>Ali</td>
      <td>36</td>
      <td>Miami</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jake</td>
      <td>Milner</td>
      <td>24</td>
      <td>Douglas</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Amy</td>
      <td>Cooze</td>
      <td>73</td>
      <td>Boston</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




```python
# transpose
df.T
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>first_name</th>
      <td>Jason</td>
      <td>Molly</td>
      <td>Tina</td>
      <td>Jake</td>
      <td>Amy</td>
    </tr>
    <tr>
      <th>last_name</th>
      <td>Miller</td>
      <td>Jacobson</td>
      <td>Ali</td>
      <td>Milner</td>
      <td>Cooze</td>
    </tr>
    <tr>
      <th>age</th>
      <td>42</td>
      <td>52</td>
      <td>36</td>
      <td>24</td>
      <td>73</td>
    </tr>
    <tr>
      <th>city</th>
      <td>San Francisco</td>
      <td>Baltimore</td>
      <td>Miami</td>
      <td>Douglas</td>
      <td>Boston</td>
    </tr>
    <tr>
      <th>debt</th>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 값 출력
df.values
```




   array([['Jason', 'Miller', 42, 'San Francisco', True],
           ['Molly', 'Jacobson', 52, 'Baltimore', True],
           ['Tina', 'Ali', 36, 'Miami', False],
           ['Jake', 'Milner', 24, 'Douglas', False],
           ['Amy', 'Cooze', 73, 'Boston', True]], dtype=object)




```python
# csv 변환
df.to_csv()
```




   ',first_name,last_name,age,city,debt\r\n0,Jason,Miller,42,San Francisco,True\r\n1,Molly,Jacobson,52,Baltimore,True\r\n2,Tina,Ali,36,Miami,False\r\n3,Jake,Milner,24,Douglas,False\r\n4,Amy,Cooze,73,Boston,True\r\n'




```python
# column을 삭제함
del df["debt"]
```


```python
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
      <th>first_name</th>
      <th>last_name</th>
      <th>age</th>
      <th>city</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jason</td>
      <td>Miller</td>
      <td>42</td>
      <td>San Francisco</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Molly</td>
      <td>Jacobson</td>
      <td>52</td>
      <td>Baltimore</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tina</td>
      <td>Ali</td>
      <td>36</td>
      <td>Miami</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jake</td>
      <td>Milner</td>
      <td>24</td>
      <td>Douglas</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Amy</td>
      <td>Cooze</td>
      <td>73</td>
      <td>Boston</td>
    </tr>
  </tbody>
</table>
</div>




```python
# column 추가
values = Series(data=["M","F","F"],index=[0,1,3])
values
```




   0    M
    1    F
    3    F
    dtype: object




```python
df["sex"] = values
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
      <th>first_name</th>
      <th>last_name</th>
      <th>age</th>
      <th>city</th>
      <th>sex</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jason</td>
      <td>Miller</td>
      <td>42</td>
      <td>San Francisco</td>
      <td>M</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Molly</td>
      <td>Jacobson</td>
      <td>52</td>
      <td>Baltimore</td>
      <td>F</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tina</td>
      <td>Ali</td>
      <td>36</td>
      <td>Miami</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jake</td>
      <td>Milner</td>
      <td>24</td>
      <td>Douglas</td>
      <td>F</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Amy</td>
      <td>Cooze</td>
      <td>73</td>
      <td>Boston</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Example from Python for data analyis


pop = {'Nevada': {2001: 2.4, 2002: 2.9},
 'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}

DataFrame(pop)
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
      <th>Nevada</th>
      <th>Ohio</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2001</th>
      <td>2.4</td>
      <td>1.7</td>
    </tr>
    <tr>
      <th>2002</th>
      <td>2.9</td>
      <td>3.6</td>
    </tr>
    <tr>
      <th>2000</th>
      <td>NaN</td>
      <td>1.5</td>
    </tr>
  </tbody>
</table>
</div>

</br>

***
https://www.boostcourse.org/ai222/lecture/23822