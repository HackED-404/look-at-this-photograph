<script setup lang="ts">
import { ref, computed } from 'vue';

const props = defineProps<{
  people: Array<{ id: number, name: string, title: string, email: string, role: string }>
  loading: boolean
}>();
const columns = [{
  key: 'id',
  label: 'ID'
},
{
  key: 'name',
  label: 'Name'
}, {
  key: 'title',
  label: 'Title'
}, {
  key: 'email',
  label: 'Email'
}, {
  key: 'role',
  label: 'Role'
}]



 console.log(props.people);


const page = ref(1)
const pageCount = 10

const rows = computed(() => {
  return props.people ? props.people.slice((page.value - 1) * pageCount, (page.value) * pageCount) : [];
})
</script>

<template>
  <UTable
    class="w-full rounded-lg shadow-md overflow-hidden"
    :loading="loading"
    :loading-state="{ icon: 'i-heroicons-arrow-path-20-solid', label: 'Loading...' }"
    :progress="{ color: 'primary', animation: 'carousel' }"
    :empty-state="{ icon: 'i-heroicons-circle-stack-20-solid', label: 'No items.' }"
     
    :columns="columns" :rows="rows">
  </UTable>
  <div class="flex justify-end px-3 py-3.5 border-t border-gray-200 dark:border-gray-700">
    <UPagination v-model="page" :page-count="pageCount" :total="props.people.length" />
  </div>
  

</template>