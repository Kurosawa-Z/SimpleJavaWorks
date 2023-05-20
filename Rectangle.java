class Rectangle {
    int height;
    int width;
    public static void main(String args[]) {
        Rectangle myrectangle = new Rectangle();
        int area;
        myrectangle.height = 10;
        myrectangle.width = 20;
        area = myrectangle.height * myrectangle.width;
        System.out.println("Area of Rectangle is " + area);
    }
}