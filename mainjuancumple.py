class Persona {
    String nombre;
    int edad;

    Persona(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    void mostrarInformacion() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Edad: " + edad);
    }

    void cumplirAnios() {
        edad++;
        System.out.println(nombre + " ha cumplido años. Ahora tiene " + edad + " años.");
    }
}

public class Main {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Juan José", 25);

        persona1.mostrarInformacion();

        persona1.cumplirAnios();
    }
}