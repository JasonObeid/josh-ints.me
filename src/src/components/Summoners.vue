<style scoped>
img.champIcon {
  border-radius: 50%;
}
img {
  border-radius: 20%;
}
.flex-container
{
  vertical-align:middle;
  align-items:center;
  text-align:center;
  white-space: nowrap;
  padding: 1% 0;
  width: 100%;
}

.champName
{
  vertical-align: top;
}
.trinket
{
  position: relative;
  top: 1.2rem;
  vertical-align: middle;
}

.btn-carry
{
  background-color: #f2e0ff;
}
.btn-carry:hover
{
  background-color: #d19af9;
}

.btn-damage
{
  background-color: #efdcba;
}
.btn-damage:hover
{
  background-color: #debb7b;
}

.btn-tank
{
  background-color: #e0f3ff;
}
.btn-tank:hover
{
  background-color: #7ec6f3;
}

.btn-darkCarry
{
  background-color: #946bb1;
}
.btn-darkCarry:hover
{
  background-color: #af8dc7;
}

.btn-darkDamage
{
  background-color: #aa7f35;
}
.btn-darkDamage:hover
{
  background-color: #cca660;
}

.btn-darkTank
{
  background-color: #3777a0;
}
.btn-darkTank:hover
{
  background-color: #3592cc;
}

.btn-darkTeam
{
  background-color: #646464 !important;
}
.btn-darkTeam:hover
{
  background-color: #808080 !important;
}

.btn-lightTeam
{
  background-color: #f3f3f3;
}
.btn-lightTeam:hover
{
  background-color: #c5c5c5;
}

.blueTeam
{
  text-align: left;
  align-items:right;
}
.redTeam
{
  text-align: right;
  align-items:right;
}
button.sort
{
  background-color: transparent;
  border-style:ridge;
}
.win
{
  background-color: #c7e6cc;
}
.loss
{
  background-color: #f9baba;
}

.winDark
{
  background-color: #2b4a2b;
}
.lossDark
{
  background-color: #611c1c;
}

.indicator.win {
  background-color: #309c30;
}
.indicator.loss {
  background-color: #a02f2f;
}

.indicator.winDark {
  background-color: #309c30;
}
.indicator.lossDark {
  background-color: #a02f2f;
}

.nav-tabsDark {
  border-bottom: 0px solid #545658;
}
.nav-tabs {
  border-bottom: 0px solid #545658;
}

.table td
{
  vertical-align: middle;
}

.summonerTab-active
{
  border-bottom: 3px solid #000000b9 !important;
}
.summonerTab-inactive
{
  background-color: #f9f8f7;
  border-bottom: 3px solid transparent;
}
.sort
{
  cursor: pointer;
}

