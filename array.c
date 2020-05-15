#include<stdio.h>
int main()
{
int a[2][2];
int i,j;
int sum=0;
a[0][0]=1;
a[0][1]=2;
a[0][2]=3;
a[1][0]=4;
a[1][1]=5;
a[1][2]=6;
a[2][0]=7;
a[2][1]=8;
a[2][2]=9;
int *b1=&a[0][0];
int *b2=&a[0][1];
int *b3=&a[0][2];
int *b4=&a[1][0];
int *b5=&a[1][1];
int *b6=&a[1][2];
int *b7=&a[2][0];
int *b8=&a[2][1];
int *b9=&a[2][2];
printf("the array is\n");
printf("%d %d %d",*b1,*b2,*b3);
printf("\n");
printf("%d %d %d",*b4,*b5,*b6);
printf("\n");
printf("%d %d %d",*b7,*b8,*b9);
printf("\n");
for(i=0;i<=2;i++)
{
for(j=0;j<=2;j++)
{
if(i==j)
{
sum+=a[i][j];
}
}
}
printf("the sum of diagnol elements is %d",sum);
return 0;
}


