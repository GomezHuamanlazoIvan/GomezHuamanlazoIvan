package com.gomez.apiAcademico.validation;

import jakarta.validation.Constraint;
import jakarta.validation.Payload;
import java.lang.annotation.Documented;
import java.lang.annotation.Retention;
import java.lang.annotation.Target;

import static java.lang.annotation.ElementType.FIELD;
import static java.lang.annotation.RetentionPolicy.RUNTIME;

@Documented
@Constraint(validatedBy = FechaValidaValidator.class)
@Target({ FIELD })
@Retention(RUNTIME)
public @interface FechaValida {
    String message() default "La fecha no es válida. El año debe ser mayor a 1900, el mes entre 1 y 12 y el día válido para el mes.";
    Class<?>[] groups() default {};
    Class<? extends Payload>[] payload() default {};
}

