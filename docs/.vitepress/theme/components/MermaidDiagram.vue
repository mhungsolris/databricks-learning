<script setup lang="ts">
import { onMounted, ref, watch } from 'vue'
import { useData } from 'vitepress'

const props = defineProps<{ source: string }>()
const { isDark } = useData()
const html = ref('')
const failure = ref('')
const ready = ref(false)
const renderedTheme = ref('')
const diagram = decodeURIComponent(props.source)
let generation = 0
let nextId = 0
// Unique across component instances as well as route changes.
const idPrefix = Math.random().toString(36).slice(2)

async function render() {
  const current = ++generation
  const theme = isDark.value ? 'dark' : 'neutral'
  try {
    const { default: mermaid } = await import('mermaid')
    mermaid.initialize({ startOnLoad: false, securityLevel: 'strict', theme, fontFamily: 'system-ui, sans-serif' })
    await mermaid.parse(diagram)
    const result = await mermaid.render(`diagram-${idPrefix}-${++nextId}`, diagram)
    if (current === generation) { html.value = result.svg; failure.value = ''; renderedTheme.value = theme }
  } catch (error) {
    if (current === generation) { failure.value = String(error); html.value = '' }
  }
}

onMounted(() => { ready.value = true; render() })
watch(isDark, () => { if (ready.value) render() })
</script>

<template>
  <figure class="mermaid-figure" aria-label="Sơ đồ kiến trúc">
    <div v-if="html" class="mermaid-render" :data-theme="renderedTheme" v-html="html" />
    <pre v-else-if="!failure" class="diagram-fallback">{{ diagram }}</pre>
    <p v-if="failure" role="alert">Không render được sơ đồ: {{ failure }}</p>
    <details><summary>Xem Mermaid source</summary><pre>{{ diagram }}</pre></details>
  </figure>
</template>
