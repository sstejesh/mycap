n=int(input("how many terms"))
a=0
b=1
count=0
if n<=0:
  print("please enter positive integer")
elif n==1:
  print("fibonacci series upto",n,":")
  print(a)
else:
  print("fibonacci series:")
  while count < n:
    print(a)
    c=a+b
    a=b
    b=c
    count+=1
  end
end  
