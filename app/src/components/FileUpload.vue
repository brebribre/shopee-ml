<template>
    <div>
      <input type="file" @change="onFileChange" />
      
      <button @click="submitFile" :disabled="!selectedFile || isLoading">
        <span v-if="isLoading">Uploading... {{ uploadProgress }}%</span>
        <span v-else>Upload File</span>
      </button>
  
      <div v-if="isLoading">
        <progress :value="uploadProgress" max="100"></progress>
      </div>
  
      <div v-if="fileUrl">
        <a :href="fileUrl" download="processed_file.xlsx">Download Processed File</a>
      </div>
  
      <div v-if="errorMessage" class="error">{{ errorMessage }}</div>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref } from 'vue';
  import { useSendExcel } from '../hooks/useSendExcel';  // Adjust the path as needed
  
  const { sendExcel } = useSendExcel();
  
  const selectedFile = ref<File | null>(null);
  const fileUrl = ref<string | null>(null);
  const errorMessage = ref<string | null>(null);
  const isLoading = ref<boolean>(false);
  const uploadProgress = ref<number>(0);
  const downloadProgress = ref<number>(0);
  
  const onFileChange = (event: Event) => {
    const target = event.target as HTMLInputElement;
    if (target.files && target.files[0]) {
      selectedFile.value = target.files[0];
    }
  };
  
  const submitFile = async () => {
    fileUrl.value = null;
    if (!selectedFile.value) return;
  
    isLoading.value = true;
    errorMessage.value = null;
  
    const { fileUrl: resultUrl, error } = await sendExcel(
      selectedFile.value,
      // Upload progress callback
      (progress: number) => {
        uploadProgress.value = progress;
      },
      // Download progress callback (optional)
      (progress: number) => {
        downloadProgress.value = progress;
      }
    );
  
    if (error) {
      errorMessage.value = error;
    } else {
      fileUrl.value = resultUrl;
    }
  
    isLoading.value = false;
  };
  </script>
  
  <style scoped>
  .error {
    color: red;
  }
  
  progress {
    width: 100%;
    margin-top: 10px;
  }
  </style>
  