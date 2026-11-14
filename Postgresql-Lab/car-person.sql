create table car(
    id BIGSERIAL NOT NULL PRIMARY KEY,
    make VARCHAR(100) NOT NULL,
    model VARCHAR(100) NOT NULL,
    price NUMERIC(19, 2) NOT NULL
);




create table person (
	id BIGSERIAL NOT NULL PRIMARY KEY,
	first_name VARCHAR(100) NOT NULL,
	last_name VARCHAR(100) NOT NULL,
	gender VARCHAR(7) NOT NULL,
	email VARCHAR(100),
	date_of_birth DATE NOT NULL,
	country_of_birth VARCHAR(100) NOT NULL,
	car_id BIGINT REFERENCES car(id),
    UNIQUE(car_id)
);
insert into person ( first_name, last_name, gender, email, date_of_birth, country_of_birth) values ('Violet', 'Dudenie', 'Female', 'vdudenie0@mail.ru', '1/8/2026', 'Georgia');
insert into person (first_name, last_name, gender, email, date_of_birth, country_of_birth) values ('Inesita', 'Roskams', 'Female', 'iroskams1@joomla.org', '10/19/2026', 'Saint Lucia');
insert into person (first_name, last_name, gender, email, date_of_birth, country_of_birth) values ('Katrine', 'Sterricks', 'Female', 'ksterricks2@dailymail.co.uk', '2/5/2026', 'Peru');

insert into car(make , model, price) values ('Toyota', 'Camry', 24000.00);
insert into car(make , model, price) values ('Honda', 'Civic', 22000.00);
