# pandas :: selecton & drop


```python
import pandas as pd
```

### Data loading

- xlrd 모듈이 없을 경우, conda install xlrd


```python
!conda install --y xlrd
```

   Collecting package metadata (current_repodata.json): ...working... done
    Solving environment: ...working... done
    
   \# All requested packages already installed.
    
    


```python
import numpy as np
df = pd.read_excel('excel-comp-data.xlsx')
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
      <th>account</th>
      <th>name</th>
      <th>street</th>
      <th>city</th>
      <th>state</th>
      <th>postal-code</th>
      <th>Jan</th>
      <th>Feb</th>
      <th>Mar</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>211829</td>
      <td>Kerluke, Koepp and Hilpert</td>
      <td>34456 Sean Highway</td>
      <td>New Jaycob</td>
      <td>Texas</td>
      <td>28752</td>
      <td>10000</td>
      <td>62000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>320563</td>
      <td>Walter-Trantow</td>
      <td>1311 Alvis Tunnel</td>
      <td>Port Khadijah</td>
      <td>NorthCarolina</td>
      <td>38365</td>
      <td>95000</td>
      <td>45000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>648336</td>
      <td>Bashirian, Kunde and Price</td>
      <td>62184 Schamberger Underpass Apt. 231</td>
      <td>New Lilianland</td>
      <td>Iowa</td>
      <td>76517</td>
      <td>91000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>109996</td>
      <td>D'Amore, Gleichner and Bode</td>
      <td>155 Fadel Crescent Apt. 144</td>
      <td>Hyattburgh</td>
      <td>Maine</td>
      <td>46021</td>
      <td>45000</td>
      <td>120000</td>
      <td>10000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>121213</td>
      <td>Bauch-Goldner</td>
      <td>7274 Marissa Common</td>
      <td>Shanahanchester</td>
      <td>California</td>
      <td>49681</td>
      <td>162000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
  </tbody>
</table>
</div>



### data selection with column names and index number


```python
# 한 개의 column 선택시
df["account"].head(2)
```




   0    211829
    1    320563
    Name: account, dtype: int64




```python
# 한개 이상의 column 선택
df[["account", "street", "state"]].head(3)
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
      <th>account</th>
      <th>street</th>
      <th>state</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>211829</td>
      <td>34456 Sean Highway</td>
      <td>Texas</td>
    </tr>
    <tr>
      <th>1</th>
      <td>320563</td>
      <td>1311 Alvis Tunnel</td>
      <td>NorthCarolina</td>
    </tr>
    <tr>
      <th>2</th>
      <td>648336</td>
      <td>62184 Schamberger Underpass Apt. 231</td>
      <td>Iowa</td>
    </tr>
  </tbody>
</table>
</div>




