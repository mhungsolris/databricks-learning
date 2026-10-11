WITH ranked AS (
  SELECT *, ROW_NUMBER() OVER (
    PARTITION BY source_system, app_id, event_id
    ORDER BY revision DESC, delivery_id DESC
  ) AS rn
  FROM raw_events
)
SELECT source_system, app_id, event_id, revision, campaign_id,
       event_date, currency, amount_cents
FROM ranked
WHERE rn = 1
