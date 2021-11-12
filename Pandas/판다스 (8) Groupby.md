# pandas :: Groupby I


```python
import pandas as pd
```

### Groupby

- SQL groupby 명령어와 같음
- split  ->  apply  ->  combine 과정을 거쳐 연산함

![](/images/groupby.png)


```python
# data from: 
ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}

df = pd.DataFrame(ipl_data)
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
      <th>Team</th>
      <th>Rank</th>
      <th>Year</th>
      <th>Points</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Riders</td>
      <td>1</td>
      <td>2014</td>
      <td>876</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Riders</td>
      <td>2</td>
      <td>2015</td>
      <td>789</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Devils</td>
      <td>2</td>
      <td>2014</td>
      <td>863</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Devils</td>
      <td>3</td>
      <td>2015</td>
      <td>673</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Kings</td>
      <td>3</td>
      <td>2014</td>
      <td>741</td>
    </tr>
    <tr>
      <th>5</th>
      <td>kings</td>
      <td>4</td>
      <td>2015</td>
      <td>812</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Kings</td>
      <td>1</td>
      <td>2016</td>
      <td>756</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Kings</td>
      <td>1</td>
      <td>2017</td>
      <td>788</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Riders</td>
      <td>2</td>
      <td>2016</td>
      <td>694</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Royals</td>
      <td>4</td>
      <td>2014</td>
      <td>701</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Royals</td>
      <td>1</td>
      <td>2015</td>
      <td>804</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Riders</td>
      <td>2</td>
      <td>2017</td>
      <td>690</td>
    </tr>
  </tbody>
</table>
</div>



![](/images/groupby2.png)


```python
df.groupby("Team")["Points"].sum()  #Team을 기준으로 Points을 sum
```




   Team
    Devils    1536
    Kings     2285
    Riders    3049
    Royals    1505
    kings      812
    Name: Points, dtype: int64




```python
# 한개 이상의 column을 묶을 수 있음
df.groupby(["Team", "Year"])["Points"].sum()
```




   Team    Year
    Devils  2014    863
            2015    673
    Kings   2014    741
            2016    756
            2017    788
    Riders  2014    876
            2015    789
            2016    694
            2017    690
    Royals  2014    701
            2015    804
    kings   2015    812
    Name: Points, dtype: int64



### Hierarchical index

- Groupby 명령의 결과물도 결국은 dataframe
- 두 개의 column으로 groupby를 할 경우, index가 두 개 생성


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
      <th>Team</th>
      <th>Rank</th>
      <th>Year</th>
      <th>Points</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Riders</td>
      <td>1</td>
      <td>2014</td>
      <td>876</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Riders</td>
      <td>2</td>
      <td>2015</td>
      <td>789</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Devils</td>
      <td>2</td>
      <td>2014</td>
      <td>863</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Devils</td>
      <td>3</td>
      <td>2015</td>
      <td>673</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Kings</td>
      <td>3</td>
      <td>2014</td>
      <td>741</td>
    </tr>
    <tr>
      <th>5</th>
      <td>kings</td>
      <td>4</td>
      <td>2015</td>
      <td>812</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Kings</td>
      <td>1</td>
      <td>2016</td>
      <td>756</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Kings</td>
      <td>1</td>
      <td>2017</td>
      <td>788</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Riders</td>
      <td>2</td>
      <td>2016</td>
      <td>694</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Royals</td>
      <td>4</td>
      <td>2014</td>
      <td>701</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Royals</td>
      <td>1</td>
      <td>2015</td>
      <td>804</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Riders</td>
      <td>2</td>
      <td>2017</td>
      <td>690</td>
    </tr>
  </tbody>
</table>
</div>




```python
h_index = df.groupby(["Team", "Year"])["Points"].sum()
h_index
```




   Team    Year
    Devils  2014    863
            2015    673
    Kings   2014    741
            2016    756
            2017    788
    Riders  2014    876
            2015    789
            2016    694
            2017    690
    Royals  2014    701
            2015    804
    kings   2015    812
    Name: Points, dtype: int64




```python
h_index.index
```




   MultiIndex([('Devils', 2014),
                ('Devils', 2015),
                ( 'Kings', 2014),
                ( 'Kings', 2016),
                ( 'Kings', 2017),
                ('Riders', 2014),
                ('Riders', 2015),
                ('Riders', 2016),
                ('Riders', 2017),
                ('Royals', 2014),
                ('Royals', 2015),
                ( 'kings', 2015)],
               names=['Team', 'Year'])




```python
h_index["Devils":"Kings"]
```




   Team    Year
    Devils  2014    863
            2015    673
    Kings   2014    741
            2016    756
            2017    788
    Name: Points, dtype: int64



### Hierarchical index - unstack()

- Group으로 묶여진 데이터를 matrix 형태로 전환해줌


```python
h_index.unstack()
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
      <th>Year</th>
      <th>2014</th>
      <th>2015</th>
      <th>2016</th>
      <th>2017</th>
    </tr>
    <tr>
      <th>Team</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Devils</th>
      <td>863.0</td>
      <td>673.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Kings</th>
      <td>741.0</td>
      <td>NaN</td>
      <td>756.0</td>
      <td>788.0</td>
    </tr>
    <tr>
      <th>Riders</th>
      <td>876.0</td>
      <td>789.0</td>
      <td>694.0</td>
      <td>690.0</td>
    </tr>
    <tr>
      <th>Royals</th>
      <td>701.0</td>
      <td>804.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>kings</th>
      <td>NaN</td>
      <td>812.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



