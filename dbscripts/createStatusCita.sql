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