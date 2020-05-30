import Vue from 'vue';
import Router from 'vue-router';

const Summoners = () => import('./components/Summoners.vue');

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Summoners',
      component: Summoners,
    },
  ],
});
