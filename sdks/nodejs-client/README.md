# Chatbot Node.js SDK
This is the Node.js SDK for the Chatbot API, which allows you to easily integrate Chatbot into your Node.js applications.

## Install
```bash
npm install chatbot-client
```

## Usage
After installing the SDK, you can use it in your project like this:

```js
import { ChatbotClient, ChatClient, CompletionClient } from 'chatbot-client'

const API_KEY = 'your-api-key-here'
const user = `random-user-id`
const inputs = {
  name: 'test name a'
}
const query = "Please tell me a short story in 10 words or less."

// Create a completion client
const completionClient = new CompletionClient(API_KEY)
// Create a completion message
completionClient.createCompletionMessage(inputs, query, responseMode, user)

// Create a chat client
const chatClient = new ChatClient(API_KEY)
// Create a chat message in stream mode
const response = await chatClient.createChatMessage(inputs, query, user, true, null)
const stream = response.data;
stream.on('data', data => {
    console.log(data);
});
stream.on('end', () => {
    console.log("stream done");
});
// Fetch conversations
chatClient.getConversations(user)
// Fetch conversation messages
chatClient.getConversationMessages(conversationId, user)
// Rename conversation
chatClient.renameConversation(conversationId, name, user)


const client = new ChatbotClient(API_KEY)
// Fetch application parameters
client.getApplicationParameters(user)
// Provide feedback for a message
client.messageFeedback(messageId, rating, user)

```

Replace 'your-api-key-here' with your actual Chatbot API key.Replace 'your-app-id-here' with your actual Chatbot APP ID.

## License
This SDK is released under the MIT License.
