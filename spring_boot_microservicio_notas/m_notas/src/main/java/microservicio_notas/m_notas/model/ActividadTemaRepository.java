package microservicio_notas.m_notas.model;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ActividadTemaRepository extends JpaRepository<ActividadTema, Integer> {
    public ActividadTema findTemaByActividadId(Integer actividad_id);

}
