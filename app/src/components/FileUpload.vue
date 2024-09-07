<script setup lang="ts">
  import { ref } from 'vue';
  import axios from 'axios';
  
  const selectedFile = ref<File | null>(null); 
  const processedFileUrl = ref<string>(""); 
  const errorMessage = ref<string>("");  
  const isLoading = ref(false);


  const onFileChange = (event: Event) => {
    const target = event.target as HTMLInputElement;
    if (target.files && target.files[0]) {
      selectedFile.value = target.files[0]; // Store the selected file
    }
  };
  
  // Method to handle the file upload and process response
  const submitFile = async () => {
    if (!selectedFile.value) return; // Exit if no file is selected
    
    isLoading.value = true; 
    const formData = new FormData();
    formData.append('file', selectedFile.value);
  
    try {
      // Send the file to the API
      const response = await axios.post('http://localhost:8000/api/process-excel', formData, {
        responseType: 'blob',  // Treat response as a binary Blob
      });
  
      // Create a URL for the processed file so the user can download it
      const blob = new Blob([response.data], {
        type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
      });
  
      // Create a downloadable URL for the processed file
      processedFileUrl.value = URL.createObjectURL(blob);
      errorMessage.value = "";  // Clear any previous errors
    } catch (error) {
      errorMessage.value = 'Error processing the file. Please try again.';
      console.error(error);
    } finally {
      isLoading.value = false;
    }
  };
  </script>

<template>
    <div class="file-upload">
      <h2>Upload Excel File</h2>
      <input type="file" @change="onFileChange" />
  
      <button @click="submitFile" :disabled="!selectedFile">Upload File</button>
  
      <div v-if="processedFileUrl">
        <a :href="processedFileUrl" download="processed_file.xlsx">Download Processed File</a>
      </div>
      <div v-if="isLoading">Loading...</div>
  
      <div v-if="errorMessage" class="error">{{ errorMessage }}</div>
    </div>
  </template>
  
  
  <style scoped>
  .file-upload {
    text-align: center;
    margin: 20px;
  }
  
  button {
    margin-top: 10px;
  }
  
  .error {
    color: red;
    margin-top: 10px;
  }
  </style>
  