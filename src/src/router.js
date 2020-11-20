import Vue from 'vue';
import Router from 'vue-router';
import Home from './components/Home.vue';

Vue.use(Router);

const Summoners = () => import('./components/Summoners.vue');
const Builds = () => import('./components/Builds.vue');

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      component: Home,
      redirect: '/builds',
      children: [
        { path: 'summoners', component: Summoners },
        {
          path: 'builds',
          component: Builds,
          name: 'Home',
        },
      ],
    },
  ],
});
