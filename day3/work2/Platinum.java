package work2;

class Platinum implements IMember{
    private static double DISCOUNT = 0.3;
    private final double totalAmount;

    public Platinum(final double totalAmount){
        this.totalAmount = totalAmount;
    }

    @Override
    public double priceCut() {
        return totalAmount - totalAmount*DISCOUNT;
    }
}