#include<stdio.h>
int main()
{
int marks;
printf("enter your marks for deciding your grade");
scanf("%d",&marks);
if(marks>=85 && marks<=100)
{
printf("you got 'Grade A'");
}
elseif(marks>=70 && marks<=84)
{
printf("you got 'Grade B'");
}
elseif(marks>=55 && marks<=69)
{
printf("you got 'Grade C'");
}
elseif(marks>=40 && marks<=54)
{
printf("you got 'Grade D'");
}
else(marks<40)
{
printf("you got 'Grade F'");
}
return 0;
}
