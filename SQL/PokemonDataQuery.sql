USE pokemondata;

-- whole database
SELECT *
FROM pokemon p
inner Join pokemontypes pt
on p.pokemonId = pt.pokemonId
join types t
on t.typeId = pt.typeId;

-- pokemon types
-- how are the types disturbed

-- the number of pokemon per type
SELECT t.pokemonType type, count(distinct p.pokemonId) amount
FROM pokemon p
inner Join pokemontypes pt
on p.pokemonId = pt.pokemonId
join types t
on t.typeId = pt.typeId
group by t.pokemonType;


-- the most popular type pairing apart from single typing 
SELECT  t1.pokemonType type1, t2.pokemonType type2, count(p1.typeId) amount
from pokemontypes p1
join pokemontypes p2
on p1.pokemonId = p2.pokemonId and p1.typeId > p2.typeId
join types t1
on t1.typeId = p1.typeId
join types t2
on t2.typeId = p2.typeId
group by p1.typeId, p2.typeId
order by amount desc;


-- Height and weight
-- How are height and weight disturbed among Pokémon
-- scatter graph of H and W
Select height, weight 
from pokemon;


-- w/h based on type
-- can do scatter or 2 bar charts
with cte as(
	SELECT t.pokemonType, pt.pokemonId
	FROM types t
	join pokemontypes pt
	on t.typeId = pt.typeId
    )
select ROUND(avg(p.height),2) mean_height, ROUND(avg(p.weight),2) mean_weight, c.pokemonType
from pokemon p
join cte c
on p.pokemonId = c.pokemonId
group by c.pokemonType
order by mean_height Desc, mean_weight Desc;

