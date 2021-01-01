<template>
  <div id="app" ref="app">
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

@font-face {
  font-family: "Roboto";
  src: local("Roboto"),
  url(./fonts/Roboto-Regular.ttf) format("truetype");
}
@font-face {
  font-family: "Roboto Light";
  src: local("Roboto Light"),
  url(./fonts/Roboto-Light.ttf) format("truetype");
}
@font-face {
  font-family: "Roboto Medium";
  src: local("Roboto Medium"),
  url(./fonts/Roboto-Medium.ttf) format("truetype");
}
#app {
  -webkit-font-smoothing: antialiased;
  font-family: "Roboto", -apple-system, BlinkMacSystemFont,
                Roboto, "Helvetica Neue",
                Arial, sans-serif, "Apple Color Emoji",
                "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
}
</style>
