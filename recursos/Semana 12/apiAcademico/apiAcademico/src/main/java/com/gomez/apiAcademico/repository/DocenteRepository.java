package com.gomez.apiAcademico.repository;

import com.gomez.apiAcademico.model.Docente;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import java.util.List;

public interface DocenteRepository extends JpaRepository<Docente, Long> {
    List<Docente> findByCiuDocente(String ciuDocente);
    List<Docente> findByTiempoServicioGreaterThanEqual(int anios);

    @Query("SELECT AVG(DATEDIFF(CURRENT_DATE, d.fecNacimiento)/365.25) FROM Docente d")
    Double findEdadPromedio();
}

