
/* ------ Nombre de la base de datos -------- */


/* --------------------------------- */
/* ------------ bd_blumer -------------- */
/* --------------------------------- */


/* ------- Creacion esquema ------- */

-- DROP SCHEMA public;

CREATE SCHEMA public AUTHORIZATION pg_database_owner;



/* ------- Secuencias ------- */

-- DROP SEQUENCE public.comments_id_seq;

CREATE SEQUENCE public.comments_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;
-- DROP SEQUENCE public.posts_id_seq;

CREATE SEQUENCE public.posts_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;


/* ------- Tabla Posts ------- */

-- public.posts definition

-- Drop table

-- DROP TABLE public.posts;

CREATE TABLE public.posts (
	id serial4 NOT NULL,
	description varchar NULL,
	video_url varchar NULL,
	created_at varchar NULL,
	CONSTRAINT posts_pkey PRIMARY KEY (id)
);



/*------- Tabla Comments ------- */


-- public."comments" definition

-- Drop table

-- DROP TABLE public."comments";

CREATE TABLE public."comments" (
	id serial4 NOT NULL,
	description varchar NULL,
	created_at varchar NULL,
	post_id int4 NOT NULL,
	CONSTRAINT comments_pkey PRIMARY KEY (id),
	CONSTRAINT fk_post_comments FOREIGN KEY (post_id) REFERENCES public.posts(id)
);