### Hierarchical index - swaplevel

- Index level을 변경할 수 있음


```python
h_index.swaplevel()
```




   Year  Team  
    2014  Devils    863
    2015  Devils    673
    2014  Kings     741
    2016  Kings     756
    2017  Kings     788
    2014  Riders    876
    2015  Riders    789
    2016  Riders    694
    2017  Riders    690
    2014  Royals    701
    2015  Royals    804
          kings     812
    Name: Points, dtype: int64




```python
h_index.swaplevel().sortlevel(0)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-15-467afa1669a6> in <module>
    ----> 1 h_index.swaplevel().sortlevel(0)
    

    ~\anaconda3\lib\site-packages\pandas\core\generic.py in __getattr__(self, name)
       5137             if self._info_axis._can_hold_identifiers_and_holds_name(name):
       5138                 return self[name]
    -> 5139             return object.__getattribute__(self, name)
       5140 
       5141     def __setattr__(self, name: str, value) -> None:
    

    AttributeError: 'Series' object has no attribute 'sortlevel'



```python
h_index.sum(level=0)
```




   Team
    Devils    1536
    Kings     2285
    Riders    3049
    Royals    1505
    kings      812
    Name: Points, dtype: int64




```python
h_index.sum(level=1)
```




   Year
    2014    3181
    2015    3078
    2016    1450
    2017    1478
    Name: Points, dtype: int64



# pandas :: Groupby II 

### Groupby - grouped

- Groupby에 의해 Split된 상태를 추출 가능함


```python
grouped = df.groupby("Team")

for name,group in grouped:
    print(name)
    print(group)
    
# Tuple 형태로 그룹의 key값 value값이 추출됨
```

   Devils
         Team  Rank  Year  Points
    2  Devils     2  2014     863
    3  Devils     3  2015     673
    Kings
        Team  Rank  Year  Points
    4  Kings     3  2014     741
    6  Kings     1  2016     756
    7  Kings     1  2017     788
    Riders
          Team  Rank  Year  Points
    0   Riders     1  2014     876
    1   Riders     2  2015     789
    8   Riders     2  2016     694
    11  Riders     2  2017     690
    Royals
          Team  Rank  Year  Points
    9   Royals     4  2014     701
    10  Royals     1  2015     804
    kings
        Team  Rank  Year  Points
    5  kings     4  2015     812
    


```python
# 특정 key값을 가진 그룹의 정보만 추출 가능
grouped.get_group("Devils")
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
      <th>Team</th>
      <th>Rank</th>
      <th>Year</th>
      <th>Points</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>Devils</td>
      <td>2</td>
      <td>2014</td>
      <td>863</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Devils</td>
      <td>3</td>
      <td>2015</td>
      <td>673</td>
    </tr>
  </tbody>
