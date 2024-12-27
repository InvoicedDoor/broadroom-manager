import { fileURLToPath } from 'node:url'
import { mergeConfig, defineConfig, configDefaults } from 'vitest/config'
import viteConfig from './vite.config'

export default mergeConfig(
  viteConfig,
  defineConfig({
    build: {
      target: 'esnext',
      minify: false
    },
    test: {
      environment: 'jsdom',
      exclude: [...configDefaults.exclude, 'e2e/**'],
      root: fileURLToPath(new URL('./', import.meta.url))
    },
    // server: {
    //   proxy: {
    //     '/api': {
    //       target: 'http://localhost:5000',
    //       changeOrigin: true
    //     }
    //   }
    // }
  })
)
