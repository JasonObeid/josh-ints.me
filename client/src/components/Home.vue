<template>
<main id="home">
<div>
  <b-card title="Nav Bar" no-body>
    <b-card-header header-tag="nav">
      <b-nav card-header pills justified>
        <!-- <b-nav-item>'s with child routes. Note the trailing slash on the first <b-nav-item> -->
        <b-nav-item to="/summoners" exact exact-active-class="active">Summoners</b-nav-item>
        <b-nav-item to="/builds" exact exact-active-class="active">Builds</b-nav-item>
      </b-nav>
    </b-card-header>

    <b-card-body>
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
