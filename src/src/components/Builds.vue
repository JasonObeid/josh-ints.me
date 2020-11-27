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
  padding: 10px 0px 0px 0px;
  display: grid;
  grid-template-columns: 2fr 1.5fr;
  grid-template-rows: 1fr;
  column-gap: 50px;
  row-gap: 0px;
}

.stats {
  grid-area: 1 / 1 / 2 / 2;
}

.build {
  grid-area: 1 / 2 / 2 / 3;
}

.bld-grid-container {
  display: grid;
  grid-template-columns: 1fr;
  gap: 0px 0px;
  grid-template-areas:
    "bld-Role" "bld-RuneHeader" "bld-Runes"
    "bld-SkillHeader" "bld-Skills" "bld-ItemHeader" "bld-Items";
  align-items: center;
  align-self: center;
  vertical-align: middle;
}

div.bld-Role {
  grid-area: bld-Role;
  font-weight: 100;
  background-color: white;
  padding: 5px 10px 10px 10px;
  border-radius: 10px;
  box-shadow: 0 1px 1px rgba(0,0,0,0.11),
              0 2px 2px rgba(0,0,0,0.11)
}

.bld-RuneHeader {
  grid-area: bld-RuneHeader;
  text-align: left;
  font-weight: bold;
}

div.bld-Runes {
  grid-area: bld-Runes;
  background-color: white;
  padding: 10px;
  border-radius: 10px;
  box-shadow: 0 1px 1px rgba(0,0,0,0.11),
              0 2px 2px rgba(0,0,0,0.11)
}

.bld-SkillHeader {
  grid-area: bld-SkillHeader;
  text-align: left;
  font-weight: bold;
}

div.bld-Skills {
  grid-area: bld-Skills;
  background-color: white;
  padding: 10px;
  border-radius: 10px;
  box-shadow: 0 1px 1px rgba(0,0,0,0.11),
              0 2px 2px rgba(0,0,0,0.11)
}

.bld-ItemHeader {
  grid-area: bld-ItemHeader;
  text-align: left;
  font-weight: bold;
}

