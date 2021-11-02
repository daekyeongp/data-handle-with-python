# 데이터 정제 :: Data Problems

### Data quality problems 
>- 데이터의 최대/최소가 다름  ->  scale에 따른 y값에 영향 미침
>- Ordinary 또는 Nominal한 값들의 표현은 어떻게 하나?
>- 잘못 기입된 값들에 대한 처리
>- 값이 없을 경우에는?
>- 극단적으로 큰 값 또는 작은 값들을 그대로 나둬야 하는가?

### Data preprocessing issues
>- 데이터가 빠진 경우 (결측치의 처리)
>- 라벨링 된 데이터 (category) 데이터의 처리
>- 데이터의 scale의 차이가 매우 크게 날 경우

***

# 데이터 정제 :: Missing Values

### 데이터가 없을 때 할 수 있는 전략
>- 데이터가 없으면 sample을 drop
>- 데이터가 없는 **최소 개수**를 정해서 **sample을 drop**
>- 데이터가 거의 없는 feature는 **feature 자체를 drop**
>- 최빈값, 평균값으로 비어있는 데이터를 채우기



***Data drop***


```python
import pandas as pd
import numpy as np
```


```python
# Eaxmple from - https://chrisalbon.com/python/pandas_missing_data.html
raw_data = {'first_name': ['Jason', np.nan, 'Tina', 'Jake', 'Amy'],
        'last_name': ['Miller', np.nan, 'Ali', 'Milner', 'Cooze'],
        'age': [42, np.nan, 36, 24, 73],
        'sex': ['m', np.nan, 'f', 'm', 'f'],
        'preTestScore': [4, np.nan, np.nan, 2, 3],
        'postTestScore': [25, np.nan, np.nan, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'sex', 'preTestScore', 'postTestScore'])
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
      <th>sex</th>
      <th>preTestScore</th>
      <th>postTestScore</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jason</td>
      <td>Miller</td>
      <td>42.0</td>
      <td>m</td>
      <td>4.0</td>
      <td>25.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tina</td>
      <td>Ali</td>
      <td>36.0</td>
      <td>f</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jake</td>
      <td>Milner</td>
      <td>24.0</td>
      <td>m</td>
      <td>2.0</td>
      <td>62.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Amy</td>
      <td>Cooze</td>
      <td>73.0</td>
      <td>f</td>
      <td>3.0</td>
      <td>70.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.isnull().sum() / len(df)  #몇퍼센트가 비어있는가?
```




   first_name       0.2
    last_name        0.2
    age              0.2
    sex              0.2
    preTestScore     0.4
    postTestScore    0.4
    dtype: float64




