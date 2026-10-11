<script setup lang="ts">
import { useData } from 'vitepress'
const { frontmatter } = useData()
</script>

<template>
  <dl class="chapter-meta" aria-label="Thông tin chương">
    <div><dt>Level</dt><dd>{{ frontmatter.level }}</dd></div>
    <div><dt>Priority</dt><dd>{{ frontmatter.priority }}</dd></div>
    <div><dt>Effort</dt><dd>{{ frontmatter.effort }}</dd></div>
    <div><dt>Prerequisites</dt><dd><slot /></dd></div>
  </dl>
</template>
