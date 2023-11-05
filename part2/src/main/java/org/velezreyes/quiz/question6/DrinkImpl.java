package org.velezreyes.quiz.question6;

public class DrinkImpl implements Drink{

    private String name;

    public DrinkImpl(String name){
        this.name = name;
    }

    @Override
    public String getName() {
       return this.name;
    }

    @Override
    public boolean isFizzy() {
      if(this.name.equals("ScottCola") || this.name.equals("BessieBooze")){
        return true;
      }else if(this.name.equals("KarenTea")){
        return false;
      }else{
        return true;
      }
    }
    
}
