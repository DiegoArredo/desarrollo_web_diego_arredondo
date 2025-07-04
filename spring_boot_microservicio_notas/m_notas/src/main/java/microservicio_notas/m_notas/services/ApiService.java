package microservicio_notas.m_notas.services;

import org.springframework.stereotype.Service;


import microservicio_notas.m_notas.model.ActividadRepository;
import microservicio_notas.m_notas.model.ActividadTemaRepository;
import microservicio_notas.m_notas.model.NotaRepository;

import microservicio_notas.m_notas.model.Actividad;
import microservicio_notas.m_notas.model.ActividadTema;
import microservicio_notas.m_notas.model.Nota;

import java.util.List;


@Service
public class ApiService {
    private final ActividadRepository actividadRepository;
    private final ActividadTemaRepository actividadTemaRepository;
    private final NotaRepository notaRepository;

    public ApiService(ActividadRepository actividadRepository, ActividadTemaRepository actividadTemaRepository, NotaRepository notaRepository) {
        this.actividadRepository = actividadRepository;
        this.actividadTemaRepository = actividadTemaRepository;
        this.notaRepository = notaRepository;
    }

    // Obetener todas las actividades
    public List<Actividad> getAllActividades() {
        return actividadRepository.findAll();
    }

    // Obtener el tema de una actividad por su id
    public ActividadTema getTemaByActividadId(Integer actividad_id) {
        return actividadTemaRepository.findTemaByActividadId(actividad_id);
    }

    
    public List<Nota> getAllNotasById(Integer actividadId) {
        return notaRepository.findNotaByActividadId(actividadId);
    }

    public void addActividadNota(Integer actividadId, Integer notaValue) {
        
        try {
            // Validar que la actividad exista y la fecha de inicio sea menor a la fecha actual
            Actividad actividad = actividadRepository.findActividadById(actividadId.longValue());
            if (actividad == null) {
                throw new IllegalArgumentException("La actividad con el ID proporcionado no existe.");
            };
            if (actividad.getDiaHoraInicio().isAfter(java.time.LocalDateTime.now())) {
                throw new IllegalArgumentException("La fecha de inicio de la actividad debe ser menor a la fecha actual.");
            };
            Nota nota = new Nota(actividadId, notaValue);
            nota.validateNota(); // Validar con la funcion que esta en la clase Nota!
            notaRepository.save(nota);
            System.out.println("Nota agregada correctamente!");
        } catch (IllegalArgumentException e) {
            throw new IllegalArgumentException("Error al agregar la nota: " + e.getMessage());
        }

    }
}
