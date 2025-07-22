package com.gomez.apiAcademico.validation;

import jakarta.validation.ConstraintValidator;
import jakarta.validation.ConstraintValidatorContext;
import java.time.LocalDate;

public class FechaValidaValidator implements ConstraintValidator<FechaValida, LocalDate> {
    @Override
    public boolean isValid(LocalDate value, ConstraintValidatorContext context) {
        if (value == null) return true; // @NotNull se encarga de la nulidad
        int year = value.getYear();
        int month = value.getMonthValue();
        int day = value.getDayOfMonth();
        if (year < 1900) return false;
        if (month < 1 || month > 12) return false;
        try {
            LocalDate.of(year, month, day);
        } catch (Exception e) {
            return false;
        }
        return true;
    }
}

