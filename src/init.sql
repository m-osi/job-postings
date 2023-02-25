BEGIN;

SET client_encoding = 'UTF8';

CREATE TABLE offers (
    id bigserial PRIMARY KEY,
    title text NOT NULL,
    street text,
    city text,
    country_code varchar(3),
    address_text text,
    marker_icon text,
    workplace_type text,
    company_name text NOT NULL,
    company_url text,
    company_size text,
    experience_level text,
    latitude numeric(13,10),
    longitude numeric(13,10),
    published_at timestamp NOT NULL,
    remote_interview boolean,
    open_to_hire_ukrainians boolean,
    display_offer boolean,
    remote boolean,
    way_of_apply text,
    type text,
    salary_from numeric(10,1),
    salary_to numeric(10,1),
    salary_currency varchar(3),
    name text,
    level integer
);

COMMIT;