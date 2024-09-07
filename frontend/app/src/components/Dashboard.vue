<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'

// Props for the message passed to the component
defineProps<{ msg: string }>()

// Reactive state for the fetched data
const count = ref(0)
const message = ref<string>('Loading...')

// Fetch data from the API when the component is mounted
onMounted(async () => {
  try {
    const response = await axios.get('http://localhost:5000/api/data')
    message.value = response.data.message  // Update message with backend data
  } catch (error) {
    console.error('Error fetching data:', error)
    message.value = 'Failed to load data'
  }
})
</script>

<template>
  <h1>{{ msg }}</h1>
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
