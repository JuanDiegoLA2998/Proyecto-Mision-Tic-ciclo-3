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
