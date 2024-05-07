import java.util.Scanner;

public class CoffeNutStash {
  private static final int[] expected = new int[] {
      578, 568, 588, 248, 573, 573, 508, 543, 618, 258,
      553, 533, 243, 608, 478, 608, 243, 588, 573, 478,
      533, 263, 593, 263, 478, 498, 243, 513, 513, 258,
      258, 478, 273, 258, 288, 253, 278, 263, 628 };

  public static void main(String[] paramArrayOfString) {
    System.out.println("Welcome to the Coffee Nut Stash!");
    System.out.println("Enter the password? ");
    Scanner scanner = new Scanner(System.in);
    String str = scanner.next();
    scanner.close();
    char[] arrayOfChar = str.toCharArray();
    if (arrayOfChar.length != expected.length) {
      System.out.println("Incorrect password!");
      return;
    }
    for (byte b = 0; b < arrayOfChar.length; b++) {
      char c = arrayOfChar[b];
      if (c * 5 + 3 != expected[b]) {
        System.out.println("Incorrect password!");
        return;
      }
    }
    System.out.println("Correct!");
  }
}
