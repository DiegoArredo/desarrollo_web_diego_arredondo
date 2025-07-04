package microservicio_notas.m_notas.model;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.validation.constraints.NotNull;
import jakarta.persistence.Id;

@Entity
public class Nota {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @NotNull
    // Se usa column para especificar el nombre de la columna en la base de datos.
    // Asi se puede usar un nombre diferente para no tener problemas con el Repository y JPA.
    @Column(name = "actividad_id")
    private Integer actividadId;

    @NotNull
    private Integer nota;

    public Nota() {
    }
    // Constructor para crear una Nota !
    public Nota(Integer actividad_id, Integer nota) {
        this.actividadId = actividad_id;
        this.nota = nota;
    }

    // Esto retornará al llamar una funcion al @repository pidiendo una Nota.
    public Long getId() {
        return id;
    }
    public Integer getActividadId() {
        return actividadId;
    }
    public Integer getNota() {
        return nota;
    }

    public void setId(Long id) {
        this.id = id;
    }

    // Setters , aun no se bien para que sirven.
    public void setActividadId(Integer actividad_id) {
        this.actividadId = actividad_id;
    }
    public void setNota(Integer nota) {
        this.nota = nota;
    }

    // No se usarlo 
    public void validateNota(){
        if (actividadId == null || actividadId <= 0) {
            throw new IllegalArgumentException("Actividad ID debe ser un número positivo.");
        }
        if (nota == null || nota < 1 || nota > 7) {
            throw new IllegalArgumentException("Nota entre 1 y 7.");
        }
        if (nota % 1 != 0) {
            throw new IllegalArgumentException("Nota debe ser un número entero.");
        }
     }
}
