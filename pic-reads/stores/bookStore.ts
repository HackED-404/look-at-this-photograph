import { defineStore } from 'pinia';

export const useBookStore = defineStore('bookStore', {
  state: () => ({
    books: [] as Array<{ title: string; author: string; cover: string }>,
  }),
  actions: {
    addBook(book: { title: string; author: string; cover: string }) {
      this.books.push(book);
    },
    removeBook(index: number) {
      this.books.splice(index, 1);
    },
  },
});
