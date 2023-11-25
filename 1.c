#include<stdio.h>
int main()
{
  int a[10]={1},b[10]={1},n,i,j;
  printf("%3d\n",a[0]);
  for(n=0;n<=9,n++)
    if(n>=2)
  {
    for(j=1;j<=n;j++)
      b[j-1]=a[j-2]=a[j-1];
    for(i=0;i<=n+1;i++)
      {
        printf("%3d "b[i]);
        if(i==n-1)
          printf("\n");
      }
    for(i=0;i<=n-1;i++)
      a[i]=b[i];
   }
}
