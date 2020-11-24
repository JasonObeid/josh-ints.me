<style scoped>

.fade-enter-active, .fade-leave-active {
  transition-property: opacity;
  transition-duration: 0.25s;
}

.fade-enter-active {
  transition-delay: 0.25s;
}

.fade-enter, .fade-leave-active {
  opacity: 0
}
.parent {
  vertical-align: middle;
  align-items: top;
  text-align: center;
  white-space: nowrap;
  padding: 1% 1% 0 1%;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-template-rows: 1fr;
  grid-column-gap: 15px;
  grid-row-gap: 10px;
  overflow-x: hidden;
  overflow-y: hidden;
}

.stats {
  grid-area: 1 / 1 / 2 / 2;
  vertical-align: top;
}

.build {
  grid-area: 1 / 2 / 2 / 3;
  vertical-align: top;
  padding-left: 6%;
  padding-right: 3%;
  padding-top: 0%;
  transition: all 0.5s;
  -webkit-transition: all 0.5s;
  opacity: 1;
}
.build.loading {
  transition: all 0.5s;
  -webkit-transition: all 0.5s;
  opacity: 0;
}

.bld-grid-container {
  display: grid;
  grid-template-columns: 1fr;
  gap: 10px 0px;
  grid-template-areas:
    "bld-Role" "bld-RuneHeader" "bld-Runes"
    "bld-SkillHeader" "bld-Skills" "bld-ItemHeader" "bld-Items";
  align-items: center;
  align-self: center;
  vertical-align: middle;
}

.bld-Role {
  grid-area: bld-Role;
}

.bld-RuneHeader {
  grid-area: bld-RuneHeader;
  text-align: left;
}

.bld-Runes {
  grid-area: bld-Runes;
}

.bld-SkillHeader {
  grid-area: bld-SkillHeader;
  text-align: left;
}

.bld-Skills {
  grid-area: bld-Skills;
}

.bld-ItemHeader {
  grid-area: bld-ItemHeader;
  text-align: left;
}

.bld-Items {
  grid-area: bld-Items;
}

table {
  vertical-align: middle;
}

.champName {
  align-items: left;
  text-align: left;
  vertical-align: middle;
}

img {
  border-radius: 20%;
}

.sort {
  cursor: pointer;
}

.itemContainer {
  text-align: left;
}

.items {
  align-items: left;
  text-align: left;
  margin: 10px 10px 0 20px;
}

.filterShadow {
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
  -webkit-transition: all 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
  transition: all 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
}

.filterShadow:hover {
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
  -webkit-transition: all 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
  transition: all 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
}

button {
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
  -webkit-transition: all 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
  transition: all 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
}

button:hover {
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
  -webkit-transition: all 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
  transition: all 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
}

.dropShadow {
  box-shadow: 0 1px 1px rgba(0,0,0,0.11),
              0 2px 2px rgba(0,0,0,0.11),
              0 4px 4px rgba(0,0,0,0.11),
              0 6px 8px rgba(0,0,0,0.11),
              0 8px 16px rgba(0,0,0,0.11)
}


.runes {
  filter: grayscale(100%);
  opacity: .27;
  border-radius: 50%;
}

.activeRune {
  filter: none;
  opacity: 1;
  border: 2px solid #3273fa;
}

.refresh {
  border-radius: 50%;
  padding: 4px 6px;
}
.shardRow {
  margin: 0.3% 0px;
}
.runeRow {
  margin: 2% 0px;
}
.runeRowHeader {
  text-align: left;
  padding: 2% 5%;
  border-radius: 6px;
  background-color: #f2f2f2;
}
.runeRowGroup {
  margin: 3% 0;
  border-radius: 6px;
}
#statsTable::-webkit-scrollbar {
    width: 8px;
    background-color: #F5F5F5;
}

#statsTable::-webkit-scrollbar-track {
    box-shadow: inset 0 0 6px rgba(104, 140, 240, 0.3);
  }

#statsTable::-webkit-scrollbar-thumb {
    background-color: lightblue;
    outline: 1px solid slategrey;
}

