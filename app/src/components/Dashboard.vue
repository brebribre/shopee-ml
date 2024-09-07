<script setup lang="ts">
import FileUpload from './FileUpload.vue'

// Props for the message passed to the component
defineProps<{ }>()

</script>

<template>
  <p>Shopee report formatter</p>
  <FileUpload/>
</template>

<style scoped>
/* Add your styles here */
h1 {
  color: #42b983;
}

p {
  font-size: 18px;
  color: #2c671d;
}
</style>
