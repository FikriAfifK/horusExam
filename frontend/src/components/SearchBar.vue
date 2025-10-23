<template>
    <div class="search-bar">
        <label for="search">Cari Pengguna:</label>
        <input
            id="search"
            :value="modelValue"
            @input="$emit('update:modelValue', $event.target.value)"
            @keyup.enter="emitSearch"
        />
        <button @click="emitSearch">Cari</button>
    </div>
</template>

<script setup>
const props = defineProps(['modelValue'])
const emits = defineEmits(['update:modelValue','search'])

const emitSearch = () => {
    // Emits 'search' event dan meneruskan value dari input field
    emits('search', props.modelValue)
}
</script>

<style scoped>
input {
  margin-left: 10px;
  padding: 8px 24px;
  border-radius: 6px;
  border: 1px solid #ccc;
  font-size: 14px;
}

button {
  margin-left: 10px;
  padding: 8px 16px;
  border-radius: 6px;
  border: none;
  background-color: #2196f3;
  color: white;
  cursor: pointer;
}

button:hover {
  background-color: #1976d2;
}
</style>