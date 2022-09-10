class Human{
    private String name;
    public Human(String name){
        this.name = name;
    }
    public void work(){
        System.out.println("Human "+this.name+ " works");
    }
}
class Doctor extends Human{
    private String medicalField;
    public Doctor(String name, String medicalField){
        super(name);
        this.medicalField = medicalField;
     }
    public void work(){
        System.out.println("Doctor "+this.name+ " works");
    }
}
class Teacher extends Human{
    private String school;
    public Teacher(String name, String school){
        super(name);
        this.school = school;
     }
    public void work(){
        System.out.println("Teacher "+this.name+ " works");
    }
}
public class Inheritance{
    public static void main(String [] args){
        Human human = new Doctor("Aye Ko", "OG")  //Sub typing
        human.work()

        Human human = new Teacher("Daw Mya", "SUOE")
        human.work()
    }
}