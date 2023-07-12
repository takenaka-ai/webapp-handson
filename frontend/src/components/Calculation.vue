<script setup lang="ts">
import { ref, Ref } from 'vue'
import axios from 'axios'

// 型の定義
interface RequestNumber {
  (): void
}

interface Calculators {
  [key: string]: RequestNumber
}

// バックエンドのURLの指定
const backendURL: string = "http://localhost:8000";

// 内部変数の初期値の設定
const a: Ref<Number> = ref(0);
const b: Ref<Number> = ref(0);
const result: Ref<Number> = ref(0);
const radioSelected: Ref<string> = ref("Add");

// 足し算をリクエストする関数
const requestAdd: RequestNumber = () => {
  axios.get(backendURL + `/add/${a.value}/${b.value}`)
    .then(res => { result.value = res.data.value })
    .catch(err => { console.log(err) })
};

// 掛け算をリクエストする関数
const requestMul: RequestNumber = () => {
  axios.get(backendURL + "/mul", {
    params: {
      "a": a.value,
      "b": b.value
    }
  })
    .then(res => { result.value = res.data.value })
    .catch(err => { console.log(err) })
};

// 引き算をリクエストする関数
const requestSub: RequestNumber = () => {
  axios.post("http://localhost:8000/sub", {
    "a": a.value,
    "b": b.value
  })
    .then(res => { result.value = res.data.value })
    .catch(err => { console.log(err) })
};

// 関数の格納先（ラジオボタン連携用）
const calculators: Ref<Calculators> = ref({
  "Add": requestAdd,
  "Mul": requestMul,
  "Sub": requestSub
})
</script>

<template>
<div class="card">
  <h3>四則演算</h3>
  <div class="group">
    <span v-for="(i, v) in calculators" :key="v">
      <input type="radio" :value="v" v-model="radioSelected" />
      <label class="labeltext">{{ v }}</label>
    </span>
  </div>
  <div class="group">
    <span>
      <label class="labeltext">A</label>
      <input type="number" v-model="a" class="inputbox"/>
    </span>
    <span>
      <label class="labeltext">B</label>
      <input type="number" v-model="b" class="inputbox"/>
    </span>
  </div>
  <div class="group">
    <button @click="calculators[radioSelected]">Calculate</button>
  </div>
  <div class="group result">
    Result: {{ result }}
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
  width: 20%;
  margin-top: 10px;
  padding: 10px;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  color: #000000;
  border: 0.4px solid rgb(123, 123, 123); 
}
</style>