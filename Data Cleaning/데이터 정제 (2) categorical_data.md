# 데이터 정제 :: Categorical Data

### 이산형 데이터를 어떻게 처리할까?
> #### One-Hot Encoding
![](/images/onehotencoding.png)


***Data Type***


```python
import pandas as pd
import numpy as np
```


```python
edges = pd.DataFrame({'source': [0, 1, 2],
                   'target': [2, 2, 3],
                       'weight': [3, 4, 5],
                       'color': ['red', 'blue', 'blue']})

edges
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
      <th>source</th>
      <th>target</th>
      <th>weight</th>
      <th>color</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>2</td>
      <td>3</td>
      <td>red</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2</td>
      <td>4</td>
      <td>blue</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>3</td>
      <td>5</td>
      <td>blue</td>
    </tr>
  </tbody>
</table>
</div>




```python
edges.dtypes
```




   source     int64
    target     int64
    weight     int64
    color     object
    dtype: object




```python
edges["color"]
```




   0     red
    1    blue
    2    blue
    Name: color, dtype: object



***One Hot Encoding***


```python
pd.get_dummies(edges)
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
      <th>source</th>
      <th>target</th>
      <th>weight</th>
      <th>color_blue</th>
      <th>color_red</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>2</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2</td>
      <td>4</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>3</td>
      <td>5</td>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.get_dummies(edges[["color"]])
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
      <th>color_blue</th>
      <th>color_red</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



***


```python
weight_dict = {3:"M", 4:"L", 5:"XL"}
edges["weight_sign"] = edges["weight"].map(weight_dict)
edges
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
      <th>source</th>
      <th>target</th>
      <th>weight</th>
      <th>color</th>
      <th>weight_sign</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>2</td>
      <td>3</td>
      <td>red</td>
      <td>M</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2</td>
      <td>4</td>
      <td>blue</td>
      <td>L</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>3</td>
      <td>5</td>
      <td>blue</td>
      <td>XL</td>
    </tr>
  </tbody>
</table>
</div>




```python
weight_sign = pd.get_dummies(edges["weight_sign"])
weight_sign
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
      <th>L</th>
      <th>M</th>
      <th>XL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.concat([edges, weight_sign], axis=1)
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
      <th>source</th>
      <th>target</th>
      <th>weight</th>
      <th>color</th>
      <th>weight_sign</th>
      <th>L</th>
      <th>M</th>
      <th>XL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>2</td>
      <td>3</td>
      <td>red</td>
      <td>M</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2</td>
      <td>4</td>
      <td>blue</td>
      <td>L</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>3</td>
      <td>5</td>
      <td>blue</td>
      <td>XL</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.get_dummies(edges).values
```




   array([[0, 2, 3, 0, 1, 0, 1, 0],
           [1, 2, 4, 1, 0, 1, 0, 0],
           [2, 3, 5, 1, 0, 0, 0, 1]], dtype=int64)



### Data Binning :: 데이터의 구간을 나눠보자
> ![](/images/databinning.png)


```python

# Example from - https://chrisalbon.com/python/pandas_binning_data.html

raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
        'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
        'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'],
        'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['regiment', 'company', 'name', 'preTestScore', 'postTestScore'])
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
      <th>regiment</th>
      <th>company</th>
      <th>name</th>
      <th>preTestScore</th>
      <th>postTestScore</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Nighthawks</td>
      <td>1st</td>
      <td>Miller</td>
      <td>4</td>
      <td>25</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Nighthawks</td>
      <td>1st</td>
      <td>Jacobson</td>
      <td>24</td>
      <td>94</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Nighthawks</td>
      <td>2nd</td>
      <td>Ali</td>
      <td>31</td>
      <td>57</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Nighthawks</td>
      <td>2nd</td>
      <td>Milner</td>
      <td>2</td>
      <td>62</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Dragoons</td>
      <td>1st</td>
      <td>Cooze</td>
      <td>3</td>
      <td>70</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Dragoons</td>
      <td>1st</td>
      <td>Jacon</td>
      <td>4</td>
      <td>25</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Dragoons</td>
      <td>2nd</td>
      <td>Ryaner</td>
      <td>24</td>
      <td>94</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Dragoons</td>
      <td>2nd</td>
      <td>Sone</td>
      <td>31</td>
      <td>57</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Scouts</td>
      <td>1st</td>
      <td>Sloan</td>
      <td>2</td>
      <td>62</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Scouts</td>
      <td>1st</td>
      <td>Piger</td>
      <td>3</td>
      <td>70</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Scouts</td>
      <td>2nd</td>
      <td>Riani</td>
      <td>2</td>
      <td>62</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Scouts</td>
      <td>2nd</td>
      <td>Ali</td>
      <td>3</td>
      <td>70</td>
    </tr>
  </tbody>
