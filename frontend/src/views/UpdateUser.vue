<template>
  <div class="container-wrapper">
    <div class="container">
      <h2>UPDATE USER</h2>
      <div v-if="loading">Memuat data user...</div>
      <div v-else>
          <div class="form-group">
              <label for="nama">Nama Lengkap:</label>
              <input id="nama" v-model="nama" />
          </div>
          <div class="form-group">
              <label for="email">Email:</label>
              <input id="email" v-model="email" />
          </div>
          <div class="form-group">
              <label for="username">Username:</label>
              <input id="username" v-model="username" />
          </div>
          <div class="buttons">
              <button @click="updateUser">Update</button>
              <button @click="goBack">Kembali</button>
          </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '../services/api'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()
const id = route.params.id
const nama = ref('')
const email = ref('')
const username = ref('')
const loading = ref(true)

onMounted(async () => {
  try {
    const res = await api.get(`/users/${id}`)
    const user = res.data.user || res.data
    nama.value = user.nama
    email.value = user.email
    username.value = user.username
  } catch (err) {
    alert('Gagal memuat data user!')
  } finally {
    loading.value = false
  }
})

const updateUser = async () => {
  try {
    await api.put(`/users/${id}`, {
      nama: nama.value,
      email: email.value,
      username: username.value,
    })
    alert('User berhasil diperbarui!')
    router.push('/dashboard')
  } catch (err) {
    alert('Gagal memperbarui user!')
  }
}

const goBack = () => router.push('/dashboard')
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
.buttons {
  display: flex;
  justify-content: space-between;
}

 button {
  margin: 5px;
  padding: 10px 20px;
  border: none;
  border-radius: 6px;
  font-size: 16px;
  cursor: pointer;
}

button:first-of-type {
  background-color: #d29512;
  color: white;
}

button:first-of-type:hover {
  background-color: #bb6c13;
}

button:last-of-type {
  background-color: #58626a;
  color: white;
}

button:last-of-type:hover {
  background-color: #2d353d;
}
</style>