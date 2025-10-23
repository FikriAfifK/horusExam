<template>
  <div class="container">
    <div class="header">
      <h2>DASHBOARD PENGGUNA</h2>
      <button class="logout-btn" @click="logout">Logout</button>
    </div>

    <div class="search-wrapper">
        <SearchBar :modelValue="search" @update:modelValue="search = $event" @search="handleSearch" />
    </div>

    <UserTable
      :users="filteredUsers"
      @update="goUpdate"
      @delete="deleteUser"
    />

    <p v-if="filteredUsers.length === 0" class="empty">Tidak ada data pengguna</p>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import api from '../services/api'
import SearchBar from '../components/SearchBar.vue'
import UserTable from '../components/UserTable.vue'
import { useAuthStore } from '../store/auth'
import { useRouter } from 'vue-router'

const router = useRouter()
const auth = useAuthStore()
const users = ref([])
const search = ref('') // tampilan search input
const currentSearchTerm = ref('') // filtering search term

const fetchUsers = async () => {
  try {
    const res = await api.get('/users/')
    users.value = res.data.users
  } catch (err) {
    alert(err.response?.data?.error || 'Gagal memuat data pengguna')
    if (err.response?.status === 401) auth.logout()
  }
}

onMounted(fetchUsers)

const handleSearch = () => {
  currentSearchTerm.value = search.value
}

const filteredUsers = computed(() =>
  users.value.filter(u =>
    u.username.toLowerCase().includes(currentSearchTerm.value.toLowerCase()) ||
    u.nama.toLowerCase().includes(currentSearchTerm.value.toLowerCase())
  )
)

const goUpdate = (id) => router.push(`/update/${id}`)

const deleteUser = async (id) => {
  if (!confirm('Apakah Anda yakin ingin menghapus user ini?')) return
  try {
    await api.delete(`/users/${id}`)
    users.value = users.value.filter(u => u.id !== id)
    alert('User berhasil dihapus')
  } catch (err) {
    alert(err.response?.data?.error || 'Gagal menghapus user')
  }
}

const logout = () => auth.logout()
</script>

<style scoped>
.container {
  max-width: 1200px;
  width: 90%;
  margin: 50px auto;
  text-align: center;
  padding: 30px;
  background-color: #fff;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.1);
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logout-btn {
  padding: 6px 12px;
  background: #58626a;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.logout-btn:hover {
  background: #2d353d;
}

.empty {
  color: #888;
  margin-top: 20px;
}

.search-wrapper {
  text-align: left;
  margin: 20px 0;
}
</style>