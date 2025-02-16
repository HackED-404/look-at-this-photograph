// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: ["@nuxt/ui", "nuxt-auth-utils", '@nuxtjs/supabase',],
  compatibilityDate: "2025-02-15",
  imports: {
    dirs: ['composables', 'components'], 
  },
  supabase: {
    // Add your Supabase configuration here
    url: process.env.SUPABASE_URL,
    key: process.env.SUPABASE_KEY,
  },
})