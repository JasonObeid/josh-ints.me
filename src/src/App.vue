<template>
  <div id="app">
    <transition name="fade" mode="out-in">
      <router-view/>
    </transition>
  </div>
</template>

<style>
#app {
  font-family:Helvetica, sans-serif;
  background-color: white;
}
</style>
