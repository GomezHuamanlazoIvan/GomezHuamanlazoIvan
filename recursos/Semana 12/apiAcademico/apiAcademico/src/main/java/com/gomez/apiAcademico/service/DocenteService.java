package com.gomez.apiAcademico.service;

import com.gomez.apiAcademico.model.Docente;
import com.gomez.apiAcademico.repository.DocenteRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;
import java.util.List;
import java.util.Optional;

@Service
public class DocenteService {

    @Autowired
    private DocenteRepository docenteRepository;

    public List<Docente> listarTodos() {
        return docenteRepository.findAll();
    }

    public Optional<Docente> obtenerPorId(Long id) {
        return docenteRepository.findById(id);
    }

    public Docente guardar(Docente docente) {
        return docenteRepository.save(docente);
    }

    public void eliminar(Long id) {
        docenteRepository.deleteById(id);
    }

    public List<Docente> listarPorCiudad(String ciudad) {
        return docenteRepository.findByCiuDocente(ciudad);
    }

    public List<Docente> listarPorExperiencia(int anios) {
        return docenteRepository.findByTiempoServicioGreaterThanEqual(anios);
    }

    public Double edadPromedio() {
        return docenteRepository.findEdadPromedio();
    }

    public Page<Docente> listarPaginado(Pageable pageable) {
        return docenteRepository.findAll(pageable);
    }
}

