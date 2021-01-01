<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition-property: opacity;
  transition-duration: 0.25s;
}

.fade-enter-active {
  transition-delay: 0.25s;
}

.fade-leave-active {
  opacity: 0;
}
.parent {
  height: 100vh;
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
  align-content: center;
  display: grid;
  grid-template-columns: 1fr;
  gap: 0px 0px;
  grid-template-areas:
    "bld-Role" "bld-Runes"
    "bld-Skills" "bld-Items";
  align-items: center;
  align-self: center;
  vertical-align: middle;
}

div.bld-Role {
  height: 7.7rem;
  grid-area: bld-Role;
  font-weight: 100;
  background-color: white;
  padding: 3px 10px 10px 10px;
  border-radius: 10px;
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.11), 0 2px 2px rgba(0, 0, 0, 0.11);
}

div.bld-Runes {
  height: 20rem;
  grid-area: bld-Runes;
  background-color: white;
  padding: 10px;
  border-radius: 10px;
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.11), 0 2px 2px rgba(0, 0, 0, 0.11);
}

div.bld-Skills {
  height: 6.6rem;
  grid-area: bld-Skills;
  background-color: white;
  padding: 10px;
  border-radius: 10px;
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.11), 0 2px 2px rgba(0, 0, 0, 0.11);
}

div.bld-Items {
  height: 14.5rem;
  text-align: left;
  grid-area: bld-Items;
  background-color: white;
  padding: 10px;
  border-radius: 10px;
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.11), 0 2px 2px rgba(0, 0, 0, 0.11);
}
div.tableBorder {
  background-color: white;
  padding: 5px 10px;
  border-radius: 10px;
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.11), 0 2px 2px rgba(0, 0, 0, 0.11);
}

th {
  text-align: -internal-center;
  font-size: 14px !important;
  font-weight: normal !important;
  vertical-align: middle !important;
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
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.11), 0 2px 2px rgba(0, 0, 0, 0.11),
    0 4px 4px rgba(0, 0, 0, 0.11), 0 6px 8px rgba(0, 0, 0, 0.11),
    0 8px 16px rgba(0, 0, 0, 0.11);
}

.runes {
  filter: grayscale(100%);
  opacity: 0.27;
  border-radius: 50%;
}

.activeRune {
  filter: none;
  opacity: 1;
  border: 2px solid #3273fa;
}

.activeKeystone {
  width: auto;
  height: 72px;
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
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.2);
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
.fade-in-enter-active {
  transition: all 0.5s ease;
}

.fade-in-leave-active {
  transition: all 0.5s ease;
}