```python
# column 이름 없이 사용하는 index number는 row 기준 표시
df[:10]
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
      <th>account</th>
      <th>name</th>
      <th>street</th>
      <th>city</th>
      <th>state</th>
      <th>postal-code</th>
      <th>Jan</th>
      <th>Feb</th>
      <th>Mar</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>211829</td>
      <td>Kerluke, Koepp and Hilpert</td>
      <td>34456 Sean Highway</td>
      <td>New Jaycob</td>
      <td>Texas</td>
      <td>28752</td>
      <td>10000</td>
      <td>62000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>320563</td>
      <td>Walter-Trantow</td>
      <td>1311 Alvis Tunnel</td>
      <td>Port Khadijah</td>
      <td>NorthCarolina</td>
      <td>38365</td>
      <td>95000</td>
      <td>45000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>648336</td>
      <td>Bashirian, Kunde and Price</td>
      <td>62184 Schamberger Underpass Apt. 231</td>
      <td>New Lilianland</td>
      <td>Iowa</td>
      <td>76517</td>
      <td>91000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>109996</td>
      <td>D'Amore, Gleichner and Bode</td>
      <td>155 Fadel Crescent Apt. 144</td>
      <td>Hyattburgh</td>
      <td>Maine</td>
      <td>46021</td>
      <td>45000</td>
      <td>120000</td>
      <td>10000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>121213</td>
      <td>Bauch-Goldner</td>
      <td>7274 Marissa Common</td>
      <td>Shanahanchester</td>
      <td>California</td>
      <td>49681</td>
      <td>162000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>132971</td>
      <td>Williamson, Schumm and Hettinger</td>
      <td>89403 Casimer Spring</td>
      <td>Jeremieburgh</td>
      <td>Arkansas</td>
      <td>62785</td>
      <td>150000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>145068</td>
      <td>Casper LLC</td>
      <td>340 Consuela Bridge Apt. 400</td>
      <td>Lake Gabriellaton</td>
      <td>Mississipi</td>
      <td>18008</td>
      <td>62000</td>
      <td>120000</td>
      <td>70000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>205217</td>
      <td>Kovacek-Johnston</td>
      <td>91971 Cronin Vista Suite 601</td>
      <td>Deronville</td>
      <td>RhodeIsland</td>
      <td>53461</td>
      <td>145000</td>
      <td>95000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>209744</td>
      <td>Champlin-Morar</td>
      <td>26739 Grant Lock</td>
      <td>Lake Juliannton</td>
      <td>Pennsylvania</td>
      <td>64415</td>
      <td>70000</td>
      <td>95000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>9</th>
      <td>212303</td>
      <td>Gerhold-Maggio</td>
      <td>366 Maggio Grove Apt. 998</td>
      <td>North Ras</td>
      <td>Idaho</td>
      <td>46308</td>
      <td>70000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# column 이름과 함께 row index 사용시, 해당 column만
df["name"][:3]
```




   0    Kerluke, Koepp and Hilpert
    1                Walter-Trantow
    2    Bashirian, Kunde and Price
    Name: name, dtype: object



### Series selection


```python
account_series = df["account"]
account_series[:3]
```




   0    211829
    1    320563
    2    648336
    Name: account, dtype: int64




```python
account_series[[1, 5, 2]]  # 1개 이상의 index
```




   1    320563
    5    132971
    2    648336
    Name: account, dtype: int64




```python
account_series[account_series<250000]  # boolean index
```




   0     211829
    3     109996
    4     121213
    5     132971
    6     145068
    7     205217
    8     209744
    9     212303
    10    214098
    11    231907
    12    242368
    Name: account, dtype: int64



### Index 변경


```python
df.index = df["account"]
```


