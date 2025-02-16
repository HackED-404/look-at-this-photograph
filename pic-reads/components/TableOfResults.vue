<script setup lang="ts">

defineProps({
  people: Array,
})


 console.log(people)


const page = ref(1)
const pageCount = 10

const rows = computed(() => {
  return props.people.slice((page.value - 1) * pageCount, (page.value) * pageCount)
})
</script>

<template>
  <div>
    <!--<UTable :rows="people" />-->
    <UTable>
      <template #default="{ row }">
        <tr v-for="person in rows" :key="person.id">
          <td v-for="(value, key) in person" :key="key">{{ key }}: {{ value }}</td>
        </tr>
      </template>
    </UTable>

    <div class="flex justify-end px-3 py-3.5 border-t border-gray-200 dark:border-gray-700">
      <UPagination v-model="page" :page-count="pageCount" :total="people.length" />
    </div>
  </div>
</template>