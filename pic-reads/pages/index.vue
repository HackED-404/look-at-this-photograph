<template>

  <div>
    <div class="dropzone" @dragover.prevent @dragenter.prevent @dragstart.prevent
      @drop.prevent="handleFileChange($event.dataTransfer || $event)">
      <input id="file-input" type="file" accept="image/png, image/jpeg" @change="handleFileChange($event.target)"
        required />
      <h2 class="text-neutral-950" for="file-input">Click or Drag N Drop Image</h2>
      <img v-bind:src="typeof preview === 'string' ? preview : undefined" />
    </div>

    <button type="submit" v-on:click="upload">Upload</button>

    <TableOfResults :books="books" :loading="isLoading" />
  </div>




</template>

<script setup lang="ts">
import { ref } from 'vue'
interface Book {
  coverImage: string;
  title: string;
  authors: string | string[];
  rating: number;
  synopsis: string;
}

const books = ref<Book[]>([])

const fileName = ref('');
const preview = ref<string | ArrayBuffer | null>(null);
const preset = ref('abc');
const formData = ref<FormData | null>(null);
const success = ref('');
const isLoading = ref(false);

function handleFileChange(event: Event | DataTransfer) {
  const input = event instanceof DataTransfer ? event.files?.[0] : (event.target as HTMLInputElement)?.files?.[0];
  if (!input) return;

  fileName.value = input.name;

  formData.value = new FormData();
  formData.value.append("upload_preset", preset.value);
  formData.value.append("file", input);

  let reader = new FileReader();
  reader.readAsDataURL(input);

  reader.onload = (e) => {
    if (e.target) {
      preview.value = e.target.result;
    }
  };
}

async function upload() {
  try {
    console.log("Uploading.*.*.*.");
    isLoading.value = true;
    const res = await fetch(
      `http://localhost:8008/upload`,
      {
        method: "POST",
        body: formData.value,
      },
    );

    const data = await res.json();
    console.log("Data:");
    console.dir(data);
    const flattenedData = data.flatMap((x) => x);
    console.dir(flattenedData);
    books.value = flattenedData;
    console.log("Upload successful:", data);
    isLoading.value = false;
    // fileName.value = "";
    // preview.value = null;
    // formData.value = null;
    success.value = data.public_id;
  } catch (error) {
    console.error("Error:", error);
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  display: flex;
  flex-direction: column;
}

.dropzone {
  height: fit-content;
  min-height: 200px;
  max-height: 400px;
  width: 600px;
  background: #f0f4f8;
  border-radius: 10px;
  border: 2px dashed #3498db;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin: 20px auto;
  padding: 20px;
  transition: background-color 0.3s, border-color 0.3s;
}

.dropzone:hover {
  background-color: #e0e7ef;
  border-color: #2980b9;
}

input[type="file"] {
  position: absolute;
  opacity: 0;
  width: inherit;
  min-height: 200px;
  max-height: 400px;
  cursor: pointer;
}

img {
  width: 50%;
  height: 50%;
  margin-top: 10px;
  border-radius: 10px;
}

button {
  background-color: #3498db;
  border: none;
  border-radius: 5px;
  color: white;
  cursor: pointer;
  display: flex;
  align-self: center;
  font-size: 1rem;
  margin: 20px auto;
  padding: 1em 2em;
  text-align: center;
  text-transform: uppercase;
  font-family: "Montserrat", sans-serif;
  font-weight: 700;
  transition: background-color 0.3s, box-shadow 0.3s;

}
button:hover {
  background-color: #2980b9;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}
</style>
