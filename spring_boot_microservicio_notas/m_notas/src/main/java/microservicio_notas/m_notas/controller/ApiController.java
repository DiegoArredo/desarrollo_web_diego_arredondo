package microservicio_notas.m_notas.controller;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import microservicio_notas.m_notas.services.ApiService;

import microservicio_notas.m_notas.model.Actividad;
import microservicio_notas.m_notas.model.ActividadTema;
import microservicio_notas.m_notas.model.Nota;

import java.util.Map;


@RestController
public class ApiController {
    private final ApiService apiService;
    public ApiController(ApiService apiService) {
        this.apiService = apiService;
    }
    @CrossOrigin(origins = "*")
    @GetMapping("/actividad_notas")
    //Se define Map<String, Collection>, usé collection por que se usa arrayList y List y no sabia como definir bien los tipos.
    public Map<String, Collection> getActividadNotas() {

        // Obtener todas las actividades.
        List<Actividad> actividades = apiService.getAllActividades();
        //Aca para inicializar las listas de notas y actividadTema
        ArrayList<List<Nota>> notasPorActividad = new ArrayList<>();
        ArrayList<ActividadTema> actividadTemas = new ArrayList<>();

        // Se recorre cada actividad para llamar apiService y ocupar el repositorio de notas y actividadTema
        // Para obtener las notas y el tema de cada actividad usando su id.
        for (Actividad actividad : actividades) {
            List<Nota> notas = apiService.getAllNotasById(actividad.getId().intValue());
            notasPorActividad.add(notas);
            ActividadTema actividadTema = apiService.getTemaByActividadId(actividad.getId().intValue());
            actividadTemas.add(actividadTema);
        }
        // Se retorna un Map, imitando al Jsonify en Python/flask.
        return Map.of("actividades", actividades ,
                      "notas", notasPorActividad,
                      "actividadTemas", actividadTemas);
    }
    
    @PostMapping("/actividad_notas")
    public String postActividadNotas(
     @RequestParam Integer actividadId,
     @RequestParam Integer notaId) throws Exception {
        apiService.addActividadNota(actividadId, notaId);
        return "Nota agergada correctamente";
    }
}
