<template>
<div class="container-wrapper">
    <div class="container">
        <h2>REGISTRASI AKUN</h2>
        <div class="form-group">
            <label for="nama">Nama Lengkap:</label>
            <input id="nama" v-model="nama" @keyup.enter="handleRegister" />
        </div>
        <div class="form-group">
            <label for="email">Email:</label>
            <input id="email" v-model="email" @keyup.enter="handleRegister" />
        </div>
        <div class="form-group">
            <label for="username">Username:</label>
            <input id="username" v-model="username" @keyup.enter="handleRegister" />
        </div>
        <div class="form-group">
            <label for="password">Password:</label>
            <input id="password" v-model="password" type="password" @keyup.enter="handleRegister" />
        </div>
        <div class="buttons">
        <button :disabled="loading" @click="handleRegister">
            {{ loading ? "Loading..." : "Registrasi" }}
        </button>
        </div>
    </div> 
</div>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '../store/auth'

const auth = useAuthStore()
const nama = ref('')
const email = ref('')
const username = ref('')
const password = ref('')
const loading = ref(false)

const handleRegister = async () => {
  if (!nama.value || !email.value || !username.value || !password.value)
    return alert('Semua field wajib diisi!')
  if (!/\S+@\S+\.\S+/.test(email.value))
    return alert("Format email tidak valid!")
  loading.value = true
  try {
    await auth.register({
      nama: nama.value,
      email: email.value,
      username: username.value,
      password: password.value
    })
  } catch (err) {
    console.error(err)
  } finally {
    loading.value = false
  }
}
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
  background-color: #2196f3;
  color: white;
}

button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

button:hover:not(:disabled) {
  background-color: #1976d2;
}
</style>