```python
df_no_missing = df.dropna()
df_no_missing  #dropna -> 데이터들이 사라짐
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
      <th>sex</th>
      <th>preTestScore</th>
      <th>postTestScore</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jason</td>
      <td>Miller</td>
      <td>42.0</td>
      <td>m</td>
      <td>4.0</td>
      <td>25.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jake</td>
      <td>Milner</td>
      <td>24.0</td>
      <td>m</td>
      <td>2.0</td>
      <td>62.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Amy</td>
      <td>Cooze</td>
      <td>73.0</td>
      <td>f</td>
      <td>3.0</td>
      <td>70.0</td>
    </tr>
  </tbody>
</table>
</div>



***


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
      <th>sex</th>
      <th>preTestScore</th>
      <th>postTestScore</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jason</td>
      <td>Miller</td>
      <td>42.0</td>
      <td>m</td>
      <td>4.0</td>
      <td>25.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tina</td>
      <td>Ali</td>
      <td>36.0</td>
      <td>f</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jake</td>
      <td>Milner</td>
      <td>24.0</td>
      <td>m</td>
      <td>2.0</td>
      <td>62.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Amy</td>
      <td>Cooze</td>
      <td>73.0</td>
      <td>f</td>
      <td>3.0</td>
      <td>70.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_cleaned = df.dropna(how='all') 
df_cleaned  #모든 데이터가 비어 있으면 drop
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
      <th>sex</th>
      <th>preTestScore</th>
      <th>postTestScore</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jason</td>
      <td>Miller</td>
      <td>42.0</td>
      <td>m</td>
      <td>4.0</td>
      <td>25.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tina</td>
      <td>Ali</td>
      <td>36.0</td>
      <td>f</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jake</td>
      <td>Milner</td>
      <td>24.0</td>
      <td>m</td>
      <td>2.0</td>
      <td>62.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Amy</td>
      <td>Cooze</td>
      <td>73.0</td>
      <td>f</td>
      <td>3.0</td>
      <td>70.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['location'] = np.nan  #nan을 생성 column
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
      <th>sex</th>
      <th>preTestScore</th>
      <th>postTestScore</th>
      <th>location</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jason</td>
      <td>Miller</td>
      <td>42.0</td>
      <td>m</td>
      <td>4.0</td>
      <td>25.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tina</td>
      <td>Ali</td>
      <td>36.0</td>
      <td>f</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jake</td>
      <td>Milner</td>
      <td>24.0</td>
      <td>m</td>
      <td>2.0</td>
      <td>62.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Amy</td>
      <td>Cooze</td>
      <td>73.0</td>
      <td>f</td>
      <td>3.0</td>
      <td>70.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.dropna(axis=1, how='all') #column을 기준으로 삭제
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
      <th>sex</th>
      <th>preTestScore</th>
      <th>postTestScore</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jason</td>
      <td>Miller</td>
      <td>42.0</td>
      <td>m</td>
      <td>4.0</td>
      <td>25.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tina</td>
      <td>Ali</td>
      <td>36.0</td>
      <td>f</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jake</td>
      <td>Milner</td>
      <td>24.0</td>
      <td>m</td>
      <td>2.0</td>
      <td>62.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Amy</td>
      <td>Cooze</td>
      <td>73.0</td>
      <td>f</td>
      <td>3.0</td>
      <td>70.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.dropna(axis=1, thresh = 3)  #column기준, 데이터가 최소 4개 이상 없을 때 drop
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
      <th>sex</th>
      <th>preTestScore</th>
      <th>postTestScore</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jason</td>
      <td>Miller</td>
      <td>42.0</td>
      <td>m</td>
      <td>4.0</td>
      <td>25.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tina</td>
      <td>Ali</td>
      <td>36.0</td>
      <td>f</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jake</td>
      <td>Milner</td>
      <td>24.0</td>
      <td>m</td>
      <td>2.0</td>
      <td>62.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Amy</td>
      <td>Cooze</td>
      <td>73.0</td>
      <td>f</td>
      <td>3.0</td>
      <td>70.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.dropna(axis=0, thresh=1)  #row기준, 데이터가 최소 2개 이상 없을 때 drop
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
      <th>sex</th>
      <th>preTestScore</th>
      <th>postTestScore</th>
      <th>location</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jason</td>
      <td>Miller</td>
      <td>42.0</td>
      <td>m</td>
      <td>4.0</td>
      <td>25.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tina</td>
      <td>Ali</td>
      <td>36.0</td>
      <td>f</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jake</td>
      <td>Milner</td>
      <td>24.0</td>
      <td>m</td>
      <td>2.0</td>
      <td>62.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Amy</td>
      <td>Cooze</td>
      <td>73.0</td>
      <td>f</td>
      <td>3.0</td>
      <td>70.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.dropna(thresh=5)
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
      <th>sex</th>
      <th>preTestScore</th>
      <th>postTestScore</th>
      <th>location</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jason</td>
      <td>Miller</td>
      <td>42.0</td>
      <td>m</td>
      <td>4.0</td>
      <td>25.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jake</td>
      <td>Milner</td>
      <td>24.0</td>
      <td>m</td>
      <td>2.0</td>
      <td>62.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Amy</td>
      <td>Cooze</td>
      <td>73.0</td>
      <td>f</td>
      <td>3.0</td>
      <td>70.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



***
### 데이터 값 채우기
>- 평균값, 중위값, 최빈값을 활용 (https://goo.gl/i8iuL9)
![](/images/attachment:image.png)


```python
# 평균값 : 해당 column의 값의 평균을 내서 채우기
df["preTestScore"].mean()
```




   3.0




```python
# 중위값 : 값을 일렬로 나열했을 때 중간에 위치한 값
df["postTestScore"].median()
```




   62.0




```python
# 최빈값 : 가장 많이 나오는 값
df["postTestScore"].mode()
```




   0    25.0
    1    62.0
    2    70.0
    dtype: float64



***Data Fill***


```python
df.fillna(0)  #데이터가 없는 곳은 0으로 집어넣어라
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
      <th>sex</th>
      <th>preTestScore</th>
      <th>postTestScore</th>
      <th>location</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jason</td>
      <td>Miller</td>
      <td>42.0</td>
      <td>m</td>
      <td>4.0</td>
      <td>25.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tina</td>
      <td>Ali</td>
      <td>36.0</td>
      <td>f</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jake</td>
      <td>Milner</td>
      <td>24.0</td>
      <td>m</td>
      <td>2.0</td>
      <td>62.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Amy</td>
      <td>Cooze</td>
      <td>73.0</td>
      <td>f</td>
      <td>3.0</td>
      <td>70.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df["preTestScore"].fillna(df["preTestScore"].mean(), inplace=True)
df  #preTestScore의 평균값을 집어넣어라
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
      <th>sex</th>
      <th>preTestScore</th>
      <th>postTestScore</th>
      <th>location</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jason</td>
      <td>Miller</td>
      <td>42.0</td>
      <td>m</td>
      <td>4.0</td>
      <td>25.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tina</td>
      <td>Ali</td>
      <td>36.0</td>
      <td>f</td>
      <td>3.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jake</td>
      <td>Milner</td>
      <td>24.0</td>
      <td>m</td>
      <td>2.0</td>
      <td>62.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Amy</td>
      <td>Cooze</td>
      <td>73.0</td>
      <td>f</td>
      <td>3.0</td>
      <td>70.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.groupby("sex")["postTestScore"].transform("mean")
```




   0    43.5
    1     NaN
    2    70.0
    3    43.5
    4    70.0
    Name: postTestScore, dtype: float64




```python
df["postTestScore"].fillna(
    df.groupby("sex")["postTestScore"].transform("mean"), inplace=True)
df  #성별로 나눠서 평균 값을 집어넣어라
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
      <th>sex</th>
      <th>preTestScore</th>
      <th>postTestScore</th>
      <th>location</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jason</td>
      <td>Miller</td>
      <td>42.0</td>
      <td>m</td>
      <td>4.0</td>
      <td>25.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tina</td>
      <td>Ali</td>
      <td>36.0</td>
      <td>f</td>
      <td>3.0</td>
      <td>70.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jake</td>
      <td>Milner</td>
      <td>24.0</td>
      <td>m</td>
      <td>2.0</td>
      <td>62.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Amy</td>
      <td>Cooze</td>
      <td>73.0</td>
      <td>f</td>
      <td>3.0</td>
      <td>70.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




</br>

***
https://www.boostcourse.org/ai222/lecture/24076