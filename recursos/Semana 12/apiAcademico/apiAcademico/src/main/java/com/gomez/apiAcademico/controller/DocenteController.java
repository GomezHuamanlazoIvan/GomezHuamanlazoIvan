package com.gomez.apiAcademico.controller;

import com.gomez.apiAcademico.model.Docente;
import com.gomez.apiAcademico.service.DocenteService;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/docentes")
public class DocenteController {

    @Autowired
    private DocenteService docenteService;

    @GetMapping
    public List<Docente> listarTodos() {
        return docenteService.listarTodos();
    }

    @GetMapping("/{id}")
    public Docente obtenerPorId(@PathVariable Long id) {
        return docenteService.obtenerPorId(id)
                .orElseThrow(() -> new RuntimeException("Docente no encontrado"));
    }

    @PostMapping
    public Docente crearDocente(@Valid @RequestBody Docente docente) {
        return docenteService.guardar(docente);
    }

    @PutMapping("/{id}")
    public Docente actualizar(@PathVariable Long id, @Valid @RequestBody Docente docente) {
        docenteService.obtenerPorId(id)
                .orElseThrow(() -> new RuntimeException("Docente no encontrado"));
        docente.setIdDocente(id);
        return docenteService.guardar(docente);
    }

    @DeleteMapping("/{id}")
    public void eliminar(@PathVariable Long id) {
        docenteService.eliminar(id);
    }

    @GetMapping("/ciudad/{ciudad}")
    public List<Docente> listarPorCiudad(@PathVariable String ciudad) {
        return docenteService.listarPorCiudad(ciudad);
    }

    @GetMapping("/experiencia/{anios}")
    public List<Docente> listarPorExperiencia(@PathVariable int anios) {
        return docenteService.listarPorExperiencia(anios);
    }

    @GetMapping("/edad-promedio")
    public Double edadPromedio() {
        return docenteService.edadPromedio();
    }

    @GetMapping(params = {"page", "size"})
    public Page<Docente> listarPaginado(@RequestParam int page, @RequestParam int size) {
        return docenteService.listarPaginado(PageRequest.of(page, size));
    }
}
