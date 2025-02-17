<script setup lang="ts">
import { useBookStore } from '@/stores/bookStore';
import { ref, computed } from 'vue';

interface Book {
  coverImage: string;
  title: string;
  authors: string | string[];
  rating: number;
  synopsis: string;
}

const props = defineProps<{
  books: Book[],
  loading: boolean
}>();
const columns = [{
  key: 'coverImage',
  label: 'Picture',
  slot: 'coverImage-data'
},
{
  key: 'title',
  label: 'Title'
}, {
  key: 'authors',
  label: 'Authors'
}, {
  key: 'rating',
  label: 'Rating'
}, {
  key: 'synopsis',
  label: 'Synopsis'
}, {
  key: 'actions',
  label: '',
  slot: 'actions-data',
  class: 'w-10' // Adjust column ]
}];



console.log(props.books);


const page = ref(1)
const pageCount = 10

const rows = computed(() => {
  return props.books ? props.books.slice((page.value - 1) * pageCount, (page.value) * pageCount) : [];
})

const totalBookCount = computed(() => {
  return props.books ? props.books.length : 0;
})

watch(rows, (newRows) => {
  console.log("Rows updated:", newRows);
}, { deep: true });



const bookStore = useBookStore();

// const addToMyBooks = (book) => {
//   bookStore.addBook(book);
// };

function addToMyBooks(row) {
  bookStore.addBook(row);
}

function select(row) {
  return;
}

</script>

<template>
  <UTable @select="select" class="w-full rounded-lg shadow-md overflow-hidden" :loading="loading"
    :loading-state="{ icon: 'i-heroicons-arrow-path-20-solid', label: 'Loading...' }"
    :progress="{ color: 'primary', animation: 'carousel' }"
    :empty-state="{ icon: 'i-heroicons-circle-stack-20-solid', label: 'No items.' }" :columns="columns" :rows="rows">

    <template #coverImage-data="{ row }">
      <img :src="row.coverImage" alt="cover" class="w-12 h-12 rounded-lg" />
      <!-- <span :class="[selected.find(person => person.id === row.id) && 'text-primary-500 dark:text-primary-400']">{{ row.name }}</span> -->
    </template>
    <template #synopsis-data="{ row }">
      {{ row.synopsis.split(' ').slice(0, 10).join(' ') + (row.synopsis.split(' ').length > 10 ? '...' : '') }}
    </template>
    <template #actions-data="{ row }">
      <button @click.stop="addToMyBooks(row)" class="outline-none border-none p-0">
        <Icon name="material-symbols:add-box-rounded" class="w-6 h-6 bg-emerald-300" />
      </button>
    </template>
  </UTable>
  <div class="flex justify-end px-3 py-3.5 border-t border-gray-200 dark:border-gray-700">
    <UPagination v-model="page" :page-count="pageCount" :total="totalBookCount" />
  </div>


</template>