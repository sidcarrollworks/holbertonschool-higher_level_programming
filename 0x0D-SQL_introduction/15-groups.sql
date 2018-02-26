-- lists number of records with the same score
select score, count(score) as number from second_table
group by score desc;
