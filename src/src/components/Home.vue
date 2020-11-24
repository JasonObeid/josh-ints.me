<style>
.bg-medium {
  background-color: #404850;
}
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
.nav-linkDark {
  border-color: #414344 !important;
  background-color: #2c3136 !important;
  color: #fdfdfd !important;
}
.nav-linkDark:hover {
  border-color: #424446 !important;
  background-color: #3a3e42 !important;
  color: #fdfdfd !important;
}
.nav-linkDark-active {
  border-color: #545658 !important;
  background-color: #535a61 !important;
  color: #fdfdfd !important;
}
.nav-linkDark-active:hover {
  border-color: #545658 !important;
  background-color: #535a61 !important;
  color: #fdfdfd !important;
}
.nav-tabsDark {
  border-bottom: 1px solid #545658 !important;
}
</style>

<template>
<main id="home">
<div>
  <b-card title="Nav Bar" no-body style="
  border: 0px;
  background-color: inherit;">
    <b-card-header header-tag="nav" ref="navHeader"
    :class="{ 'navbar-dark bg-dark': darkMode }">
      <b-nav card-header tabs justified
      :class="{ 'nav-tabsDark': darkMode }">
        <b-button v-b-toggle.settingSidebar ref="darkToggle"
        :class="{ 'btn-secondary': darkMode, 'btn-light': !darkMode }">
          <b-icon icon="three-dots-vertical"></b-icon>
        </b-button>
        <b-sidebar id="settingSidebar" title="Settings" shadow width="15%"
        :bg-variant="getVariant" no-enforce-focus
        :text-variant="getInverseVariant">
          <div class="px-3 py-2">
            <p>Squigie Mode:</p>
            <b-button block :class="{ 'btn-light': darkMode, 'btn-dark': !darkMode }"
            @click="toggleDarkMode()">
              <b-icon :icon="darkModeIcon"></b-icon>
            </b-button>
          </div>
        </b-sidebar>

        <b-nav-item v-if="darkMode" to="/summoners" ref="summonerTab" class="nav-linkDark"
        exact exact-active-class="active nav-linkDark-active"
        link-classes="nav-linkDark">Summoners</b-nav-item>

        <b-nav-item v-else to="/summoners" ref="summonerTab"
        exact exact-active-class="active">Summoners</b-nav-item>

        <b-nav-item v-if="darkMode" to="/builds" ref="buildsTab" class="nav-linkDark"
        exact exact-active-class="active nav-linkDark-active"
        link-classes="nav-linkDark">Summoners</b-nav-item>

        <b-nav-item v-else to="/builds" ref="buildsTab"
        exact exact-active-class="active">Summoners</b-nav-item>
      </b-nav>
    </b-card-header>

    <b-card-body style="padding: 0px;" ref="activeContainer"
    :class="{ 'text-white bg-medium': darkMode }">
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
  data() {
    return {
      darkModeIcon: 'sun',
    };
  },
  computed: {
    currentRouteName() {
      return this.$route.path;
    },
    darkMode() {
      return this.$store.state.darkMode;
    },
    getVariant() {
      if (this.darkMode === true) {
        return 'dark';
      }
      return 'light';
    },
    getInverseVariant() {
      if (this.darkMode === true) {
        return 'light';
      }
      return 'dark';
    },
  },
  methods: {
    toggleDarkMode() {
      this.$store.commit('toggle');
      if (this.$store.state.darkMode === true) {
        this.darkModeIcon = 'moon';
      } else {
        this.darkModeIcon = 'sun';
      }
    },
  },
  watch: {
    $route(to) {
      if (to.path === '/builds') {
        if (to.params.champName !== undefined) {
          if (to.params.champName !== this.champName) {
            this.champName = to.params.champName.toLowerCase();
            const champIndex = this.indexMap[this.champName];
            this.changeSelected(champIndex);
          }
        }
      }
    },
  },
};
</script>
