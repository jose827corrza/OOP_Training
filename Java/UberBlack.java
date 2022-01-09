import java.util.ArrayList;
import java.util.Map;

class UberBlack extends Car{
    Map<String, Map<String, Integer>> typeAccepted;
    ArrayList<String> seatMaterial;

    public UberBlack(String license, Account driver, Map<String, Map<String, Integer>> typeAccepted, ArrayList<String> seatMaterial) {
        super(license, driver);
        this.typeAccepted = typeAccepted;
        this.seatMaterial = seatMaterial;
        //TODO Auto-generated constructor stub
    }
    
}