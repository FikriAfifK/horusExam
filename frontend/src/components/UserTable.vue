<template>
  <table border="1" width="100%">
    <thead>
      <tr>
        <th>ID</th>
        <th>Username</th>
        <th>Nama Lengkap</th>
        <th>Email</th>
        <th>Aksi</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="u in users" :key="u.id">
        <td>{{ u.id }}</td>
        <td>{{ u.username }}</td>
        <td>{{ u.nama }}</td>
        <td>{{ u.email }}</td>
        <td>
          <button @click="$emit('update', u.id)">U</button>
          <button @click="$emit('delete', u.id)">H</button>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script setup>
defineProps({ users: Array })
</script>

<style scoped>
button {
  margin: 5px;
  padding: 5px 15px;
  border: none;
  border-radius: 3px;
  font-size: 14px;
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
  background-color: #f44336;
  color: white;
}

button:last-of-type:hover {
  background-color: #d32f2f;
}
</style>