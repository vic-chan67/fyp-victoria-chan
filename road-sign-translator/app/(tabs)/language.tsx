import React from "react";
import { Text, View, StyleSheet } from "react-native";
import { Picker } from "@react-native-picker/picker";
import { useLanguage } from "../../context/LanguageContext";

export default function Language() {
  const { language, setLanguage } = useLanguage();

  return (
    <View style={styles.container}>
      <Text style={styles.text}>Choose your preferred language:</Text>
      <Picker
        selectedValue={language}
        onValueChange={(value) => setLanguage(value)}
        style={styles.picker}
      >
        <Picker.Item label="English" value="en" color="#fff"/>
        <Picker.Item label="French" value="fr" color="#fff"/>
        <Picker.Item label="Spanish" value="es" color="#fff"/>
        <Picker.Item label="German" value="de" color="#fff"/>
        <Picker.Item label="Italian" value="it" color="#fff"/>
      </Picker>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#25292e',
    justifyContent: 'center',
    alignItems: 'center',
  },
  text: {
    color: '#fff',
    fontSize: 20,
    marginBottom: 20,
    textAlign: 'center',
  },
  picker: {
    width: "100%",
    height: 50,
    color: '#fff',
  }
});
