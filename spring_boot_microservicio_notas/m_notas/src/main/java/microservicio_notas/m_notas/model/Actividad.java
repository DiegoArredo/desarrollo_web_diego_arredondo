package microservicio_notas.m_notas.model;

import java.time.LocalDateTime;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.validation.constraints.NotNull;

@Entity
public class Actividad {
    @Id
    private Long id;

    @NotNull
    private String nombre;


    private String sector;

    @NotNull
    @Column(name = "dia_hora_inicio")  
    private LocalDateTime diaHoraInicio;


    // Esto retornará al llamar una funcion al @repository pidiendo una Actividad.
    public Long getId() {
        return id;
    }
    public String getNombre() {
        return nombre;
    }
    public String getSector() {
        return sector;
    }
    public LocalDateTime getDiaHoraInicio() {
        return diaHoraInicio;
    }
   
    

}
