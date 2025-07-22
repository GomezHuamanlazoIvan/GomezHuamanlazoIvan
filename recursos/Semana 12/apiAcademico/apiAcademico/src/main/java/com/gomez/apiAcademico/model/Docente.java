package com.gomez.apiAcademico.model;

import jakarta.persistence.*;
import jakarta.validation.constraints.*;
import java.time.LocalDate;
import com.gomez.apiAcademico.validation.FechaValida;

@Entity
public class Docente {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long idDocente;

    @NotBlank(message = "El nombre no puede estar vacío ni solo contener espacios.")
    @Pattern(regexp = "^[^\\d]+$", message = "El nombre no puede contener números.")
    private String nomDocente;

    @NotBlank(message = "La dirección no puede estar vacía ni solo contener espacios.")
    private String dirDocente;

    @NotBlank(message = "La ciudad no puede estar vacía ni solo contener espacios.")
    @Pattern(regexp = "^[^\\d]+$", message = "La ciudad no puede contener números.")
    private String ciuDocente;

    @Email(message = "El email debe tener un formato válido.")
    @NotBlank(message = "El email no puede estar vacío.")
    private String emailDocente;

    @Past(message = "La fecha de nacimiento debe ser en el pasado.")
    @NotNull(message = "La fecha de nacimiento es obligatoria.")
    @FechaValida
    private LocalDate fecNacimiento;

    @NotNull(message = "El campo 'tiempoServicio' es obligatorio y debe ser un número entero no negativo.")
    @Min(value = 0, message = "El tiempo de servicio no puede ser negativo.")
    private Integer tiempoServicio;

    // Getters y Setters
    public Long getIdDocente() {
        return idDocente;
    }

    public void setIdDocente(Long idDocente) {
        this.idDocente = idDocente;
    }
    public String getNomDocente() {
        return nomDocente;
    }

    public void setNomDocente(String nomDocente) {
        this.nomDocente = nomDocente;
    }

    public String getDirDocente() {
        return dirDocente;
    }

    public void setDirDocente(String dirDocente) {
        this.dirDocente = dirDocente;
    }

    public String getCiuDocente() {
        return ciuDocente;
    }

    public void setCiuDocente(String ciuDocente) {
        this.ciuDocente = ciuDocente;
    }

    public String getEmailDocente() {
        return emailDocente;
    }

    public void setEmailDocente(String emailDocente) {
        this.emailDocente = emailDocente;
    }

    public LocalDate getFecNacimiento() {
        return fecNacimiento;
    }

    public void setFecNacimiento(LocalDate fecNacimiento) {
        this.fecNacimiento = fecNacimiento;
    }

    public Integer getTiempoServicio() {
        return tiempoServicio;
    }

    public void setTiempoServicio(Integer tiempoServicio) {
        this.tiempoServicio = tiempoServicio;
    }
}
