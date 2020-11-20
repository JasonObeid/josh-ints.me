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
      <transition>
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
