SET client_encoding = 'UTF8';

CREATE TABLE activity (
    id serial PRIMARY KEY,
    description text NOT NULL,
    room smallint,
    weekday smallint,
    weektime time without time zone NOT NULL,
    CONSTRAINT u_act_constraint UNIQUE (description, room, weekday, weektime)
);

CREATE TABLE associate (
    id serial PRIMARY KEY,
    fullname text UNIQUE NOT NULL,
    nickname text,
    rg text,
    cpf text,
    maritalstatus smallint,
    email text,
    streetaddress text,
    complement text,
    district text,
    province smallint,
    city text,
    cep text,
    resphone text,
    comphone text,
    privphone text,
    debt money DEFAULT 0
);

CREATE TABLE associate_in_activity (
    id_associate integer NOT NULL REFERENCES associate(id),
    id_activity integer NOT NULL REFERENCES activity(id),
    CONSTRAINT associate_in_activity_pkey PRIMARY KEY (id_associate, id_activity)
);

CREATE TABLE users (
    username text PRIMARY KEY,
    password text NOT NULL,
    access integer,
    CONSTRAINT empty_str_chk CHECK (((username)::text <> ''::text))
);

CREATE TABLE author (
	id serial PRIMARY KEY,
	name text NOT NULL
);

CREATE TABLE s_author (
	id serial PRIMARY KEY,
	name text NOT NULL
);

CREATE TABLE subject (
	id serial PRIMARY KEY,
	name text NOT NULL
);

CREATE TABLE book (
	id serial PRIMARY KEY,
	image bytea,
	title text NOT NULL,
	author_id integer REFERENCES author(id),
	s_author_id integer REFERENCES s_author(id),
	description text,
	price money DEFAULT 0,
	stock integer DEFAULT 0,
	barcode text UNIQUE
);

CREATE TABLE book_in_subject(
	book_id integer REFERENCES book(id),
	subject_id integer REFERENCES subject(id),
	CONSTRAINT book_in_subject_pkey PRIMARY KEY (book_id, subject_id)
);

CREATE TABLE history (
    id serial PRIMARY KEY,
    type text,
    description text,
    date timestamp without time zone,
    username text REFERENCES users(username)
);
