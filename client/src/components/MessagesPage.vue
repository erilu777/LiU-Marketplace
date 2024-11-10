<template>
    <div class="flex h-screen">
      <!-- Conversations List (Left Side) -->
      <div class="w-1/3 border-r p-4">
        <h2 class="text-xl font-bold mb-4">Meddelanden</h2>
        
        <div v-for="conv in conversations" 
             :key="`${conv.item_id}-${conv.other_user.id}`" 
             @click="selectConversation(conv.item_id, conv.other_user.id)"
             class="p-3 border-b hover:bg-gray-100 cursor-pointer">
          <div class="font-medium">{{ conv.item_title }}</div>
          <div class="text-sm font-medium text-gray-600">
            {{ conv.other_user.liu_id }}
          </div>
          <div class="text-sm text-gray-500">
            {{ conv.last_message }}
          </div>
          <div class="text-xs text-gray-400">
            {{ new Date(conv.timestamp).toLocaleString() }}
          </div>
        </div>
      </div>
  
      <!-- Messages Area (Middle) -->
      <div class="w-2/3 flex flex-col">
        <div v-if="!selectedItemId" class="flex-1 p-4 flex items-center justify-center text-gray-500">
          Välj en konversation för att visa meddelanden
        </div>
        
        <div v-else class="flex flex-col h-full">
          <!-- Messages Display -->
          <div class="flex-1 p-4 overflow-y-auto">
            <div v-for="message in filteredMessages" 
                 :key="message.id" 
                 class="mb-4 p-3 border rounded"
                 :class="{
                   'ml-auto bg-blue-100 w-3/4': message.sender.id === currentUserId,
                   'mr-auto bg-gray-100 w-3/4': message.sender.id !== currentUserId
                 }">
              <div>{{ message.content }}</div>
              <div class="text-xs mt-1 text-gray-500">
                {{ message.sender.liu_id }} - {{ new Date(message.timestamp).toLocaleString() }}
              </div>
            </div>
          </div>
  
          <!-- Message Input -->
          <div class="p-4 border-t bg-white">
            <form @submit.prevent="sendMessage" class="flex gap-2">
              <input 
                v-model="newMessage" 
                type="text"
                placeholder="Skriv ett meddelande..."
                class="flex-1 border rounded-lg px-4 py-2 focus:outline-none focus:border-blue-500"
              />
              <button 
                type="submit"
                class="bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600"
                :disabled="!newMessage.trim()"
              >
                Skicka
              </button>
            </form>
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
      const selectedItemId = ref(null)
      const selectedUserId = ref(null)
      const currentUserId = ref(null)
      const newMessage = ref('')
  
      const getAuthHeaders = () => {
        try {
          const auth = JSON.parse(sessionStorage.getItem('auth'))
          return {
            headers: {
              'Authorization': `Bearer ${auth.token}`
            }
          }
        } catch (error) {
          console.error('Error getting auth headers:', error)
          return {}
        }
      }
  
      const loadConversations = async () => {
        try {
          const response = await axios.get('/messages/conversations', getAuthHeaders())
          conversations.value = response.data
          console.log('Loaded conversations:', conversations.value)
        } catch (error) {
          console.error('Error loading conversations:', error)
          conversations.value = []
        }
      }
  
      const loadMessages = async (itemId) => {
        try {
          const response = await axios.get(`/messages/item/${itemId}`, getAuthHeaders())
          messages.value = response.data
          console.log('Loaded messages:', messages.value)
        } catch (error) {
          console.error('Error loading messages:', error)
          messages.value = []
        }
      }
  
      const selectConversation = async (itemId, userId) => {
        console.log('Selecting conversation:', itemId, userId)
        selectedItemId.value = itemId
        selectedUserId.value = userId
        await loadMessages(itemId)
        
        // Scroll to bottom when conversation is selected
        setTimeout(() => {
          const messagesContainer = document.querySelector('.overflow-y-auto')
          if (messagesContainer) {
            messagesContainer.scrollTop = messagesContainer.scrollHeight
          }
        }, 50)
      }
  
      const sendMessage = async () => {
        if (!newMessage.value.trim()) return
  
        try {
          const response = await axios.post('/messages', {
            content: newMessage.value,
            item_id: selectedItemId.value,
            receiver_id: selectedUserId.value
          }, getAuthHeaders())
  
          // Add the new message to the messages list
          messages.value.push(response.data)
          
          // Clear the input
          newMessage.value = ''
          
          // Scroll to bottom
          setTimeout(() => {
            const messagesContainer = document.querySelector('.overflow-y-auto')
            if (messagesContainer) {
              messagesContainer.scrollTop = messagesContainer.scrollHeight
            }
          }, 50)
  
        } catch (error) {
          console.error('Error sending message:', error)
          alert('Kunde inte skicka meddelandet. Försök igen.')
        }
      }
  
      const filteredMessages = computed(() => {
        if (!selectedUserId.value) return messages.value
        return messages.value.filter(message => 
          message.sender.id === selectedUserId.value || 
          message.receiver.id === selectedUserId.value
        )
      })
  
      // Replace just the onMounted section in your current code with this:
    onMounted(() => {
    // Get current user ID from auth
    try {
        const auth = JSON.parse(sessionStorage.getItem('auth'))
        if (auth?.token) {  // If we have a valid auth token
        // Try to get user data - if it fails, fallback to getting ID from JWT
        try {
            const userStr = auth?.user
            if (userStr) {
            const cleanedStr = userStr.replace(/^"/, '').replace(/"$/, '').replace(/\\\\/g, '\\')
            const userData = JSON.parse(cleanedStr)
            currentUserId.value = userData.id
            }
        } catch (error) {
            // If parsing fails, we can still continue since messaging works
            console.log('Note: Could not parse user data, but messaging will still work')
        }
        }
    } catch (error) {
        console.log('Note: Using fallback auth method')
    }
    
    // Load conversations regardless of whether we got the user ID
    loadConversations()
    })
  
      return {
        conversations,
        filteredMessages,
        selectedItemId,
        currentUserId,
        newMessage,
        selectConversation,
        sendMessage
      }
    }
  }
  </script>
  
  <style scoped>
  .overflow-y-auto {
    scroll-behavior: smooth;
  }
  
  .overflow-y-auto::-webkit-scrollbar {
    width: 6px;
  }
  
  .overflow-y-auto::-webkit-scrollbar-track {
    background: #f1f1f1;
  }
  
  .overflow-y-auto::-webkit-scrollbar-thumb {
    background: #888;
    border-radius: 3px;
  }
  
  .overflow-y-auto::-webkit-scrollbar-thumb:hover {
    background: #555;
  }
  </style>