</table>
</div>




```python
bins = [0, 25, 50, 75, 100] # Define bins as 0 to 25, 25 to 50, 60 to 75, 75 to 100
group_names = ['Low', 'Okay', 'Good', 'Great']  #구간명
categories = pd.cut(df['postTestScore'], bins, labels=group_names)  #cut후 categories에 할당
categories
```




   0       Low
    1     Great
    2      Good
    3      Good
    4      Good
    5       Low
    6     Great
    7      Good
    8      Good
    9      Good
    10     Good
    11     Good
    Name: postTestScore, dtype: category
    Categories (4, object): ['Low' < 'Okay' < 'Good' < 'Great']




```python
df['categories'] = pd.cut(df['postTestScore'], bins, labels=group_names)
pd.value_counts(df['categories'])  #기존 dataframe에 할당
```




   Good     8
    Great    2
    Low      2
    Okay     0
    Name: categories, dtype: int64




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
      <th>regiment</th>
      <th>company</th>
      <th>name</th>
      <th>preTestScore</th>
      <th>postTestScore</th>
      <th>categories</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Nighthawks</td>
      <td>1st</td>
      <td>Miller</td>
      <td>4</td>
      <td>25</td>
      <td>Low</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Nighthawks</td>
      <td>1st</td>
      <td>Jacobson</td>
      <td>24</td>
      <td>94</td>
      <td>Great</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Nighthawks</td>
      <td>2nd</td>
      <td>Ali</td>
      <td>31</td>
      <td>57</td>
      <td>Good</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Nighthawks</td>
      <td>2nd</td>
      <td>Milner</td>
      <td>2</td>
      <td>62</td>
      <td>Good</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Dragoons</td>
      <td>1st</td>
      <td>Cooze</td>
      <td>3</td>
      <td>70</td>
      <td>Good</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Dragoons</td>
      <td>1st</td>
      <td>Jacon</td>
      <td>4</td>
      <td>25</td>
      <td>Low</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Dragoons</td>
      <td>2nd</td>
      <td>Ryaner</td>
      <td>24</td>
      <td>94</td>
      <td>Great</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Dragoons</td>
      <td>2nd</td>
      <td>Sone</td>
      <td>31</td>
      <td>57</td>
      <td>Good</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Scouts</td>
      <td>1st</td>
      <td>Sloan</td>
      <td>2</td>
      <td>62</td>
      <td>Good</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Scouts</td>
      <td>1st</td>
      <td>Piger</td>
      <td>3</td>
      <td>70</td>
      <td>Good</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Scouts</td>
      <td>2nd</td>
      <td>Riani</td>
      <td>2</td>
      <td>62</td>
      <td>Good</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Scouts</td>
      <td>2nd</td>
      <td>Ali</td>
      <td>3</td>
      <td>70</td>
      <td>Good</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.get_dummies(df)
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
      <th>preTestScore</th>
      <th>postTestScore</th>
      <th>regiment_Dragoons</th>
      <th>regiment_Nighthawks</th>
      <th>regiment_Scouts</th>
      <th>company_1st</th>
      <th>company_2nd</th>
      <th>name_Ali</th>
      <th>name_Cooze</th>
      <th>name_Jacobson</th>
      <th>...</th>
      <th>name_Milner</th>
      <th>name_Piger</th>
      <th>name_Riani</th>
      <th>name_Ryaner</th>
      <th>name_Sloan</th>
      <th>name_Sone</th>
      <th>categories_Low</th>
      <th>categories_Okay</th>
      <th>categories_Good</th>
      <th>categories_Great</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>25</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>24</td>
      <td>94</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>31</td>
      <td>57</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>62</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3</td>
      <td>70</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>4</td>
      <td>25</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>24</td>
      <td>94</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>7</th>
      <td>31</td>
      <td>57</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2</td>
      <td>62</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>3</td>
      <td>70</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2</td>
      <td>62</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>3</td>
      <td>70</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>12 rows × 22 columns</p>
