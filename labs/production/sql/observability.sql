-- DATABRICKS WORKSPACE design-only queries. Check UC grants/table availability first.
SELECT statement_id, start_time, execution_status, total_duration_ms,
       execution_duration_ms, waiting_at_capacity_duration_ms, read_bytes
FROM system.query.history
WHERE start_time >= current_timestamp() - INTERVAL 1 DAY
ORDER BY start_time DESC
LIMIT 20;

-- Usage quantity has a unit/SKU; it is not currency or a complete invoice.
SELECT usage_date, sku_name, usage_unit, SUM(usage_quantity) AS quantity
FROM system.billing.usage
WHERE usage_date >= current_date() - INTERVAL 7 DAYS
GROUP BY usage_date, sku_name, usage_unit
ORDER BY usage_date DESC
LIMIT 50;

SELECT run_id, period_start_time, period_end_time, result_state
FROM system.lakeflow.job_run_timeline
WHERE period_start_time >= current_timestamp() - INTERVAL 1 DAY
ORDER BY period_start_time DESC
LIMIT 20;
