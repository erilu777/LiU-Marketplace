<template>
  <div class="messages-container">
    <!-- Left side: Conversations list -->
    <div class="conversations-list">
      <h2>Meddelanden</h2>
      <div v-for="conv in groupedConversations" 
           :key="`${conv.item_id}-${conv.other_user.id}`" 
           @click="selectConversation(conv)"
           class="conversation-item"
           :class="{'selected': isSelectedConversation(conv)}">
        <div class="conversation-title">{{ conv.item_title }}</div>
        <div class="conversation-user">{{ conv.other_user.liu_id }}</div>
        <div class="conversation-preview">{{ conv.last_message }}</div>
        <div class="conversation-time">{{ new Date(conv.timestamp).toLocaleString() }}</div>
      </div>
    </div>

    <!-- Right side: Messages -->
    <div class="messages-area">
      <div v-if="!selectedConversation" class="no-conversation">
        Välj en konversation för att visa meddelanden
      </div>

      <div v-else class="conversation-view">
        <div class="messages-list">
          <div v-for="message in messages" 
            :key="message.id" 
            class="message"
            :class="getMessageClass(message)">
            <div class="message-wrapper">
              <div class="message-content">{{ message.content }}</div>
              <div class="message-info">
                {{ message.sender.liu_id }} - {{ new Date(message.timestamp).toLocaleString() }}
              </div>
            </div>
          </div>
        </div>
        <div class="message-input">
          <textarea 
            v-model="newMessage" 
            @keydown.enter.exact.prevent="sendMessage"
            @keydown.shift.enter.prevent="newMessage += '\n'"
            @input="adjustTextareaHeight"
            placeholder="Skriv ett meddelande..."
            ref="messageInput"
        ></textarea>
          <button @click="sendMessage">Skicka</button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'

