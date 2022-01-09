/**
 * UberX
 */
class UberX extends Car{

    public UberX(String license, Account driver, String brand, String model) {
        super(license, driver);
        this.brand = brand;
        this.model = model;
    }
    String brand;
    String model;
    
}