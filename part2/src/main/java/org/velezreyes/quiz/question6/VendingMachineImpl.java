package org.velezreyes.quiz.question6;

public class VendingMachineImpl implements VendingMachine{

  private int coins;

  public VendingMachineImpl(){
    System.err.println(coins);
  }

  public static VendingMachine getInstance() {
    // Fix me!
    return new VendingMachineImpl();
  }

  @Override
  public void insertQuarter() {
    ++this.coins;
  }

  public int getCoins(){
    return this.coins;
  }  
  
  public void restCoins(int lessCoins){
    this.coins =- lessCoins;
  }


  @Override
  public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
    if(name.equals("ScottCola")){
      if(coins >= 3){
        restCoins(coins);
        System.out.println("Cambio: " + coins);
        return new DrinkImpl("ScottCola");
      }
      throw new NotEnoughMoneyException();
    }else if(name.equals("KarenTea")){
       if(coins >= 4){
        restCoins(coins);
        System.out.println("Cambio: " + coins);
        return new DrinkImpl("KarenTea");
      }
      throw new NotEnoughMoneyException();

    }
    throw new UnknownDrinkException();
  
  }
}