```python
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
      <th>account</th>
      <th>name</th>
      <th>street</th>
      <th>city</th>
      <th>state</th>
      <th>postal-code</th>
      <th>Jan</th>
      <th>Feb</th>
      <th>Mar</th>
    </tr>
    <tr>
      <th>account</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>211829</th>
      <td>211829</td>
      <td>Kerluke, Koepp and Hilpert</td>
      <td>34456 Sean Highway</td>
      <td>New Jaycob</td>
      <td>Texas</td>
      <td>28752</td>
      <td>10000</td>
      <td>62000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>320563</th>
      <td>320563</td>
      <td>Walter-Trantow</td>
      <td>1311 Alvis Tunnel</td>
      <td>Port Khadijah</td>
      <td>NorthCarolina</td>
      <td>38365</td>
      <td>95000</td>
      <td>45000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>648336</th>
      <td>648336</td>
      <td>Bashirian, Kunde and Price</td>
      <td>62184 Schamberger Underpass Apt. 231</td>
      <td>New Lilianland</td>
      <td>Iowa</td>
      <td>76517</td>
      <td>91000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>109996</th>
      <td>109996</td>
      <td>D'Amore, Gleichner and Bode</td>
      <td>155 Fadel Crescent Apt. 144</td>
      <td>Hyattburgh</td>
      <td>Maine</td>
      <td>46021</td>
      <td>45000</td>
      <td>120000</td>
      <td>10000</td>
    </tr>
    <tr>
      <th>121213</th>
      <td>121213</td>
      <td>Bauch-Goldner</td>
      <td>7274 Marissa Common</td>
      <td>Shanahanchester</td>
      <td>California</td>
      <td>49681</td>
      <td>162000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
  </tbody>
</table>
</div>




```python
del df["account"]
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
      <th>name</th>
      <th>street</th>
      <th>city</th>
      <th>state</th>
      <th>postal-code</th>
      <th>Jan</th>
      <th>Feb</th>
      <th>Mar</th>
    </tr>
    <tr>
      <th>account</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>211829</th>
      <td>Kerluke, Koepp and Hilpert</td>
      <td>34456 Sean Highway</td>
      <td>New Jaycob</td>
      <td>Texas</td>
      <td>28752</td>
      <td>10000</td>
      <td>62000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>320563</th>
      <td>Walter-Trantow</td>
      <td>1311 Alvis Tunnel</td>
      <td>Port Khadijah</td>
      <td>NorthCarolina</td>
      <td>38365</td>
      <td>95000</td>
      <td>45000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>648336</th>
      <td>Bashirian, Kunde and Price</td>
      <td>62184 Schamberger Underpass Apt. 231</td>
      <td>New Lilianland</td>
      <td>Iowa</td>
      <td>76517</td>
      <td>91000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>109996</th>
      <td>D'Amore, Gleichner and Bode</td>
      <td>155 Fadel Crescent Apt. 144</td>
      <td>Hyattburgh</td>
      <td>Maine</td>
      <td>46021</td>
      <td>45000</td>
      <td>120000</td>
      <td>10000</td>
    </tr>
    <tr>
      <th>121213</th>
      <td>Bauch-Goldner</td>
      <td>7274 Marissa Common</td>
      <td>Shanahanchester</td>
      <td>California</td>
      <td>49681</td>
      <td>162000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
  </tbody>
</table>
</div>



### Basic, loc, iloc selection


```python
# column과 index number (주로 col 많을 때 사용)
df[["name", "street"]][:2]
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
      <th>street</th>
    </tr>
    <tr>
      <th>account</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>211829</th>
      <td>Kerluke, Koepp and Hilpert</td>
      <td>34456 Sean Highway</td>
    </tr>
    <tr>
      <th>320563</th>
      <td>Walter-Trantow</td>
      <td>1311 Alvis Tunnel</td>
    </tr>
  </tbody>
</table>
</div>




```python
# column number와 index number (col이 몇 개 없을 때 사용)
df.iloc[:2, :2]
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
      <th>street</th>
    </tr>
    <tr>
      <th>account</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>211829</th>
      <td>Kerluke, Koepp and Hilpert</td>
      <td>34456 Sean Highway</td>
    </tr>
    <tr>
      <th>320563</th>
      <td>Walter-Trantow</td>
      <td>1311 Alvis Tunnel</td>
    </tr>
  </tbody>
</table>
</div>




```python
# column과 index name
df.loc[[211829, 320563], ["name", "street"]]
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
      <th>street</th>
    </tr>
    <tr>
      <th>account</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>211829</th>
      <td>Kerluke, Koepp and Hilpert</td>
      <td>34456 Sean Highway</td>
    </tr>
    <tr>
      <th>320563</th>
      <td>Walter-Trantow</td>
      <td>1311 Alvis Tunnel</td>
    </tr>
  </tbody>
</table>
</div>



### index 재설정


```python
df.index = list(range(0, 15))
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
      <th>name</th>
      <th>street</th>
      <th>city</th>
      <th>state</th>
      <th>postal-code</th>
      <th>Jan</th>
      <th>Feb</th>
      <th>Mar</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Kerluke, Koepp and Hilpert</td>
      <td>34456 Sean Highway</td>
      <td>New Jaycob</td>
      <td>Texas</td>
      <td>28752</td>
      <td>10000</td>
      <td>62000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Walter-Trantow</td>
      <td>1311 Alvis Tunnel</td>
      <td>Port Khadijah</td>
      <td>NorthCarolina</td>
      <td>38365</td>
      <td>95000</td>
      <td>45000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Bashirian, Kunde and Price</td>
      <td>62184 Schamberger Underpass Apt. 231</td>
      <td>New Lilianland</td>
      <td>Iowa</td>
      <td>76517</td>
      <td>91000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>D'Amore, Gleichner and Bode</td>
      <td>155 Fadel Crescent Apt. 144</td>
      <td>Hyattburgh</td>
      <td>Maine</td>
      <td>46021</td>
      <td>45000</td>
      <td>120000</td>
      <td>10000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Bauch-Goldner</td>
      <td>7274 Marissa Common</td>
      <td>Shanahanchester</td>
      <td>California</td>
      <td>49681</td>
      <td>162000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
  </tbody>
