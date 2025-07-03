package microservicio_notas.m_notas.model;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.validation.constraints.NotNull;

@Entity
public class ActividadTema {
    @Id
    private Integer id;

    @NotNull
    private String tema;

    @Column(name = "glosa_otro")
    private String glosaOtro;

    @Column(name = "actividad_id")
    private Integer actividadId;

    public Integer getId() {
        return id;
    }
    
    public String getTema() {
        return tema;
    }

    public String getGlosaOtro() {
        return glosaOtro;
    }

    public Integer getActividadId() {
        return actividadId;
    }


}
