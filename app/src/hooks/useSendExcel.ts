import axios from 'axios';

export const useSendExcel = () => {
  const sendExcel = async (data: File, onUploadProgress?: (progress: number) => void, onDownloadProgress?: (progress: number) => void) => {
    const formData = new FormData();
    formData.append('file', data);

    try {
      // Send the file to the API and track upload/download progress
      const response = await axios.post('http://localhost:8000/api/process-excel', formData, {
        responseType: 'blob',
        onUploadProgress: (progressEvent) => {
          if (onUploadProgress && progressEvent.total) {
            const percentCompleted = Math.round((progressEvent.loaded * 100) / progressEvent.total);
            onUploadProgress(percentCompleted); // Call the provided progress function
          }
        },
        onDownloadProgress: (progressEvent) => {
          if (onDownloadProgress && progressEvent.total) {
            const percentCompleted = Math.round((progressEvent.loaded * 100) / progressEvent.total);
            onDownloadProgress(percentCompleted); // Call the provided progress function
          }
        }
      });

      // Create a Blob from the response data
      const blob = new Blob([response.data], {
        type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
      });

      return { fileUrl: URL.createObjectURL(blob), error: null };
    } catch (error) {
      console.error(error);
      return { fileUrl: null, error: 'Error processing the file. Please try again.' };
    }
  };

  return { sendExcel };
};