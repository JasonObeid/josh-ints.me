<style>
html {
  --scrollbarBG: #cccccc;
  --thumbBG: #ffffff;
  --light-gray: #edf0f5;
  --medium-gray: #9CA3AF;
  --dark-gray: #4B5563;
  --background: #F3F4F6;
  --brand: #d8c7a5;
  --brand-dark: #4e4c32;
  --brand-accent: #E0E7FF;
  --brand-font: #4e3d1b;
  font-size: 1rem;
}

.bg-default {
  background-color: var(--background);
}

body {
  scrollbar-color: var(--thumbBG) var(--scrollbarBG);
}

div.dark::-webkit-scrollbar {
  width: 15px;
}
div.dark {
  scrollbar-color: #c0c0c0 #727272;
}
div.dark::-webkit-scrollbar-track {
  background: #727272;
}
div.dark::-webkit-scrollbar-thumb {
  background-color: #c0c0c0;
  border-radius: 6px;
  border: 3px solid #727272;
}

div::-webkit-scrollbar {
  width: 15px;
}
div {
  scrollbar-color: var(--thumbBG) var(--scrollbarBG);
}
div::-webkit-scrollbar-track {
  background: var(--scrollbarBG);
}
div::-webkit-scrollbar-thumb {
  background-color: var(--thumbBG) ;
  border-radius: 6px;
  border: 3px solid var(--scrollbarBG);
}

.bg-medium {
  background-color: #404850;
}
button.bg-medium:hover {
  background-color: #2c3238;
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
button {
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
  -webkit-transition: all 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
  transition: all 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
}

button:hover {
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.2);
  -webkit-transition: all 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
  transition: all 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
}
.navlink > a {
  color: #000000ce !important;
  border-bottom: transparent 3px solid;
}
.navlink:hover {
  color: #000000 !important;
}
a.navlink-active {
  color: #000000 !important;
  border-bottom: #4e3d1b 3px solid !important;
}

.navlink-dark > a {
  color: #ffffffce !important;
  border-bottom: transparent 3px solid;
}
a.navlink-dark:hover {
  color: #ffffff !important;
}
a.navlink-dark-active {
  color: #ffffff !important;
  border-bottom: #8c7646 3px solid !important;
}

.navbar-Dark {
  background-color: var(--brand-dark) !important;
}
.caps-spacing {
  letter-spacing: 2px;
}
.navbar {
  background-color: var(--brand);
}
.navBtn {
  background-color: #ffffff3d !important;
  border: transparent !important;
  width: 10% !important;
}
.navBtnDark {
  background-color: #6666663d !important;
  border: transparent !important;
  width: 10% !important;
}
</style>

<template>
<main id="home">
<div>
<b-navbar toggleable="lg" class="bg-medium d-flex" :class="{ 'navbar-Dark text-white': darkMode }">
  <b-navbar-brand class="caps-spacing ml-5" :class="{ 'text-white': darkMode }">
    JOSH-INTS.ME
  </b-navbar-brand>

  <b-navbar-nav align="center" class="m-auto w-100">
    <button class="btn btn-light p-0 m-0 mx-2"
    :class="{ 'navBtn': !darkMode, 'navBtnDark': darkMode}">
      <b-nav-item to="/summoners" ref="summonerTab"
      :class="{ 'navlink-dark': darkMode, 'navlink': !darkMode}"
      exact :exact-active-class="getNavLink">Summoners</b-nav-item>
    </button>
    <button class="btn btn-light p-0 m-0 mx-2"
    :class="{ 'navBtn': !darkMode, 'navBtnDark': darkMode}">
      <b-nav-item to="/builds" ref="buildsTab"
      :class="{ 'navlink-dark': darkMode, 'navlink': !darkMode}"
      exact :exact-active-class="getNavLink">Builds</b-nav-item>
    </button>
  </b-navbar-nav>

  <b-button class="m-auto" :class="{ 'btn-light': !darkMode, 'btn-dark': darkMode }"
  @click="toggleDarkMode()">
    <b-icon :icon="darkModeIcon"></b-icon>
  </b-button>

</b-navbar>
  <b-row align-v="center" align-h="center" ref="activeContainer"
  :class="{ 'text-white bg-medium': darkMode }" class="pb-2">
    <b-col cols="9">
      <transition name="fade" mode="out-in">
        <keep-alive>
          <router-view></router-view>
        </keep-alive>
      </transition>
    </b-col>
  </b-row>
</div>
</main>
</template>

<script>

export default {
  name: 'Home',
  data() {
    return {
    };
  },
  computed: {
    getNavLink() {
      if (this.darkMode === true) {
        return 'navlink-dark-active';
      }
      return 'navlink-active';
    },
    darkModeIcon() {
      if (this.darkMode === true) {
        return 'sun';
      }
      return 'moon';
    },
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
    },
  },
  watch: {
    darkMode() {
      if (this.darkMode === true) {
        document.getElementById('root').classList.add('bg-medium');
        document.getElementById('root').classList.remove('bg-default');
      } else {
        document.getElementById('root').classList.remove('bg-medium');
        document.getElementById('root').classList.add('bg-default');
      }
    },
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
