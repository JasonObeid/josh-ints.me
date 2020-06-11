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
.div24 { grid-area: 4 / 1 / 5 / 2; }
.div25 { grid-area: 5 / 1 / 6 / 2; }
.div26 { grid-area: 6 / 1 / 7 / 2; }
.div27 { grid-area: 7 / 1 / 8 / 2; }

.stats { grid-area: 1 / 1 / 2 / 2;
vertical-align: top; }
.build { grid-area: 1 / 2 / 2 / 3;
vertical-align: top; }

.champName {
  align-items: left;
  text-align: left;
  vertical-align: middle;
}

.champIcon {
  margin-right: 10%;
  margin-left: 0%;
  border-radius: 50%;
}

td
{
  vertical-align: middle;
}

.sort
{
  cursor: pointer;
}

.roles {
  margin-right: 0.05rem;
  margin-left: 0.05rem;
}
.champText {
  margin-right: 10%;
}
</style>
<template>
  <div class="parent">
    <div class="stats">
      <b-row>
        <b-col class='roles'
          v-for="(btn, idx) in buttons"
          :key="idx"
        >
          <b-button
          :pressed.sync="btn.state"
          variant="light"
          size="md"
          block>
            {{ btn.caption }}
          </b-button>
        </b-col>
        </b-row>
      <br>
      <b-form-input
        v-model="searchText"
        type="text"
        placeholder="Filter by Name"
      ></b-form-input>
      <br>
      <b-table small :fields="fields" :items="filtered" style="vertical-align: middle;"
      :sort-by.sync="sortBy" :sort-desc.sync="sortDesc" responsive="sm">
        <!-- A custom formatted column -->
          <template v-slot:cell(name)="filtered">
            <div class="champName">
                <b-button @click='changeSelected(filtered.item.idx)' class="btn btn-light btn-sm"
                style='background-color: #e2e2e2b8; color: black;'>
                <img :src="filtered.item.imgPath" class='champIcon'
                    :alt="filtered.item.name" width='32px'>
                <a class="champText">{{ filtered.item.name }}</a>
                </b-button>
              </div>
          </template>
          <!-- Optional default data cell scoped slot -->
          <template v-slot:cell(banRate)="filtered">
            {{ filtered.item.banRate + '%' }}
          </template>
          <!-- Optional default data cell scoped slot -->
          <template v-slot:cell(pickRate)="filtered">
            {{ filtered.item.pickRate + '%' }}
          </template>
          <!-- Optional default data cell scoped slot -->
          <template v-slot:cell(winRate)="filtered">
            {{ filtered.item.winRate + '%' }}
          </template>
          <!-- Optional default data cell scoped slot -->
          <template v-slot:cell(lanes)="filtered">
            <a v-for="lane in filtered.item.lanes" :key='lane'>
              <img :src="'/images/lanes/'+lane+'.png'" class='champIcon'
                    :alt="filtered.item.name" width='24px'>
            </a>
          </template>
      </b-table>
    </div>
    <div class="build">
      <div class="div21">
        <b-row>
          <b-col>
            <h1>{{ selected.name }}</h1>
            <img :src='selected.imgPath' class='champIcon'>
          </b-col>
          <b-col>
            <img :src='build.spells[0].imgPath' :alt='build.spells[0].name' style="padding: 5%">
            <img :src='build.spells[1].imgPath' :alt='build.spells[0].name' style="padding: 5%">
          </b-col>
        </b-row>
        <b-form-select v-model="selectedRole">
          <b-form-select-option v-for="(role, index) in selected.roles"
          :key='index' :value="role" @click="chooseBuild(role)">
            {{ role.lane }}
          </b-form-select-option>
        </b-form-select>
          <b-form-group>
            <b-form-radio v-for="(buildOpt, index) in selectedRole.builds" :key="index"
            v-model="build" name="some-radios" :value="buildOpt" :text="buildOpt.name">
              {{ buildOpt.name }}
            </b-form-radio>
          </b-form-group>
          </div>
      <div class="div22">
        runes
      </div>
      <div class="div23">
        <b-row>
          <b-col>
            <b-row>
              <b-col><img  :src='build.runes.primaryBranch.keystone.imgPath' width='64px'></b-col>
            </b-row>
            <b-row>
              <b-col><img  :src='build.runes.primaryBranch.perk1.imgPath'></b-col>
            </b-row>
            <b-row>
              <b-col><img  :src='build.runes.primaryBranch.perk2.imgPath'></b-col>
            </b-row>
            <b-row>
              <b-col><img  :src='build.runes.primaryBranch.perk3.imgPath'></b-col>
            </b-row>
          </b-col>
          <b-col>
            <b-row>
              <b-col><img  :src='build.runes.secondaryBranch.perk0.imgPath'></b-col>
            </b-row>
            <b-row>
              <b-col><img  :src='build.runes.secondaryBranch.perk1.imgPath'></b-col>
            </b-row>
            <b-row>
              <b-col><img  :src='build.runes.auxillary[0].imgPath'></b-col>
            </b-row>
            <b-row>
              <b-col><img  :src='build.runes.auxillary[1].imgPath'></b-col>
            </b-row>
            <b-row>
              <b-col><img  :src='build.runes.auxillary[2].imgPath'></b-col>
            </b-row>
          </b-col>
        </b-row>
      </div>
      <div class="div24"> skills </div>
      <div class="div25">
        <b-row>
          <b-col>
            <img :src="'images/spell/'+ build.skills[0].imgPath">
          </b-col>
          <b-col>
            <b-icon icon='arrow-right'></b-icon>
          </b-col>
          <b-col>
            <img :src="'images/spell/'+ build.skills[1].imgPath">
          </b-col>
          <b-col>
            <b-icon icon='arrow-right'></b-icon>
          </b-col>
          <b-col>
            <img :src="'images/spell/'+ build.skills[2].imgPath">
          </b-col>
        </b-row>
      </div>
      <div class="div26"> items </div>
      <div class="div27">
        <b-row>
          <b-col v-for="(item, index) in build.items.general.start" :key="index">
            <img :src='item.imgPath'>
          </b-col>
        </b-row>
        <br>
        <b-row>
          <b-col v-for="(item, index) in build.items.general.core" :key="index">
            <img :src='item.imgPath' >
          </b-col>
        </b-row>
        <br>
        <b-row>
          <b-col v-for="(item, index) in build.items.general.full" :key="index">
            <img :src='item.imgPath' >
          </b-col>
        </b-row>
        <br>
        situational
        <b-row>
          <b-col v-for="(item, index) in build.items.situational" :key="index">
            <img :src='item.imgPath'>
          </b-col>
        </b-row>
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
      buttons: [
        { caption: 'top', state: true },
        { caption: 'jungle', state: true },
        { caption: 'mid', state: true },
        { caption: 'adc', state: true },
        { caption: 'support', state: true },
      ],
      sortBy: 'winRate',
      sortDesc: true,
      fields: [
        { key: 'name', label: 'name', sortable: true },
        { key: 'banRate', label: 'Ban Rate', sortable: true },
        { key: 'pickRate', label: 'Pick Rate', sortable: true },
        { key: 'winRate', label: 'Win Rate', sortable: true },
        { key: 'lanes', label: 'Role', sortable: true },
      ],
      selectedRole: [],
      build: [],
      runes: [],
      selected: [],
      laneFilter: '',
      searchText: '',
      allChampions: [],
      builds: [],
      activeItem: '',
    };
  },
  computed: {
    filtered() {
      const buttonStates = this.btnStates;
      if (this.searchText === '' && !buttonStates.includes(null)) {
        return this.allChampions;
      }
      if (buttonStates.includes(null)) {
        const filtered = this.allChampions.filter((champion) => {
          if (this.checkLanes(champion.lanes) === true) {
            return champion;
          }
          return null;
        });
        return filtered;
      }
      const filtered = this.allChampions.filter((champion) => {
        if (champion.name.toLowerCase()
          .indexOf(this.searchText.toLowerCase()) !== '-1'
          && this.checkLanes(champion.lanes) === true) {
          return champion;
        }
        return null;
      });
      return filtered;
    },
    btnStates() {
      return this.buttons.map((btn) => {
        if (btn.state === true) return btn.caption;
        return null;
      });
    },
  },
  methods: {
    chooseBuild(role) {
      console.log('here');
      // eslint-disable-next-line prefer-destructuring
      this.build = role.builds[0];
    },
    isActive(menuItem) {
      return this.activeItem === menuItem;
    },
    setActive(menuItem) {
      this.activeItem = menuItem;
    },
    checkLanes(lanes) {
      for (let i = 0; i < lanes.length; i += 1) {
        if (this.btnStates.includes(lanes[i])) {
          return true;
        }
      }
      return false;
    },
    changeSelected(index) {
      // eslint-disable-next-line radix
      const idx = parseInt(index);
      this.selected = this.builds[idx];
      this.activeItem = this.selected.roles[0].lane;
      // eslint-disable-next-line prefer-destructuring
      this.selectedRole = this.selected.roles[0];
      // eslint-disable-next-line prefer-destructuring
      this.build = this.selected.roles[0].builds[0];
      console.log(JSON.stringify(this.build));
      // console.log(JSON.stringify(this.selected));
    },
    getBuilds() {
      const path = `${localhost}/builds`;
      axios.get(path)
        .then((res) => {
          // console.log(res);
          this.allChampions = res.data.stats;
          this.builds = res.data.builds;
          // eslint-disable-next-line prefer-destructuring
          this.selected = this.builds[1];
          // eslint-disable-next-line prefer-destructuring
          this.selectedRole = this.selected.roles[0];
          // eslint-disable-next-line prefer-destructuring
          this.build = this.selected.roles[0].builds[0];
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
