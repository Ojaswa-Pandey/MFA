x=[12.1, 13.2, 15.6, 17.2, 18.8, 10.3, 11.7, 16.4]
y=[48, 59, 32, 18, 41, 32, 31, 30]
z=[101, 171, 112, 132, 140, 112, 151, 96]

meanX= sum(x)/len(x)
meanY= sum(y)/len(y)
meanZ= sum(z)/len(z)

def covariance(a,b):
    n=len(a)
    meanA= sum(a)/len(a)
    meanB= sum(b)/len(b)
    total=0
    for i in range (n):
        total+=(a[i]-meanA)*(b[i]-meanB)
    return total/(n-1)

covxx= covariance(x,x)
covxy= covariance(x,y)
covxz= covariance(x,z)
covyy= covariance(y,y)
covyz= covariance(y,z)
covzz= covariance(z,z)

covMatrix=[covxx, covxy, covxz],[covxy, covyy, covyz], [covxz, covyz, covzz]

for row in covMatrix:
    print(row)




