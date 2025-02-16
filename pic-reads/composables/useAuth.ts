import { useSupabaseClient } from '#imports';

export const useAuth = () => {
  const supabase = useSupabaseClient();

  const login = async () => {
    const { error } = await supabase.auth.signInWithOAuth({
      provider: 'github',
    });

    if (error) {
      console.error(error);
    }
  };

  const logout = async () => {
    const { error } = await supabase.auth.signOut();
    if (error) {
      console.error(error);
    }
  };

  return { login, logout };
};
