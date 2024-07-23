class demoException {
    public static void main(String[] args) {
        try {
            if (args.length != 2) { throw new IllegalArgumentException("Enter two number"); }
            System.out.println("Result is: " + (Integer.parseInt(args[0]) / Integer.parseInt(args[1])));
        } catch (Exception ex) {
            System.err.println(ex);
        }
    }
}