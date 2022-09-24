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

