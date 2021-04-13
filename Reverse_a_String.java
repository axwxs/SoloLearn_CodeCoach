/*
Write a program to take a string as input and output its reverse.
The given code takes a string as input and converts it into a char array, which contains letters of the string as its elements. 

Sample Input:
hello there

Sample Output: 
ereht olleh
*/


import java.util.Scanner;

public class Program
{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String text = scanner.nextLine();
        char[] arr = text.toCharArray();
  
  
  
  String backwardsText = "";
  for (char i:arr) {
      backwardsText = i + backwardsText;
  }
  System.out.println(backwardsText );
  
  // System.out.println(arr);
        
    }
}
