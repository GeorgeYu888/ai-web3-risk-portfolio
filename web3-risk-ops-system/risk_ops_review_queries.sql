-- Practical review queries for the Web3 risk operations system.
-- Run after: python3 web3_risk_ops_pipeline.py

.headers on
.mode column

select scenario, count(*) as cases, round(avg(risk_score), 1) as avg_score
from case_queue
group by scenario
order by cases desc;

select priority, count(*) as cases, round(sum(amount_usd), 2) as value_usd
from case_queue
group by priority
order by case priority
  when 'critical' then 1
  when 'high' then 2
  when 'medium' then 3
  else 4
end;

select case_id, customer_segment, scenario, priority, risk_score, amount_usd, assigned_queue, reviewer_note
from case_queue
where priority in ('critical', 'high')
order by risk_score desc, amount_usd desc
limit 20;

select customer_segment, scenario, count(*) as cases, round(avg(risk_score), 1) as avg_score
from case_queue
group by customer_segment, scenario
having count(*) >= 2
order by avg_score desc, cases desc;

select action, count(*) as cases
from case_queue
group by action
order by cases desc;
