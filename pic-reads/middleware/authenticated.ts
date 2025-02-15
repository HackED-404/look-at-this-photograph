export default defineNuxtRouteMiddleware(() => {
    const { loggedIn } = useUserSession()
    console.log("authenticated")
    
    // redirect the user to the login screen if they're not authenticated
    if (!loggedIn.value) {
      return navigateTo('/login')
    }
  })
  