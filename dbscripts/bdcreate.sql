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

CREATE TABLE profesional
(
 id_profesional   NOT NULL,
 nombre          varchar(50) NOT NULL,
 id_user          NOT NULL,
 apellidos       varchar(50) NOT NULL,
 codigo_empleado int NOT NULL,
 facultad        text NOT NULL,
 CONSTRAINT PK_1 PRIMARY KEY ( id_profesional ),
 CONSTRAINT FK_4 FOREIGN KEY ( id_user ) REFERENCES "user" ( id_user )
);

CREATE INDEX FK_2 ON profesional
(
 id_user
);

CREATE TABLE rol
(
 id_rol      NOT NULL,
 nombre_rol text NOT NULL,
 id_user     NOT NULL,
 CONSTRAINT PK_1 PRIMARY KEY ( id_rol ),
 CONSTRAINT FK_6_1 FOREIGN KEY ( id_user ) REFERENCES "user" ( id_user )
);

CREATE INDEX FK_2 ON rol
(
 id_user
);

CREATE TABLE status_cita
(
 id_status_cita  NOT NULL,
 status_cita    text NULL,
 id_cita         NOT NULL,
 asistencia     text NULL,
 CONSTRAINT PK_1 PRIMARY KEY ( id_status_cita ),
 CONSTRAINT FK_6 FOREIGN KEY ( id_cita ) REFERENCES cita ( id_cita )
);

CREATE INDEX FK_2 ON status_cita
(
 id_cita
);

CREATE TABLE "user"
(
 id_user   NOT NULL,
 email    varchar(50) NOT NULL,
 password varchar(50) NOT NULL,
 CONSTRAINT PK_1 PRIMARY KEY ( id_user )
);

