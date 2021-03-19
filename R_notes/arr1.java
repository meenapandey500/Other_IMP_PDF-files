import java.util.Scanner;
public class arr1
{
    public static void main(String[] args) 
    {
        int n,i,j,b, sum = 0;
        Scanner s = new Scanner(System.in);
        System.out.print("Enter no. of elements you want in array:");
        n = s.nextInt();
        int a[] = new int[n];
        System.out.println("Enter all the elements:");
        for(i = 0; i < n; i++)
        {
            a[i] = s.nextInt();
            
        }
		sum=0;
		for(i = 0; i < n; i++)
        {
			if(a[i]<100)
			{
            b = a[i];
			sum=sum+b;
            }
        }
		for(i = 0; i < n; i++)
        {
			if(a[i]<100)
			{
				a[i]=sum;
			}
			
		}
		for(i = 0; i < n; i++)
        {
		
        System.out.println("Array "+a[i]);
		}
	}
}