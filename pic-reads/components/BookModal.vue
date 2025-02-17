<template>
    <div v-if="show" class="modal-overlay" @click.self="closeModal">
        <div class="modal">
            <button class="close-btn" @click="closeModal">X</button>
            <div class="modal-content">
                <img :src="book.coverImage" alt="Book Cover" class="book-cover" />
                <div class="book-details">
                    <h2>{{ book.title }}</h2>
                    <p><strong>Author:</strong> {{ book.authors }}</p>
                    <p><strong>Rating:</strong> {{ book.rating }}</p>
                    <p><strong>Synopsis:</strong> {{ book.synopsis }}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { defineProps, defineEmits } from "vue";

defineProps<{ show: boolean; book: any }>();
const emit = defineEmits(["close"]);

function closeModal() {
    emit("close");
}
</script>

<style>
.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
}

.modal {
    background: white;
    padding: 20px;
    border-radius: 8px;
    width: 50%;
    max-width: 600px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    position: relative;
}

.close-btn {
    position: absolute;
    top: 10px;
    right: 10px;
    border: none;
    background: red;
    color: white;
    padding: 5px;
    cursor: pointer;
}

.modal-content {
    display: flex;
    gap: 20px;
}

.book-cover {
    width: 150px;
    height: auto;
}

.book-details {
    flex-grow: 1;
}
</style>