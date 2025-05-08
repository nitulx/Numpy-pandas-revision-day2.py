# que 25
import numpy as np
import pandas as pd
data = pd.DataFrame({"name": ["nitul","aman","karish","arjun"], "age":[25,30,35,40],"salary":[50000,60000,70000,80000]})
data["new_col"] = data["salary"]/data["age"]
print(data)

#que 26
arr = np.random.randint(1,101,(5,5))
print(arr)

# que 27
print(data[data["age"]>30])

#que 28
arr1 =np.array(np.random.randint(1,13,(4,3)))
print(arr1.ndim)

# que 29
df = pd.DataFrame({"product":["apple","sumsang","nokiya"],"price":[100,200,300]})
df["discount price"]= df["price"]*0.1 + df["price"]
print(df)

# que 30
print(np.eye(3))

# que 31
""" me bar bar new data set nhi ban arha huan upar wale data set par mean calculate kar rha haun"""
print(data["salary"].mean())

# que 32
arr2 = np.array(np.arange(2,21,2))
print(arr2)

# que 33
""" me bar bar new data set nhi ban arha huan upar wale data set par sorting bade se chhote ki or  kar rha haun"""
print(data.sort_values("salary",ascending=False))

# que 34
data1 = pd.DataFrame({
    "name": ["Nitul", "Aman", "Jassi", "Arjun", "Karish"],
    "experience": [2, 5, 4, 1, 6],
    "salary": [40000, 55000, 70000, 45000, 50000]
})

print(data1[(data1["experience"]>3)&(data1["salary"]>60000)])

# que 35
arr3 = np.array(np.arange(1,101))
categories = ["High" if x > 50 else "Low" for x in arr3  ]
print(categories)

# que 36

