<script setup lang="ts">
import Dashboard from './components/Dashboard.vue'
import Sidebar from './components/Sidebar.vue'
</script>

<template>
  <div class="main">
    <Sidebar class="sidebar" />
    <Dashboard class="dashboard" />
  </div>
</template>

<style scoped>
.main{
  display: flex;
  height: 100vh;
}

.sidebar{
  width: 20%;
  border-right: 0.5vh solid hwb(0 9% 90%);
}

.dashboard{
  width: 80%;
}
</style>
