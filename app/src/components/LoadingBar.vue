<script setup lang="ts">
defineProps<{ isLoading: boolean }>();
</script>

<template>
    <div v-if="isLoading" class="progress-bar-container">
        <div class="progress-bar"></div>
    </div>
</template>

<style scoped>
.progress-bar-container {
  width: 100%;
  height: 8px;
  background-color: #f3f3f3;
  border-radius: 10px;
  overflow: hidden;
  position: relative;
}

.progress-bar {
  width: 100%;
  height: 100%;
  background-color: #4caf50;
  animation: loadingAnimation 2s infinite ease-in-out;
  transform-origin: left;
  position: absolute;
}

@keyframes loadingAnimation {
  0% {
    transform: scaleX(0);
  }
  50% {
    transform: scaleX(1);
  }
  100% {
    transform: scaleX(0);
  }
}
</style>