<script setup lang="ts">
import { ref, onMounted } from 'vue'

// Props for the message passed to the component
defineProps<{ }>()

// Reactive state for the fetched data
const message = ref<string>('Loading...')

// Fetch data from the API when the component is mounted
onMounted(async () => {
      try {
        const response = await fetch('/api/hello')
        const data = await response.json()
        message.value = data.message  // Update message with backend data
      } catch (error) {
        console.error('Error fetching data:', error)
        message.value = 'Failed to load data'
      }
    })
</script>

<template>
  <p>{{ message }}</p>
</template>

<style scoped>
/* Add your styles here */
h1 {
  color: #42b983;
}

p {
  font-size: 18px;
  color: #333;
}
</style>
