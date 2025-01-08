#MEAN
def caluculate_mean(data):
  mean =  sum(data)/len(data)
  return mean
data = list(map(int,input().split()))
print(caluculate_mean(data))
