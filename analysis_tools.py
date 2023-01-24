#Importing math function
import math

#Writing class for math needed
class MyMath:

   #Removing blank spaces from data
   def cleanup(data):
        new_list = []
        for i in data:
            if i != '':
                new_list.append(float(i))
        return new_list

   #Calculating mean of data
   def mean(data):
       new_list = MyMath.cleanup(data)
       total = 0
       for var in new_list:
           var = float(var)
           total = total+var
       mean = float(total)/len(new_list)
       return mean

   #Calculating median of data
   def median(data):
       new_list = MyMath.cleanup(data)
       new_list.sort()
       if len(new_list)%2==1:
           p = len(new_list)//2
           return new_list[p]
       else:
           p=len(new_list)//2
           p=new_list[p]
           p2=(len(new_list)//2)-1
           p2= new_list[p2]
           finalP= p+p2
           return finalP/2
   #Calculating standard deviation of data
   def stddev(data):
       total = 0
       new_list = MyMath.cleanup(data)
       mean = MyMath.mean(new_list)
       for number in new_list:
           number = number - mean
           number = number**2
           total = total+number
       total = total/len(new_list)
       return math.sqrt(total)

   #Finding smallest value in data
   def min(data):
       new_list = MyMath.cleanup(data)
       return min(new_list)

   #Finding Biggest Value in data
   def max(data):
       new_list = MyMath.cleanup(data)
       return max(new_list)



'''new_list=MyMath.cleanup([1,2,3,4,5,"", 6])
print(MyMath.mean(new_list))
MyMath.median(new_list)
MyMath.stddev(new_list)
MyMath.min(new_list)
MyMath.max(new_list)'''
