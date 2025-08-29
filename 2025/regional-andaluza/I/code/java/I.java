package enchantedforest;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.InputStream;

public class solution {

	public static Integer beauty(Integer n, List<Integer> beauty1, List<Integer> beauty2) {
		if (n==1) return Math.max(beauty1.get(0), beauty2.get(0));;
		List<Integer> dp1 = new ArrayList<>();
		List<Integer> dp2 = new ArrayList<>();
		dp1.add(beauty1.get(0));
		dp2.add(beauty2.get(0));
		if (n>1) {
			dp1.add(dp2.get(0) + beauty1.get(1));
			dp2.add(dp1.get(0) + beauty2.get(1));
		}
			
		for(int i =2;i<n;i++) {
			dp1.add(beauty1.get(i)+Math.max(dp2.get(i-1), dp2.get(i-2)));
			dp2.add(beauty2.get(i)+Math.max(dp1.get(i-1), dp1.get(i-2)));
		}
		return Math.max(dp1.get(n-1),dp2.get(n-1));
	}
	
	public static void test(String[] args) {
		InputStream inputStream = solution.class.getClassLoader().getResourceAsStream("in.txt");

		if (inputStream == null) {
			System.out.println("File not found in resources.");
		    return;
		}
		Scanner scanner = new Scanner(inputStream);

		int t = scanner.nextInt();
		scanner.nextLine(); 
		for (int i = 0; i < t; i++) {
		    int n = scanner.nextInt(); 
			scanner.nextLine(); 
		    List<Integer> list1 = new ArrayList<>();
		    String[] parts1 = scanner.nextLine().split(" ");
		    for (String part : parts1) {
		        list1.add(Integer.parseInt(part));
		    }
		    List<Integer> list2 = new ArrayList<>();
		    String[] parts2 = scanner.nextLine().split(" ");
		    for (String part : parts2) {
		        list2.add(Integer.parseInt(part));
		    }
			
		    Integer beauty = beauty(n, list1,list2);		
		    System.out.println(beauty); 
		}
		scanner.close();
	}
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        scanner.nextLine(); 
        for (int i = 0; i < t; i++) {
            int n = scanner.nextInt(); 
        	scanner.nextLine(); 
            List<Integer> list1 = new ArrayList<>();
            String[] parts1 = scanner.nextLine().split(" ");
            for (String part : parts1) {
                list1.add(Integer.parseInt(part));
            }
            List<Integer> list2 = new ArrayList<>();
            String[] parts2 = scanner.nextLine().split(" ");
            for (String part : parts2) {
                list2.add(Integer.parseInt(part));
            }
    		
            Integer beauty = beauty(n, list1,list2);

            System.out.println(beauty); 
        }
        scanner.close();
    }
}
