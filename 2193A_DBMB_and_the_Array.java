import java.util.*;
import java.io.*;
public class cp{
  public static void main(String[]args) throws IOException{
    BufferedReader br=new BufferedReader(new InputStreamReader(System.in));    
    int t=Integer.parseInt(br.readLine().trim());
    while(t-->0){
    StringTokenizer st=new StringTokenizer(br.readLine());
    int n=Integer.parseInt(st.nextToken());
    int s=Integer.parseInt(st.nextToken());
    int x=Integer.parseInt(st.nextToken());
    int [] a= new int[n];
    StringTokenizer st2=new StringTokenizer(br.readLine());
    for (int i=0;i<n;i++){
      int c=Integer.parseInt(st2.nextToken());
      a[i]=c;
  }
    int sum=0;
    for(int i=0;i<n;i++){
                sum+=a[i];
            }
    int diff=s-sum;
    if(diff>=0&&diff%x==0){
        System.out.println("Yes");
            }
    else{
         System.out.println("No");
            }
    }
  }
}
    