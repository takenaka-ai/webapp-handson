<script setup lang="ts">
import Calculation from './components/Calculation.vue'
import SyncvsAsync from './components/SyncvsAsync.vue'
</script>

<template>
  <div>
    <h2>Web アプリケーションハンズオン</h2>
    <a href="https://vuejs.org/" target="_blank">
      <img src="./assets/github-mark.svg" class="logo"/>
    </a>
  </div>
  <hr/>
  <Calculation/>
  <hr/>
  <SyncvsAsync/>
</template>

<style scoped>
.logo {
  height: 3em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #bdbdbdaa);
}
</style>
