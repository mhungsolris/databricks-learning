-- DESIGN ONLY: existing group names and privileges must be reviewed by an administrator.
-- Substitute the chosen catalog/schema; do not execute against existing production objects.
GRANT USE CATALOG ON CATALOG roas_prod TO `marketing_analysts`;
GRANT USE SCHEMA ON SCHEMA roas_prod.gold TO `marketing_analysts`;
GRANT SELECT ON TABLE roas_prod.gold.roas TO `marketing_analysts`;
SHOW GRANTS ON TABLE roas_prod.gold.roas;
-- Parent grants and group membership must also be inspected for an effective-access review.
