SELECT event_date, currency, SUM(revenue_cents) AS revenue_cents,
       SUM(cost_cents) AS cost_cents,
       CASE WHEN SUM(cost_cents) = 0 THEN NULL
            ELSE CAST(SUM(revenue_cents) AS DOUBLE) / SUM(cost_cents) END AS roas
FROM gold_roas
GROUP BY event_date, currency;

SELECT * FROM gold_roas WHERE app_id = 'a' AND campaign_id = 'A';

SELECT g.*, d.campaign_name
FROM gold_roas g JOIN campaign_dim d
  USING (source_system, app_id, campaign_id);

SELECT campaign_id, currency, SUM(revenue_cents) AS revenue_cents,
       SUM(cost_cents) AS cost_cents
FROM gold_roas WHERE event_date = DATE '2026-10-01'
GROUP BY campaign_id, currency ORDER BY revenue_cents DESC;
