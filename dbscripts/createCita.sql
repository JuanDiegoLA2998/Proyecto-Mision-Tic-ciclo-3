CREATE TABLE cita
(
 id_cita         NOT NULL,
 id_estudiante   NOT NULL,
 id_profesional  NOT NULL,
 fecha_inicio   timestamp NOT NULL,
 fecha_final    timestamp NOT NULL,
 fecha          timestamp NOT NULL,
 comentario     text NOT NULL,
 CONSTRAINT PK_1 PRIMARY KEY ( id_cita ),
 CONSTRAINT FK_1 FOREIGN KEY ( id_estudiante ) REFERENCES estudiante ( id_estudiante ),
 CONSTRAINT FK_2 FOREIGN KEY ( id_profesional ) REFERENCES profesional ( id_profesional )
);

CREATE INDEX FK_2 ON cita
(
 id_estudiante
);

CREATE INDEX FK_3 ON cita
(
 id_profesional
);