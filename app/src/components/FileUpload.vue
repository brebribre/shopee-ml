<script setup lang="ts">
  import { ref } from 'vue';
  import { useSendExcel } from '../hooks/useSendExcel'; 
  import LoadingBar from './LoadingBar.vue';
  
  const selectedFile = ref<File | null>(null);
  const fileUrl = ref<string | null>(null);
  
  const errorMessage = ref<string | null>(null);

  const isLoading = ref<boolean>(false);
  const uploadProgress = ref<number>(0);
  
  const { sendExcel } = useSendExcel();
  const submitFile = async () => {
    fileUrl.value = null;
    if (!selectedFile.value) return;
  
    isLoading.value = true;
    errorMessage.value = null;
  
    const { fileUrl: resultUrl, error } = await sendExcel(
      selectedFile.value,
      (progress: number) => {
        uploadProgress.value = progress;
      },
    );
  
    if (error) {
      errorMessage.value = error;
    } else {
      fileUrl.value = resultUrl;
    }
  
    isLoading.value = false;
  };

  const onFileChange = (event: Event) => {
    const target = event.target as HTMLInputElement;
    if (target.files && target.files[0]) {
      selectedFile.value = target.files[0];
    }
  };
  
  </script>

<template>
    <div class="container">
        <div class="upload">
            <input type="file" @change="onFileChange" />
            <button @click="submitFile" :disabled="!selectedFile || isLoading">
                <span v-if="isLoading">Uploading... {{ uploadProgress }}%</span>
                <span v-else>Upload File</span>
            </button>
        </div>
        <LoadingBar :isLoading="isLoading" />
        <div v-if="fileUrl">
            <a :href="fileUrl" download="processed_file.xlsx">Download Processed File</a>
        </div>
    
        <div v-if="errorMessage" class="error">{{ errorMessage }}</div>
    </div>
  </template>
  
  
  
  <style scoped>
  .container{
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  .error {
    color: red;
  }
  
  progress {
    width: 100%;
    margin-top: 10px;
  }

  </style>
  