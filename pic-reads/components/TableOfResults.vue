<script setup lang="ts">
import { ref, computed } from 'vue';
const columns = [{
  key: 'id',
  label: 'ID'
}, {
  key: 'name',
  label: 'User name'
}, {
  key: 'title',
  label: 'Job position'
}, {
  key: 'email',
  label: 'Email'
}, {
  key: 'role'
}]
const props = defineProps<{
  people: Array<{ id: string, name: string, title: string, email: string, role: string }>,
  
}>();



 console.log(props.people);


const page = ref(1)
const pageCount = 10

const rows = computed(() => {
  return props.people ? props.people.slice((page.value - 1) * pageCount, (page.value) * pageCount) : [];
})
</script>

<template>
  <UTable :columns="columns" :rows="rows" />
  <!--
  <div class="overflow-x-auto">
    <table class="min-w-full bg-white dark:bg-gray-800">
      <thead>
        <tr>
          <th class="py-3 px-6 text-left text-xs font-medium text-gray-500 uppercase tracking-wider dark:text-gray-400">Name</th>
          <th class="py-3 px-6 text-left text-xs font-medium text-gray-500 uppercase tracking-wider dark:text-gray-400">Title</th>
          <th class="py-3 px-6 text-left text-xs font-medium text-gray-500 uppercase tracking-wider dark:text-gray-400">Email</th>
          <th class="py-3 px-6 text-left text-xs font-medium text-gray-500 uppercase tracking-wider dark:text-gray-400">Role</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-gray-200 dark:divide-gray-700">
        <tr v-for="person in rows" :key="person.id">
          <td class="py-4 px-6 whitespace-nowrap dark:text-gray-200">{{ person.name }}</td>
          <td class="py-4 px-6 whitespace-nowrap dark:text-gray-200">{{ person.title }}</td>
          <td class="py-4 px-6 whitespace-nowrap dark:text-gray-200">{{ person.email }}</td>
          <td class="py-4 px-6 whitespace-nowrap dark:text-gray-200">{{ person.role }}</td>
        </tr>
      </tbody>
    </table>
  </div>
  <div v-if="props.people && props.people.length > 0">  

    <UTable>
      <template #default="{ row }">
        <tr v-for="person in rows" :key="person.id">
          <td v-for="(value, key) in person" :key="key">{{ key }}: {{ value }}</td>
        </tr>
      </tr>
      </template>
    </UTable>-->

    <div class="flex justify-end px-3 py-3.5 border-t border-gray-200 dark:border-gray-700">
      <UPagination v-model="page" :page-count="pageCount" :total="props.people.length" />
    </div>
  

</template>