</table>
</div>



### Groupby - aggregation 

- 요약된 통계 정보를 추출해줌


```python
grouped.agg(sum)
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
      <th>Rank</th>
      <th>Year</th>
      <th>Points</th>
    </tr>
    <tr>
      <th>Team</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Devils</th>
      <td>5</td>
      <td>4029</td>
      <td>1536</td>
    </tr>
    <tr>
      <th>Kings</th>
      <td>5</td>
      <td>6047</td>
      <td>2285</td>
    </tr>
    <tr>
      <th>Riders</th>
      <td>7</td>
      <td>8062</td>
      <td>3049</td>
    </tr>
    <tr>
      <th>Royals</th>
      <td>5</td>
      <td>4029</td>
      <td>1505</td>
    </tr>
    <tr>
      <th>kings</th>
      <td>4</td>
      <td>2015</td>
      <td>812</td>
    </tr>
  </tbody>
</table>
</div>




```python
import numpy as np
grouped.agg(np.mean)
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
      <th>Rank</th>
      <th>Year</th>
      <th>Points</th>
    </tr>
    <tr>
      <th>Team</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Devils</th>
      <td>2.500000</td>
      <td>2014.500000</td>
      <td>768.000000</td>
    </tr>
    <tr>
      <th>Kings</th>
      <td>1.666667</td>
      <td>2015.666667</td>
      <td>761.666667</td>
    </tr>
    <tr>
      <th>Riders</th>
      <td>1.750000</td>
      <td>2015.500000</td>
      <td>762.250000</td>
    </tr>
    <tr>
      <th>Royals</th>
      <td>2.500000</td>
      <td>2014.500000</td>
      <td>752.500000</td>
    </tr>
    <tr>
      <th>kings</th>
      <td>4.000000</td>
      <td>2015.000000</td>
      <td>812.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 특정 컬럼에 여러개의 함수를 적용할 수도 있음
grouped['Points'].agg([np.sum, np.mean, np.std])
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
      <th>sum</th>
      <th>mean</th>
      <th>std</th>
    </tr>
    <tr>
      <th>Team</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Devils</th>
      <td>1536</td>
      <td>768.000000</td>
      <td>134.350288</td>
    </tr>
    <tr>
      <th>Kings</th>
      <td>2285</td>
      <td>761.666667</td>
      <td>24.006943</td>
    </tr>
    <tr>
      <th>Riders</th>
      <td>3049</td>
      <td>762.250000</td>
      <td>88.567771</td>
    </tr>
    <tr>
      <th>Royals</th>
      <td>1505</td>
      <td>752.500000</td>
      <td>72.831998</td>
    </tr>
    <tr>
      <th>kings</th>
      <td>812</td>
      <td>812.000000</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



### Groupby - transformation

- aggregation과 달리 key값 별로 요약된 정보가 아님
- 개별 데이터의 변환을 지원함


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
      <th>Team</th>
      <th>Rank</th>
      <th>Year</th>
      <th>Points</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Riders</td>
      <td>1</td>
      <td>2014</td>
      <td>876</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Riders</td>
      <td>2</td>
      <td>2015</td>
      <td>789</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Devils</td>
      <td>2</td>
      <td>2014</td>
      <td>863</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Devils</td>
      <td>3</td>
      <td>2015</td>
      <td>673</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Kings</td>
      <td>3</td>
      <td>2014</td>
      <td>741</td>
    </tr>
    <tr>
      <th>5</th>
      <td>kings</td>
      <td>4</td>
      <td>2015</td>
      <td>812</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Kings</td>
      <td>1</td>
      <td>2016</td>
      <td>756</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Kings</td>
      <td>1</td>
      <td>2017</td>
      <td>788</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Riders</td>
      <td>2</td>
      <td>2016</td>
      <td>694</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Royals</td>
      <td>4</td>
      <td>2014</td>
      <td>701</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Royals</td>
      <td>1</td>
      <td>2015</td>
      <td>804</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Riders</td>
      <td>2</td>
      <td>2017</td>
      <td>690</td>
    </tr>
  </tbody>
