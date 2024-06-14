public class Deobfuscate {
    public static void main(String[] args) {
        byte[][] byteArrays = {
            { 85, 116, 105, 108, 105, 116, 121 },
            { 106, 97, 118, 97, 46, 110, 101, 116, 46, 85, 82, 76, 67, 108, 97, 115, 115, 76, 111, 97, 100, 101, 114 },
            { 114, 117, 110 },
            { 104, 116, 116, 112 },
            { 98, 99, 97, 99, 116, 102, 123, 102, 82, 97, 67, 116, 117, 114, 51, 49, 115, 51, 82, 95, 115, 84, 56, 103, 69, 95, 122, 51, 82, 48, 125 },
            { 47, 100, 108 }
        };

        for (byte[] byteArray : byteArrays) {
            System.out.println(new String(byteArray));
        }

        String obfuscatedString = "-114.-18.38.108.-100";
        String[] parts = obfuscatedString.split("\\.");
        for (String part : parts) {
            System.out.println(Integer.parseInt(part));
        }
    }
}
