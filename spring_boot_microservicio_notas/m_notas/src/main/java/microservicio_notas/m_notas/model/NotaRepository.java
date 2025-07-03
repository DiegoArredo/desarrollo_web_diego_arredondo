package microservicio_notas.m_notas.model;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import java.util.List;

@Repository
public interface NotaRepository extends JpaRepository<Nota, Long> {
    public List<Nota> findNotaByActividadId(Integer actividadId);

}