</style>
<template>
<transition name="fade" mode="out-in">
  <div class="parent">
    <div class="stats" ref="statsContainer">
      <b-row align-v="center" align-h="center">
        <b-col v-for="(btn, idx) in buttons" :key="idx">
          <b-button
            :pressed.sync="btn.state"
            variant="outline-info"
            size="md"
            block
          >{{ btn.caption }}</b-button>
        </b-col>
        <b-col cols="1">
          <b-button size="sm" class="refresh" ref="refresh" @click='updateBuilds()'
          :variant="getInverseVariant">
            <b-icon icon="arrow-clockwise" v-if="!showUpdate"></b-icon>
            <b-spinner small v-if="showUpdate" class="align-middle"></b-spinner>
          </b-button>
        </b-col>
      </b-row>
      <br>
      <b-row align-v="center" align-h="center">
        <b-col>
          <b-form-input v-model="searchText" type="search" ref="filterBox"
          placeholder="Filter by Name" autofocus class=filterShadow
          :class="{ 'text-white bg-dark': darkMode}">
          </b-form-input>
        </b-col>
      </b-row>
      <br>
      <b-table striped ref="statsTable"
        small no-border-collapse
        sticky-header="715px"
        responsive="false"
        :fields="fields"
        :items="filtered"
        style="overflow-x: hidden; "
        :sort-by.sync="sortBy"
        :sort-desc.sync="sortDesc"
        :dark="darkMode"
      >
        <!-- A custom formatted column -->
        <template v-slot:cell(name)="filtered">
          <div style="text-align: left;">
            <b-button block @click="changeSelected(filtered.item.idx)"
            size="sm" class="champName champBtn"
            :class="{ 'btn-secondary': darkMode, 'btn-light': !darkMode}">
              <b-row align-v="center" align-h="start" no-gutters>
                <b-col>
                  <img :src="filtered.item.imgPath" :alt="filtered.item.name" width="32px"
                  style="margin-right: 10%;"/>
                  {{ filtered.item.name }}
                </b-col>
              </b-row>
            </b-button>
          </div>
        </template>
        <!-- Optional default data cell scoped slot -->
        <template v-slot:cell(banRate)="filtered">{{ filtered.item.banRate + '%' }}</template>
        <!-- Optional default data cell scoped slot -->
        <template v-slot:cell(pickRate)="filtered">{{ filtered.item.pickRate + '%' }}</template>
        <!-- Optional default data cell scoped slot -->
        <template v-slot:cell(winRate)="filtered">{{ filtered.item.winRate + '%' }}</template>
        <!-- Optional default data cell scoped slot -->
        <template v-slot:cell(lanes)="filtered">
         <b-row no-gutters>
            <b-col v-for="lane in filtered.item.lanes" :key="lane">
              <b-button @click="changeSelectedWithRole(filtered.item.idx, lane)"
                size="sm" class="roleBtn"
                :class="{ 'btn-secondary': darkMode, 'btn-light': !darkMode}">
                <img :src="'/images/lanes/'+lane+'.png'"
                  :alt="filtered.item.name" width="24px"/>
              </b-button>
            </b-col>
          </b-row>
        </template>
      </b-table>
    </div>
    <div class="build" ref="buildContainer">
      <div class="bld-grid-container">
        <div class="bld-Role">
            <b-row align-v="center" align-h="center">
              <b-col cols="5">
                <b-row align-v="center" align-h="center">
                  <b-col cols="7" >
                    <!--<h6> {{ selected.name }} </h6>-->
                    <img :src="selected.imgPath" class="dropShadow"/>
                  </b-col>
                  <b-col cols="5">
                    <b-col>
                      <img class="dropShadow"
                        :src="build.spells[0].imgPath"
                        :alt="build.spells[0].name"
                      />
                    </b-col>
                    <b-col>
                      <img class="dropShadow"
                        :src="build.spells[1].imgPath"
                        :alt="build.spells[1].name"
                      />
                    </b-col>
                  </b-col>
                </b-row>
              </b-col>
              <b-col cols="7">
                <b-row align-v="center" align-h="center">
                  <b-col cols="4">
                    <b-form-select v-model="selectedRole" ref="laneDropdown"
                    :class="{ 'text-white bg-dark': darkMode}">
                      <b-form-select-option
                        v-for="(role, index) in selected.roles"
                        :key="index"
                        :value="role"
                        @click="chooseBuild(role)"
                      >{{ role.lane }}</b-form-select-option>
                    </b-form-select>
                  </b-col>
                  <b-col cols="8">
                    <b-form-group ref="roleRadio">
                      <b-form-radio
                        v-for="(buildOpt, index) in selectedRole.builds"
                        :key="index"
                        v-model="build"
                        name="some-radios"
                        :value="buildOpt"
                        :text="buildOpt.name"
                      >
                        {{ buildOpt.name }}
                      </b-form-radio>
                    </b-form-group>
                  </b-col>
                </b-row>
              </b-col>
            </b-row>
        </div>
        <div class="bld-RuneHeader">
          <h4>Runes</h4>
        </div>
        <div class="bld-Runes">
          <b-row>
              <b-col>
                <div class="primary-container">
                  <div class="runeRowHeader" ref="primaryRuneHeader"
                  :class="{ 'bg-dark': darkMode}">
                    <b-row no-gutters align-v="center" align-h="center">
                      <b-col cols="3">
                        <img :src="build.runes.primaryBranch.imgPath"
                        class="runes dropShadow activeRune" width="32px"/>
                      </b-col>
                      <b-col cols="9">
                        {{ build.runes.primaryBranch.name }}
                      </b-col>
                    </b-row>
                  </div>
                  <div class="runeRowGroup">
                    <b-row no-gutters align-v="center" align-h="center" class="runeRow">
                      <b-col v-for="rune in runeMap[build.runes.primaryBranch.id].runeRows[0]"
                      :key="rune.name">
                        <img :src="rune.imgPath"
                        class="runes dropShadow" width="64px"
                        :class="{ 'activeRune': isActiveRune(rune.id) }"/>
                      </b-col>
                    </b-row>
                  </div>
                  <div class="runeRowGroup">
                    <b-row no-gutters align-v="center" align-h="center" class="runeRow"
                    v-for="runeRow in runeMap[build.runes.primaryBranch.id].runeRows.slice(1)"
                    :key="runeRow.name">
                      <b-col v-for="rune in runeRow" :key="rune.name">
                        <img :src="rune.imgPath"
                        class="runes dropShadow" width="36px"
                        :class="{ 'activeRune': isActiveRune(rune.id) }"/>
                      </b-col>
                    </b-row>
                  </div>
                </div>
              </b-col>
              <b-col>
                <div class="secondary-container">
                  <div class="runeRowHeader" ref="secondaryRuneHeader"
                  :class="{ 'bg-dark': darkMode}">
                    <b-row no-gutters align-v="center" align-h="center">
                      <b-col cols="3">
                        <img :src="build.runes.secondaryBranch.imgPath"
                        class="runes dropShadow activeRune" width="32px"/>
                      </b-col>
                      <b-col cols="9">
                        {{ build.runes.secondaryBranch.name }}
                      </b-col>
                    </b-row>
                  </div>
                  <div class="runeRowGroup">
                    <b-row no-gutters align-v="center" align-h="center" class="runeRow"
                    v-for="runeRow in runeMap[build.runes.secondaryBranch.id].runeRows.slice(1)"
                    :key="runeRow.name">
                      <b-col v-for="rune in runeRow" :key="rune.name">
                        <img :src="rune.imgPath"
                        class="runes dropShadow" width="36px"
                        :class="{ 'activeRune': isActiveRune(rune.id) }"/>
                      </b-col>
                    </b-row>
                  </div>
                  <div class="runeRowGroup">
                    <b-row no-gutters align-v="center" align-h="center" class="shardRow"
                    v-for="(auxRow, rowIndex) in shardMap" :key="rowIndex">
                      <b-col v-for="(shard, colIndex) in auxRow" :key="colIndex">
                        <img :src="shard.imgPath"
                        class="runes dropShadow" height="24px" width="auto" :ref="shard.id"
                        :class="{ 'activeRune': isActiveShard(shard.id, rowIndex) }"/>
                      </b-col>
                    </b-row>
                  </div>
                </div>
              </b-col>
            </b-row>
        </div>
        <div class="bld-SkillHeader">
          <h4>Skills</h4>
        </div>
        <div class="bld-Skills">
          <b-row align-v="center" align-h="center" style="padding-bottom: 1%">
            <b-col>
              {{ build.skills[0].name }}
              <br />
              <div>{{ build.skills[0].button }}</div>
              <img :src="build.skills[0].imgPath" class="dropShadow"/>
            </b-col>
            <b-col>
              <div>
                <b-icon icon="arrow-right"></b-icon>
              </div>
            </b-col>
            <b-col>
              {{ build.skills[1].name }}
              <br />
              <div>{{ build.skills[1].button }}</div>
              <img :src="build.skills[1].imgPath" class="dropShadow"/>
            </b-col>
            <b-col>
              <div>
                <b-icon icon="arrow-right"></b-icon>
              </div>
            </b-col>
            <b-col>
              {{ build.skills[2].name }}
              <br />
              <div>{{ build.skills[2].button }}</div>
              <img :src="build.skills[2].imgPath" class="dropShadow"/>
            </b-col>
          </b-row>
        </div>
        <div class="bld-ItemHeader">
          <h4>Items</h4>
        </div>
        <div class="itemContainer">
          <div class="Early">
            <b-row align-v="center" no-gutters class="itemRow">
              <b-col cols="1" style="text-align: right">
                Early
              </b-col>
              <b-col cols="1">
              </b-col>
              <b-col>
                <img
                  v-for="(item, index) in build.items.general.start"
                  :key="index" :src="item.imgPath" class="items dropShadow"
                  v-b-tooltip.left.hover.left = "{ variant: 'secondary' }" :title="item.name"
                />
              </b-col>
            </b-row>
          </div>
          <div class="Core">
            <b-row align-v="center" no-gutters class="itemRow">
              <b-col cols="1" style="text-align: right">
                Core
              </b-col>
              <b-col cols="1">
              </b-col>
              <b-col>
                <img
                  v-for="(item, index) in build.items.general.core"
                  :key="index"
                  :src="item.imgPath"
                  class="items dropShadow"
                  v-b-tooltip.left.hover = "{ variant: 'secondary' }" :title="item.name"
                />
              </b-col>
            </b-row>
          </div>
          <div class="Late">
            <b-row align-v="center" no-gutters class="itemRow">
              <b-col cols="1" style="text-align: right">
                Late
              </b-col>
              <b-col cols="1">
              </b-col>
              <b-col>
                <img
                  v-for="(item, index) in build.items.general.full"
                  :key="index" :src="item.imgPath" class="items dropShadow" tabindex="0"
                  data-toggle="tooltip" data-placement="top" :title="item.name"
                />
              </b-col>
            </b-row>
          </div>
          <div class="Situational">
            <b-row align-v="center" no-gutters class="itemRow">
              <b-col cols="1" style="text-align: right">
                Situational
              </b-col>
              <b-col cols="1">
              </b-col>
              <b-col>
                <img
                  v-for="(item, index) in build.items.situational"
                  :key="index"
                  :src="item.imgPath"
                  class="items dropShadow"
                  v-b-tooltip.left.hover = "{ variant: 'secondary' }" :title="item.name"
                />
              </b-col>
            </b-row>
          </div>
        </div>
      </div>
    </div>
  </div>
