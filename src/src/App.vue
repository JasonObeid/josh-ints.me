<template>
  <div id="app" ref="app" class="bg-default">
    <transition name="fade" mode="out-in">
      <router-view/>
    </transition>
  </div>
</template>

<style>
.noYOverflow {
  overflow-y: hidden;
}
.noXOverflow {
  overflow-x: hidden;
}
#app {
  -webkit-font-smoothing: antialiased;
  font-family: sans-serif;
}
</style>
