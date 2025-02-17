<script setup lang="ts">
import { useBookStore } from '@/stores/bookStore';
import { computed, ref } from 'vue';

interface Book {
    coverImage: string;
    title: string;
    authors: string | string[];
    rating: number;
    synopsis: string;
}

const bookStore = useBookStore();

// Define columns for NuxtUI Table
const columns = [{
    key: 'coverImage',
    label: 'Picture',
    slot: 'coverImage-data'
}, {
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
    label: 'Actions',
    slot: 'actions-data'
}];

// Pagination setup
const page = ref(1);
const pageCount = 10;

const rows = computed(() => {
    return bookStore.books.slice((page.value - 1) * pageCount, page.value * pageCount);
});

const totalBookCount = computed(() => bookStore.books.length);

// Remove book from bookshelf
function removeBook(index: number) {
    bookStore.removeBook(index);
}
</script>

<template>
    <div class="p-4">
        <h1 class="text-xl font-bold mb-4">My Bookshelf</h1>

        <UTable class="w-full rounded-lg shadow-md overflow-hidden"
            :empty-state="{ icon: 'i-heroicons-circle-stack-20-solid', label: 'No books added.' }" :columns="columns"
            :rows="rows">
            <!-- Cover Image Slot -->
            <template #coverImage-data="{ row }">
                <img :src="row.coverImage" alt="cover" class="w-12 h-12 rounded-lg" />
            </template>

            <!-- Synopsis Truncated -->
            <template #synopsis-data="{ row }">
                {{ row.synopsis.split(' ').slice(0, 10).join(' ') + (row.synopsis.split(' ').length > 10 ? '...' : '')
                }}
            </template>

            <!-- Actions Slot (Remove Button) -->
            <template #actions-data="{ row, index }">
                <UButton color="red" size="xs" @click="removeBook(index)">
                    Remove
                </UButton>
            </template>
        </UTable>

        <!-- Pagination Controls -->
        <div class="flex justify-end px-3 py-3.5 border-t border-gray-200 dark:border-gray-700">
            <UPagination v-model="page" :page-count="pageCount" :total="totalBookCount" />
        </div>
    </div>
</template>
