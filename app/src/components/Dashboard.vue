<script setup lang="ts">
import FileUpload from './FileUpload.vue'

// Props for the message passed to the component
defineProps<{ }>()

</script>

<template>
  <p>Shopee Report Formatter</p>
  <FileUpload/>
</template>

<style scoped>
/* Add your styles here */
h1 {
  color: #42b983;
}

p {
  font-size: 18px;
  color: #c2ebb8;
}
</style>
