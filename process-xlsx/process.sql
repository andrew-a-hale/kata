with detect_target_tables as (
  select
    *,
    concat_ws(',', *columns(*)) as row_concat,
    case
      when row_concat ilike '%a,%,g%' then 2
      when row_concat ilike '%a,%e%' then 1
      else 0
    end as target_groups,
    sum(target_groups = 1) over (partition by filepath, sheet order by "row") as row_group_1,
    sum(target_groups = 2) over (partition by filepath, sheet order by "row") as row_group_2
  from 'parquet_output/final.parquet'
),

filter as (
  select * exclude (row_concat)
  from detect_target_tables
  where A is not null and try_cast(A as int) is not null
)

-- target_group: 1
select A as id, E as name
from filter
where row_group_1 > 0 and E is not null
-- target_group: 2
union all select A, G
from filter
where row_group_2 > 0 and E is not null;
