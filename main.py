from sklearn import datasets
iris = datasets.load_iris()

print(type(iris))
print('-----------------------------')
print(dir(iris))
print('-----------------------------')
target = iris.target
print(target)