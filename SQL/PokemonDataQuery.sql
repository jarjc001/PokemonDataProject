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
group by t.pokemonType
order by amount desc;


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
-- avg w/h for each type
-- can do scatter or 2 bar charts
-- with counting part for each part 
with cte as(
	SELECT t.pokemonType, pt.pokemonId
	FROM types t
	join pokemontypes pt
	on t.typeId = pt.typeId
    )
select ROUND(avg(p.height),2) mean_height, ROUND(STD(p.height),2) sd_height,
ROUND(avg(p.weight),2) mean_weight, ROUND(STD(p.weight),2) sd_weight,
count(*) counting,
c.pokemonType
from pokemon p
join cte c
on p.pokemonId = c.pokemonId
group by c.pokemonType
order by mean_height Desc, mean_weight Desc;


-- remove top and bottom 5%
-- for heights 

-- edit and check this 

with cte as(
	SELECT t.pokemonType, pt.pokemonId
	FROM types t
	join pokemontypes pt
	on t.typeId = pt.typeId
    )
select ROUND(avg(p.height),2) mean_height, ROUND(STD(p.height),2) sd_height,
c.pokemonType
from 
(select 
	*, NTILE(20) OVER (order by height) as Buckets
    from pokemon
) p
join cte c
on p.pokemonId = c.pokemonId
where p.Buckets between 2 And 19
group by c.pokemonType
order by mean_height Desc;

-- for weights 

-- edit and check this 

with cte as(
	SELECT t.pokemonType, pt.pokemonId
	FROM types t
	join pokemontypes pt
	on t.typeId = pt.typeId
    )
select ROUND(avg(p.weight),2) mean_weight, ROUND(STD(p.weight),2) sd_weight,
count(*) counting,
c.pokemonType
from 
(select 
	*, NTILE(20) OVER (order by weight) as Buckets
    from pokemon
) p
join cte c
on p.pokemonId = c.pokemonId
where p.Buckets between 2 And 19
group by c.pokemonType
order by mean_weight Desc;




-- w and h for a certian type
-- either do the ones with the greatest number of pokemon
-- or do ones with largest and smallest sd
with cte as(
	SELECT t.pokemonType, pt.pokemonId
	FROM types t
	join pokemontypes pt
	on t.typeId = pt.typeId
    )
select p.height , p.weight, c.pokemonType
from pokemon p
join cte c
on p.pokemonId = c.pokemonId
where  c.pokemonType = "fire"
order by p.height Desc,  p.weight Desc;


-- stats

-- overall stats of each pokemon
select hp, attack,
 defense, special_attack,
 special_defense, speed, 
 (attack+defense) as 'physical_stats',
 (special_attack+special_defense) as 'special_stats',
 (hp+attack+defense+special_attack+special_defense+speed) as 'overall_stats'
from pokemon;

-- the mean and std of stats for each pokemon type
WITH cte AS(
	SELECT pt.pokemonId, t.pokemonType
    from types t 
    join pokemontypes pt
    on pt.typeId = t.typeId
),
cte2 as(
select
pokemonId,
 (attack+defense) as 'physical_stats',
 (special_attack+special_defense) as 'special_stats',
 (hp+attack+defense+special_attack+special_defense+speed) as 'overall_stats'
from pokemon)
SELECT c.pokemonType,
ROUND(avg(p.hp),2) mean_hp, ROUND(STD(p.hp),2) sd_hp,
ROUND(avg(p.attack),2) mean_attack, ROUND(STD(p.attack),2) sd_attack,
ROUND(avg(p.defense),2) mean_defense, ROUND(STD(p.defense),2) sd_defense,
ROUND(avg(p.special_attack),2) mean_special_attack, ROUND(STD(p.special_attack),2) sd_special_attack,
ROUND(avg(p.special_defense),2) mean_special_defense, ROUND(STD(p.special_defense),2) sd_special_defense,
ROUND(avg(p.speed),2) mean_speed, ROUND(STD(p.speed),2) sd_speed,
ROUND(avg(c2.physical_stats),2) mean_physical_stats, ROUND(STD(c2.physical_stats),2) sd_physical_stats,
ROUND(avg(c2.special_stats),2) mean_special_stats, ROUND(STD(c2.special_stats),2) sd_special_stats,
ROUND(avg(c2.overall_stats),2) mean_overall_stats, ROUND(STD(c2.overall_stats),2) sd_overall_stats
from pokemon p
join cte c
on c.pokemonId = p.pokemonId
join cte2 c2
on c2.pokemonId = p.pokemonId
group by c.pokemonType
order by mean_hp Desc;






