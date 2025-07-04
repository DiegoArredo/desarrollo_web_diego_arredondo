package microservicio_notas.m_notas.controller;

import java.util.ArrayList;
import java.util.List;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
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
    // Se define Map<String, Object>, Object para encampsular el tipo List y el tipo ArrayList
    public Map<String, Object> getActividadNotas() {

        // Obtener todas las actividades que tienen fecha de inicio anterior a la actual.

        List<Actividad> actividades = apiService.getAllActividadesAlreadyStarted();
        // Aca para inicializar las listas de notas y actividadTema
        ArrayList<List<Nota>> notasPorActividad = new ArrayList<>();
        ArrayList<ActividadTema> actividadTemas = new ArrayList<>();

        // Se recorre cada actividad para llamar apiService y ocupar el repositorio de
        // notas y actividadTema
        // Para obtener las notas y el tema de cada actividad usando su id.
        for (Actividad actividad : actividades) {
            List<Nota> notas = apiService.getAllNotasById(actividad.getId().intValue());
            notasPorActividad.add(notas);
            ActividadTema actividadTema = apiService.getTemaByActividadId(actividad.getId().intValue());
            actividadTemas.add(actividadTema);
        }
        // Se retorna un Map, imitando al Jsonify en Python/flask.
        return Map.of("actividades", actividades,
                "notas", notasPorActividad,
                "actividadTemas", actividadTemas);
    }

    @CrossOrigin(origins = "*")
    @PostMapping("/actividad_notas")
    public Map<String, Object> postActividadNotas(
            @RequestBody Map<String, Integer> notaJsonMap) throws Exception {
        int actividadId = notaJsonMap.get("actividadId");
        int nota = notaJsonMap.get("nota");
        apiService.addActividadNota(actividadId, nota);
        return Map.of("message", "Nota agregada correctamente",
                "success", true);
    }
}
