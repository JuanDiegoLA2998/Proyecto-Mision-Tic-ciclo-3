CREATE TABLE estudiante
(
 id_estudiante      NOT NULL,
 nombre            varchar(50) NOT NULL,
 id_user            NOT NULL,
 apellidos         varchar(50) NOT NULL,
 codigo_estudiante int NOT NULL,
 fecha_nacimiento  timestamp NOT NULL,
 carrera           text NOT NULL,
 semestre          int NOT NULL,
 CONSTRAINT PK_1 PRIMARY KEY ( id_estudiante ),
 CONSTRAINT FK_5 FOREIGN KEY ( id_user ) REFERENCES "user" ( id_user )
);

CREATE INDEX FK_2 ON estudiante
(
 id_user
);