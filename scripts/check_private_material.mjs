import fs from 'node:fs'
import path from 'node:path'
import assert from 'node:assert/strict'

const root = 'docs/.vitepress/dist'
let checked = 0
function walk(dir) {
  for (const item of fs.readdirSync(dir, { withFileTypes: true })) {
    const file = path.join(dir, item.name)
    if (item.isDirectory()) {
      assert(!/reviewer/i.test(item.name), `Reviewer directory published: ${file}`)
      walk(file)
    } else if (/\.(html|js|json|txt|md)$/.test(file)) {
      const text = fs.readFileSync(file, 'utf8')
      assert(!/REVIEWER_ONLY_ROAS_SOLUTION|Reviewer only: Mid Gate|reviewer\/mid-gate-/.test(text), `Reviewer solution leaked: ${file}`)
      assert(!/\bdapi[a-f0-9]{32}\b|\bAKIA[A-Z0-9]{16}\b|https:\/\/(?:dbc-[a-z0-9-]+|adb-[0-9]+\.[0-9]+)\.(?:cloud\.databricks\.com|azuredatabricks\.net)/i.test(text), `Possible credential/private workspace URL: ${file}`)
      checked++
    }
  }
}
walk(root)
const platformPaths = ['labs/platform', 'docs/platform', 'docs/public/evidence/platform', 'labs/production', 'docs/production', 'docs/public/evidence/production', 'labs/iceberg', 'docs/iceberg', 'docs/system-design', 'docs/adr', 'docs/public/evidence/iceberg']
function privacy(dir) {
  for (const item of fs.readdirSync(dir, { withFileTypes: true })) {
    if (item.name.startsWith('.') || item.name === '__pycache__') continue
    const file = path.join(dir, item.name)
    if (item.isDirectory()) privacy(file)
    else {
      const text = fs.readFileSync(file, 'utf8')
      assert(!/\bdapi[a-f0-9]{32}\b|\bAKIA[A-Z0-9]{16}\b|[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}/i.test(text), `Possible private data in platform artifact: ${file}`)
      assert(!/"(?:account_id|workspace_id|job_id|pipeline_id|warehouse_id)"\s*:\s*(?:\d+|"[^"]+")/.test(text), `Unredacted platform identifier: ${file}`)
    }
  }
}
platformPaths.forEach(privacy)
console.log(`PASS reviewer solution excluded from ${checked} built HTML/search/script/JSON artifacts`)
console.log('PASS platform credential/email/identifier pattern guard; manual screenshot redaction still required')
