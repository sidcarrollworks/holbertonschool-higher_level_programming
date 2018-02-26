-- script that creates multiple rows in table
create table if not exists second_table (id INT, name VARCHAR(256), score INT);
insert into `second_table` (`id`, `name`, `score`) VALUES (1, 'John', 10);
insert into `second_table` (`id`, `name`, `score`) VALUES (2, 'Alex', 3);
insert into `second_table` (`id`, `name`, `score`) VALUES (3, 'Bob', 14);
insert into `second_table` (`id`, `name`, `score`) VALUES (4, 'George', 8);