.fade-in-enter, .fade-in-leave-to {
  position: absolute; /* add for smooth transition between elements */
  opacity: 0;
}
.v-align-middle {
  vertical-align: middle;
}
.tableCells {
  position: relative;
  top: 0.6rem;
}
</style>
<template>
  <transition name="fade" mode="out-in">
    <div class="parent">
      <div class="stats" ref="statsContainer">
        <b-row align-v="end" align-h="center" no-gutters>
          <b-col cols="1">
            <b-button
              size="sm"
              class="refresh"
              ref="refresh"
              :variant="getInverseVariant"
              @click="updateBuilds()"
              v-b-tooltip
              title="Refresh Stats"
            >
              <b-icon icon="arrow-clockwise" v-if="!showUpdate"></b-icon>
              <b-spinner small v-if="showUpdate" class="align-middle"></b-spinner>
            </b-button>
          </b-col>
          <b-col v-for="(btn, idx) in buttons" :key="idx" class="ml-4">
            <span class="smallFont" :class="{ 'smallFont-dark': darkMode }">{{ btn.caption }}</span>
            <b-button :variant="getVariant" block size="sm" :pressed.sync="btn.state"
            @click="syncButtonFilters(btn.caption)">
              <img
                :src="'/images/lanes/'+ btn.caption.toLowerCase() +'.png'"
                :alt="btn.caption.toLowerCase()"
                width="24px" height="auto"
                :class="{ 'grayscale': !btn.state }"
              />
            </b-button>
          </b-col>
        </b-row>
        <br />
        <b-row align-v="center" align-h="center">
          <b-col>
            <b-row no-gutters>
              <b-col cols="1" class="searchIcon shadow-sm" :class="{ 'bg-medium': darkMode}">
                <b-icon icon="search" class="svgAlign"></b-icon>
              </b-col>
              <b-col>
                <input
                  v-model="searchText"
                  type="search"
                  ref="filterBox"
                  size="md"
                  placeholder="Filter by Name"
                  autofocus
                  class="form-control filterShadow"
                  :class="{ 'text-white bg-dark': darkMode}"
                />
              </b-col>
            </b-row>
          </b-col>
        </b-row>
        <br />
        <div class="tableBorder mt-1" :class="{ 'bg-dark': darkMode}">
          <b-table
            ref="statsTable"
            small
            no-border-collapse
            borderless
            striped
            sticky-header="42.4rem"
            responsive="false"
            :class="{ 'dark': darkMode}"
            :fields="fields"
            :items="filtered"
            style="overflow-x: hidden;
                   font-size: 14px !important;"
            :sort-by.sync="sortBy"
            :sort-desc.sync="sortDesc"
            :dark="darkMode"
            id="statsTable"
          >
            <template v-slot:head()="fields">
              <span class="font-weight-normal">{{ fields.label }}</span>
            </template>
            <template v-slot:cell(name)="filtered" class="v-align-middle">
              <div class="text-left v-align-middle">
                <b-button
                  block
                  @click="changeSelected(filtered.item.idx)"
                  size="sm"
                  class="champName champBtn"
                  :class="{ 'btn-dark bg-medium': darkMode, 'btn-light': !darkMode}"
                  style="font-family: 'Roboto';"
                >
                  <b-row align-v="center" align-h="start" no-gutters>
                    <b-col>
                      <img
                        :src="'./' + filtered.item.imgPath"
                        :alt="filtered.item.name"
                        width="32px" height="auto"
                        style="margin-right: 15px;"
                      />
                      <span>{{ filtered.item.name }}</span>
                    </b-col>
                  </b-row>
                </b-button>
              </div>
            </template>

            <template v-slot:cell(banRate)="filtered">
              <span class="tableCells"
              :class="{ 'font-weight-bold' : isBoldBanRate(filtered.item.banRate) }">
                {{ filtered.item.banRate + '%' }}
              </span>
            </template>

            <template v-slot:cell(pickRate)="filtered">
              <span class="tableCells"
              :class="{ 'font-weight-bold' : isBoldPickRate(filtered.item.pickRate) }">
                {{ filtered.item.pickRate + '%' }}
              </span>
            </template>

            <template v-slot:cell(winRate)="filtered">
              <span class="tableCells"
              :class="{ 'font-weight-bold' : isBoldWinRate(filtered.item.winRate) }">
                {{ filtered.item.winRate + '%' }}
              </span>
            </template>

            <template v-slot:cell(lanes)="filtered">
              <b-button
                style="position: relative; top: 0.2rem;"
                v-for="lane in filtered.item.lanes"
                :key="lane"
                @click="changeSelectedWithRole(filtered.item.idx, lane)"
                size="sm"
                class="roleBtn mx-1"
                :class="{ 'btn-dark bg-medium': darkMode, 'btn-light': !darkMode}"
              >
                <img :src="'./images/lanes/'+lane+'.png'" :alt="lane" width="24px" height="auto" />
              </b-button>
            </template>
          </b-table>
        </div>
      </div>
      <div class="build" ref="buildContainer">
        <div class="bld-grid-container">
          <div class="bld-Role" :class="{ 'bg-dark': darkMode }">
            <b-row align-v="center" align-h="center">
              <b-col cols="3">
                <div class="pl-1 text-center">{{ selected.name }}</div>
                <img :src="'./' + selected.imgPath"
                class="dropShadow bigChampImg" :key="selected.name" />
              </b-col>
              <b-col cols="3">
                <img
                  class="dropShadow mr-3"
                  :src="'./' + build.spells[0].imgPath"
                  :alt="build.spells[0].name"
                  :key="build.spells[0].name"
                />
                <img
                  class="dropShadow"
                  :src="'./' + build.spells[1].imgPath"
                  :alt="build.spells[1].name"
                  :key="build.spells[1].name"
                />
              </b-col>
              <b-col cols="6">
                <b-row align-v="center" align-h="center">
                  <b-col>
                    <b-row align-v="center" align-h="start">
                      <b-col cols="9" class="pt-2 ml-4">
                        <b-form-select
                          v-model="selectedRole"
                          ref="laneDropdown"
                          size="sm"
                          :class="{ 'text-white bg-dark darkSelect': darkMode}"
                          plain
                        >
                          <b-form-select-option
                            v-for="(role, index) in selected.roles"
                            :key="index"
                            :value="role"
                            @click="chooseBuild(role)"
                          >{{ role.lane }}</b-form-select-option>
                        </b-form-select>
                        <b-form-group ref="roleRadio" class="pt-2 mb-1">
                          <b-form-radio
                            v-for="(buildOpt, index) in selectedRole.builds"
                            :key="index"
                            v-model="build"
                            name="some-radios"
                            :value="buildOpt"
                            :text="buildOpt.name"
                            class="mediumFont text-left"
                            :class="{ 'mediumFont-dark': darkMode }"
                          >{{ buildOpt.name }}</b-form-radio>
                        </b-form-group>
                      </b-col>
                    </b-row>
                  </b-col>
                </b-row>
              </b-col>
            </b-row>
          </div>
          <div class="bld-Runes mt-4" :class="{ 'bg-dark': darkMode }">
            <b-row>
              <b-col cols="6">
                <div class="primary-container">
                  <div
                    class="runeRowHeader"
                    ref="primaryRuneHeader"
                    :class="{ 'bg-medium': darkMode}"
                  >
                    <b-row no-gutters align-v="center"
                    align-h="center" style="flex-wrap: nowrap;">
                      <b-col cols="3">
                        <img
                          :src="'./' + runeMap[build.runes.primaryBranch].imgPath"
                          class="runes dropShadow activeRune"
                          width="40px" height="auto"
                          :key="build.runes.primaryBranch"
                        />
                      </b-col>
                      <b-col cols="9" class="pl-4">
                        {{ runeMap[build.runes.primaryBranch].name }}
                      </b-col>
                    </b-row>
                  </div>
                  <div class="runeRowGroup pt-2">
                    <b-row no-gutters align-v="center" align-h="center"
                    class="my-2 flex-nowrap">
                      <b-col
                        v-for="rune in runeMap[build.runes.primaryBranch].runeRows[0]"
                        :key="rune.name"
                      >
                        <transition name="fade" mode="out-in">
                        <img
                          :src="'./' + rune.imgPath"
                          class="runes dropShadow"
                          width="54px" height="auto"
                          :class="{ 'activeKeystone': isActiveRune(rune.id) }"
                          :key="rune.name"
                        />
                        </transition>
                      </b-col>
                    </b-row>
                  </div>
                  <svg width="85%" height="2">
                    <rect width="100%" height="2"
                    :style="darkMode ? 'fill: var(--dark-gray);' : 'fill: var(--light-gray);'"/>
                  </svg>
                  <div class="runeRowGroup">
                    <b-row no-gutters align-v="center"
                    align-h="center" class="pt-1">
                      <b-col v-for="rune in runeMap[build.runes.primaryBranch].runeRows[1]"
                      :key="rune.name">
                        <transition name="fade" mode="out-in">
                        <img
                          :src="'./' + rune.imgPath"
                          class="runes dropShadow"
                          height="40px"
                          width="auto"
                          :class="{ 'activeRune': isActiveRune(rune.id) }"
                          :key="rune.name"
                        />
                        </transition>
                      </b-col>
                    </b-row>
                    <b-row no-gutters align-v="center"
                    align-h="center" class="pt-1">
                      <b-col v-for="rune in runeMap[build.runes.primaryBranch].runeRows[2]"
                      :key="rune.name">
                        <transition name="fade" mode="out-in">
                        <img
                          :src="'./' + rune.imgPath"
                          class="runes dropShadow"
                          height="40px"
                          width="auto"
                          :class="{ 'activeRune': isActiveRune(rune.id) }"
                          :key="rune.name"
                        />
                        </transition>
                      </b-col>
                    </b-row>
                    <b-row no-gutters align-v="center"
                    align-h="center" class="pt-1">
                      <b-col v-for="rune in runeMap[build.runes.primaryBranch].runeRows[3]"
                      :key="rune.name">
                        <transition name="fade" mode="out-in">
                        <img
                          :src="'./' + rune.imgPath"
                          class="runes dropShadow"
                          height="40px"
                          width="auto"
                          :class="{ 'activeRune': isActiveRune(rune.id) }"
                          :key="rune.name"
                        />
                        </transition>
                      </b-col>
                    </b-row>
                  </div>
                </div>
              </b-col>
              <b-col cols="6">
                <div class="secondary-container">
                  <div class="runeRowHeader" ref="secondaryRuneHeader"
                  :class="{ 'bg-medium': darkMode}">
                    <b-row no-gutters align-v="center" align-h="center">
                      <b-col cols="3">
                        <img
                          :src="'./' + runeMap[build.runes.secondaryBranch].imgPath"
                          class="runes dropShadow activeRune"
                          width="40px" height="auto"
                          :key="build.runes.secondaryBranch"
                        />
                      </b-col>
                      <b-col cols="9" class="pl-4">
                        {{ runeMap[build.runes.secondaryBranch].name }}
                      </b-col>
                    </b-row>
                  </div>
                  <div class="runeRowGroup pt-1">
                    <b-row no-gutters align-v="center" align-h="center" class="pt-1">
                      <b-col v-for="rune in runeMap[build.runes.secondaryBranch].runeRows[1]"
                      :key="rune.name">
                        <transition name="fade" mode="out-in">
                          <img
                            :src="'./' + rune.imgPath"
                            class="runes dropShadow"
                            height="40px"
                            width="auto"
                            :class="{ 'activeRune': isActiveRune(rune.id) }"
                          />
                        </transition>
                      </b-col>
                    </b-row>
                    <b-row no-gutters align-v="center" align-h="center" class="pt-1">
                      <b-col v-for="rune in runeMap[build.runes.secondaryBranch].runeRows[2]"
                      :key="rune.name">
                        <transition name="fade" mode="out-in">
                          <img
                            :src="'./' + rune.imgPath"
                            class="runes dropShadow"
                            height="40px"
                            width="auto"
                            :class="{ 'activeRune': isActiveRune(rune.id) }"
                          />
                        </transition>
                      </b-col>
                    </b-row>

                    <b-row no-gutters align-v="center" align-h="center" class="pt-1">
                      <b-col v-for="rune in runeMap[build.runes.secondaryBranch].runeRows[3]"
                      :key="rune.name">
                        <transition name="fade" mode="out-in">
                          <img
                            :src="'./' + rune.imgPath"
                            class="runes dropShadow"
                            height="40px"
                            width="auto"
                            :class="{ 'activeRune': isActiveRune(rune.id) }"
                          />
                        </transition>
                      </b-col>
                    </b-row>
                  </div>
                  <svg width="85%" height="2">
                    <rect width="100%" height="2"
                    :style="darkMode ? 'fill: var(--dark-gray);' : 'fill: var(--light-gray);'"/>
                  </svg>
                  <div class="runeRowGroup">
                    <b-row no-gutters align-v="center"
                    align-h="center" class="pt-1">
                      <b-col v-for="(shard, colIndex) in shardMap[0]" :key="colIndex">
                        <transition name="fade" mode="out-in">
                          <img
                            :src="'./' + shard.imgPath"
                            class="runes dropShadow"
                            height="27px"
                            width="auto"
                            :ref="shard.id"
                            :class="{ 'activeRune': isActiveShard(shard.id, 0) }"
                            :key="shard.id"
                          />
                        </transition>
                      </b-col>
                    </b-row>
                    <b-row no-gutters align-v="center"
                    align-h="center" class="pt-1">
                      <b-col v-for="(shard, colIndex) in shardMap[1]" :key="colIndex">
                        <transition name="fade" mode="out-in">
                          <img
                            :src="'./' + shard.imgPath"
                            class="runes dropShadow"
                            height="27px"
                            width="auto"
                            :ref="shard.id"
                            :class="{ 'activeRune': isActiveShard(shard.id, 1) }"
                            :key="shard.id"
                          />
                        </transition>
                      </b-col>
                    </b-row>
                    <b-row no-gutters align-v="center"
                    align-h="center" class="pt-1">
                      <b-col v-for="(shard, colIndex) in shardMap[2]" :key="colIndex">
                        <transition name="fade" mode="out-in">
                          <img
                            :src="'./' + shard.imgPath"
                            class="runes dropShadow"
                            height="27px"
                            width="auto"
                            :ref="shard.id"
                            :class="{ 'activeRune': isActiveShard(shard.id, 2) }"
                            :key="shard.id"
                          />
                        </transition>
                      </b-col>
                    </b-row>
                  </div>
                </div>
              </b-col>
            </b-row>
          </div>
          <div class="bld-Skills mt-4" :class="{ 'bg-dark': darkMode }">
            <b-row align-v="center" align-h="center" class="pb-2">
              <b-col :key="build.skills[0].name" cols="3">
                <span
                  class="smallFont"
                  :class="{ 'smallFont-dark': darkMode }"
                >{{ build.skills[0].name }}</span>
                <br />
                <div :key="build.skills[0].button">{{ build.skills[0].button }}</div>
                <img :src="'./' + build.skills[0].imgPath"
                :key="build.skills[0].imgPath" class="dropShadow"/>
              </b-col>
              <b-col>
                <div>
                  <b-icon icon="arrow-right"></b-icon>
                </div>
              </b-col>
              <b-col :key="build.skills[1].name" cols="3">
                <span
                  class="smallFont"
                  :class="{ 'smallFont-dark': darkMode }"
                >{{ build.skills[1].name }}</span>
                <br />
                <div :key="build.skills[1].button">{{ build.skills[1].button }}</div>
                <img :src="'./' + build.skills[1].imgPath"
                :key="build.skills[1].imgPath" class="dropShadow"/>
              </b-col>
              <b-col>
                <div>
                  <b-icon icon="arrow-right"></b-icon>
                </div>
              </b-col>
              <b-col :key="build.skills[2].name" cols="3">
                <span
                  class="smallFont"
                  :class="{ 'smallFont-dark': darkMode }"
                >{{ build.skills[2].name }}</span>
                <br />
                <div :key="build.skills[2].button">{{ build.skills[2].button }}</div>
                <img :src="'./' + build.skills[2].imgPath"
                :key="build.skills[2].imgPath" class="dropShadow"/>
              </b-col>
            </b-row>
          </div>
          <div class="bld-Items mt-4" :class="{ 'bg-dark': darkMode }">
            <b-row align-v="center" no-gutters class="py-1">
              <b-col cols="2" class="text-center">Early</b-col>
              <b-col>
                <img
                  v-for="(item, index) in build.items.general.start"
                  :key="index"
                  :src="'./' + item.imgPath"
                  class="mx-2 mb-2 dropShadow"
                  v-b-tooltip
                  :title="item.name"
                />
              </b-col>
            </b-row>
            <b-row align-v="center" no-gutters class="py-1">
              <b-col cols="2" class="text-center">Core</b-col>
              <b-col>
                <img
                  v-for="(item, index) in build.items.general.core"
                  :key="index"
                  :src="'./' + item.imgPath"
                  class="mx-2 mb-2 dropShadow"
                  v-b-tooltip
                  :title="item.name"
                />
              </b-col>
            </b-row>
            <b-row align-v="center" align-h="center" no-gutters class="py-1">
              <b-col cols="2" class="text-center">Late</b-col>
              <b-col>
                <img
                  v-for="(item, index) in build.items.general.full"
                  :key="index"
                  :src="'./' + item.imgPath"
                  class="mx-2 mb-2 dropShadow"
                  v-b-tooltip
                  :title="item.name"
                />
              </b-col>
            </b-row>
            <b-row align-v="center" no-gutters class="py-1 pb-1">
              <b-col cols="2" class="text-center">Situational</b-col>
              <b-col>
                <img
                  v-for="(item, index) in build.items.situational"
                  :key="index"
                  :src="'./' + item.imgPath"
                  class="mx-2 dropShadow"
                  v-b-tooltip
                  :title="item.name"
                />
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
      filterCount: 0,
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
    syncButtonFilters(buttonName) {
      if (this.filterCount === 0) {
        for (let i = 0; i < this.buttons.length; i += 1) {
          if (this.buttons[i].caption !== buttonName) {
            this.buttons[i].state = false;
          } else {
            this.buttons[i].state = true;
          }
        }
      }
      this.filterCount += 1;
    },
    isBoldBanRate(value) {
      if (value >= 15) {
        return true;
      }
      return false;
    },
    isBoldWinRate(value) {
      if (value >= 53) {
        return true;
      }
      return false;
    },
    isBoldPickRate(value) {
      if (value >= 7) {
        return true;
      }
      return false;
    },
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
