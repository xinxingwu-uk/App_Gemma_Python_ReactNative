import React, { useState } from "react";
import {
  SafeAreaView,
  View,
  Text,
  TextInput,
  Button,
  ActivityIndicator,
  StyleSheet,
} from "react-native";

const HF_API_URL = "https://router.huggingface.co/v1/chat/completions";
// Put your own token here, but NEVER share it or commit it to GitHub
const HF_TOKEN = "Your Token";

async function askGemma(prompt) {
  const body = {
    model: "google/gemma-2-2b-it",
    messages: [{ role: "user", content: prompt }],
    max_tokens: 128,
    temperature: 0.5,
  };

  const response = await fetch(HF_API_URL, {
    method: "POST",
    headers: {
      "Authorization": "Bearer " + HF_TOKEN,
      "Content-Type": "application/json",
    },
    body: JSON.stringify(body),
  });

  const data = await response.json();
  return data.choices[0].message.content;
}

function App() {
  const [prompt, setPrompt] = useState("Write a program from 1 to 100.");
  const [answer, setAnswer] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [errorText, setErrorText] = useState("");

  async function handleSend() {
    if (!prompt.trim()) {
      return;
    }

    setIsLoading(true);
    setErrorText("");
    setAnswer("");

    try {
      const text = await askGemma(prompt);
      setAnswer(text);
    } catch (error) {
      console.log(error);
      setErrorText("Something went wrong. Please try again.");
    } finally {
      setIsLoading(false);
    }
  }

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.inner}>
        <Text style={styles.title}>Gemma 2B Chat</Text>

        <Text style={styles.label}>Prompt:</Text>
        <TextInput
          style={styles.input}
          multiline
          value={prompt}
          onChangeText={setPrompt}
          placeholder="Type your prompt here..."
        />

        <View style={styles.buttonBox}>
          <Button
            title={isLoading ? "Generating..." : "Send"}
            onPress={handleSend}
            disabled={isLoading}
          />
        </View>

        {isLoading && <ActivityIndicator style={styles.loading} />}

        {errorText ? <Text style={styles.error}>{errorText}</Text> : null}

        {answer ? (
          <View style={styles.answerBox}>
            <Text style={styles.label}>Response:</Text>
            <Text style={styles.answerText}>{answer}</Text>
          </View>
        ) : null}
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#ffffff",
  },
  inner: {
    flex: 1,
    padding: 16,
  },
  title: {
    fontSize: 20,
    fontWeight: "600",
    marginBottom: 12,
  },
  label: {
    fontSize: 14,
    marginBottom: 4,
  },
  input: {
    borderWidth: 1,
    borderColor: "#cccccc",
    borderRadius: 8,
    padding: 8,
    minHeight: 80,
    textAlignVertical: "top",
    marginBottom: 12,
  },
  buttonBox: {
    marginBottom: 12,
  },
  loading: {
    marginBottom: 12,
  },
  error: {
    color: "red",
    marginBottom: 12,
  },
  answerBox: {
    flex: 1,
    borderWidth: 1,
    borderColor: "#dddddd",
    borderRadius: 8,
    padding: 8,
  },
  answerText: {
    fontSize: 14,
  },
});

export default App;
