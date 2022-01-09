import Car from './Car'

class UberBlack extends Car {
    constructor(license, driver, typeCarAccepted, seatMaterial){
        super(license, driver)
        this.typeCarAccepted = typeCarAccepted
        this.seatMaterial = seatMaterial
    }
}