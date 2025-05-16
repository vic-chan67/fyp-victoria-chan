import { LanguageProvider } from '@/context/LanguageContext';
import { Stack } from 'expo-router';

export default function RootLayout() {
  return (
    <LanguageProvider>
      <Stack>
        <Stack.Screen name="(tabs)" options={{ headerShown: false }} />
        <Stack.Screen name="+not-found" />
      </Stack>
    </LanguageProvider>
  );
}