</div>



### using scikit-learn preprocessing

***Label encoding by sklearn***
- scikit-learn의 preprocessing 패키지도 label, one-hot 지원


```python
raw_example = df.values
raw_example[:3]
```




   array([['Nighthawks', '1st', 'Miller', 4, 25, 'Low'],
           ['Nighthawks', '1st', 'Jacobson', 24, 94, 'Great'],
           ['Nighthawks', '2nd', 'Ali', 31, 57, 'Good']], dtype=object)




```python
data = raw_example.copy()
```


```python
from sklearn import preprocessing
le = preprocessing.LabelEncoder()  #Encoder 생성
```


```python
raw_example[:,0]  
```




   array(['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons',
           'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts',
           'Scouts'], dtype=object)




```python
le.fit(raw_example[:,0])  #data에 맞게 encoding fitting
```




   LabelEncoder()




```python
le.transform(raw_example[:,0])  #실제 데이터 -> labelling data
```




   array([1, 1, 1, 1, 0, 0, 0, 0, 2, 2, 2, 2])




```python
data[:,0] = le.transform(raw_example[:,0])
data[:3]
```




   array([[1, '1st', 'Miller', 4, 25, 'Low'],
           [1, '1st', 'Jacobson', 24, 94, 'Great'],
           [1, '2nd', 'Ali', 31, 57, 'Good']], dtype=object)



##### ※ Label encoder의 fit과 transform의 과정이 나눠진 이유
>- 새로운 데이터 입력시, 기존 labelling 규칙을 그대로 적용할 필요가 있음
>- fit은 규칙을 생성하는 과정
>- transform은 규칙을 적용하는 과정
>- fit을 통해 규칙이 생성된 라벨인코더는 따로 저장하여 새로운 데이터를 입력할 경우 사용할 수 있음
>- 인코더들을 실제 시스템에 사용할 경우 pickle화 필요


```python
label_column = [0,1,2,5]
label_enconder_list = []
for column_index in  label_column:
    le = preprocessing.LabelEncoder()
    le.fit(raw_example[:,column_index])
    data[:,column_index] = le.transform(raw_example[:,column_index])
    label_enconder_list.append(le)  #기존 라벨인코더를 따로 저장
    del le 
data[:3]
```



   array([[1, 0, 4, 4, 25, 2],
           [1, 0, 2, 24, 94, 1],
           [1, 1, 0, 31, 57, 0]], dtype=object)




```python
#저장된 le로 새로운 데이터에 적용
label_enconder_list[0].transform(raw_example[:10,0])
```




   array([1, 1, 1, 1, 0, 0, 0, 0, 2, 2])



### One-hot encoding by sklearn
>- numeric labelling이 완료된 데이터에 one-hot 적용
>- data는 1차원으로 변환하여 넣어줄 것을 권장


```python
one_hot_enc = preprocessing.OneHotEncoder()
data[:,0].reshape(-1,1) 
```




   array([[1],
           [1],
           [1],
           [1],
           [0],
           [0],
           [0],
           [0],
           [2],
           [2],
           [2],
           [2]], dtype=object)




```python
#1-dim 변환하여 fit
one_hot_enc.fit(data[:,0].reshape(-1,1))
```




   OneHotEncoder()




```python
onehotlabels = one_hot_enc.transform(data[:,0].reshape(-1,1)).toarray()
onehotlabels
```




   array([[0., 1., 0.],
           [0., 1., 0.],
           [0., 1., 0.],
           [0., 1., 0.],
           [1., 0., 0.],
           [1., 0., 0.],
           [1., 0., 0.],
           [1., 0., 0.],
           [0., 0., 1.],
           [0., 0., 1.],
           [0., 0., 1.],
           [0., 0., 1.]])



</br>

***
https://www.boostcourse.org/ai222/lecture/24076