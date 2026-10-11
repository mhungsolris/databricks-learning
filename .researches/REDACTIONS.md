# Research archive redactions

## 2026-10-11: public Google documentation keys

Twelve archived Google HTML files contain ten distinct Google API key patterns embedded in the source websites. All ten matched current public HTML at https://docs.cloud.google.com/bigquery/docs/introduction or https://cloud.google.com/bigquery/pricing during inspection on 2026-10-11. This comparison establishes public provenance, not credential ownership, validity or authorization to use them. No key was used in an API request.

The archives replace each matching value with `[REDACTED_GOOGLE_API_KEY]`. These HTML files are sanitized research copies, not byte-identical captures. Retrieval dates, source URLs and teaching prose retain their original meaning. The affected files and before/after SHA256 values are recorded in `google-html-redactions.json` without credential values.

The collector redacts this pattern in future captures. The repository credential pattern check runs in Pages CI. Pattern checks cannot prove the absence of every possible secret.

The initial published commit still contains the original HTML. Removing values from current files does not remove Git history or close GitHub alerts. A repository owner must review the matching alert locations and record their public third-party provenance when resolving them.
