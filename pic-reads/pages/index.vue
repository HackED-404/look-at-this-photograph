<template >
  <div
      v-if="isVisible"
      class="dropzone"
      @dragover.prevent
      @dragenter.prevent
      @dragstart.prevent
      @drop.prevent="handleFileChange($event.dataTransfer)"
  >
    <input
        id="file-input"
        type="file"
        accept="image/png, image/jpeg"
        @change="handleFileChange($event.target)"
        required
    />
    <h2 for="file-input">Click or Drag N Drop Image</h2>
    <img v-bind:src="preview" />
    <h3 v-if="preview">File name: {{ fileName }}</h3>
  </div>
  <div v-if="isHidden">  <TableOfResults></TableOfResults></div>

  <button type="submit" v-if="isVisible" v-on:click="upload">Upload</button>
  <button type="submit" v-if="isHidden" v-on:click="toggleVisibility">New Image</button>
</template>
<script >

export default {
  name: "App",
  data() {
    return {
      fileName: "",
      preview: null,
      preset: "abc",
      formData: null,
      cloudName: "abc",
      success: "",
      isVisible: true, // Initially the element will be visible
      isHidden: false, // Initially this element is not hidden
    };
  },
  methods: {
    handleFileChange: function (event) {
      this.file = event.files[0];
      this.fileName = this.file.name;

      this.formData = new FormData();
      this.formData.append("upload_preset", this.preset);

      let reader = new FileReader();
      reader.readAsDataURL(this.file);

      reader.onload = (e) => {
        this.preview = e.target.result;
        this.formData.append("file", this.preview);
      };
    },
    upload: async function () {
      const res = await fetch(
          `https://api.cloudinary.com/v1_1/${this.cloudName}/image/upload`,
          {
            method: "POST",
            body: this.formData,
          }
      );
      console.log(res)
      const data = await res.json();
      this.fileName = "";
      this.preview = null;
      this.formData = null;
      this.success = data.public_id;
      this.toggleVisibility()
    },
    toggleVisibility() {
      this.isVisible = !this.isVisible; // Toggles visibility
      this.isHidden = !this.isHidden;   // Toggles hidden state for the second element
    },
  },
};
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
  background: #fdfdfd;
  border-radius: 5px;
  border: 2px dashed #000;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin: 0 auto;
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
}
button {
  background-color: transparent;
  border: 2px solid #e74c3c;
  border-radius: 1em;
  color: #e74c3c;
  cursor: pointer;
  display: flex;
  align-self: center;
  font-size: 1rem;
  margin: 20px;
  padding: 1.2em 2.4em;
  text-align: center;
  text-transform: uppercase;
  font-family: "Montserrat", sans-serif;
  font-weight: 700;
}
</style>
