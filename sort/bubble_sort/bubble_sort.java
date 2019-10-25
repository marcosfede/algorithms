import java.util.*;
import java.io.*;
class Main {
  public static void main(String[] args) {

    int[] arr = new int[]{ 1, 5, 65, 23, 57, 1232, -1, -5, -2, 242, 100,
         4, 423, 2, 564, 9, 0, 10, 43, 64, 32, 1, 999 }; 

    System.out.println("Before Sorting : ");
    for(int x:arr)
    System.out.print(x+" ");
    System.out.println();
    Main obj = new Main();
    obj.bubblesort(arr,23);
  }
  public void bubblesort(int[] arr,int n)
  {
    for(int i=0;i<n-1;i++)
    {
        for(int j=i;j<n;j++)
        {
            if(arr[i]>arr[j])
            {
                int temp=arr[i];
                arr[i]=arr[j];
                arr[j]=temp;
            }
        }
    }
    System.out.println("After Sorting : ");
    for(int x:arr)
    System.out.print(x+" ");
  }
}
