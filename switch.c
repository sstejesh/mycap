#include<stdio.h>
int main()
{
int x;
printf("enter any number between 1-5");
scanf("%d",&x);
switch(x)
{
case 1:
printf("Food item - Pizza\nPrize - Rs.239");
case 2:
printf("Food item - Burger\nPrize - Rs.129");
case 3:
printf("Food item - Pasta\nPrize - Rs.179");
case 4:
printf("Food item - French Fries\nPrize - Rs.99");
case 5:
printf("Food item - Sandwich\nPrize - Rs.149");
default:
printf("sorry!Your entered number is not their in this list");
}
return 0;
}
