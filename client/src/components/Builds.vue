<style scoped>
.flex-container
{
  vertical-align:middle;
  align-items:center;
  text-align:center;
  white-space: nowrap;
  padding: 3%;
}
</style>

<template>
  <div class="flex-container">
    <div>
      <b-nav tabs justified>
        v-model if active add to laneFilter
        <b-nav-item exact exact-active-class="active">All</b-nav-item>
        <b-nav-item exact exact-active-class="active">Top</b-nav-item>
        <b-nav-item exact exact-active-class="active">Jungle</b-nav-item>
        <b-nav-item exact exact-active-class="active">Mid</b-nav-item>
        <b-nav-item exact exact-active-class="active">Bot</b-nav-item>
        <b-nav-item exact exact-active-class="active">Support</b-nav-item>
      </b-nav>
      <b-container class="bv-example-row">
        <b-row>
          <b-col>
             <b-form-input
                v-model="searchText"
                type="text"
                placeholder="Search by Name"
              ></b-form-input>
               <div class="container-fluid">
                <div class="row">
                  <div class="col-md-6 pad-15-ver"
                  v-for="champ in filtered" :key="champ.key">
                    <div class="card-inner">
                      <img class="card-img" :src="champ.championInfo.champImgPath">
                    </div>
                  </div>
                </div>
              </div>
          </b-col>
          <div class="w-100"></div>
          <b-col>Column</b-col>
        </b-row>
        <b-row>
          <b-col>Column</b-col>
          <b-col>Column</b-col>
        </b-row>
      </b-container>
    </div>
  </div>
</template>

<script>
import axios from 'axios';


// const localhost = '/api';
const localhost = 'http://localhost:5000';

export default {
  data() {
    return {
      top: ['zilean'],
      jungle: [],
      mid: ['zilean'],
      bot: [],
      support: ['zilean'],
      laneFilter: '',
      intSortCount: 0,
      dateSortCount: 0,
      searchText: '',
      allChampions: [],
    };
  },
  computed: {
    filtered() {
      if (this.searchText === '') {
        return this.allChampions;
      }
      return Object.fromEntries(
        Object.entries(this.allChampions)
          // eslint-disable-next-line no-unused-vars
          .filter(([k, v]) => v.championInfo.champName.toLowerCase()
            .indexOf(this.searchText.toLowerCase()) !== -1),
      );
    },
  },
  methods: {
    getBuilds() {
      const path = `${localhost}/builds`;
      axios.get(path)
        .then((res) => {
          console.log(res);
          this.allChampions = res.data.builds;
          console.log(this.allChampions);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getBuilds();
  },
};
</script>
