#How to use listcomprehension

Nums=[i for i in range(16)]
print(Nums)

Hello=[i for i in ("Hello")]
print(Hello)

Pow3 =[i ** 3 for i in range(10)]
print(Pow3)

Five=[[5*i+j for j in range(1,6)] for i in range(5)]
print(Five)

List1=['a','x']
List2=['y','b']

Merge=[i1 + i2 for i1 in List1 for i2 in List2]
print(Merge)