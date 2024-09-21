--
-- PostgreSQL database dump
--

-- Dumped from database version 14.11 (Ubuntu 14.11-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.11 (Ubuntu 14.11-0ubuntu0.22.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: account; Type: TABLE; Schema: public; Owner: yelaco
--

CREATE TABLE public.account (
    id integer NOT NULL,
    name character varying(16),
    balance integer,
    groupid integer
);


ALTER TABLE public.account OWNER TO yelaco;

--
-- Name: account_id_seq; Type: SEQUENCE; Schema: public; Owner: yelaco
--

CREATE SEQUENCE public.account_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_id_seq OWNER TO yelaco;

--
-- Name: account_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: yelaco
--

ALTER SEQUENCE public.account_id_seq OWNED BY public.account.id;


--
-- Name: account id; Type: DEFAULT; Schema: public; Owner: yelaco
--

ALTER TABLE ONLY public.account ALTER COLUMN id SET DEFAULT nextval('public.account_id_seq'::regclass);


--
-- Data for Name: account; Type: TABLE DATA; Schema: public; Owner: yelaco
--

COPY public.account (id, name, balance, groupid) FROM stdin;
1	An	10	1
2	Binh	15	1
3	Cuong	20	1
4	Lam	12	2
5	Vinh	9	2
6	Dzung	20	1
7	Tri	21	1
8	Thanh	22	1
9	Tuan	19	3
10	Mai	25	3
11	Tram	25	2
12	Hang	25	1
13	Lan	25	2
\.


--
-- Name: account_id_seq; Type: SEQUENCE SET; Schema: public; Owner: yelaco
--

SELECT pg_catalog.setval('public.account_id_seq', 13, true);


--
-- PostgreSQL database dump complete
--

