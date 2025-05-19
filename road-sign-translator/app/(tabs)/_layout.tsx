import { Tabs } from 'expo-router';

export default function TabLayout() {
  return (
    <Tabs>
      <Tabs.Screen name="index" options={{ title: 'Home' }} />
      <Tabs.Screen name="translate" options={{ title: 'Translate' }} />
      <Tabs.Screen name="language" options={{ title: 'Language' }} />
    </Tabs>
  );
}
