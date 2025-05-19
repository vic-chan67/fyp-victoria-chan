// translate.tpx
// Allows user to upload a road sign image and get a prediction of its meaning

import React, { useState, useEffect } from "react";
import { View, Text, Button, Image, StyleSheet } from "react-native";
import * as ImagePicker from "expo-image-picker";
import { useLanguage } from "../../context/LanguageContext";

export default function Translate() {
  const [image, setImage] = useState<string | null>(null);
  const [prediction, setPrediction] = useState<string | null>(null);
  const { language } = useLanguage();

  // Request permissions for image picker
  useEffect(() => {
    const getPermissions = async () => {
      const { status } = await ImagePicker.requestMediaLibraryPermissionsAsync();
      if (status !== "granted") {
        alert("Camera roll permissions required");
      }
    };

    getPermissions();
  }, []);

  // Function to pick an image
  const pickImage = async () => {
    let result = await ImagePicker.launchImageLibraryAsync({
      mediaTypes: ['images'],
      allowsEditing: true,
      aspect: [1, 1],
      quality: 1,
    });

    // Check if assets were returned and pick the first image asset
    if (result.assets && result.assets.length > 0) {
      const selectedImage = result.assets[0];
      setImage(selectedImage.uri); //set image URI
      getPrediction(selectedImage.uri); //send URI for prediction
    }
  };

  // Function to send the image to the Flask server for prediction
  const getPrediction = async (uri: string) => {
    const formData = new FormData();

    const file = {
      uri,
      type: "image/jpeg",
      name: "upload.jpg",
    };

    formData.append("image", file as any);
    formData.append("lang", String(language));

    try {
      const response = await fetch(`http://172.16.6.207:5001/pipeline?lang=${language}`, {
        method: "POST",
        body: formData,
      });

      const contentType = response.headers.get("Content-Type");
      const text = await response.text();

      // Check if the response is JSON and valid
      if (contentType && contentType.includes("application/json")) {
        const data = JSON.parse(text);

        const translatedLabel = data.results.map((res: any, index: number) =>
        `Sign ${index + 1}: ${res.translation}\n(${res.label})`
        ).join("\n\n");

        setPrediction(translatedLabel); //set prediction to translated label

      } else {
        // Handle non-JSON response
        console.error("Invalid response format:", text);
        setPrediction("Error: Invalid response format");
        }

      } catch (error) {
        console.error("Error fetching prediction:", error);
        setPrediction("Error parsing JSON");
      }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.text}>Upload a full road scene image to predict</Text>

      {image && <Image source={{ uri: image }} style={styles.image} />}
      {prediction && <Text style={styles.text}>{prediction}</Text>}

      <Button title="Pick an image" onPress={pickImage} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    paddingHorizontal: 20,
  },
  text: {
    fontSize: 18,
    marginVertical: 8,
  },
  image: {
    width: "90%",
    aspectRatio: 1.77,
    resizeMode: "contain",
    marginVertical: 10,
  },
});