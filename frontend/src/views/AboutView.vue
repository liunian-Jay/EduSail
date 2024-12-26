<template>
  <div id="app">
    <div class="chat-container">
      <div class="messages">
        <div v-for="(message, index) in messages" :key="index" class="message">
          <div class="message-content">{{ message.text }}</div>
        </div>
      </div>
      <div class="input-container">
        <input v-model="userInput" @keyup.enter="sendMessage" placeholder="Type a message..." />
        <button @click="sendMessage">Send</button>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";

export default {
  name: "AboutView",
  setup() {
    const messages = ref([]);
    const userInput = ref("");

    // 发送消息
    const sendMessage = async () => {
      if (userInput.value.trim() === "") return;

      // 用户输入消息
      const userMessage = { text: userInput.value, sender: "user" };
      messages.value.push(userMessage);

      // 清空输入框
      const message = userInput.value;
      userInput.value = "";

      try {
        // 请求接口
        const response = await fetch("http://127.0.0.1:15000/test/test", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ message }),
        });
        const data = await response.json();

        // 模拟从接口获取的聊天消息
        const botMessage = { text: data.reply, sender: "bot" };
        messages.value.push(botMessage);
      } catch (error) {
        const errorMessage = { text: "Error connecting to the server", sender: "bot" };
        messages.value.push(errorMessage);
      }
    };

    return {
      messages,
      userInput,
      sendMessage,
    };
  },
};
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  background-color: #f1f1f1;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.chat-container {
  background-color: white;
  width: 400px;
  max-width: 100%;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  padding: 20px;
  display: flex;
  flex-direction: column;
}

.messages {
  flex-grow: 1;
  overflow-y: auto;
  margin-bottom: 10px;
}

.message {
  margin: 10px 0;
}

.message-content {
  padding: 8px;
  border-radius: 10px;
  background-color: #e1e1e1;
  max-width: 80%;
}

.message.sender-user .message-content {
  background-color: #aad8ff;
  align-self: flex-end;
}

.input-container {
  display: flex;
  gap: 10px;
}

input {
  flex-grow: 1;
  padding: 8px;
  border-radius: 5px;
  border: 1px solid #ccc;
}

button {
  padding: 8px 12px;
  border-radius: 5px;
  border: 1px solid #ccc;
  cursor: pointer;
}
</style>