export default {
  setup() {
    const conversations = ref([])
    const messages = ref([])
    const selectedConversation = ref(null)
    const newMessage = ref('')
    const currentUserId = ref(null)

    // Move sorting to the loadConversations function
    const loadConversations = async () => {
      try {
        const response = await axios.get('/messages/conversations', getAuthHeaders())
        // Sort conversations here instead of in computed property
        conversations.value = response.data.sort((a, b) => 
          new Date(b.timestamp) - new Date(a.timestamp)
        )
      } catch (error) {
        console.error('Error loading conversations:', error)
      }
    }

    // Computed property now just returns the sorted array
    const groupedConversations = computed(() => conversations.value)

    const getAuthHeaders = () => {
      const auth = JSON.parse(sessionStorage.getItem('auth'))
      return {
        headers: {
          'Authorization': `Bearer ${auth.token}`
        }
      }
    }

    const isSelectedConversation = (conv) => {
      return selectedConversation.value && 
             selectedConversation.value.item_id === conv.item_id && 
             selectedConversation.value.other_user.id === conv.other_user.id
    }

    const loadMessages = async () => {
  if (!selectedConversation.value) return

  try {
    const response = await axios.get(
      `/messages/item/${selectedConversation.value.item_id}?user_id=${selectedConversation.value.other_user.id}`, 
      getAuthHeaders()
    )
    messages.value = response.data
  } catch (error) {
    console.error('Error loading messages:', error)
    messages.value = []
  }
}

    const selectConversation = async (conversation) => {
      selectedConversation.value = conversation
      await loadMessages()
    }

    const sendMessage = async () => {
      if (!newMessage.value.trim() || !selectedConversation.value) return

      try {
        const response = await axios.post('/messages', {
          content: newMessage.value,
          item_id: selectedConversation.value.item_id,
          receiver_id: selectedConversation.value.other_user.id
        }, getAuthHeaders())
        
        messages.value.push(response.data)
        newMessage.value = ''
      } catch (error) {
        console.error('Error sending message:', error)
      }
    }

    const getMessageClass = (message) => {
    const senderId = Number(message.sender.id);
    const userId = Number(currentUserId.value);
    
    return {
      'sent': senderId === userId,
      'received': senderId !== userId
    };
  };

    const getCurrentUserId = () => {
  try {
    const auth = sessionStorage.getItem('auth')
    if (auth) {
      const authData = JSON.parse(auth)
      if (authData.user) {
        const userStr = authData.user.replace(/\\054/g, ',').replace(/\\\\/g, '\\')
        const cleanUserStr = JSON.parse(JSON.parse(userStr))
        currentUserId.value = cleanUserStr.id
      }
    }
  } catch (error) {
    console.error('Error getting user ID')
  }
}

    const messageInput = ref(null)

    const adjustTextareaHeight = () => {
    const textarea = messageInput.value
    if (textarea) {
      // Reset height before calculating scrollHeight
      textarea.style.height = '36px'  // Match initial height
      
      // Calculate new height based on content
      const newHeight = Math.min(textarea.scrollHeight, 100)
      textarea.style.height = newHeight + 'px'
      
      // Adjust scroll position if needed
      if (textarea.scrollHeight > 100) {
        textarea.style.overflowY = 'auto'
      } else {
        textarea.style.overflowY = 'hidden'
      }
    }
  }

    // Initialize
    onMounted(() => {
      getCurrentUserId()
      loadConversations()
    })

    return {
      groupedConversations,
      messages,
      selectedConversation,
      currentUserId,
      newMessage,
      isSelectedConversation,
      selectConversation,
      sendMessage,
      getMessageClass,

      messageInput,
      adjustTextareaHeight
    }
  }
}
</script>

  <!-- Keep your existing styles -->
  
  <style scoped>
  .messages-container {
    display: flex;
    /* This will leave space just for header (80px) and a small gap (20px) */
    height: calc(100vh - 100px);
    background-color: white;
    margin-bottom: 20px;  /* Small gap before footer */
    position: relative;
  }
  
  .conversations-list {
    width: 300px;
    border-right: 1px solid #e5e7eb;
    overflow-y: auto;
    background-color: white;
  }
  
  .conversations-list h2 {
    padding: 20px;
    font-size: 24px;
    font-weight: bold;
    color: #0C254A;
    border-bottom: 1px solid #e5e7eb;
  }
  
  .conversation-item {
    padding: 15px 20px;
    border-bottom: 1px solid #e5e7eb;
    cursor: pointer;
  }
  
  .conversation-item:hover {
    background-color: #f3f4f6;
  }
  
  .conversation-item.selected {
    background-color: #e5e7eb;
  }
  
  .conversation-title {
    font-weight: bold;
    color: #0C254A;
  }
  
  .conversation-user {
    font-size: 14px;
    color: #4b5563;
    margin-top: 4px;
  }
  
  .conversation-preview {
    font-size: 14px;
    color: #6b7280;
    margin-top: 4px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  
  .conversation-time {
    font-size: 12px;
    color: #9ca3af;
    margin-top: 4px;
  }
  
  .messages-area {
    flex: 1;
    display: flex;
    flex-direction: column;
    background-color: #f9fafb;
    position: relative;
  }
  
  .no-conversation {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #6b7280;
    font-size: 16px;
  }
  
  .conversation-view {
    flex: 1;
    display: flex;
    flex-direction: column;
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
  }
  
  .messages-list {
    flex: 1;
    padding: 20px;
    overflow-y: auto;
    background-color: #f0f2f5;
  }
  
  .message {
    display: flex;
    margin-bottom: 10px;
    width: 100%;
  }
  
  .message.sent {
    justify-content: flex-end;
  }
  
  .message.received {
    justify-content: flex-start;
  }
  
  .message-wrapper {
    max-width: 60%;
  }
  
  .message-content {
    padding: 12px 16px;
    border-radius: 18px;
    font-size: 14px;
    word-wrap: break-word;
    max-width: fit-content;
  }
  
  .sent .message-content {
    background-color: #0c264d;
    color: white;
    border-bottom-right-radius: 4px;
    margin-left: auto;
  }
  
  .received .message-content {
    background-color: #4e8cff;
    color: white;
    border-bottom-left-radius: 4px;
    margin-right: auto;
  }
  
  .message-info {
    font-size: 11px;
    color: #65676B;
    margin-top: 4px;
    padding: 0 8px;
  }
  
  .sent .message-info {
    text-align: right;
  }
  
  .received .message-info {
    text-align: left;
  }
  
  .message-input {
  padding: 16px;
  background-color: white;
  border-top: 1px solid #E4E6EB;
  display: flex;
  align-items: center;  /* This centers items vertically */
  gap: 12px;
  position: sticky;
  bottom: 0;
}

.message-input textarea {
  flex: 1;
  padding: 8px 16px;
  border: 1px solid #E4E6EB;
  border-radius: 20px;
  outline: none;
  font-size: 14px;
  resize: none;
  height: 36px;
  max-height: 100px;
  line-height: 20px;
  overflow-y: auto;
  display: block;  /* Added this */
}
  
  .message-input textarea:focus {
    border-color: #0c264d;
  }
  
  .message-input button {
  padding: 8px 20px;
  background-color: #0c264d;
  color: white;
  border: none;
  border-radius: 20px;
  cursor: pointer;
  font-size: 14px;
  transition: background-color 0.2s;
  height: 36px;  /* Match textarea height */
  white-space: nowrap;  /* Prevent button text wrapping */
}
  
  .message-input button:hover {
    background-color: #0a1f3d;
  }
  
  /* Scrollbar styling */
  .messages-list::-webkit-scrollbar {
    width: 8px;
  }
  
  .messages-list::-webkit-scrollbar-track {
    background: transparent;
  }
  
  .messages-list::-webkit-scrollbar-thumb {
    background-color: rgba(0, 0, 0, 0.2);
    border-radius: 4px;
  }
  
  .messages-list::-webkit-scrollbar-thumb:hover {
    background-color: rgba(0, 0, 0, 0.3);
  }

  </style>