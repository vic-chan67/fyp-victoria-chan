import { Tabs } from 'expo-router';

export default function TabLayout() {
  return (
    <Tabs>
      <Tabs.Screen name="index" options={{ title: 'Home' }} />
      <Tabs.Screen name="tester" options={{ title: 'Tester' }} />
      {/* <Tabs.Screen name="signs" options={{ title: 'Signs' }} /> */}
      <Tabs.Screen name="about" options={{ title: 'About' }} />
    </Tabs>
  );
}
