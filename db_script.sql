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
    debt numeric(15,2) DEFAULT 0.00,
    active boolean
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
	name text UNIQUE NOT NULL
);

CREATE TABLE s_author (
	id serial PRIMARY KEY,
	name text UNIQUE NOT NULL
);

CREATE TABLE publisher (
	id serial PRIMARY KEY,
	name text UNIQUE NOT NULL
);

CREATE TABLE subject (
	id serial PRIMARY KEY,
	name text UNIQUE NOT NULL
);

CREATE TABLE book (
	id serial PRIMARY KEY,
  barcode text UNIQUE,
  title text NOT NULL,
	author_id integer REFERENCES author(id),
	s_author_id integer REFERENCES s_author(id),
  publisher_id integer REFERENCES publisher(id),
  year numeric(4,0),
  price numeric(6,2) DEFAULT 0.00,
  description text,
  stock integer DEFAULT 0,
  image bytea,
  availability smallint NOT NULL DEFAULT 0
);

CREATE TABLE book_in_subject(
	book_id integer REFERENCES book(id),
	subject_id integer REFERENCES subject(id),
	CONSTRAINT book_in_subject_pkey PRIMARY KEY (book_id, subject_id)
);

CREATE TABLE p_order(
  id serial PRIMARY KEY,
  associate_id integer REFERENCES associate(id),
  date timestamp without time zone NOT NULL DEFAULT now(),
  obs text,
  -- keeping this field stored for better performance (instead of calculating on the fly)
  total numeric(6,2) NOT NULL DEFAULT 0.00
);
-- client's rule: don't keep a reference to the product itself
CREATE TABLE p_order_item(
  id serial PRIMARY KEY,
  p_order_id integer REFERENCES p_order(id) NOT NULL,
  p_name text NOT NULL,
  price numeric(6,2) NOT NULL,
  quantity smallint NOT NULL DEFAULT 1
);

CREATE TABLE history (
    id serial PRIMARY KEY,    
    type text,
    id_ref integer,
    description text,
    date timestamp without time zone NOT NULL DEFAULT now(),
    username text REFERENCES users(username) NOT NULL
);
