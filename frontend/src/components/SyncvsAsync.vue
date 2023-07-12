<script setup lang="ts">
import { ref, Ref } from 'vue'
import axios from 'axios'

// バックエンドのURLの指定
const backendURL = "http://localhost:8000"

// 内部変数の初期値の設定
const interval: Ref<number> = ref(null);
const selectedMethod1: Ref<string> = ref("sync1");
const selectedMethod2: Ref<string> = ref("sync2");
const loading: Ref<boolean> = ref(false);

// 3秒のタイムラグでバックエンドに2回問い合わせる関数
const request2times = (path1: string, path2: string) => {
  interval.value = null;
  loading.value = true;
  const start: number = Date.now();
  axios.get(path1)
    .catch(err => { console.log(err) })
  setTimeout(
    () => {
      axios.get(path2)
        .then(res => {
          const end: number = Date.now();
          interval.value = (end - start) / 1000;
          loading.value = false;
        })
        .catch(err => {
          loading.value = false;
        })
    }, 3000
  )
};
</script>

<template>
<div class="card">
  <h3>同期・非同期リクエスト</h3>
  <div class="group">
    <span>
      <label class="labeltext">タスク1</label>
      <select v-model="selectedMethod1" class="inputbox">
        <option value="sync1">同期1</option>
        <option value="sync2">同期2</option>
        <option value="async1">非同期1</option>
        <option value="async2">非同期2</option>
      </select>
    </span>
    <span>
      <label class="labeltext">タスク2</label>
      <select v-model="selectedMethod2" class="inputbox">
        <option value="sync1">同期1</option>
        <option value="sync2">同期2</option>
        <option value="async1">非同期1</option>
        <option value="async2">非同期2</option>
      </select>
    </span>
  </div>
  <div class="group">
    <button
      class="static-width-button"
      @click="request2times(backendURL + '/' + selectedMethod1 , backendURL + '/' + selectedMethod2)"
    >
      <div v-if="!loading">Request</div>
      <div v-else class="spinner"></div>
    </button>
  </div>
  <div class="group result">
    <div v-if="!loading">Total time: {{ interval }} s</div>
    <div v-else>Requesting...</div>
  </div>
</div>
</template>

<style>
.group {
  padding: 5px;
}
.result {
  color: #747bff;
  font-weight: bold;
}
.labeltext {
  width: 30px;
  font-size:  16px;
  font-weight: bold;
  padding: 10px;
}
.inputbox {
  position: relative;
  width: 100px;
  margin-top: 10px;
  padding: 10px;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  color: #000000;
  border: 0.4px solid rgb(123, 123, 123); 
}

.static-width-button {
  width: 100px;
}

.spinner {
  width: 10px;
  height: 10px;
  margin: 2px auto;
  border: 4px #ddd solid;
  border-top: 4px #747bff solid;
  border-radius: 50%;
  animation: sp-anime 1.0s infinite linear;
}

@keyframes sp-anime {
  100% { 
    transform: rotate(360deg); 
  }
}
</style>