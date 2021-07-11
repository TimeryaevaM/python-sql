with grouped_dates as (
    select
        subsid,
        dateid,
        dateid - (row_number() over (partition by subsid order by dateid))::integer as date_group
    from sql_csv)
select
    subsid as SUBS_ID,
    min(dateid) as START_DTTM,
    max(dateid) as END_DTTM
from grouped_dates
group by subsid, date_group
order by SUBS_ID, START_DTTM, END_DTTM;