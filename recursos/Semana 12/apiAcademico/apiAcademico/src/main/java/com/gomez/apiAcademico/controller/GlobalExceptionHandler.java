package com.gomez.apiAcademico.controller;

import org.springframework.http.HttpStatus;
import org.springframework.http.converter.HttpMessageNotReadableException;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.Map;

@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(MethodArgumentNotValidException.class)
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    public Map<String, String> handleValidationExceptions(MethodArgumentNotValidException ex) {
        Map<String, String> errors = new HashMap<>();
        ex.getBindingResult().getFieldErrors().forEach(error ->
                errors.put(error.getField(), error.getDefaultMessage()));
        return errors;
    }

    @ExceptionHandler(RuntimeException.class)
    @ResponseStatus(HttpStatus.NOT_FOUND)
    public Map<String, String> handleRuntimeException(RuntimeException ex) {
        Map<String, String> error = new HashMap<>();
        error.put("error", ex.getMessage());
        return error;
    }

    @ExceptionHandler(HttpMessageNotReadableException.class)
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    public Map<String, String> handleHttpMessageNotReadable(HttpMessageNotReadableException ex) {
        Map<String, String> error = new HashMap<>();
        String mensaje = ex.getMostSpecificCause().getMessage();
        if (mensaje != null && mensaje.contains("LocalDate")) {
            error.put("fecNacimiento", "Formato de datos inválido. Verifica el formato de la fecha (debe ser yyyy-MM-dd).");
        } else if (mensaje != null && (mensaje.contains("java.lang.Integer") || mensaje.contains("Integer") || mensaje.contains("from String \"\""))) {
            error.put("tiempoServicio", "El campo 'tiempoServicio' es obligatorio, debe ser un número entero no negativo y no puede estar vacío ni contener texto.");
        } else if (mensaje != null && mensaje.contains("null") && mensaje.contains("Integer")) {
            error.put("tiempoServicio", "El campo 'tiempoServicio' es obligatorio y no puede estar vacío.");
        } else {
            error.put("error", "Error en los datos enviados. Verifica los tipos y valores de todos los campos.");
        }
        return error;
    }
}
