import DefaultTheme from 'vitepress/theme'
import ChapterMeta from './components/ChapterMeta.vue'
import MermaidDiagram from './components/MermaidDiagram.vue'
import './style.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('ChapterMeta', ChapterMeta)
    app.component('MermaidDiagram', MermaidDiagram)
  },
}
