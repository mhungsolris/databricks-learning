import fs from 'node:fs'
import path from 'node:path'

const sections = ['Why this matters', 'Scenario', 'Learner reasoning', 'Mental model', 'Core concepts', 'Example data', 'How it works', 'Databricks implementation', 'Production failure', 'Debugging', 'BigQuery / Airflow mapping', 'Code', 'Common mistakes', 'Production notes', 'Interview checkpoint', 'PASS criteria', 'Official references']
const markdownFiles = []
function walk(dir) {
  for (const file of fs.readdirSync(dir, { withFileTypes: true })) {
    if (file.name.startsWith('.')) continue
    const full = path.join(dir, file.name)
    if (file.isDirectory()) walk(full)
    else if (file.name.endsWith('.md')) markdownFiles.push(full)
  }
}
walk('docs')
let chapters = 0
for (const file of markdownFiles) {
  const content = fs.readFileSync(file, 'utf8').replace(/\r\n/g, '\n')
  if (/docs[\\/](foundations|spark|storage|architecture|ingestion|correctness|streaming|platform|production|iceberg|system-design)[\\/]\d+/.test(file)) {
    chapters++
    for (const heading of sections) {
      if (!content.includes(`## ${heading}\n`)) throw new Error(`${file} missing ${heading}`)
    }
    for (const field of ['level', 'priority', 'effort']) {
      if (!new RegExp(`^${field}: .+`, 'm').test(content)) throw new Error(`${file} missing ${field}`)
    }
    if (!content.includes('<ChapterMeta>') || !content.includes('NOT YET')) throw new Error(`${file} missing learning header/checkpoint`)
    if (/[\\/](0[4-9]|1[0-9]|2[0-9]|[3-5][0-9]|60)-/.test(file) && !content.includes('## How to explain this in an interview\n')) throw new Error(`${file} missing interview articulation`)
  }
  if (content.includes('TODO') || content.includes('Lorem ipsum')) throw new Error(`Placeholder content: ${file}`)
  if ((content.match(/^```/gm) || []).length % 2) throw new Error(`Unclosed code fence: ${file}`)
}
for (const file of markdownFiles) {
  const content = fs.readFileSync(file, 'utf8')
  if (/REVIEWER_ONLY_ROAS_SOLUTION|reviewer\/mid-gate-/.test(content)) throw new Error(`Reviewer material exposed: ${file}`)
}
console.log(`PASS ${chapters} chapter schemas and ${markdownFiles.length} authored Markdown pages; dead links checked by build.`)