</transition>
</template>

<script>
import axios from 'axios';

// const localhost = '/api';
const localhost = 'http://localhost:5000/api';

export default {
  data() {
    return {
      buttons: [
        { caption: 'Top', state: true },
        { caption: 'Jungle', state: true },
        { caption: 'Mid', state: true },
        { caption: 'ADC', state: true },
        { caption: 'Support', state: true },
      ],
      sortBy: 'pickRate',
      sortDesc: true,
      fields: [
        { key: 'name', label: 'Name', sortable: true },
        { key: 'banRate', label: 'Ban Rate', sortable: true },
        { key: 'pickRate', label: 'Pick Rate', sortable: true },
        { key: 'winRate', label: 'Win Rate', sortable: true },
        { key: 'lanes', label: 'Role', sortable: true },
      ],
      laneFilter: '',
      searchText: '',
      allChampions: [],

      builds: [],
      build: [],
      selected: [],
      champName: '',
      selectedRole: [],

      indexMap: {},
      runeMap: {},
      shardMap: {},

      activeItem: '',
      showUpdate: false,
    };
  },
  computed: {
    getVariant() {
      if (this.darkMode === true) {
        return 'outline-dark';
      }
      return 'outline-light';
    },
    getInverseVariant() {
      if (this.darkMode === true) {
        return 'outline-light';
      }
      return 'outline-dark';
    },
    currentRouteName() {
      return this.$route.name;
    },
    darkMode() {
      return this.$store.state.darkMode;
    },
    filtered() {
      const buttonStates = this.btnStates;
      if (buttonStates.includes(null) && this.searchText !== '') {
        const filtered = this.allChampions.filter((champion) => {
          if (
            champion.name
              .toLowerCase()
              .indexOf(this.searchText.toLowerCase()) !== -1
            && this.checkLanes(champion.lanes) === true
          ) {
            return champion;
          }
          return null;
        });
        return filtered;
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
      if (this.searchText !== '') {
        const filtered = this.allChampions.filter((champion) => {
          if (
            champion.name
              .toLowerCase()
              .indexOf(this.searchText.toLowerCase()) !== -1
          ) {
            return champion;
          }
          return null;
        });
        return filtered;
      }
      return this.allChampions;
    },
    btnStates() {
      return this.buttons.map((btn) => {
        if (btn.state === true) return btn.caption;
        return null;
      });
    },
  },
  methods: {
    isActiveRune(runeId) {
      const { runes } = this.build.runes;
      for (let i = 0; i < runes.length; i += 1) {
        if (runeId === runes[i]) {
          return true;
        }
      }
      return false;
    },
    isActiveShard(shardId, row) {
      const rowShard = this.build.runes.runes[6 + row];
      if (shardId === rowShard) {
        return true;
      }
      return false;
    },
    chooseBuild(role) {
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
      document.getElementById('buildContainer').classList.add('loading');
      console.log(document.getElementById('buildContainer'));
      // eslint-disable-next-line radix
      const idx = parseInt(index);
      this.selected = this.builds[idx];
      // eslint-disable-next-line prefer-destructuring
      this.selectedRole = this.selected.roles[0];
      this.activeItem = this.selected.roles[0].lane;
      // eslint-disable-next-line prefer-destructuring
      this.build = this.selected.roles[0].builds[0];
      // console.log(JSON.stringify(this.selected));
      this.$nextTick(() => {
        document.getElementById('buildContainer').classList.remove('loading');
      });
    },
    changeSelectedWithRole(index, lane) {
      // eslint-disable-next-line radix
      const idx = parseInt(index);
      for (let i = 0; i < this.builds[idx].roles.length; i += 1) {
        const role = this.builds[idx].roles[i];
        if (role.lane === lane) {
          this.selected = this.builds[idx];
          this.activeItem = role.lane;
          // eslint-disable-next-line prefer-destructuring
          this.selectedRole = role;
          // eslint-disable-next-line prefer-destructuring
          this.build = role.builds[0];
          // console.log(JSON.stringify(this.selected));
        }
      }
    },
    updateBuilds() {
      const path = `${localhost}/update`;
      console.log('loading...');
      this.showUpdate = true;
      axios
        .get(path)
        .then((res) => {
          console.log(res);
          this.showUpdate = false;
          this.allChampions = res.data.stats;
          this.builds = res.data.builds;
          // eslint-disable-next-line prefer-destructuring
          this.selected = this.builds[31];
          // eslint-disable-next-line prefer-destructuring
          this.selectedRole = this.builds[31].roles[0];
          // eslint-disable-next-line prefer-destructuring
          this.build = this.builds[31].roles[0].builds[0];
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    getBuilds() {
      const path = `${localhost}/builds`;
      axios
        .get(path)
        .then((res) => {
          console.log(res);
          this.allChampions = res.data.stats;
          this.builds = res.data.builds;
          this.indexMap = res.data.indexMap;
          this.runeMap = res.data.runeMap;
          this.shardMap = res.data.shardMap;
          if (this.champName === '') {
            // eslint-disable-next-line prefer-destructuring
            this.selected = this.builds[31];
            console.log(this.selected);
            // eslint-disable-next-line prefer-destructuring
            this.selectedRole = this.builds[31].roles[0];
            // eslint-disable-next-line prefer-destructuring
            this.build = this.builds[31].roles[0].builds[0];
            this.runes = {
              primary: this.runeMap[this.build.runes.primaryBranch.id],
              secondary: this.runeMap[this.build.runes.secondaryBranch.id],
            };
            console.log(this.runes);
          }
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
