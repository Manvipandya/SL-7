/*

	Assignment: 3
	Roll Number: 43227
	Batch: Q10
	Lab: CL7

*/

import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Scanner;

public class SHA
{
	public static String encrypt(String input)
	{
		try
		{
			MessageDigest md = MessageDigest.getInstance("SHA-1");
			byte[] messageDigest = md.digest(input.getBytes());
			BigInteger no = new BigInteger(1, messageDigest);
			String hashtext = no.toString(16);
			while (hashtext.length() < 32)
			{
				hashtext = "0" + hashtext;
			}
			return hashtext;
		}
		catch(NoSuchAlgorithmException e)
		{
			throw new RuntimeException(e);
		}
	}
	
	public static void main(String args[]) throws NoSuchAlgorithmException
	{
		Scanner in = new Scanner(System.in);
		System.out.println("Enter string for hashcode generation:");
		String s = in.nextLine();
		System.out.println("HashCode Generated by SHA-1 for " + s + ":\n" + encrypt(s));
	}
}

/*

Output:

$ java SHA
Enter string for hashcode generation:
Hello World
HashCode Generated by SHA-1 for Hello World:
a4d55a8d778e5022fab701977c5d840bbc486d0

*/