.dropShadow {
  box-shadow: 0 1px 1px rgba(0,0,0,0.11),
              0 2px 2px rgba(0,0,0,0.11),
              0 4px 4px rgba(0,0,0,0.11),
              0 6px 8px rgba(0,0,0,0.11),
              0 8px 16px rgba(0,0,0,0.11);
}
.iconShadow {
  filter: drop-shadow(.05rem .1rem 0.3rem #1a1a1a);
}

.champIcon {
  box-shadow: 0 1px 1px rgba(0,0,0,0.11),
              0 2px 2px rgba(0,0,0,0.11),
              0 4px 4px rgba(0,0,0,0.11),
              0 6px 8px rgba(0,0,0,0.11),
              0 8px 16px rgba(0,0,0,0.11);
  -webkit-transition: all 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
  transition: all 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
}

.champIcon:hover {
  box-shadow: 0 2px 1px rgba(0,0,0,0.09),
              0 4px 2px rgba(0,0,0,0.09),
              0 8px 4px rgba(0,0,0,0.09),
              0 16px 8px rgba(0,0,0,0.09),
              0 32px 16px rgba(0,0,0,0.09);
  -webkit-transition: all 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
  transition: all 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
}

.smallChampIcon {
  box-shadow: 0 1px 1px rgba(0,0,0,0.11),
              0 2px 2px rgba(0,0,0,0.11),
              0 4px 4px rgba(0,0,0,0.11),
              0 6px 8px rgba(0,0,0,0.11),
              0 8px 16px rgba(0,0,0,0.11);
  -webkit-transition: all 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
  transition: all 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
}

.smallChampIcon:hover {
  box-shadow: 0 2px 1px rgba(0,0,0,0.09),
              0 4px 2px rgba(0,0,0,0.09),
              0 8px 4px rgba(0,0,0,0.09),
              0 16px 8px rgba(0,0,0,0.09),
              0 32px 16px rgba(0,0,0,0.09);
  -webkit-transition: all 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
  transition: all 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
}

.btn-sm {
  box-shadow: 0 2px 3px rgba(0, 0, 0, 0.2);
  -webkit-transition: all 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
  transition: all 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
}

.btn-sm:hover {
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
  -webkit-transition: all 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
  transition: all 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
}

.darkMode {
  background-color: #535a61;
  color: white;
}
.modal-open body {
  -moz-filter: blur(1px);
  -o-filter: blur(1px);
  -ms-filter: blur(1px);
  filter: blur(5px) grayscale(90%);
  -webkit-filter: blur(5px) grayscale(90%);
}

.nav-linkDark {
  border-color: #414344;
  background-color: #2c3136 !important;
  color: #fdfdfd !important;
}
.nav-linkDark:hover {
  border-top-color: #414344 !important;
  border-right-color: #414344 !important;
  border-left-color: #414344 !important;
  background-color: #3a3e42 !important;
  color: #fdfdfd !important;
}
.nav-linkDark:focus {
  border-color: #252525;
}
.nav-linkDark-active {
  border-top-color: #414344 !important;
  border-right-color: #414344 !important;
  border-left-color: #414344 !important;
  background-color: #3a3e42 !important;
  color: #fdfdfd !important;
}
.nav-linkDark-active:hover {
  border-top-color: rgb(66, 68, 70) !important;
  border-right-color: rgb(66, 68, 70) !important;
  border-left-color: rgb(66, 68, 70) !important;
  background-color: #3a3e42 !important;
  color: #fdfdfd !important;
}
.nav-linkDark .summonerTab-active
{
  border-bottom: 3px solid #ffffff93 !important;
}
.nav-linkDark .summonerTab-inactive
{
  border-bottom: 3px solid #3a3e42;
}

.teammateBtn {
  font-size: 9pt;
}
.match {
  border-radius: 1rem;
  display: grid;
  grid-template-columns: 2% 13% 20% 13% minmax(120px,25%) minmax(155px,15%) 17%;
  align-items: center;
  width: 100%;
}

.sortIcon {
  cursor: pointer;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
  -webkit-transition: all 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
  transition: all 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
}

.sortIcon:hover {
  text-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
  -webkit-transition: all 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
  transition: all 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
}
.smaller {
  font-size: 8pt;
  letter-spacing: 1px;
}

@keyframes fadeIn {
  0% {opacity:0.5;}
  50% {opacity:0.8;}
  100% {opacity:0.5;}
}

@keyframes fadeOut {
  0% {opacity:0.8;}
  50% {opacity:0.5;}
  100% {opacity:0.8;}
}
.animate-flicker:nth-child(even) {
    animation: fadeIn 2s infinite ease-in-out;
}
.animate-flicker:nth-child(odd) {
    animation: fadeOut 2s infinite ease-in-out;
}
</style>

<template>
<transition name="fade" mode="out-in">
  <div class="flex-container">
     <ul class="nav nav-tabs" width='100%' ref="summonerTab"
      :class="{ 'nav-tabsDark': darkMode }">
      <li v-for="(summoner, index) in summoners"
      :key="index" :title="summoner.name"
      :class="{ 'nav-linkDark': darkMode}">
        <button type="button" class="btn nav-link summonerTab-inactive"
        @click.prevent="setActiveTab(summoner.name)"
        :class="{ 'active summonerTab-active': isActiveTab(summoner.name),
        'nav-linkDark': darkMode,
        'nav-linkDark-active': darkMode && isActiveTab(summoner.name)}">
          <a>{{ summoner.name }} | </a>
          <a>{{ summoner.rank }}</a>
          <b-button size='sm' @click.prevent="removeSummoner(summoner.id, summoner.name)"
          variant="outline-danger" class="ml-3">
            x
          </b-button>
        </button>
      </li>
      <li class="nav-item">
        <a class="nav-link" :class="{ 'nav-linkDark': darkMode}">
          <b-button variant="outline-primary" size='sm' v-b-modal.addSummonerModal>
            +
          </b-button>
        </a>
      </li>
      <li class="nav-item ml-auto">
        <button type="button" class="btn btn-secondary btn-sm"
        ref="refresh" @click='refreshSummoners()'>
          <b-icon icon="arrow-clockwise"></b-icon>
          Refresh
          <b-spinner small v-if="showRefresh" class="align-middle"></b-spinner>
        </button>
      </li>
    </ul>
    <div class="px-3 py-1 mt-1 tab-content rounded-lg" ref="myTabContent"
    key="tab" :class="darkMode ? 'bg-dark': 'bg-light'">
      <div v-for="(summoner, index) in summoners" :key="index"
      class="tab-pane fade" :ref=(summoner.name)
      :class="{ 'active show': isActiveTab(summoner.name) }">
        <div v-if="!summoner.hasOwnProperty('matchInfo')">
          <div v-for="index in 4" :key="index" style="height: 11.2rem;"
          class="mx-0 my-3 py-2 match dropShadow bg-medium animate-flicker"
          no-gutters align-v="center" align-h="center"
          :class="darkMode ? 'text-white':''">
          </div>
        </div>
        <div v-for="(match, index) in summoner.matchInfo" :key="index"
        class="mx-0 my-3 py-2 match dropShadow" no-gutters align-v="center" align-h="center"
        :class="getWinLossClass(match.stats.win) + matchClass">
          <div class="indicator d-flex m-auto w-25 h-75 rounded-lg">
          </div>
          <div>
            <div>{{ winLoss(match.stats.win) + ': '}}</div>
            <div class="small">{{ match.gameInfo.queue }}</div>
            <br>
            <a>{{ match.matchDuration }}</a>
            <br>
            <span class="sortIcon" @click='sortByDate(summoner)'>
                <b-icon :icon="dateSortIcon"></b-icon>
                {{ match.matchDate }}
            </span>
          </div>
          <div class="d-flex justify-content-center m-auto">
              <div class="d-flex justify-content-center m-auto">
                <router-link :to="{ name: 'Home',
                params: { champName: match.championInfo.champName.toLowerCase() } }">
                  <img :src="match.championInfo.champImgPath" class="mx-2 dropShadow"
                  :alt="match.championInfo.champName" height="84px" width="84px"
                  v-b-tooltip.hover = "{ variant: 'secondary' }"
                  :title="match.championInfo.champName">
                </router-link>
              </div>
              <div class="d-flex flex-column justify-content-center">
                  <img class="dropShadow m-2" :src="match.spells.spell1.imgPath"
                  :alt="match.spells.spell1.name" height="32px" width="32px">
                  <img class="dropShadow m-2" :src="match.spells.spell2.imgPath"
                  :alt="match.spells.spell2.name" height="32px" width="32px">
              </div>
              <div class="d-flex flex-column justify-content-center">
                  <img class="iconShadow mt-1 mb-2"
                  :src="match.runes.primaryBranch.keystone.imgPath"
                  :alt="match.runes.primaryBranch.keystone.name" height="40px" width="40px">
                  <img class="iconShadow m-auto"
                  :src="match.runes.secondaryBranch.imgPath"
                  :alt="match.runes.secondaryBranch.name" height="24px" width="24px">
              </div>
          </div>
          <div class="m-auto">
            <div class="d-flex flex-column justify-content-center">
              <div class="small">
                Int Score:
              </div>
              <div class="sortIcon" @click='sortByInt(summoner)'>
                <b-icon :icon="intSortIcon"></b-icon>
                {{ match.stats.intScore + '%' }}
              </div>
              <br>
              <div>
                {{match.stats.kills + ' / ' + match.stats.deaths + ' / ' + match.stats.assists}}
              </div>
              <div class="d-flex justify-content-around mx-2">
                <div class="text-left mr-2">
                  {{ match.stats.kda }}
                  <span class="smaller">{{ ' KDA' }}</span>
                </div>
                <div class="text-right ml-2">
                  {{ match.stats.creepScore }}
                  <span class="smaller">{{ ' CS' }}</span>
                </div>
              </div>
            </div>
          </div>
          <div class="d-flex justify-content-center m-auto">
            <div class="d-flex flex-column justify-content-center">
              <div class="d-flex justify-content-start">
                <div v-for="(item, index) in match.items.itemsList.slice(0,3)"
                :key="index" class="m-2">
                  <div v-if="item !== '0'">
                    <img class="dropShadow" :src="item.imgPath" :alt="item.name"
                    v-b-tooltip.hover = "{ variant: 'secondary' }" :title="item.name">
                  </div>
                  <div v-else style="height: 40px; width: 40px; border-radius: 20%; opacity: 50%;"
                  class="dropShadow" :class="darkMode ? 'bg-dark' : 'bg-medium'">
                  </div>
                </div>
                <div class="trinket m-2 mt-3">
                  <img class="dropShadow" :src="match.items.trinket.imgPath"
                  :alt="match.items.trinket.name"
                  v-b-tooltip.hover = "{ variant: 'secondary' }"
                  :title="match.items.trinket.name">
                </div>
              </div>
              <div class="d-flex justify-content-start">
                <div v-for="(item, index) in match.items.itemsList.slice(3)"
                :key="index" class="m-2">
                  <div v-if="item !== '0'">
                    <img class="dropShadow" :src="item.imgPath" :alt="item.name"
                    v-b-tooltip.hover = "{ variant: 'secondary' }" :title="item.name">
                  </div>
                  <div v-else style="height: 40px; width: 40px; border-radius: 20%; opacity: 50%;"
                  class="dropShadow" :class="darkMode ? 'bg-dark' : 'bg-medium'">
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="text-left m-auto">
            <div class="my-1" v-for="(player, index) in match.teamInfo.blue" :key="index">
              <router-link :to="{ name: 'Home',
              params: { champName: player.champName.toLowerCase() } }">
                <img class="smallChampIcon"
                :src="player.champImgPath" width="20px" height="auto"
                :alt="player.champName">
              </router-link>
              <a v-if="player.participantId === match.teamInfo.blueTeamTankIndex &&
              player.participantId === match.teamInfo.blueTeamDPSIndex"
              v-b-tooltip.hover.left = "{ variant: 'secondary' }" title="Carried">
                <button type="button" @click=addTeammate(player.summonerName)
                  class="btn btn-sm teammateBtn btn-carry"
                  :class="{ 'btn-darkCarry text-white': darkMode }">
                  {{ player.summonerName }}
                </button>
              </a>
              <a v-else-if="player.participantId === match.teamInfo.blueTeamDPSIndex"
              v-b-tooltip.hover.left = "{ variant: 'secondary' }" title="Team dmg">
                <button type="button" @click=addTeammate(player.summonerName)
                  class="btn btn-sm teammateBtn btn-damage"
                  :class="{ 'btn-darkDamage text-white': darkMode }">
                  {{ player.summonerName }}
                </button>
              </a>
              <a v-else-if="player.participantId === match.teamInfo.blueTeamTankIndex "
              v-b-tooltip.hover.left = "{ variant: 'secondary' }" title="Team tank">
                <button type="button" @click=addTeammate(player.summonerName)
                  variant="tank" class="btn btn-sm teammateBtn btn-tank"
                  :class="{ 'btn-darkTank text-white': darkMode }">
                  {{ player.summonerName }}
                </button>
              </a>
              <a v-else>
                <button type="button" @click=addTeammate(player.summonerName)
                  class="btn btn-sm teammateBtn btn-lightTeam"
                  :class="{ 'btn-darkTeam text-white': darkMode }">
                  {{ player.summonerName }}
                </button>
              </a>
            </div>
          </div>
          <div class="text-right pr-3">
            <div class="my-1" v-for="(player, index) in match.teamInfo.red" :key="index">
              <router-link :to="{ name: 'Home',
              params: { champName: player.champName.toLowerCase() } }">
                <img class="smallChampIcon"
                :src="player.champImgPath" width="20px" height="auto"
                :alt="player.champName">
              </router-link>
              <a v-if="player.participantId === match.teamInfo.redTeamTankIndex &&
              player.participantId === match.teamInfo.redTeamDPSIndex"
              v-b-tooltip.hover = "{ variant: 'secondary', placement: 'right' }" title="Carried">
                <button type="button" @click=addTeammate(player.summonerName)
                  class="btn btn-sm teammateBtn btn-carry"
                  :class="{ 'btn-darkCarry text-white': darkMode }">
                  {{ player.summonerName }}
                </button>
              </a>
              <a v-else-if="player.participantId === match.teamInfo.redTeamDPSIndex"
              v-b-tooltip.hover = "{ variant: 'secondary', placement: 'right'}" title="Team dmg">
                <button type="button" @click=addTeammate(player.summonerName)
                  class="btn btn-sm teammateBtn btn-damage"
                  :class="{ 'btn-darkDamage text-white': darkMode }">
                  {{ player.summonerName }}
                </button>
              </a>
              <a v-else-if="player.participantId === match.teamInfo.redTeamTankIndex "
              v-b-tooltip.hover = "{ variant: 'secondary', placement: 'right' }" title="Team tank">
                <button type="button" @click=addTeammate(player.summonerName)
                  variant="tank" class="btn btn-sm teammateBtn btn-tank"
                  :class="{ 'btn-darkTank text-white': darkMode }">
                  {{ player.summonerName }}
                </button>
              </a>
              <a v-else>
                <button type="button" @click=addTeammate(player.summonerName)
                  class="btn btn-sm teammateBtn btn-lightTeam"
                  :class="{ 'btn-darkTeam text-white': darkMode }">
                  {{ player.summonerName }}
                </button>
              </a>
            </div>
          </div>
        </div>
        <div class="mx-3 mt-4 mb-2">
          <button type="button" class="btn btn-secondary btn-block"
          @click="getMoreMatches(summoner)">
              Load more
              <b-spinner small v-if="showRefresh" class="align-middle"></b-spinner>
          </button>
        </div>
      </div>
      <div v-if="summoners.length === 0" class="mx-3 mt-4 mb-2 text-left" style="height:48.5rem;
      white-space: pre-wrap;
      ">
        <h1>No active summoners, click the plus icon to add one</h1>
      </div>
    </div>
    <b-modal ref="addSummonerModal" id="addSummonerModal"
      title="Add a new summoner" hide-footer :header-bg-variant="getVariant"
      :header-text-variant="getInverseVariant" :body-bg-variant="getVariant"
      :body-text-variant="getInverseVariant" @shown="focusInput()">
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group ref="form-name-group"
          label="Summoner:" label-for="addSummoner">
            <b-form-input ref="addSummoner"
              type="text" v-model="addSummonerForm.name" required
              autofocus placeholder="Enter summoner name">
            </b-form-input>
          </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
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
      summoners: [],
      addSummonerForm: {
        name: '',
      },
      showRefresh: false,
      editForm: {
        name: '',
      },
      activeItem: '',
      intSortIcon: 'chevron-expand',
      dateSortIcon: 'chevron-expand',
      intSortCount: 0,
      dateSortCount: 0,
    };
  },
  methods: {
    focusInput() {
      this.$refs.addSummoner.focus();
    },
    addTeammate(name) {
      const found = this.checkForSummonerByName(name);
      if (!found) {
        const payload = {
          name,
          code: 'goTabSummoner',
        };
        this.addSummoner(payload);
      } else {
        this.setActiveTab(name);
      }
    },
    setSortIcons(sortCount, type) {
      if (type === 'intScore') {
        if (sortCount % 2 === 0) {
          this.intSortIcon = 'chevron-down';
        } else {
          this.intSortIcon = 'chevron-up';
        }
        this.dateSortIcon = 'chevron-expand';
      } else if (type === 'date') {
        if (sortCount % 2 === 0) {
          this.dateSortIcon = 'chevron-down';
        } else {
          this.dateSortIcon = 'chevron-up';
        }
        this.intSortIcon = 'chevron-expand';
      }
    },
    sortArrays(itemArray, sortCount) {
      const tempArray = itemArray;
      if (sortCount % 2 === 0) {
        for (let i = 1; i < tempArray.length; i += 1) {
          for (let j = 0; j < i; j += 1) {
            if (itemArray[i].stats.intScore > itemArray[j].stats.intScore) {
              const x = itemArray[i];
              tempArray[i] = itemArray[j];
              tempArray[j] = x;
            }
          }
        }
      } else {
        for (let i = 1; i < tempArray.length; i += 1) {
          for (let j = 0; j < i; j += 1) {
            if (itemArray[i].stats.intScore < itemArray[j].stats.intScore) {
              const x = itemArray[i];
              tempArray[i] = itemArray[j];
              tempArray[j] = x;
            }
          }
        }
      }
      return tempArray;
    },
    sortByInt(summoner) {
      let index = '';
      // search for location of this summoner
      for (let i = 0; i < this.summoners.length; i += 1) {
        if (this.summoners[i].id === summoner.id) {
          index = i;
        }
      }
      const sortedSummoner = summoner;
      const sortedMatches = this.sortArrays(summoner.matchInfo, this.intSortCount);
      sortedSummoner.matchInfo = sortedMatches;
      this.$set(this.summoners, index, sortedSummoner);
      this.intSortCount += 1;
      this.setSortIcons(this.intSortCount, 'intScore');
    },
    sortByDate(summoner) {
      let index = '';
      // search for location of this summoner
      for (let i = 0; i < this.summoners.length; i += 1) {
        if (this.summoners[i].id === summoner.id) {
          index = i;
        }
      }
      const sortedDates = summoner.matchInfo;
      if (this.dateSortCount % 2 === 0) {
        for (let i = 1; i < sortedDates.length; i += 1) {
          for (let j = 0; j < i; j += 1) {
            if (sortedDates[i].matchDate > sortedDates[j].matchDate) {
              const x = sortedDates[i];
              sortedDates[i] = sortedDates[j];
              sortedDates[j] = x;
            }
          }
        }
      } else {
        for (let i = 1; i < sortedDates.length; i += 1) {
          for (let j = 0; j < i; j += 1) {
            if (sortedDates[i].matchDate < sortedDates[j].matchDate) {
              const x = sortedDates[i];
              sortedDates[i] = sortedDates[j];
              sortedDates[j] = x;
            }
          }
        }
      }
      const sortedSummoner = summoner;
      sortedSummoner.matchInfo = sortedDates;
      this.$set(this.summoners, index, sortedSummoner);
      this.dateSortCount += 1;
      this.setSortIcons(this.dateSortCount, 'date');
    },
    isActiveTab(menuItem) {
      return this.activeItem === menuItem;
    },
    setActiveTab(menuItem) {
      this.activeItem = menuItem;
    },
    winLoss(game) {
      if (game) {
        return 'Win';
      }
      return 'Loss';
    },
    getWinLossClass(game) {
      if (game) {
        if (this.darkMode) {
          return 'winDark';
        }
        return 'win';
      }
      if (this.darkMode) {
        return 'lossDark';
      }
      return 'loss';
    },
    getSummoners(run = 'goTab0') {
      const path = `${localhost}/summoners`;
      if (run === 'goTabSummoner') {
        axios.get(path)
          .then((res) => {
            this.summoners = res.data.summoners;
            const len = this.summoners.length;
            if (len > 0) {
              this.setActiveTab(this.summoners[len - 1].name);
            }
          })
          .catch((error) => {
            console.error(error);
          });
      } else {
        axios.get(path)
          .then((res) => {
            this.summoners = res.data.summoners;
            const len = this.summoners.length;
            if (len > 0) {
              this.setActiveTab(this.summoners[0].name);
            }
          })
          .catch((error) => {
            console.error(error);
          });
      }
    },
    refreshSummoners() {
      const path = `${localhost}/refresh`;
      this.showRefresh = true;
      axios.put(path)
        .then((res) => {
          console.log(res);
          this.summoners = res.data.summoners;
          this.showRefresh = false;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    addSummoner(payload) {
      const path = `${localhost}/summoners`;
      this.showRefresh = true;
      this.summoners.push({ name: payload.name });
      this.setActiveTab(payload.name);
      axios.put(path, payload)
        .then((res) => {
          const index = this.summoners.length - 1;
          this.$set(this.summoners, index, res.data.summoners);
          this.showRefresh = false;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    initForm() {
      this.addSummonerForm.name = '';
      this.editForm.name = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addSummonerModal.hide();
      const { name } = this.addSummonerForm;
      const found = this.checkForSummonerByName(name);
      if (!found) {
        const payload = {
          name,
          code: 'goTabSummoner',
        };
        this.addSummoner(payload);
      } else {
        this.setActiveTab(name);
      }
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addSummonerModal.hide();
      this.initForm();
    },
    removeSummoner(summonerID, name) {
      const path = `${localhost}/summoners/${summonerID}`;
      this.showRefresh = true;
      axios.delete(path)
        .then(() => {
          this.summoners = this.summoners.filter((summoner) => summoner.id !== summonerID);
          const summonerCount = this.summoners.length;
          if (summonerCount > 0) {
            if (this.isActiveTab(name)) {
              this.setActiveTab(this.summoners[summonerCount - 1].name);
            }
          }
          this.showRefresh = false;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    getMoreMatches(summoner) {
      const payload = {
        id: summoner.id,
        startIndex: summoner.startIndex + 10,
        endIndex: summoner.endIndex + 10,
      };
      const path = `${localhost}/summoners/${summoner.id}`;
      this.showRefresh = true;
      axios.put(path, payload)
        .then((res) => {
          const index = this.getSummonerIndexById(payload.id);
          this.$set(this.summoners, index, res.data[payload.id]);
          this.showRefresh = false;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    checkForSummonerByName(name) {
      let exists = false;
      for (let i = 0; i < this.summoners.length; i += 1) {
        if (this.summoners[i].name === name) { exists = true; }
      }
      return exists;
    },
    getSummonerIndexById(id) {
      for (let i = 0; i < this.summoners.length; i += 1) {
        if (this.summoners[i].id === id) {
          return i;
        }
      }
      return 0;
    },
    /* checkForSummonerByID(id) {
      let exists = false;
      for (let i = 0; i < this.summoners.length; i += 1) {
        if (this.summoners[i].id === id) { exists = true; }
      }
      return exists;
    },
    getNameByID(id) {
      for (let i = 0; i < this.summoners.length; i += 1) {
        if (this.summoners[i].id === id) {
          return this.summoners[i].name;
        }
      }
      return '';
    }, */
  },
  computed: {
    matchClass() {
      let classList = '';
      if (this.darkMode) {
        classList += ' text-white';
      }
      if (this.showRefresh) {
        classList += ' animate-flicker';
      }
      return classList;
    },
    getTabVariant() {
      if (this.darkMode === true) {
        return 'light';
      }
      return 'light';
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
    currentRouteName() {
      return this.$route.name;
    },
    darkMode() {
      return this.$store.state.darkMode;
    }, /*
    cleanSummoners() {
      // eslint-disable-next-line prefer-destructuring
      const summoners = [];
      // console.log(this.summoners);
      for (let i = 0; i < summoners.length; i += 1) {
        // console.log(this.summoners[i].id);
        if (summoners.id !== undefined) {
          console.log(summoners[i]);
          console.log(summoners[i].id);
          summoners.push(i);
        }
      }
      console.log(summoners);
      return this.summoners;
    }, */
  },
  created() {
    this.getSummoners('goTab0');
  },
};
</script>
