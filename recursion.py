class recursion:

    def factorial(self,n):
        if n==0:
            return 1
        else:
            return n * (self.factorial(n-1))
    
    #let print the fabonicee series
    def fabonicce(self,num):
        if num==0:
            return 0
        elif num==1:
            return 1 
        else:
            return self.fabonicce(num - 1)  + self.fabonicce(num - 2)     
        
r=recursion()
print(r.factorial(int(input("enter your number to get te factorial number "))))
print(r.fabonicce(int(input("enter your number to get the fabbpincce number "))))