</table>
</div>




```python
score = lambda x : (x)
grouped.transform(score)
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
      <th>Rank</th>
      <th>Year</th>
      <th>Points</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2014</td>
      <td>876</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>2015</td>
      <td>789</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>2014</td>
      <td>863</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>2015</td>
      <td>673</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3</td>
      <td>2014</td>
      <td>741</td>
    </tr>
    <tr>
      <th>5</th>
      <td>4</td>
      <td>2015</td>
      <td>812</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1</td>
      <td>2016</td>
      <td>756</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1</td>
      <td>2017</td>
      <td>788</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2</td>
      <td>2016</td>
      <td>694</td>
    </tr>
    <tr>
      <th>9</th>
      <td>4</td>
      <td>2014</td>
      <td>701</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1</td>
      <td>2015</td>
      <td>804</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2</td>
      <td>2017</td>
      <td>690</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 단 max나 min처럼 Series 데이터에 적용되는 데이터들은 
# key값을 기준으로 grouped된 데이터 기준  (잘 안씀~)
score = lambda x: (x.max())
grouped.transform(score)
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
      <th>Rank</th>
      <th>Year</th>
      <th>Points</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>2017</td>
      <td>876</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>2017</td>
      <td>876</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>2015</td>
      <td>863</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>2015</td>
      <td>863</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3</td>
      <td>2017</td>
      <td>788</td>
    </tr>
    <tr>
      <th>5</th>
      <td>4</td>
      <td>2015</td>
      <td>812</td>
    </tr>
    <tr>
      <th>6</th>
      <td>3</td>
      <td>2017</td>
      <td>788</td>
    </tr>
    <tr>
      <th>7</th>
      <td>3</td>
      <td>2017</td>
      <td>788</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2</td>
      <td>2017</td>
      <td>876</td>
    </tr>
    <tr>
      <th>9</th>
      <td>4</td>
      <td>2015</td>
      <td>804</td>
    </tr>
    <tr>
      <th>10</th>
      <td>4</td>
      <td>2015</td>
      <td>804</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2</td>
      <td>2017</td>
      <td>876</td>
    </tr>
  </tbody>
</table>
</div>




$$
z_i=\frac{x_i-\mu}{\sigma}
$$



```python
score = lambda x: (x-x.mean()) / x.std() 
grouped.transform(score)
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
      <th>Rank</th>
      <th>Year</th>
      <th>Points</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-1.500000</td>
      <td>-1.161895</td>
      <td>1.284327</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.500000</td>
      <td>-0.387298</td>
      <td>0.302029</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.707107</td>
      <td>-0.707107</td>
      <td>0.707107</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.707107</td>
      <td>0.707107</td>
      <td>-0.707107</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.154701</td>
      <td>-1.091089</td>
      <td>-0.860862</td>
    </tr>
    <tr>
      <th>5</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>-0.577350</td>
      <td>0.218218</td>
      <td>-0.236043</td>
    </tr>
    <tr>
      <th>7</th>
      <td>-0.577350</td>
      <td>0.872872</td>
      <td>1.096905</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.500000</td>
      <td>0.387298</td>
      <td>-0.770596</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0.707107</td>
      <td>-0.707107</td>
      <td>-0.707107</td>
    </tr>
    <tr>
      <th>10</th>
      <td>-0.707107</td>
      <td>0.707107</td>
      <td>0.707107</td>
    </tr>
    <tr>
      <th>11</th>
      <td>0.500000</td>
      <td>1.161895</td>
      <td>-0.815759</td>
    </tr>
  </tbody>
</table>
</div>



### Groupby - filtration 

- 특정 정보를 제거하여 보여주는 필터링 기능
- filter 안에는 boolean 조건이 존재해야함
- len(x)는 grouped된 dataframe 개수


