<template>
<div class="container-wrapper">
    <div class="container">
        <h2>LOGIN</h2>
        <div class="form-group">
            <label for="username">Username:</label>
            <input id="username" v-model="username" @keyup.enter="handleLogin" />
        </div>
        <div class="form-group">
            <label for="password">Password:</label>
            <input id="password" v-model="password" type="password" @keyup.enter="handleLogin" />
        </div>
        
        
        <div class="buttons">
          <button :disabled="loading" @click="handleLogin">
              {{ loading ? "Loading..." : "Login" }}
          </button>
          <button :disabled="loading" @click="goRegister">Registrasi</button>
        </div>
    </div>
</div>
</template>

<script setup>
import { ref } from "vue";
import { useAuthStore } from "../store/auth"
import { useRouter } from "vue-router"

const auth = useAuthStore()
const router = useRouter()
const username = ref("")
const password = ref("")
const loading = ref(false)

const handleLogin = async () => {
  if (!username.value || !password.value)
    return alert("Isi semua field!")
  loading.value = true
  try {
    await auth.login(username.value, password.value)
  } catch (err) {
    console.error(err)
  } finally {
    loading.value = false
  }
}

const goRegister = () => router.push("/register")
</script>

<style scoped>
.container-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f0f2f5;
}

.container {
  width: 350px;
  padding: 30px;
  border-radius: 12px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.2);
  background-color: #fff;
  text-align: center;
}

.form-group {
  display: flex;
  align-items: center;
  margin-bottom: 15px;
}

label {
  width: 120px;
  text-align: left;
  margin-right: 10px;
}

input {
  flex: 1;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-size: 14px;
}

button {
  margin: 5px;
  padding: 10px 20px;
  border: none;
  border-radius: 6px;
  font-size: 16px;
  cursor: pointer;
}

button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

button:first-of-type {
  background-color: #4caf50;
  color: white;
}

button:first-of-type:hover:not(:disabled) {
  background-color: #45a049;
}

button:last-of-type {
  background-color: #2196f3;
  color: white;
}

button:last-of-type:hover:not(:disabled) {
  background-color: #1976d2;
}
</style>