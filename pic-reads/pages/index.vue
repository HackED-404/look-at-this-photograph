
<template>
  <NuxtLayout>
    <div>
      <div
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
    </div>
    <button type="submit" v-on:click="upload">Upload</button>

    <TableOfResults
        
        :people="results"></TableOfResults>

  </NuxtLayout>

  
</template>

<script>
const results = [{
  id: 1,
  name: 'Lindsay Walton',
  title: 'Front-end Developer',
  email: 'lindsay.walton@example.com',
  role: 'Member'
}, {
  id: 2,
  name: 'Courtney Henry',
  title: 'Designer',
  email: 'courtney.henry@example.com',
  role: 'Admin'
}, {
  id: 3,
  name: 'Tom Cook',
  title: 'Director of Product',
  email: 'tom.cook@example.com',
  role: 'Member'
}, {
  id: 4,
  name: 'Whitney Francis',
  title: 'Copywriter',
  email: 'whitney.francis@example.com',
  role: 'Admin'
}, {
  id: 5,
  name: 'Leonard Krasner',
  title: 'Senior Designer',
  email: 'leonard.krasner@example.com',
  role: 'Owner'
}, {
  id: 6,
  name: 'Floyd Miles',
  title: 'Principal Designer',
  email: 'floyd.miles@example.com',
  role: 'Member'
}, {
  id: 7,
  name: 'Emily Selman',
  title: 'VP, User Experience',
  email: '',
  role: 'Admin'
}, {
  id: 8,
  name: 'Kristin Watson',
  title: 'VP, Human Resources',
  email: '',
  role: 'Member'
}, {
  id: 9,
  name: 'Emma Watson',
  title: 'Front-end Developer',
  email: '',
  role: 'Member'
}, {
  id: 10,
  name: 'John Doe',
  title: 'Designer',
  email: '',
  role: 'Admin'
}, {
  id: 11,
  name: 'Jane Doe',
  title: 'Director of Product',
  email: '',
  role: 'Member'
}, {
  id: 12,
  name: 'John Smith',
  title: 'Copywriter',
  email: '',
  role: 'Admin'
}, {
  id: 13,
  name: 'Jane Smith',
  title: 'Senior Designer',
  email: '',
  role: 'Owner'
}]

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
      /**
      const data = await res.json();
      this.fileName = "";
      this.preview = null;
      this.formData = null;
      this.success = data.public_id; */
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
