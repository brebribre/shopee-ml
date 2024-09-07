<script setup lang="ts">
import FileUpload from './FileUpload.vue'

// Props for the message passed to the component
defineProps<{ }>()

</script>

<template>
  <div class="container">
    <h2>Laporan Penjualan Shopee</h2>
    <p>
    1. Pilih file Excel yang berisi data penjualan Shopee.
    <br />
    2. Klik tombol "Upload File" untuk mengirim file.
    <br />
    3. Tunggu hingga proses selesai (2-4 menit).
    <br />
    4. Klik tombol "Download" untuk mengunduh file hasil.
    </p>
    <FileUpload/>
  </div>
</template>

<style scoped>
.container{
  display: flex;
  flex-direction: column;
  margin-top: 24px;
  align-items: center;
}

h2 {
  font-size: 32px;
  color: #42b983;
}

p {
  font-size: 16px;
  color: #c7cbc6;
}
</style>
