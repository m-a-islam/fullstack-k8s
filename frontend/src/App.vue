<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

// State
const todos = ref([])
const newTodo = ref('')
const error = ref('')

// Configuration
// NOTE: We will change this URL later to point to the real Kubernetes backend!
const API_URL = 'http://192.168.178.28:8080'

// Fetch Todos on load
onMounted(async () => {
  await fetchTodos()
})

async function fetchTodos() {
  try {
    const response = await axios.get(`${API_URL}/todos`)
    todos.value = response.data
    error.value = ''
  } catch (e) {
    console.error(e)
    error.value = 'Could not connect to backend. Is the port-forward running?'
  }
}

async function addTodo() {
  if (!newTodo.value) return
  try {
    await axios.post(`${API_URL}/todos`, { title: newTodo.value })
    newTodo.value = ''
    await fetchTodos()
  } catch (e) {
    error.value = 'Error adding todo.'
  }
}
</script>

<template>
  <div class="container">
    <h1>📝 Kubernetes Todo List</h1>
    
    <div v-if="error" class="error">{{ error }}</div>

    <div class="input-group">
      <input 
        v-model="newTodo" 
        @keyup.enter="addTodo"
        placeholder="What needs to be done?" 
      />
      <button @click="addTodo">Add</button>
    </div>

    <ul>
      <li v-for="todo in todos" :key="todo.id">
        {{ todo.title }}
      </li>
    </ul>
  </div>
</template>

<style scoped>
.container { max-width: 500px; margin: 2rem auto; font-family: sans-serif; }
.input-group { display: flex; gap: 10px; margin-bottom: 20px; }
input { flex: 1; padding: 10px; font-size: 16px; }
button { padding: 10px 20px; cursor: pointer; background: #42b883; color: white; border: none; }
ul { list-style: none; padding: 0; }
li { padding: 10px; border-bottom: 1px solid #eee; }
.error { color: red; background: #fee; padding: 10px; margin-bottom: 10px; }
</style>