
package threefunctions;

public class ThreeFunctions {

// REVERSE STRING
//    public static void main(String[] args) {
//        String r = reverse("Ruy López");
//        System.out.println(r);
//    }
//    
//    public static String reverse(String s) {
//        char[] letters = new char[s.length()];
//        
//        for (int i = s.length() - 1; i >= 0; i--) {
//            System.out.println(s.charAt(i));
//        }
//        return s;
//    }
    // PALINDROME STRING
//    public static void main(String[] args) {
//     String original = "Ruy López";
//     original = original.replace(" ", "");
//    String reverse = "";
//    for(int i = original.length() - 1; i >= 0; i--) {
//        reverse += original.charAt(i);
//        System.out.println(reverse);
//    }   
// 
//    boolean palindrome = true;
//    for(int i = 0; i < original.length(); i++) {
//        if(original.charAt(i) != reverse.charAt(i)) {
//            palindrome = false;
//        }
//        }
//        if(palindrome) {
//            System.out.println("True");
//        } 
//        else {
//            System.out.println("False");
//        }
//    }
    
//         RANDOM NUMBER BETWEEN TWO INTEGERS
        public static void main(String[] args) {
            int min = 100;
            int max = 1000;
            
            System.out.println("Random value in int from "+min+" to "+max+ ":");
            int random_int = (int)Math.floor(Math.random()*(max-min)+min);
            System.out.println(random_int);
        }
    }