</table>
</div>



### data drop


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
      <th>name</th>
      <th>street</th>
      <th>city</th>
      <th>state</th>
      <th>postal-code</th>
      <th>Jan</th>
      <th>Feb</th>
      <th>Mar</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Kerluke, Koepp and Hilpert</td>
      <td>34456 Sean Highway</td>
      <td>New Jaycob</td>
      <td>Texas</td>
      <td>28752</td>
      <td>10000</td>
      <td>62000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Walter-Trantow</td>
      <td>1311 Alvis Tunnel</td>
      <td>Port Khadijah</td>
      <td>NorthCarolina</td>
      <td>38365</td>
      <td>95000</td>
      <td>45000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Bashirian, Kunde and Price</td>
      <td>62184 Schamberger Underpass Apt. 231</td>
      <td>New Lilianland</td>
      <td>Iowa</td>
      <td>76517</td>
      <td>91000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>D'Amore, Gleichner and Bode</td>
      <td>155 Fadel Crescent Apt. 144</td>
      <td>Hyattburgh</td>
      <td>Maine</td>
      <td>46021</td>
      <td>45000</td>
      <td>120000</td>
      <td>10000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Bauch-Goldner</td>
      <td>7274 Marissa Common</td>
      <td>Shanahanchester</td>
      <td>California</td>
      <td>49681</td>
      <td>162000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Williamson, Schumm and Hettinger</td>
      <td>89403 Casimer Spring</td>
      <td>Jeremieburgh</td>
      <td>Arkansas</td>
      <td>62785</td>
      <td>150000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Casper LLC</td>
      <td>340 Consuela Bridge Apt. 400</td>
      <td>Lake Gabriellaton</td>
      <td>Mississipi</td>
      <td>18008</td>
      <td>62000</td>
      <td>120000</td>
      <td>70000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Kovacek-Johnston</td>
      <td>91971 Cronin Vista Suite 601</td>
      <td>Deronville</td>
      <td>RhodeIsland</td>
      <td>53461</td>
      <td>145000</td>
      <td>95000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Champlin-Morar</td>
      <td>26739 Grant Lock</td>
      <td>Lake Juliannton</td>
      <td>Pennsylvania</td>
      <td>64415</td>
      <td>70000</td>
      <td>95000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Gerhold-Maggio</td>
      <td>366 Maggio Grove Apt. 998</td>
      <td>North Ras</td>
      <td>Idaho</td>
      <td>46308</td>
      <td>70000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Goodwin, Homenick and Jerde</td>
      <td>649 Cierra Forks Apt. 078</td>
      <td>Rosaberg</td>
      <td>Tenessee</td>
      <td>47743</td>
      <td>45000</td>
      <td>120000</td>
      <td>55000</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Hahn-Moore</td>
      <td>18115 Olivine Throughway</td>
      <td>Norbertomouth</td>
      <td>NorthDakota</td>
      <td>31415</td>
      <td>150000</td>
      <td>10000</td>
      <td>162000</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Frami, Anderson and Donnelly</td>
      <td>182 Bertie Road</td>
      <td>East Davian</td>
      <td>Iowa</td>
      <td>72686</td>
      <td>162000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Walsh-Haley</td>
      <td>2624 Beatty Parkways</td>
      <td>Goodwinmouth</td>
      <td>RhodeIsland</td>
      <td>31919</td>
      <td>55000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>14</th>
      <td>McDermott PLC</td>
      <td>8917 Bergstrom Meadow</td>
      <td>Kathryneborough</td>
      <td>Delaware</td>
      <td>27933</td>
      <td>150000</td>
      <td>120000</td>
      <td>70000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.drop(1)  # index number로 drop (column 단위는 drop 아닌 del로 삭제)
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
      <th>street</th>
      <th>city</th>
      <th>state</th>
      <th>postal-code</th>
      <th>Jan</th>
      <th>Feb</th>
      <th>Mar</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Kerluke, Koepp and Hilpert</td>
      <td>34456 Sean Highway</td>
      <td>New Jaycob</td>
      <td>Texas</td>
      <td>28752</td>
      <td>10000</td>
      <td>62000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Bashirian, Kunde and Price</td>
      <td>62184 Schamberger Underpass Apt. 231</td>
      <td>New Lilianland</td>
      <td>Iowa</td>
      <td>76517</td>
      <td>91000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>D'Amore, Gleichner and Bode</td>
      <td>155 Fadel Crescent Apt. 144</td>
      <td>Hyattburgh</td>
      <td>Maine</td>
      <td>46021</td>
      <td>45000</td>
      <td>120000</td>
      <td>10000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Bauch-Goldner</td>
      <td>7274 Marissa Common</td>
      <td>Shanahanchester</td>
      <td>California</td>
      <td>49681</td>
      <td>162000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Williamson, Schumm and Hettinger</td>
      <td>89403 Casimer Spring</td>
      <td>Jeremieburgh</td>
      <td>Arkansas</td>
      <td>62785</td>
      <td>150000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Casper LLC</td>
      <td>340 Consuela Bridge Apt. 400</td>
      <td>Lake Gabriellaton</td>
      <td>Mississipi</td>
      <td>18008</td>
      <td>62000</td>
      <td>120000</td>
      <td>70000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Kovacek-Johnston</td>
      <td>91971 Cronin Vista Suite 601</td>
      <td>Deronville</td>
      <td>RhodeIsland</td>
      <td>53461</td>
      <td>145000</td>
      <td>95000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Champlin-Morar</td>
      <td>26739 Grant Lock</td>
      <td>Lake Juliannton</td>
      <td>Pennsylvania</td>
      <td>64415</td>
      <td>70000</td>
      <td>95000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Gerhold-Maggio</td>
      <td>366 Maggio Grove Apt. 998</td>
      <td>North Ras</td>
      <td>Idaho</td>
      <td>46308</td>
      <td>70000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Goodwin, Homenick and Jerde</td>
      <td>649 Cierra Forks Apt. 078</td>
      <td>Rosaberg</td>
      <td>Tenessee</td>
      <td>47743</td>
      <td>45000</td>
      <td>120000</td>
      <td>55000</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Hahn-Moore</td>
      <td>18115 Olivine Throughway</td>
      <td>Norbertomouth</td>
      <td>NorthDakota</td>
      <td>31415</td>
      <td>150000</td>
      <td>10000</td>
      <td>162000</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Frami, Anderson and Donnelly</td>
      <td>182 Bertie Road</td>
      <td>East Davian</td>
      <td>Iowa</td>
      <td>72686</td>
      <td>162000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Walsh-Haley</td>
      <td>2624 Beatty Parkways</td>
      <td>Goodwinmouth</td>
      <td>RhodeIsland</td>
      <td>31919</td>
      <td>55000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>14</th>
      <td>McDermott PLC</td>
      <td>8917 Bergstrom Meadow</td>
      <td>Kathryneborough</td>
      <td>Delaware</td>
      <td>27933</td>
      <td>150000</td>
      <td>120000</td>
      <td>70000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.drop([0, 1, 2, 3])  # 한 개 이상의 index number로 drop
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
      <th>street</th>
      <th>city</th>
      <th>state</th>
      <th>postal-code</th>
      <th>Jan</th>
      <th>Feb</th>
      <th>Mar</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>Bauch-Goldner</td>
      <td>7274 Marissa Common</td>
      <td>Shanahanchester</td>
      <td>California</td>
      <td>49681</td>
      <td>162000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Williamson, Schumm and Hettinger</td>
      <td>89403 Casimer Spring</td>
      <td>Jeremieburgh</td>
      <td>Arkansas</td>
      <td>62785</td>
      <td>150000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Casper LLC</td>
      <td>340 Consuela Bridge Apt. 400</td>
      <td>Lake Gabriellaton</td>
      <td>Mississipi</td>
      <td>18008</td>
      <td>62000</td>
      <td>120000</td>
      <td>70000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Kovacek-Johnston</td>
      <td>91971 Cronin Vista Suite 601</td>
      <td>Deronville</td>
      <td>RhodeIsland</td>
      <td>53461</td>
      <td>145000</td>
      <td>95000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Champlin-Morar</td>
      <td>26739 Grant Lock</td>
      <td>Lake Juliannton</td>
      <td>Pennsylvania</td>
      <td>64415</td>
      <td>70000</td>
      <td>95000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Gerhold-Maggio</td>
      <td>366 Maggio Grove Apt. 998</td>
      <td>North Ras</td>
      <td>Idaho</td>
      <td>46308</td>
      <td>70000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Goodwin, Homenick and Jerde</td>
      <td>649 Cierra Forks Apt. 078</td>
      <td>Rosaberg</td>
      <td>Tenessee</td>
      <td>47743</td>
      <td>45000</td>
      <td>120000</td>
      <td>55000</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Hahn-Moore</td>
      <td>18115 Olivine Throughway</td>
      <td>Norbertomouth</td>
      <td>NorthDakota</td>
      <td>31415</td>
      <td>150000</td>
      <td>10000</td>
      <td>162000</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Frami, Anderson and Donnelly</td>
      <td>182 Bertie Road</td>
      <td>East Davian</td>
      <td>Iowa</td>
      <td>72686</td>
      <td>162000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Walsh-Haley</td>
      <td>2624 Beatty Parkways</td>
      <td>Goodwinmouth</td>
      <td>RhodeIsland</td>
      <td>31919</td>
      <td>55000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>14</th>
      <td>McDermott PLC</td>
      <td>8917 Bergstrom Meadow</td>
      <td>Kathryneborough</td>
      <td>Delaware</td>
      <td>27933</td>
      <td>150000</td>
      <td>120000</td>
      <td>70000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.drop("city", axis = 1)  # column중에 "city"
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
      <th>street</th>
      <th>state</th>
      <th>postal-code</th>
      <th>Jan</th>
      <th>Feb</th>
      <th>Mar</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Kerluke, Koepp and Hilpert</td>
      <td>34456 Sean Highway</td>
      <td>Texas</td>
      <td>28752</td>
      <td>10000</td>
      <td>62000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Walter-Trantow</td>
      <td>1311 Alvis Tunnel</td>
      <td>NorthCarolina</td>
      <td>38365</td>
      <td>95000</td>
      <td>45000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Bashirian, Kunde and Price</td>
      <td>62184 Schamberger Underpass Apt. 231</td>
      <td>Iowa</td>
      <td>76517</td>
      <td>91000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>D'Amore, Gleichner and Bode</td>
      <td>155 Fadel Crescent Apt. 144</td>
      <td>Maine</td>
      <td>46021</td>
      <td>45000</td>
      <td>120000</td>
      <td>10000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Bauch-Goldner</td>
      <td>7274 Marissa Common</td>
      <td>California</td>
      <td>49681</td>
      <td>162000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Williamson, Schumm and Hettinger</td>
      <td>89403 Casimer Spring</td>
      <td>Arkansas</td>
      <td>62785</td>
      <td>150000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Casper LLC</td>
      <td>340 Consuela Bridge Apt. 400</td>
      <td>Mississipi</td>
      <td>18008</td>
      <td>62000</td>
      <td>120000</td>
      <td>70000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Kovacek-Johnston</td>
      <td>91971 Cronin Vista Suite 601</td>
      <td>RhodeIsland</td>
      <td>53461</td>
      <td>145000</td>
      <td>95000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Champlin-Morar</td>
      <td>26739 Grant Lock</td>
      <td>Pennsylvania</td>
      <td>64415</td>
      <td>70000</td>
      <td>95000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Gerhold-Maggio</td>
      <td>366 Maggio Grove Apt. 998</td>
      <td>Idaho</td>
      <td>46308</td>
      <td>70000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Goodwin, Homenick and Jerde</td>
      <td>649 Cierra Forks Apt. 078</td>
      <td>Tenessee</td>
      <td>47743</td>
      <td>45000</td>
      <td>120000</td>
      <td>55000</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Hahn-Moore</td>
      <td>18115 Olivine Throughway</td>
      <td>NorthDakota</td>
      <td>31415</td>
      <td>150000</td>
      <td>10000</td>
      <td>162000</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Frami, Anderson and Donnelly</td>
      <td>182 Bertie Road</td>
      <td>Iowa</td>
      <td>72686</td>
      <td>162000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Walsh-Haley</td>
      <td>2624 Beatty Parkways</td>
      <td>RhodeIsland</td>
      <td>31919</td>
      <td>55000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>14</th>
      <td>McDermott PLC</td>
      <td>8917 Bergstrom Meadow</td>
      <td>Delaware</td>
      <td>27933</td>
      <td>150000</td>
      <td>120000</td>
      <td>70000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.drop(["street", "state"], axis = 1)  # column중에 "street", "state"
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
      <th>city</th>
      <th>postal-code</th>
      <th>Jan</th>
      <th>Feb</th>
      <th>Mar</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Kerluke, Koepp and Hilpert</td>
      <td>New Jaycob</td>
      <td>28752</td>
      <td>10000</td>
      <td>62000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Walter-Trantow</td>
      <td>Port Khadijah</td>
      <td>38365</td>
      <td>95000</td>
      <td>45000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Bashirian, Kunde and Price</td>
      <td>New Lilianland</td>
      <td>76517</td>
      <td>91000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>D'Amore, Gleichner and Bode</td>
      <td>Hyattburgh</td>
      <td>46021</td>
      <td>45000</td>
      <td>120000</td>
      <td>10000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Bauch-Goldner</td>
      <td>Shanahanchester</td>
      <td>49681</td>
      <td>162000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Williamson, Schumm and Hettinger</td>
      <td>Jeremieburgh</td>
      <td>62785</td>
      <td>150000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Casper LLC</td>
      <td>Lake Gabriellaton</td>
      <td>18008</td>
      <td>62000</td>
      <td>120000</td>
      <td>70000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Kovacek-Johnston</td>
      <td>Deronville</td>
      <td>53461</td>
      <td>145000</td>
      <td>95000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Champlin-Morar</td>
      <td>Lake Juliannton</td>
      <td>64415</td>
      <td>70000</td>
      <td>95000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Gerhold-Maggio</td>
      <td>North Ras</td>
      <td>46308</td>
      <td>70000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Goodwin, Homenick and Jerde</td>
      <td>Rosaberg</td>
      <td>47743</td>
      <td>45000</td>
      <td>120000</td>
      <td>55000</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Hahn-Moore</td>
      <td>Norbertomouth</td>
      <td>31415</td>
      <td>150000</td>
      <td>10000</td>
      <td>162000</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Frami, Anderson and Donnelly</td>
      <td>East Davian</td>
      <td>72686</td>
      <td>162000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Walsh-Haley</td>
      <td>Goodwinmouth</td>
      <td>31919</td>
      <td>55000</td>
      <td>120000</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>14</th>
      <td>McDermott PLC</td>
      <td>Kathryneborough</td>
      <td>27933</td>
      <td>150000</td>
      <td>120000</td>
      <td>70000</td>
    </tr>
  </tbody>
</table>
</div>

</br>

***
https://www.boostcourse.org/ai222/lecture/23822
