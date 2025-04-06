// tester.tpx
// Allows user to upload a road sign image and get a prediction of its meaning

import React, { useState, useEffect } from "react";
import { View, Text, Button, Image, StyleSheet } from "react-native";
import * as ImagePicker from "expo-image-picker";

export default function Tester() {
  const [image, setImage] = useState<string | null>(null);
  const [prediction, setPrediction] = useState<string | null>(null);

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
      uri: uri,
      type: "image/jpeg",
      name: "upload.jpg",
    };

    // Append the image file to formData
    formData.append("image", file as any);

    try {
      const response = await fetch("http://127.0.0.1:5001/predict", {
        method: "POST",
        body: formData,
      });
      const data = await response.json();  //parse response as JSON

      setPrediction(`${data.predicted_label} - ${data.description}`);
    } catch (error) {
      console.error("Error fetching prediction:", error);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.text}>Upload a road sign image to predict</Text>

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
  },
  text: {
    fontSize: 18,
    marginBottom: 10,
  },
  image: {
    width: 200,
    height: 200,
    marginBottom: 10,
  },
});