WITH revenue AS (
  SELECT source_system, app_id, event_date, campaign_id, currency,
         SUM(amount_cents) AS revenue_cents, COUNT(*) AS events
  FROM silver_events
  GROUP BY source_system, app_id, event_date, campaign_id, currency
)
SELECT c.source_system, c.app_id, c.event_date, c.campaign_id, c.currency,
       COALESCE(r.revenue_cents, 0) AS revenue_cents, c.cost_cents,
       COALESCE(r.events, 0) AS events,
       CASE WHEN c.cost_cents = 0 THEN NULL
            ELSE CAST(COALESCE(r.revenue_cents, 0) AS DOUBLE) / c.cost_cents END AS roas
FROM costs c
LEFT JOIN revenue r USING (source_system, app_id, event_date, campaign_id, currency)
