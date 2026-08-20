-- Analyst review queries for the synthetic crypto risk dashboard.
-- Run after: python3 risk_pipeline.py
-- Database: crypto-risk-dashboard/risk_cases.sqlite

-- 1. Highest priority cases for manual review.
select
  tx_id,
  user_id,
  asset,
  amount_usd,
  country,
  risk_score,
  typology,
  reasons,
  reviewer_note
from risk_cases
order by risk_score desc, amount_usd desc
limit 20;

-- 2. KRI summary by typology.
select
  typology,
  count(*) as cases,
  round(avg(risk_score), 1) as avg_risk_score,
  round(sum(amount_usd), 2) as total_value_usd
from risk_cases
group by typology
order by cases desc, avg_risk_score desc;

-- 3. High-value outflows by asset.
select
  asset,
  count(*) as cases,
  round(sum(amount_usd), 2) as total_value_usd,
  round(avg(risk_score), 1) as avg_risk_score
from risk_cases
where typology = 'high_value_outflow'
group by asset
order by total_value_usd desc;

-- 4. Cases that need reviewer attention because multiple signals appear together.
select
  tx_id,
  user_id,
  risk_score,
  typology,
  reasons,
  reviewer_note
from risk_cases
where reasons like '%,%'
order by risk_score desc;

-- 5. Reviewer workload by user.
select
  user_id,
  count(*) as review_cases,
  max(risk_score) as max_score,
  round(sum(amount_usd), 2) as review_value_usd
from risk_cases
where risk_score >= 35
group by user_id
order by review_cases desc, max_score desc, review_value_usd desc;

