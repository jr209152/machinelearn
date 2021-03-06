from numpy import *
import scipy.spatial.distance as dist
#范数
A = [8,1,6]
print(power(A,2))
modA = sqrt(sum(power(A,2)))
print(linalg.norm(A))
#闵可夫斯基距离：一组距离的定义

#欧式距离
vector1 = mat([1,2,3])
vector2 = mat([4,5,6])
print(sqrt((vector1-vector2)*(vector1-vector2).T))

#曼哈顿距离
vector1 = mat([1,2,3])
vector2 = mat([4,5,6])
print(sum(abs(vector1-vector2)))

#切比雪夫距离
vector1 = mat([1,2,3])
vector2 = mat([4,7,5])
print(abs(vector1-vector2).max())

#夹角余弦
vector1 = mat([4,5,6])
vector2 = mat([4,5,6])
print((dot(vector1,vector2.T))/(linalg.norm(vector1)*linalg.norm(vector2)))
print("------------------------------------------------------")

#汉明距离
matV = mat([[1,1,0,1,0,1,0,0,1],[0,1,1,0,0,0,1,1,1]])
smstr = nonzero(matV[0]-matV[1])#查看哪些位置不同
print(shape(smstr)[1])

#杰卡德距离
Vector1 = array([1,1,0,1,0,1,0,0,1])
Vector2 = array([0,1,1,0,0,0,1,1,1])
matV = mat([Vector1 ,Vector2])
print(matV)
print("dist.jaccard:",dist.pdist(matV,'jaccard'))

#相关系数
featuremat = mat([[88.5,96.8,104.1,111.3,117.7,124.0,130.0,135.4,140.2,145.3,151.9,159.5,165.9,169.8,171.6,172.3,172.7],
    [12.54,14.65,16.64,18.98,21.26,24.06,27.33,30.46,33.74,37.69,42.49,48.08,53.37,57.08,59.35,60.68,61.40]])
print(featuremat)

#均值
mv1 = mean(featuremat[0])
mv2 = mean(featuremat[1])
print(mv1,mv2) 

#标准差
dv1 = std(featuremat[0])
dv2 = std(featuremat[1])
print(dv1,dv2) 

corref = mean(multiply(featuremat[0]-mv1,featuremat[1]-mv2)/(dv1*dv2))
print(corref)

print(corrcoef(featuremat))

vectormat = mat([[1,2,3],[4,5,6]])
v12 = vectormat[0] - vectormat[1]
print(sqrt(v12 * v12.T))

varmat = std(vectormat.T,axis = 0)
normvmat = (vectormat - mean(vectormat)) / varmat.T
normv12 = normvmat[0] - normvmat[1]
print(sqrt(normv12*normv12.T))

