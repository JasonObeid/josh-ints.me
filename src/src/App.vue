<template>
  <div id="app" ref="app" class="bg-default noXOverflow"
  :class="{'noYOverflow': $route.path === '/builds'}">
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
  font-family: sans-serif;
}
</style>
