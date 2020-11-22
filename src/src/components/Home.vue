<style>
.fade-enter-active,
.fade-leave-active {
  transition-duration: 0.3s;
  transition-property: opacity;
  transition-timing-function: ease;
}

.fade-enter,
.fade-leave-active {
  opacity: 0
}
</style>

<template>
<main id="home">
<div>
  <b-card title="Nav Bar" no-body style="
  border: 0px;
  background-color: inherit;">
    <b-card-header header-tag="nav">
      <b-nav card-header tabs justified>
        <b-nav-item to="/summoners" exact exact-active-class="active">Summoners</b-nav-item>
        <b-nav-item to="/builds" exact exact-active-class="active">Builds</b-nav-item>
      </b-nav>
    </b-card-header>

    <b-card-body style="padding: 0px;">
      <transition name="fade" mode="out-in">
        <keep-alive>
          <router-view></router-view>
        </keep-alive>
      </transition>
    </b-card-body>
  </b-card>
</div>
</main>
</template>

<script>

export default {
  name: 'Home',
};
</script>