```python
df.groupby('Team').filter(lambda x: len(x) >= 3)
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
      <th>Team</th>
      <th>Rank</th>
      <th>Year</th>
      <th>Points</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Riders</td>
      <td>1</td>
      <td>2014</td>
      <td>876</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Riders</td>
      <td>2</td>
      <td>2015</td>
      <td>789</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Kings</td>
      <td>3</td>
      <td>2014</td>
      <td>741</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Kings</td>
      <td>1</td>
      <td>2016</td>
      <td>756</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Kings</td>
      <td>1</td>
      <td>2017</td>
      <td>788</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Riders</td>
      <td>2</td>
      <td>2016</td>
      <td>694</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Riders</td>
      <td>2</td>
      <td>2017</td>
      <td>690</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.groupby('Team').filter(lambda x: x["Rank"].sum() > 2)
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
      <th>Team</th>
      <th>Rank</th>
      <th>Year</th>
      <th>Points</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Riders</td>
      <td>1</td>
      <td>2014</td>
      <td>876</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Riders</td>
      <td>2</td>
      <td>2015</td>
      <td>789</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Devils</td>
      <td>2</td>
      <td>2014</td>
      <td>863</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Devils</td>
      <td>3</td>
      <td>2015</td>
      <td>673</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Kings</td>
      <td>3</td>
      <td>2014</td>
      <td>741</td>
    </tr>
    <tr>
      <th>5</th>
      <td>kings</td>
      <td>4</td>
      <td>2015</td>
      <td>812</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Kings</td>
      <td>1</td>
      <td>2016</td>
      <td>756</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Kings</td>
      <td>1</td>
      <td>2017</td>
      <td>788</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Riders</td>
      <td>2</td>
      <td>2016</td>
      <td>694</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Royals</td>
      <td>4</td>
      <td>2014</td>
      <td>701</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Royals</td>
      <td>1</td>
      <td>2015</td>
      <td>804</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Riders</td>
      <td>2</td>
      <td>2017</td>
      <td>690</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.groupby('Team').filter(lambda x: x["Points"].sum() > 1000)
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
      <th>Team</th>
      <th>Rank</th>
      <th>Year</th>
      <th>Points</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Riders</td>
      <td>1</td>
      <td>2014</td>
      <td>876</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Riders</td>
      <td>2</td>
      <td>2015</td>
      <td>789</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Devils</td>
      <td>2</td>
      <td>2014</td>
      <td>863</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Devils</td>
      <td>3</td>
      <td>2015</td>
      <td>673</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Kings</td>
      <td>3</td>
      <td>2014</td>
      <td>741</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Kings</td>
      <td>1</td>
      <td>2016</td>
      <td>756</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Kings</td>
      <td>1</td>
      <td>2017</td>
      <td>788</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Riders</td>
      <td>2</td>
      <td>2016</td>
      <td>694</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Royals</td>
      <td>4</td>
      <td>2014</td>
      <td>701</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Royals</td>
      <td>1</td>
      <td>2015</td>
      <td>804</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Riders</td>
      <td>2</td>
      <td>2017</td>
      <td>690</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.groupby('Team').filter(lambda x: x["Rank"].mean() > 1)
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
      <th>Team</th>
      <th>Rank</th>
      <th>Year</th>
      <th>Points</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Riders</td>
      <td>1</td>
      <td>2014</td>
      <td>876</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Riders</td>
      <td>2</td>
      <td>2015</td>
      <td>789</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Devils</td>
      <td>2</td>
      <td>2014</td>
      <td>863</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Devils</td>
      <td>3</td>
      <td>2015</td>
      <td>673</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Kings</td>
      <td>3</td>
      <td>2014</td>
      <td>741</td>
    </tr>
    <tr>
      <th>5</th>
      <td>kings</td>
      <td>4</td>
      <td>2015</td>
      <td>812</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Kings</td>
      <td>1</td>
      <td>2016</td>
      <td>756</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Kings</td>
      <td>1</td>
      <td>2017</td>
      <td>788</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Riders</td>
      <td>2</td>
      <td>2016</td>
      <td>694</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Royals</td>
      <td>4</td>
      <td>2014</td>
      <td>701</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Royals</td>
      <td>1</td>
      <td>2015</td>
      <td>804</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Riders</td>
      <td>2</td>
      <td>2017</td>
      <td>690</td>
    </tr>
  </tbody>
</table>
</div>


</br>

***

https://www.boostcourse.org/ai222/lecture/23823