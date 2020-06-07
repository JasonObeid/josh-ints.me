<style scoped>
.parent {
  vertical-align:middle;
  align-items:top;
  text-align:center;
  white-space: nowrap;
  padding: 1%;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-template-rows: 1fr;
  grid-column-gap: 15px;
  grid-row-gap: 10px;
}

.builds {
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: 1fr 0.2fr 1fr 0.2fr 1fr;
  grid-column-gap: 0px;
  grid-row-gap: 15px;
}

.div21 { grid-area: 1 / 1 / 2 / 2; }
.div22 { grid-area: 2 / 1 / 3 / 2; }
.div23 { grid-area: 3 / 1 / 4 / 2; }
.div26 { grid-area: 6 / 1 / 7 / 2; }
.div27 { grid-area: 7 / 1 / 8 / 2; }

.stats { grid-area: 1 / 1 / 2 / 2;
vertical-align: top; }
.build { grid-area: 1 / 2 / 2 / 3;
vertical-align: top; }

.champName {
  align-items: left;
  text-align: left;
}

.champIcon {
  margin-right: 10%;
  margin-left: 0%;
  border-radius: 50%;
}

.table td
{
  vertical-align: middle;
}
</style>

<template>
  <div class="parent">
    <div class="stats">
      <b-nav tabs justified>
        <b-nav-item exact exact-active-class="active">All</b-nav-item>
        <b-nav-item exact exact-active-class="active">Top</b-nav-item>
        <b-nav-item exact exact-active-class="active">Jungle</b-nav-item>
        <b-nav-item exact exact-active-class="active">Mid</b-nav-item>
        <b-nav-item exact exact-active-class="active">Bot</b-nav-item>
        <b-nav-item exact exact-active-class="active">Support</b-nav-item>
      </b-nav>
      <b-form-input
        v-model="searchText"
        type="text"
        placeholder="Filter by Name"
      ></b-form-input>
      <br>
      <table class="table">
        <tbody>
            <tr align="center">
              <th>Champion</th>
              <th>W/L</th>
              <th>Pick Rate</th>
              <th>Score</th>
              <th>CS</th>
              <th>Sample Size</th>
            </tr>
            <tr v-for="(champ, name) in filtered" :key="champ.key">
              <td>
                <div class="champName">
                <b-button @click='changeSelected(name)'
                style='background-color: #e2e2e2b8; color: black;'>
                <img :src="champ.imgPath" class='champIcon'
                    :alt="champ.name" width='32px'>
                    {{ champ.name }}
                </b-button>
                </div>
              </td>
              <td>
                {{ champ.stats.wins }}
              </td>
              <td>
                {{ champ.stats.pickRate }}
              </td>
              <td class="trinket">
                {{ champ.stats.kills + ' / ' + champ.stats.deaths + ' / ' + champ.stats.assists }}
              </td>
              <td class="trinket">{{ champ.stats.cs }}</td>
              <td class="trinket">{{ champ.samples }}</td>
            </tr>
        </tbody>
      </table>
    </div>
    <div class="build">
      <div class="builds">
        <div class="div21">
          <b-row>
            <b-col><img :src='selected.imgPath' class='champIcon'></b-col>
            <b-col>
              <b-row>
                <b-col><h1>{{ selected.name }}</h1></b-col>
              </b-row>
              <b-row>
                <b-col><img :src='selected.spells.spell1.imgPath' class='champIcon'></b-col>
                <b-col><img :src='selected.spells.spell2.imgPath' class='champIcon'></b-col>
              </b-row>
            </b-col>
          </b-row>
        </div>
        <div class="div22">
           <b-nav tabs justified>
            <b-nav-item exact exact-active-class="active" @click="changeRunes('0')">
              <img class='champIcon' :src="selected.runes['0'].primaryBranch.keystone.imgPath">
              <img class='champIcon' width='24px'
              :src="selected.runes['0'].secondaryBranch.imgPath">
              {{ selected.runes['0'].pickRate }}
            </b-nav-item>
            <b-nav-item exact exact-active-class="active" @click="changeRunes('1')">
              <img class='champIcon' :src="selected.runes['1'].primaryBranch.keystone.imgPath">
              <img class='champIcon' width='24px'
              :src="selected.runes['1'].secondaryBranch.imgPath">
              {{ selected.runes['1'].pickRate }}
            </b-nav-item>
           </b-nav>
        </div>
        <div class="div23">
          <b-row>
            <b-col>
              <img class='champIcon' :src='runes.primaryBranch.imgPath'>
            </b-col>
            <b-col>
              <img class='champIcon' :src='runes.secondaryBranch.imgPath'>
            </b-col>
          </b-row>
          <b-row>
            <b-col>
              <b-row>
                <b-col><img class='champIcon' :src='runes.primaryBranch.keystone.imgPath'></b-col>
              </b-row>
              <b-row>
                <b-col><img class='champIcon' :src='runes.primaryBranch.perk1.imgPath'></b-col>
              </b-row>
              <b-row>
                <b-col><img class='champIcon' :src='runes.primaryBranch.perk2.imgPath'></b-col>
              </b-row>
              <b-row>
                <b-col><img class='champIcon' :src='runes.primaryBranch.perk3.imgPath'></b-col>
              </b-row>
            </b-col>
            <b-col>
              <b-row>
                <b-col><img class='champIcon' :src='runes.secondaryBranch.perk0.imgPath'></b-col>
              </b-row>
              <b-row>
                <b-col><img class='champIcon' :src='runes.secondaryBranch.perk1.imgPath'></b-col>
              </b-row>
            </b-col>
          </b-row>
        </div>
        <div class="div26"> items </div>
        <div class="div27">
          <b-row>
            <b-col v-for="item in selected.items.itemsList" :key="item.name">
              <img :src='item.imgPath' class='champIcon'>
            </b-col>
            <b-col>
              <img :src='selected.items.trinket.imgPath' class='champIcon'>
            </b-col>
          </b-row>
        </div>
      </div>
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
      runes: [],
      selected: [],
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
      builds: [],
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
          .filter(([k, v]) => v.name.toLowerCase()
            .indexOf(this.searchText.toLowerCase()) !== -1),
      );
    },
  },
  methods: {
    changeRunes(option) {
      this.runes = this.selected.runes[option];
      console.log(JSON.stringify(this.runes));
    },
    changeSelected(name) {
      this.selected = this.builds[name];
      this.runes = this.selected.runes['0'];
      // console.log(JSON.stringify(this.selected));
    },
    getBuilds() {
      const path = `${localhost}/builds`;
      axios.get(path)
        .then((res) => {
          console.log(res);
          this.allChampions = res.data.stats;
          this.builds = res.data.builds;
          console.log(this.allChampions);
          console.log(this.builds);
          this.selected = this.builds['1'];
          this.runes = this.selected.runes['0'];
          console.log(JSON.stringify(this.selected));
          console.log(JSON.stringify(this.runes));
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
