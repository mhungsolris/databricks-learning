import { chromium } from 'playwright'
import { spawn } from 'node:child_process'
import fs from 'node:fs'
import assert from 'node:assert/strict'

const base = process.env.DOCS_BASE || '/Databricks-learning/'
const origin = 'http://127.0.0.1:4173'
const preview = spawn(process.execPath, ['node_modules/vitepress/bin/vitepress.js', 'preview', 'docs', '--host', '127.0.0.1', '--port', '4173', '--strictPort'], { stdio: 'pipe' })
let output = ''
preview.stdout.on('data', data => { output += data })
preview.stderr.on('data', data => { output += data })
let browser
try {
  let serving = false
  for (let attempt = 0; attempt < 60; attempt++) {
    try { if ((await fetch(`${origin}${base}`)).ok) { serving = true; break } } catch {}
    await new Promise(resolve => setTimeout(resolve, 250))
  }
  assert(serving, `Preview failed to serve: ${output}`)
  const chrome = process.platform === 'win32' ? 'C:/Program Files/Google/Chrome/Application/chrome.exe' : undefined
  browser = await chromium.launch({ headless: true, ...(chrome && fs.existsSync(chrome) ? { executablePath: chrome } : {}) })
  const page = await browser.newPage({ viewport: { width: 1440, height: 1000 } })
  const errors = []
  page.on('pageerror', error => errors.push(error.message))
  page.on('response', response => { if (response.url().startsWith(origin) && response.status() >= 400) errors.push(`${response.status()} ${response.url()}`) })
  fs.mkdirSync('.skills-test/screenshots', { recursive: true })
  await page.goto(`${origin}${base}`, { waitUntil: 'networkidle' })
  await page.locator('.mermaid-render svg').waitFor()
  assert.equal((await page.locator('h1').innerText()).replace(/\u200b/g, '').trim(), 'Learn Databricks for Data Engineering')
  await page.screenshot({ path: '.skills-test/screenshots/home-desktop.png', fullPage: true })
  await page.locator('.mermaid-figure').screenshot({ path: '.skills-test/screenshots/roadmap-diagram.png' })
  await page.getByRole('link', { name: 'Bắt đầu Chapter 00', exact: false }).click()
  await page.locator('h1').filter({ hasText: '00 · Databricks' }).waitFor()
  await page.locator('.mermaid-render svg').nth(1).waitFor()
  assert.equal(await page.locator('.chapter-meta').count(), 1)
  assert(await page.locator('.VPDocAsideOutline').isVisible())
  assert(await page.locator('button.copy').count() > 0)
  await page.screenshot({ path: '.skills-test/screenshots/chapter-desktop.png', fullPage: true })
  await page.locator('.mermaid-figure').first().screenshot({ path: '.skills-test/screenshots/architecture-diagram.png' })
  const theme = page.locator('.VPSwitchAppearance').first()
  await theme.click()
  await page.waitForFunction(() => document.documentElement.classList.contains('dark'))
  await page.locator('.mermaid-render[data-theme="dark"] svg').nth(1).waitFor()
  await page.screenshot({ path: '.skills-test/screenshots/chapter-dark.png', fullPage: true })
  await page.screenshot({ path: '.skills-test/screenshots/dark-viewport.png' })
  await theme.click()
  await page.locator('.VPNavBarSearch button').click()
  const search = page.locator('#localsearch-input')
  await search.fill('snapshot')
  await page.locator('.VPLocalSearchBox .result').first().waitFor()
  assert(await page.locator('.VPLocalSearchBox .result').count() > 0, 'No indexed result for snapshot query')
  const searchHref = await page.locator('.VPLocalSearchBox .result').first().getAttribute('href')
  assert(searchHref?.includes(base), `Search result bypasses project path: ${searchHref}`)
  await page.screenshot({ path: '.skills-test/screenshots/search.png' })
  await page.keyboard.press('Escape')
  // Follow actual previous/next controls, not only direct URL loads.
  await page.locator('.pager-link.next').click()
  await page.locator('h1').filter({ hasText: 'Lab 00' }).waitFor()
  for (const route of ['guide/learning-path.html', 'guide/how-to-learn.html', 'guide/sources.html', 'guide/authoring.html']) {
    const response = await page.goto(`${origin}${base}${route}`, { waitUntil: 'networkidle' })
    assert.equal(response.status(), 200, route)
    assert(await page.locator('h1').isVisible(), route)
  }
  await page.setViewportSize({ width: 390, height: 844 })
  await page.goto(`${origin}${base}foundations/00-mental-model.html`, { waitUntil: 'networkidle' })
  await page.locator('.mermaid-render svg').nth(1).waitFor()
  const overflow = await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth + 1)
  assert(!overflow, 'Mobile page has horizontal overflow')
  await page.locator('.VPLocalNav .menu').click()
  assert(await page.locator('.VPSidebar.open').isVisible())
  await page.waitForFunction(() => document.querySelector('.VPSidebar.open')?.getBoundingClientRect().left >= -1)
  await page.screenshot({ path: '.skills-test/screenshots/mobile-nav.png', fullPage: false })
  await page.locator('.VPSidebar.open a[href*="/labs/00-files-and-tables"]').click()
  await page.locator('h1').filter({ hasText: 'Lab 00' }).waitFor()
  assert.equal(await page.locator('.VPSidebar.open').count(), 0, 'Mobile menu stayed open after navigation')
  await page.goto(`${origin}${base}foundations/00-mental-model.html`, { waitUntil: 'networkidle' })
  await page.locator('.mermaid-render svg').nth(1).waitFor()
  await page.screenshot({ path: '.skills-test/screenshots/chapter-mobile.png', fullPage: true })
  await page.screenshot({ path: '.skills-test/screenshots/mobile-viewport.png', fullPage: false })
  const newChapters = [
    ['46', 'iceberg/46-why-iceberg', 'labs/46-why-iceberg'],
    ['47', 'iceberg/47-metadata-snapshots', 'labs/47-metadata-snapshots'],
    ['48', 'iceberg/48-catalogs', 'labs/48-catalogs'],
    ['49', 'iceberg/49-schema-partition-evolution', 'labs/49-schema-partition-evolution'],
    ['50', 'iceberg/50-row-level-changes', 'labs/50-row-level-changes'],
    ['51', 'iceberg/51-delta-vs-iceberg', 'labs/51-delta-vs-iceberg'],
    ['52', 'iceberg/52-managed-iceberg', 'labs/52-managed-iceberg'],
    ['53', 'system-design/53-databricks-vs-bigquery', 'labs/53-databricks-vs-bigquery'],
    ['54', 'system-design/54-databricks-vs-snowflake', 'labs/54-databricks-vs-snowflake'],
    ['55', 'system-design/55-databricks-vs-fabric', 'labs/55-databricks-vs-fabric'],
    ['56', 'system-design/56-decision-framework', 'labs/56-decision-framework'],
    ['57', 'system-design/57-when-not-databricks', 'labs/57-when-not-databricks'],
    ['58', 'system-design/58-lock-in-layers', 'labs/58-lock-in-layers'],
    ['59', 'system-design/59-open-lakehouse', 'labs/59-open-lakehouse'],
    ['60', 'system-design/60-system-design-cases', 'labs/60-system-design-cases'],

    ['01', 'foundations/01-grain-keys-fanout', 'labs/01-grain-fanout'],
    ['02', 'foundations/02-lake-warehouse-lakehouse', 'labs/02-layout-contract'],
    ['03', 'spark/03-architecture-dataframes-sql', 'labs/03-pipeline-execution'],
    ['04', 'spark/04-partitioning', 'labs/04-partitioning'],
    ['05', 'spark/05-shuffle', 'labs/05-shuffle'],
    ['06', 'spark/06-joins-broadcast-skew', 'labs/06-joins-skew'],
    ['07', 'storage/07-parquet', 'labs/07-parquet'],
    ['08', 'storage/08-delta-fundamentals', 'labs/08-delta-log'],
    ['09', 'architecture/09-medallion', 'labs/09-medallion-design'],
    ['10', 'ingestion/10-incremental-boundaries', 'labs/10-incremental-failures'],
    ['11', 'correctness/11-idempotency', 'labs/11-retry-batch'],
    ['12', 'correctness/12-merge-correctness', 'labs/12-merge-matrix'],
    ['13', 'correctness/13-time-semantics', 'labs/13-time-semantics'],
    ['14', 'correctness/14-late-lookback-reconciliation', 'labs/14-attribution-72h'],
    ['15', 'correctness/15-backfill-reconciliation', 'labs/15-failed-backfill'],
    ['16', 'streaming/16-structured-streaming', 'labs/16-structured-streaming'],
    ['17', 'streaming/17-stateless-stateful', 'labs/17-stateless-stateful'],
    ['18', 'streaming/18-checkpoints', 'labs/18-checkpoints'],
    ['19', 'streaming/19-windows-watermarks', 'labs/19-windows-watermarks'],
    ['20', 'streaming/20-streaming-dedup', 'labs/20-streaming-dedup'],
    ['21', 'streaming/21-stream-stream-joins', 'labs/21-stream-stream-joins'],
    ['22', 'streaming/22-output-modes-sinks', 'labs/22-output-modes-sinks'],
    ['23', 'streaming/23-delivery-semantics', 'labs/23-delivery-semantics'],
    ['24', 'streaming/24-recovery-runbook', 'labs/24-recovery-runbook'],
    ['25', 'platform/25-compute-mental-model', 'labs/25-compute-mental-model'],
    ['26', 'platform/26-lakeflow-jobs', 'labs/26-lakeflow-jobs'],
    ['27', 'platform/27-declarative-pipelines', 'labs/27-declarative-pipelines'],
    ['28', 'platform/28-unity-catalog', 'labs/28-unity-catalog'],
    ['29', 'platform/29-databricks-sql', 'labs/29-databricks-sql'],
    ['30', 'platform/30-platform-boundaries', 'labs/30-platform-boundaries'],
    ['31', 'production/31-performance-mental-model', 'labs/31-performance-mental-model'],
    ['32', 'production/32-query-plans', 'labs/32-query-plans'],
    ['33', 'production/33-small-files', 'labs/33-small-files'],
    ['34', 'production/34-data-layout', 'labs/34-data-layout'],
    ['35', 'production/35-photon', 'labs/35-photon'],
    ['36', 'production/36-performance-case-study', 'labs/36-performance-case-study'],
    ['37', 'production/37-observability-mental-model', 'labs/37-observability-mental-model'],
    ['38', 'production/38-databricks-observability', 'labs/38-databricks-observability'],
    ['39', 'production/39-data-quality', 'labs/39-data-quality'],
    ['40', 'production/40-expectations', 'labs/40-expectations'],
    ['41', 'production/41-testing-strategy', 'labs/41-testing-strategy'],
    ['42', 'production/42-ci-cd', 'labs/42-ci-cd'],
    ['43', 'production/43-declarative-automation-bundles', 'labs/43-declarative-automation-bundles'],
    ['44', 'production/44-github-actions', 'labs/44-github-actions'],
    ['45', 'production/45-release-rollback', 'labs/45-release-rollback'],
  ]
  for (const [number, route, lab] of newChapters) {
    await page.setViewportSize({ width: 1440, height: 1000 })
    // Exercise actual current-content links from the existing sidebar.
    const currentLink = page.locator(`.VPSidebar a[href*="/${route}"]`).first()
    if (!(await currentLink.isVisible())) {
      const group = currentLink.locator('xpath=ancestor::*[contains(@class,"VPSidebarItem") and contains(@class,"level-0")][1]')
      await group.locator(':scope > .item').click()
    }
    await currentLink.click()
    await page.waitForURL(`**/${route}.html`)
    await page.locator('h1').filter({ hasText: `${number} ·` }).waitFor()
    await page.locator('.mermaid-render svg').waitFor()
    assert(await page.locator('h1').innerText().then(text => text.includes(`${number} ·`)))
    assert(await page.locator('.chapter-meta').isVisible())
    assert(await page.locator('.VPDocAsideOutline').isVisible())
    assert(await page.locator('button.copy').count() > 0)
    await page.screenshot({ path: `.skills-test/screenshots/chapter-${number}-desktop.png` })
    // Tall element screenshots can include the fixed nav over the stitched diagram.
    const captureNav = page.locator('.VPNav, .VPLocalNav')
    await captureNav.evaluateAll(elements => elements.forEach(element => { element.style.visibility = 'hidden' }))
    try {
      await page.locator('.mermaid-figure').screenshot({ path: `.skills-test/screenshots/diagram-${number}.png` })
    } finally {
      await captureNav.evaluateAll(elements => elements.forEach(element => { element.style.removeProperty('visibility') }))
    }
    assert(await page.locator('.VPNav').isVisible(), 'Navigation was not restored after diagram capture')
    const switcher = page.locator('.VPSwitchAppearance').first()
    await switcher.click()
    await page.locator('.mermaid-render[data-theme="dark"] svg').waitFor()
    await switcher.click()
    await page.locator('.mermaid-render[data-theme="neutral"] svg').waitFor()
    assert.equal(await page.locator('[role="alert"]').count(), 0, route)
    // Navigate chapter -> lab -> following dependency using real pager controls.
    await page.locator('.pager-link.next').click()
    await page.waitForURL(`**/${lab}.html`)
    await page.locator('h1').filter({ hasText: `Lab ${number}` }).waitFor()
    assert(await page.locator('h1').innerText().then(text => text.includes(`Lab ${number}`)))
    await page.locator('.pager-link.prev').click()
    await page.waitForURL(`**/${route}.html`)
    await page.setViewportSize({ width: 390, height: 844 })
    await page.goto(`${origin}${base}${route}.html`, { waitUntil: 'networkidle' })
    await page.locator('.mermaid-render svg').waitFor()
    assert(!(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth + 1)), `Mobile overflow: ${route}`)
    await page.screenshot({ path: `.skills-test/screenshots/chapter-${number}-mobile.png` })
    await page.goto(`${origin}${base}${lab}.html`, { waitUntil: 'networkidle' })
    assert(!(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth + 1)), `Mobile overflow: ${lab}`)
  }
  await page.setViewportSize({ width: 1440, height: 1000 })
  await page.locator('.VPNavBarSearch button').click()
  await page.locator('#localsearch-input').fill('fan-out')
  await page.locator('.VPLocalSearchBox .result[href*="01-grain"]').first().waitFor()
  await page.keyboard.press('Escape')
  assert.equal(await page.locator('[role="alert"]').count(), 0, 'Mermaid render failure')
  assert.deepEqual(errors, [], 'Browser JS or local request errors')
  await page.locator('.VPNavBarSearch button').click()
  await page.locator('#localsearch-input').fill('transaction log')
  await page.locator('.VPLocalSearchBox .result[href*="08-delta"]').first().waitFor()
  await page.keyboard.press('Escape')
  for (const route of ['setup/local-spark', 'labs/runtime-evidence']) {
    assert.equal((await page.goto(`${origin}${base}${route}.html`, { waitUntil: 'networkidle' })).status(), 200)
  }
  const manifestResponse = await page.request.get(`${origin}${base}evidence/spark/manifest.json`)
  assert.equal(manifestResponse.status(), 200)
  const manifest = await manifestResponse.json()
  assert(Object.keys(manifest.files).length >= 44)
  const commitResponse = await page.request.get(`${origin}${base}evidence/spark/delta/lab08/delta-table/_delta_log/00000000000000000002.json`)
  assert.equal(commitResponse.status(), 200)
  const actions = (await commitResponse.text()).trim().split('\n').map(line => JSON.parse(line))
  assert(actions.some(action => action.add) && actions.some(action => action.remove))
  assert.deepEqual(errors, [], 'Browser errors after setup/evidence navigation')
  await page.goto(`${origin}${base}assessments/mid-gate-pipeline-correctness.html`, { waitUntil: 'networkidle' })
  assert((await page.locator('h1').innerText()).includes('Mid Gate'))
  assert.equal(await page.locator('details').count(), 0, 'Assessment must not contain hidden solution reveal')
  assert.equal(await page.locator('a[href*="reviewer"]').count(), 0)
  await page.locator('.VPNavBarSearch button').click()
  await page.locator('#localsearch-input').fill('Mid Gate')
  await page.locator('.VPLocalSearchBox .result[href*="mid-gate-pipeline-correctness"]').first().waitFor()
  await page.keyboard.press('Escape')
  const input = await page.request.get(`${origin}${base}assessment/pipeline-input.json`)
  assert.equal(input.status(), 200)
  assert.equal((await input.json()).deliveries.length, 6)
  const correctnessManifest = await page.request.get(`${origin}${base}evidence/correctness/manifest.json`)
  assert.equal(correctnessManifest.status(), 200)
  assert.equal(Object.keys((await correctnessManifest.json()).files).length, 25)
  const retry = await page.request.get(`${origin}${base}evidence/correctness/lab11/result.json`)
  assert.equal(retry.status(), 200)
  const retryResult = await retry.json()
  assert.equal(retryResult.onceHash, retryResult.ackRetryHash)
  await page.setViewportSize({ width: 390, height: 844 })
  if (await page.locator('.VPSidebar.open').count()) {
    await page.locator('.VPBackdrop').click({ position: { x: 370, y: 400 } })
  }
  // Desktop -> mobile changes can animate a closed sidebar off-screen without .open.
  await page.waitForFunction(() => document.querySelector('.VPSidebar')?.getBoundingClientRect().right <= 1)
  assert.equal(await page.locator('.VPSidebar.open').count(), 0, 'Assessment must be visible without navigation overlay')
  assert(await page.evaluate(() => {
    const heading = document.querySelector('h1')
    const box = heading.getBoundingClientRect()
    return document.elementFromPoint(box.x + box.width / 2, box.y + box.height / 2)?.closest('h1') === heading
  }), 'Assessment heading is covered by an overlay')
  assert(!(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth + 1)), 'Assessment mobile overflow')
  await page.screenshot({ path: '.skills-test/screenshots/mid-gate-mobile.png', animations: 'disabled' })
  assert.deepEqual(errors, [], 'Browser errors after correctness assessment/evidence')
  await page.setViewportSize({ width: 1440, height: 1000 })
  await page.goto(`${origin}${base}assessments/mid-gate-streaming-correctness.html`, { waitUntil: 'networkidle' })
  assert((await page.locator('h1').innerText()).includes('Streaming Correctness'))
  assert.equal(await page.locator('details').count(), 0)
  assert.equal(await page.locator('a[href*="reviewer"]').count(), 0)
  await page.locator('.VPNavBarSearch button').click()
  await page.locator('#localsearch-input').fill('Streaming Correctness')
  await page.locator('.VPLocalSearchBox .result[href*="mid-gate-streaming-correctness"]').first().waitFor()
  await page.keyboard.press('Escape')
  const streamingInput = await page.request.get(`${origin}${base}assessment/streaming-input.json`)
  assert.equal(streamingInput.status(), 200)
  assert.equal((await streamingInput.json()).deliveries.length, 5)
  await page.goto(`${origin}${base}labs/streaming-evidence.html`, { waitUntil: 'networkidle' })
  const streamingManifest = await page.request.get(`${origin}${base}evidence/streaming/manifest.json`)
  assert.equal(streamingManifest.status(), 200)
  assert.equal(Object.keys((await streamingManifest.json()).files).length, 13)
  for (const n of [16, 17, 18, 19, 20, 21, 22, 23, 24]) {
    const artifact = await page.request.get(`${origin}${base}evidence/streaming/lab${n}/result.json`)
    assert.equal(artifact.status(), 200)
    const observed = await artifact.json()
    if (n === 18) assert.deepEqual(observed.phases.map(p => p.target.length), [3, 3, 4, 8])
    if (n === 23) {
      assert.equal(observed.unsafe.after.target.length, 2)
      assert.equal(observed.transactional.after.target.length, 1)
    }
  }
  await page.goto(`${origin}${base}assessments/mid-gate-streaming-correctness.html`, { waitUntil: 'networkidle' })
  await page.setViewportSize({ width: 390, height: 844 })
  await page.waitForFunction(() => document.querySelector('.VPSidebar')?.getBoundingClientRect().right <= 1)
  assert(!(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth + 1)), 'Streaming assessment mobile overflow')
  await page.screenshot({ path: '.skills-test/screenshots/streaming-mid-gate-mobile.png', animations: 'disabled' })
  assert.deepEqual(errors, [], 'Browser errors after streaming assessment/evidence')
  await page.setViewportSize({ width: 1440, height: 1000 })
  for (const route of ['setup/databricks-free-edition', 'labs/platform-evidence', 'assessments/mid-gate-platform-design']) {
    assert.equal((await page.goto(`${origin}${base}${route}.html`, { waitUntil: 'networkidle' })).status(), 200)
    assert(await page.locator('h1').isVisible())
    assert((await page.locator('.vp-doc').innerText()).includes('PENDING USER WORKSPACE'))
  }
  assert.equal(await page.locator('details').count(), 0, 'Platform assessment must not reveal solutions')
  assert.equal(await page.locator('a[href*="reviewer"]').count(), 0)
  await page.locator('.VPNavBarSearch button').click()
  await page.locator('#localsearch-input').fill('Databricks Platform Design')
  await page.locator('.VPLocalSearchBox .result[href*="mid-gate-platform-design"]').first().waitFor()
  await page.keyboard.press('Escape')
  const platformManifest = await page.request.get(`${origin}${base}evidence/platform/manifest.json`)
  assert.equal(platformManifest.status(), 200)
  const localManifest = await platformManifest.json()
  assert.equal(localManifest.evidenceTier, 'LOCAL SPARK TEST')
  assert.equal(localManifest.workspaceStatus, 'PENDING USER WORKSPACE')
  assert.equal(Object.keys(localManifest.files).length, 5)
  const platformResult = await page.request.get(`${origin}${base}evidence/platform/result.json`)
  assert.equal(platformResult.status(), 200)
  const localResult = await platformResult.json()
  assert.equal(localResult.gold.reduce((sum, row) => sum + row.revenue_cents, 0), 1250)
  await page.setViewportSize({ width: 390, height: 844 })
  await page.waitForFunction(() => document.querySelector('.VPSidebar')?.getBoundingClientRect().right <= 1)
  assert(!(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth + 1)), 'Platform assessment mobile overflow')
  await page.screenshot({ path: '.skills-test/screenshots/platform-mid-gate-mobile.png', animations: 'disabled' })
  assert.deepEqual(errors, [], 'Browser errors after platform assessment/evidence')
  for (const [route, label] of [
    ['assessments/mid-gate-performance-diagnosis', 'Performance Diagnosis'],
    ['assessments/mid-gate-production-readiness', 'Production Readiness'],
    ['assessments/mid-gate-platform-lakehouse-system-design', 'Platform and Lakehouse System Design'],
  ]) {
    await page.setViewportSize({ width: 1440, height: 1000 })
    assert.equal((await page.goto(`${origin}${base}${route}.html`, { waitUntil: 'networkidle' })).status(), 200)
    assert((await page.locator('h1').innerText()).includes(label))
    assert.equal(await page.locator('details').count(), 0)
    assert.equal(await page.locator('a[href*="reviewer"]').count(), 0)
    await page.locator('.VPNavBarSearch button').click()
    await page.locator('#localsearch-input').fill(label)
    await page.locator(`.VPLocalSearchBox .result[href*="${route}"]`).first().waitFor()
    await page.keyboard.press('Escape')
    await page.setViewportSize({ width: 390, height: 844 })
    await page.waitForFunction(() => document.querySelector('.VPSidebar')?.getBoundingClientRect().right <= 1)
    assert(!(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth + 1)), route)
    await page.screenshot({ path: `.skills-test/screenshots/${route.split('/').pop()}-mobile.png`, animations: 'disabled' })
  }
  assert.equal((await page.goto(`${origin}${base}labs/production-evidence.html`, { waitUntil: 'networkidle' })).status(), 200)
  assert((await page.locator('body').innerText()).includes('PENDING USER WORKSPACE'))
  const productionResponse = await page.request.get(`${origin}${base}evidence/production/manifest.json`)
  assert.equal(productionResponse.status(), 200)
  const productionManifest = await productionResponse.json()
  assert.equal(Object.keys(productionManifest.files).length, 14)
  assert.equal(productionManifest.workspaceStatus, 'PENDING USER WORKSPACE')
  for (const file of Object.keys(productionManifest.files)) {
    assert.equal((await page.request.get(`${origin}${base}evidence/production/${file}`)).status(), 200)
  }
  const productionResult = await (await page.request.get(`${origin}${base}evidence/production/result.json`)).json()
  assert.equal(productionResult.layouts.tiny.files, 32)
  assert.equal(productionResult.layouts.compact.files, 2)
  assert.equal(productionResult.rollback.afterRestore, 1250)
  assert.equal(productionResult.quality.platformExpectationExecuted, false)
  assert.deepEqual(errors, [], 'Browser errors after production chapters/gates/evidence')

  for (const route of ['setup/local-iceberg','labs/iceberg-evidence','iceberg/current-platform-support','adr/ADR-001-table-format','adr/ADR-002-platform-choice']) {
    assert.equal((await page.goto(origin+base+route+'.html', { waitUntil: 'networkidle' })).status(),200)
    assert(!(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth + 1)), route)
  }
  const icebergManifest = await (await page.request.get(origin+base+'evidence/iceberg/manifest.json')).json()
  assert.equal(Object.keys(icebergManifest.files).length,9)
  for (const file of Object.keys(icebergManifest.files)) assert.equal((await page.request.get(origin+base+'evidence/iceberg/'+file)).status(),200)
  const iceberg = await (await page.request.get(origin+base+'evidence/iceberg/results.json')).json()
  assert.equal(iceberg.snapshots.oldRows,2)
  assert.equal(iceberg.partition.revenue,350)
  assert.deepEqual(iceberg.partition.specIds,[0,1])
  assert.equal(iceberg.mor.positionDeleteObserved,true)
  await page.locator('.VPNavBarSearch button').click()
  await page.locator('#localsearch-input').fill('When not to use Databricks')
  await page.locator('.VPLocalSearchBox .result[href*="57-when-not-databricks"]').first().waitFor()
  await page.keyboard.press('Escape')
  await page.goto(origin+base+'capstone/', { waitUntil: 'networkidle' })
  assert.equal((await page.locator('h1').innerText()).replace(/\u200b/g, '').trim(), 'Near-real-time Advertising ROAS Platform')
  assert(await page.locator('.vp-doc').innerText().then(text => text.includes('Phase 1: requirements interview') && text.includes('NOT YET') && text.includes('Nộp requirements interview')))
  assert(await page.locator('.VPSidebar a[href*="/capstone/"]').count() > 0)
  await page.setViewportSize({ width: 390, height: 844 })
  assert(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth), 'Capstone mobile overflow')
  await page.screenshot({ path: '.skills-test/screenshots/capstone-requirements-mobile.png', fullPage: true })
  assert.deepEqual(errors, [], 'Browser errors after architecture/evidence and capstone challenge')
  console.log('PASS desktop/mobile, sixty-three rendered Mermaid diagrams, search, themes, code controls, chapters00-60/lab pagers, setup/evidence/six assessment routes and page responses. Screenshots: .skills-test/screenshots/')
} finally {
  await browser?.close()
  preview.kill()
}