div.bld-Items {
  text-align: left;
  grid-area: bld-Items;
  background-color: white;
  padding: 7px 10px;
  border-radius: 10px;
  box-shadow: 0 1px 1px rgba(0,0,0,0.11),
              0 2px 2px rgba(0,0,0,0.11)
}
div.tableBorder {
  background-color: white;
  padding: 7px 10px;
  border-radius: 10px;
  box-shadow: 0 1px 1px rgba(0,0,0,0.11),
              0 2px 2px rgba(0,0,0,0.11)
}
table > tbody > tr > td {
    font-size: 8px !important;
    vertical-align: middle !important;
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
.bigChampImg {
  height: 80px;
  width: auto;
}
.sort {
  cursor: pointer;
}

.items {
  text-align: left;
}

.filterShadow {
  border: 0px;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
  -webkit-transition: all 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
  transition: all 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
  border-radius: 0 5px 5px 0;
}

.filterShadow:hover {
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
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
.runeRowHeader {
  text-align: left;
  padding: 2% 5%;
  border-radius: 10px;
  background-color: var(--light-gray);
  box-shadow: 0 1px 1px rgba(0,0,0,0.2);
}
.runeRowGroup {
  margin: 3% 0;
  border-radius: 10px;
}

.svgAlign {
  position: absolute;
  top: 50%;
  -webkit-transform: translateY(-50%);
  -ms-transform: translateY(-50%);
  transform: translateY(-50%);
  left: 0;
  right: 0;
  margin: auto;
  text-align: center;
}

.searchIcon {
  background-color: var(--light-gray);
  border-radius: 5px 0 0 5px;
}

.smallFont {
  font-size: 12px;
  color: var(--dark-gray);
}

.mediumFont {
  font-size: 13px;
  color: var(--dark-gray);
}

.smallFont-dark {
  color: var(--light-gray);
}

.mediumFont-dark {
  color: var(--light-gray);
}
.bg-medium {
  background-color: var(--dark-gray);
}
.grayscale {
  filter: grayscale(1);
}
</style>
<template>
<transition name="fade" mode="out-in">
  <div class="parent">
    <div class="stats" ref="statsContainer">
      <!--<b-row align-v="center" align-h="start">
        <b-col style="text-align: left" class="smallFont" :class="{ 'smallFont-dark': darkMode }">
          <span style="margin-right: 5px">Filters</span>
          <b-icon icon='filter'></b-icon>
        </b-col>
      </b-row>!-->
      <b-row align-v="end" align-h="center" no-gutters>
        <b-col cols="1">
          <b-button size="sm" class="refresh" ref="refresh"
          :variant="getInverseVariant" @click='updateBuilds()'>
            <b-icon icon="arrow-clockwise" v-if="!showUpdate"></b-icon>
            <b-spinner small v-if="showUpdate" class="align-middle"></b-spinner>
          </b-button>
        </b-col>
        <b-col v-for="(btn, idx) in buttons" :key="idx" class="mx-2">
          <span class="smallFont" :class="{ 'smallFont-dark': darkMode }">{{ btn.caption }}</span>
          <b-button :pressed.sync="btn.state" :variant="getVariant" block size="sm">
            <img :src="'/images/lanes/'+ btn.caption.toLowerCase() +'.png'"
            :alt="btn.caption.toLowerCase()" width="24px"
            :class="{ 'grayscale': !btn.state }"/>
          </b-button>
        </b-col>
      </b-row>
      <br>
      <b-row align-v="center" align-h="center">
        <b-col>
          <b-row no-gutters>
            <b-col cols="1" class="searchIcon" :class="{ 'bg-medium': darkMode}">
              <b-icon icon='search' class="svgAlign"></b-icon>
            </b-col>
            <b-col>
              <input v-model="searchText" type="search" ref="filterBox" size="md"
              placeholder="Filter by Name" autofocus class="form-control filterShadow"
              :class="{ 'text-white bg-dark': darkMode}">
            </b-col>
          </b-row>
        </b-col>
      </b-row>
      <br>
      <div class="tableBorder" :class="{ 'bg-dark': darkMode}">
        <b-table ref="statsTable"
          small no-border-collapse
          borderless striped
          sticky-header="688px"
          responsive="false"
          :class="{ 'dark': darkMode}"
          :fields="fields"
          :items="filtered"
          style="overflow-x: hidden; vertical-align: middle;"
          :sort-by.sync="sortBy"
          :sort-desc.sync="sortDesc"
          :dark="darkMode"
          thead-class="tableHeader"
          id="statsTable">
          <!-- A custom formatted column -->
          <template v-slot:cell(name)="filtered">
            <div class="text-left">
              <b-button block @click="changeSelected(filtered.item.idx)"
              size="sm" class="champName champBtn"
              :class="{ 'btn-dark bg-medium': darkMode, 'btn-light': !darkMode}">
                <b-row align-v="center" align-h="start" no-gutters>
                  <b-col>
                    <img :src="filtered.item.imgPath" :alt="filtered.item.name" width="32px"
                    style="margin-right: 15px;"/>
                    <span>{{ filtered.item.name }}</span>
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
                  :class="{ 'btn-dark bg-medium': darkMode, 'btn-light': !darkMode}">
                  <img :src="'/images/lanes/'+lane+'.png'"
                    :alt="lane" width="24px"/>
                </b-button>
              </b-col>
            </b-row>
          </template>
        </b-table>
      </div>
    </div>
    <div class="build" ref="buildContainer">
      <div class="bld-grid-container">
        <div class="bld-Role" :class="{ 'bg-dark': darkMode }">
            <b-row align-v="center" align-h="center">
              <b-col cols="5">
                <b-row align-v="center" align-h="center">
                  <b-col cols="7" >
                    <div class="pl-1 text-center">
                      {{ selected.name }}
                    </div>
                    <img :src="selected.imgPath" class="dropShadow bigChampImg"
                    :key="selected.name"/>
                  </b-col>
                  <b-col cols="5">
                    <b-col>
                      <img class="dropShadow"
                        :src="build.spells[0].imgPath"
                        :alt="build.spells[0].name"
                        :key="build.spells[0].name"
                      />
                    </b-col>
                    <b-col class="mt-3">
                      <img class="dropShadow"
                        :src="build.spells[1].imgPath"
                        :alt="build.spells[1].name"
                        :key="build.spells[1].name"
                      />
                    </b-col>
                  </b-col>
                </b-row>
              </b-col>
              <b-col cols="7">
                <b-row align-v="center" align-h="center">
                  <b-col>
                    <b-row align-v="center" align-h="start">
                      <b-col cols="9" class='pt-2  ml-4'>
                        <b-form-select v-model="selectedRole" ref="laneDropdown" size="sm"
                        :class="{ 'text-white bg-dark darkSelect': darkMode}" plain>
                          <b-form-select-option
                            v-for="(role, index) in selected.roles"
                            :key="index"
                            :value="role"
                            @click="chooseBuild(role)"
                          >{{ role.lane }}</b-form-select-option>
                        </b-form-select>
                        <b-form-group ref="roleRadio">
                          <b-form-radio
                            v-for="(buildOpt, index) in selectedRole.builds"
                            :key="index"
                            v-model="build"
                            name="some-radios"
                            :value="buildOpt"
                            :text="buildOpt.name"
                            class="mediumFont pt-2 text-left"
                            :class="{ 'mediumFont-dark': darkMode }">
                            {{ buildOpt.name }}
                          </b-form-radio>
                        </b-form-group>
                      </b-col>
                    </b-row>
                  </b-col>
                </b-row>
              </b-col>
            </b-row>
        </div>
        <div class="bld-RuneHeader pt-3">
          Runes
        </div>
        <div class="bld-Runes" :class="{ 'bg-dark': darkMode }">
          <b-row>
            <b-col>
              <div class="primary-container">
                <div class="runeRowHeader" ref="primaryRuneHeader"
                :class="{ 'bg-medium': darkMode}">
                  <b-row no-gutters align-v="center" align-h="center">
                    <b-col cols="3">
                      <img :src="runeMap[build.runes.primaryBranch].imgPath"
                      class="runes dropShadow activeRune" width="32px"
                      :key="build.runes.primaryBranch"/>
                    </b-col>
                    <b-col cols="9" class="pl-4">
                      {{ runeMap[build.runes.primaryBranch].name }}
                    </b-col>
                  </b-row>
                </div>
                <div class="runeRowGroup">
                  <b-row no-gutters align-v="center" align-h="center" class="my-3">
                    <b-col v-for="rune in runeMap[build.runes.primaryBranch].runeRows[0]"
                    :key="rune.name">
                      <img :src="rune.imgPath"
                      class="runes dropShadow" width="64px"
                      :class="{ 'activeRune': isActiveRune(rune.id) }"
                      :key="rune.name"/>
                    </b-col>
                  </b-row>
                </div>
                <div class="runeRowGroup">
                  <b-row no-gutters align-v="center" align-h="center" class="my-2"
                  v-for="runeRow in runeMap[build.runes.primaryBranch].runeRows.slice(1)"
                  :key="runeRow.name">
                    <b-col v-for="rune in runeRow" :key="rune.name">
                      <img :src="rune.imgPath"
                      class="runes dropShadow" width="36px"
                      :class="{ 'activeRune': isActiveRune(rune.id) }"
                      :key="rune.name"/>
                    </b-col>
                  </b-row>
                </div>
              </div>
            </b-col>
            <b-col>
              <div class="secondary-container">
                <div class="runeRowHeader" ref="secondaryRuneHeader"
                :class="{ 'bg-medium': darkMode}">
                  <b-row no-gutters align-v="center" align-h="center">
                    <b-col cols="3">
                      <img :src="runeMap[build.runes.secondaryBranch].imgPath"
                      class="runes dropShadow activeRune" width="32px"
                      :key="build.runes.secondaryBranch"/>
                    </b-col>
                    <b-col cols="9" class="pl-4">
                      {{ runeMap[build.runes.secondaryBranch].name }}
                    </b-col>
                  </b-row>
                </div>
                <div class="runeRowGroup">
                  <b-row no-gutters align-v="center" align-h="center" class="my-2"
                  v-for="runeRow in runeMap[build.runes.secondaryBranch].runeRows.slice(1)"
                  :key="runeRow.name">
                    <b-col v-for="rune in runeRow" :key="rune.name">
                      <img :src="rune.imgPath"
                      class="runes dropShadow" width="36px"
                      :class="{ 'activeRune': isActiveRune(rune.id) }"/>
                    </b-col>
                  </b-row>
                </div>
                <div class="runeRowGroup">
                  <b-row no-gutters align-v="center" align-h="center" class="my-1"
                  v-for="(auxRow, rowIndex) in shardMap" :key="rowIndex">
                    <b-col v-for="(shard, colIndex) in auxRow" :key="colIndex">
                      <img :src="shard.imgPath"
                      class="runes dropShadow" height="24px" width="auto" :ref="shard.id"
                      :class="{ 'activeRune': isActiveShard(shard.id, rowIndex) }"
                      :key="shard.id"/>
                    </b-col>
                  </b-row>
                </div>
              </div>
            </b-col>
          </b-row>
        </div>
        <div class="bld-SkillHeader pt-3">
          Skills
        </div>
        <div class="bld-Skills" :class="{ 'bg-dark': darkMode }">
          <b-row align-v="center" align-h="center">
            <b-col :key="build.skills[0].name" cols="3">
              <span class="smallFont" :class="{ 'smallFont-dark': darkMode }">
                {{ build.skills[0].name }}
              </span>
              <br />
              <div :key="build.skills[0].button" >{{ build.skills[0].button }}</div>
              <img :src="build.skills[0].imgPath"
              :key="build.skills[0].imgPath" class="dropShadow"/>
            </b-col>
            <b-col>
              <div>
                <b-icon icon="arrow-right"></b-icon>
              </div>
            </b-col>
            <b-col :key="build.skills[1].name" cols="3">
              <span class="smallFont" :class="{ 'smallFont-dark': darkMode }">
                {{ build.skills[1].name }}
              </span>
              <br />
              <div :key="build.skills[1].button" >{{ build.skills[1].button }}</div>
              <img :src="build.skills[1].imgPath"
              :key="build.skills[1].imgPath" class="dropShadow"/>
            </b-col>
            <b-col>
              <div>
                <b-icon icon="arrow-right"></b-icon>
              </div>
            </b-col>
            <b-col :key="build.skills[2].name" cols="3">
              <span class="smallFont"
              :class="{ 'smallFont-dark': darkMode }">
                {{ build.skills[2].name }}
              </span>
              <br />
              <div :key="build.skills[2].button" >{{ build.skills[2].button }}</div>
              <img :src="build.skills[2].imgPath"
              :key="build.skills[2].imgPath" class="dropShadow"/>
            </b-col>
          </b-row>
        </div>
        <div class="bld-ItemHeader pt-3">
          Items
        </div>
        <div class="bld-Items" :class="{ 'bg-dark': darkMode }">
          <b-row align-v="center" no-gutters class="itemRow">
            <b-col cols="2" class="text-center">
              Early
            </b-col>
            <b-col>
              <img v-for="(item, index) in build.items.general.start"
                :key="index" :src="item.imgPath" class="mx-2  mb-2 dropShadow"
                v-b-tooltip :title="item.name"/>
            </b-col>
          </b-row>
          <b-row align-v="center" no-gutters class="itemRow">
            <b-col cols="2" class="text-center">
              Core
            </b-col>
            <b-col>
              <img v-for="(item, index) in build.items.general.core"
                :key="index" :src="item.imgPath" class="mx-2 mb-2 dropShadow"
                v-b-tooltip :title="item.name"/>
            </b-col>
          </b-row>
          <b-row align-v="center" align-h="center" no-gutters>
            <b-col cols="2" class="text-center">
              Late
            </b-col>
            <b-col>
              <img v-for="(item, index) in build.items.general.full"
                :key="index" :src="item.imgPath" class="mx-2 mb-2 dropShadow"
                v-b-tooltip :title="item.name"/>
            </b-col>
          </b-row>
          <b-row align-v="center" no-gutters class="itemRow">
            <b-col cols="2" class="text-center">
              Situational
            </b-col>
            <b-col>
              <img v-for="(item, index) in build.items.situational"
                :key="index" :src="item.imgPath" class="mx-2 dropShadow"
                v-b-tooltip :title="item.name"/>
            </b-col>
          </b-row>
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
      build: {},
      selected: [],
      champName: '',
      selectedRole: {},
      runes: {},

      indexMap: {},
      runeMap: {},
      shardMap: {},

      activeItem: '',
      showUpdate: false,
    };
  },
  computed: {
    getTipVariant() {
      if (this.darkMode === true) {
        return 'light';
      }
      return 'dark';
    },
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
      console.log(buttonStates);
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
        if (btn.state === true) return btn.caption.toLowerCase();
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
      this.runes = {
        primary: this.runeMap[this.build.runes.primaryBranch],
        secondary: this.runeMap[this.build.runes.secondaryBranch],
      };
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
      // eslint-disable-next-line prefer-destructuring
      this.selectedRole = this.selected.roles[0];
      this.activeItem = this.selected.roles[0].lane;
      // eslint-disable-next-line prefer-destructuring
      this.build = this.selected.roles[0].builds[0];
      this.runes = {
        primary: this.runeMap[this.build.runes.primaryBranch],
        secondary: this.runeMap[this.build.runes.secondaryBranch],
      };
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
          this.runes = {
            primary: this.runeMap[this.build.runes.primaryBranch],
            secondary: this.runeMap[this.build.runes.secondaryBranch],
          };
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
          this.runes = {
            primary: this.runeMap[this.build.runes.primaryBranch],
            secondary: this.runeMap[this.build.runes.secondaryBranch],
          };
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
              primary: this.runeMap[this.build.runes.primaryBranch],
              secondary: this.runeMap[this.build.runes.secondaryBranch],
            };
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
  watch: {
    selectedRole() {
      // eslint-disable-next-line prefer-destructuring
      this.build = this.selectedRole.builds[0];
      this.runes = {
        primary: this.runeMap[this.build.runes.primaryBranch],
        secondary: this.runeMap[this.build.runes.secondaryBranch],
      };
    },
  },
};
</script>
