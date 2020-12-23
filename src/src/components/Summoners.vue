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
}

.champName
{
  vertical-align: top;
}
.trinket
{
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
  background-color: #ffc4c9;
}
.btn-damage:hover
{
  background-color: #ea737d;
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
  background-color: #9c4c53;
}
.btn-darkDamage:hover
{
  background-color: #bb434d;
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
  background-color: #d3d3d3;
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
  background-color: #c2f0c2a8;
}
.loss
{
  background-color: #ff9999a8;
}

.winDark
{
  background-color: #2f5d2fab;
}
.lossDark
{
  background-color: #bb3333ab;
}

.nav-tabsDark {
  border-bottom: 1px solid #545658;
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
              0 8px 16px rgba(0,0,0,0.11)
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

.keystone {
  border-radius: 50%;
}

.runeBranch {
  border-radius: 50%;
}

.btn-sm {
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
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
.summonerTable {
  background-color: #f9f8f7;
}
</style>

<template>
<transition name="fade" mode="out-in">
  <div class="flex-container">
     <ul class="nav nav-tabs pl-2" width='100%' ref="summonerTab"
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
          <b-button size='sm' @click="onDeleteSummoner(summoner)"
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
    <transition-group tag="div">
    <div class="tab-content" ref="myTabContent" key="tab">
      <div v-for="(summoner, index) in summoners" :key="index"
      class="tab-pane fade" :ref=(summoner.name)
      :class="{ 'active show': isActiveTab(summoner.name) }">
        <table class="table table-borderless table-striped summonerTable"
        :class="{ 'table-dark text-white bg-dark': darkMode }">
          <thead>
            <tr align="center">
              <th>Champion</th>
              <th>Runes</th>
              <th>Items</th>
              <th>W/L</th>
              <th>Score</th>
              <th>KDA</th>
              <th>CS</th>
              <th class="sort" @click='sortByInt(summoner)'>
                Int Score
                <b-icon :icon="intSortIcon"></b-icon>
              </th>
              <th>Blue Team</th>
              <th>Red Team</th>
              <th class="sort" @click='sortByDate(summoner)'>
                Date
                <b-icon :icon="dateSortIcon"></b-icon>
              </th>
            </tr>
          </thead>
          <tbody is="transition-group">
              <tr v-for="(match, index) in summoner.matchInfo" :key="index">
                <td><router-link
                :to="{ name: 'Home',
                params: { champName: match.championInfo.champName.toLowerCase() } }">
                  <span class="champName" :class="{'text-white' : darkMode}">
                    {{ match.championInfo.champName }}
                  </span>
                  <br>
                  <img class="champIcon" :src="match.championInfo.champImgPath"
                  :alt="match.championInfo.champName"></router-link>
                </td>
                <td>
                  <tr>
                    <td>
                      <img class="dropShadow" :src="match.spells.spell1.imgPath"
                      :alt="match.spells.spell1.name">
                    </td>
                    <td>
                      <img class="dropShadow" :src="match.spells.spell2.imgPath"
                      :alt="match.spells.spell2.name">
                    </td>
                  </tr>
                  <tr>
                    <td>
                      <img class="keystone dropShadow"
                      :src="match.runes.primaryBranch.keystone.imgPath"
                      :alt="match.runes.primaryBranch.keystone.name" height="40px" width="auto">
                    </td>
                    <td>
                      <img class="runeBranch dropShadow"
                      :src="match.runes.secondaryBranch.imgPath"
                      :alt="match.runes.secondaryBranch.name" height="25px" width="auto">
                    </td>
                  </tr>
                </td>
                <td>
                  <div v-if="match.items.count < 3">
                    <tr>
                      <td v-for="(item, index) in match.items.itemsList
                      .slice(0,match.items.count)" :key="index">
                        <div v-if="item !== '0'">
                          <img class="dropShadow" :src="item.imgPath" :alt="item.name"
                          v-b-tooltip.hover = "{ variant: 'secondary' }" :title="item.name">
                        </div>
                        <div v-else>
                          <svg width="40" height="40"><rect width="40"
                          height="40" style="opacity: 0"></rect></svg>
                        </div>
                      </td>
                      <td rowspan="2" class="trinket">
                        <img class="dropShadow" :src="match.items.trinket.imgPath"
                        :alt="match.items.trinket.name"
                        v-b-tooltip.hover = "{ variant: 'secondary' }"
                        :title="match.items.trinket.name">
                      </td>
                    </tr>
                    <tr>
                    </tr>
                  </div>
                  <div v-else>
                    <tr>
                      <td v-for="(item, index) in match.items.itemsList.slice(0,3)"
                      :key="index">
                        <div v-if="item !== '0'">
                          <img class="dropShadow" :src="item.imgPath" :alt="item.name"
                          v-b-tooltip.hover = "{ variant: 'secondary' }" :title="item.name">
                        </div>
                        <div v-else>
                          <svg width="40" height="40"><rect width="40"
                          height="40" style="opacity: 0"></rect></svg>
                        </div>
                      </td>
                      <td rowspan="2" class="trinket">
                        <img class="dropShadow" :src="match.items.trinket.imgPath"
                        :alt="match.items.trinket.name"
                        v-b-tooltip.hover = "{ variant: 'secondary' }"
                        :title="match.items.trinket.name">
                      </td>
                    </tr>
                    <tr>
                      <td v-for="(item, index) in match.items.itemsList.slice(3)"
                      :key="index">
                        <img class="dropShadow" :src="item.imgPath" :alt="item.name"
                        v-b-tooltip.hover = "{ variant: 'secondary' }" :title="item.name">
                      </td>
                    </tr>
                  </div>
                </td>
                <td v-if="match.stats.win == true" class="win"
                :class="{ 'winDark': darkMode }">
                  <p>{{ winLoss(match.stats.win) + ': ' }}</p>
                  <a>{{ match.gameInfo.queue}}</a>
                </td>
                <td v-else class="loss"
                :class="{ 'lossDark': darkMode }">
                  <p>{{ winLoss(match.stats.win) + ': ' }}</p>
                  <a>{{ match.gameInfo.queue}}</a>
                </td>
                <td class="trinket">
                  {{ match.stats.kills + '/' + match.stats.deaths + '/' + match.stats.assists }}
                </td>
                <td class="trinket">{{ match.stats.kda }}</td>
                <td class="trinket">{{ match.stats.creepScore }}</td>
                <td class="trinket">{{ match.stats.intScore + '%' }}</td>
                <td class='blueTeam'>
                  <div class="my-1" v-for="(player, index)
                  in match.teamInfo.blue" :key="index">
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
                </td>
                <td class='redTeam'>
                  <div class="my-1" v-for="(player, index) in match.teamInfo.red" :key="index">
                    <a v-if="player.participantId === match.teamInfo.redTeamTankIndex &&
                    player.participantId === match.teamInfo.redTeamDPSIndex"
                    v-b-tooltip.right.hover = "{ variant: 'secondary' }" title="Carried">
                      <button type="button" @click=addTeammate(player.summonerName)
                        class="btn btn-sm teammateBtn btn-carry"
                        :class="{ 'btn-darkCarry text-white': darkMode }">
                        {{ player.summonerName }}
                      </button>
                    </a>
                    <a v-else-if="player.participantId === match.teamInfo.redTeamDPSIndex"
                    v-b-tooltip.right.hover = "{ variant: 'secondary' }" title="Team dmg">
                      <button type="button" @click=addTeammate(player.summonerName)
                        class="btn btn-sm teammateBtn btn-damage"
                        :class="{ 'btn-darkDamage text-white': darkMode }">
                        {{ player.summonerName }}
                      </button>
                    </a>
                    <a v-else-if="player.participantId === match.teamInfo.redTeamTankIndex "
                    v-b-tooltip.right.hover = "{ variant: 'secondary' }" title="Team tank">
                      <button type="button" @click=addTeammate(player.summonerName)
                      class="teammateBtn btn btn-sm teammateBtn btn-tank"
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
                    <router-link :to="{ name: 'Home',
                    params: { champName: player.champName.toLowerCase() } }">
                      <img class="smallChampIcon"
                      :src="player.champImgPath" width="20px" height="auto"
                      :alt="player.champName">
                    </router-link>
                  </div>
                </td>
                <td align="middle">
                    <a>{{ match.matchDuration }}</a>
                    <br>
                    <a>{{ match.matchDate }}</a>
                </td>
              </tr>
              <tr v-if="summoners.length != 0">
                <td colspan="11">
                  <button type="button" class="btn btn-secondary btn-block"
                  @click="getMoreMatches(summoner)">
                      Load more
                      <b-spinner small v-if="showRefresh" class="align-middle"></b-spinner>
                  </button>
                </td>
              </tr>
          </tbody>
        </table>
      </div>
    </div>
    </transition-group>
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
      if (game === true) {
        return 'Win';
      }
      return 'Loss';
    },
    getSummoners(run = 'goTab0') {
      const path = `${localhost}/summoners`;
      if (run === 'goTabSummoner') {
        axios.get(path)
          .then((res) => {
            this.summoners = res.data.summoners;
            const len = this.summoners.length - 1;
            this.setActiveTab(this.summoners[len].name);
          })
          .catch((error) => {
            console.error(error);
          });
      } else {
        axios.get(path)
          .then((res) => {
            this.summoners = res.data.summoners;
            this.setActiveTab(this.summoners[0].name);
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
        })
        .catch((error) => {
          console.error(error);
        });
      this.showRefresh = false;
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
    removeSummoner(summonerID) {
      const path = `${localhost}/summoners/${summonerID}`;
      this.showRefresh = true;
      axios.delete(path)
        .then(() => {
          for (let i = 0; i < this.summoners.length; i += 1) {
            if (this.summoners[i].id === summonerID) {
              this.summoners.pop(i);
            }
          }
          this.showRefresh = false;
          const summonerCount = this.summoners.length - 1;
          this.setActiveTab(this.summoners[summonerCount].name);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    onDeleteSummoner(summoner) {
      this.removeSummoner(summoner.id);
    },
    getMoreMatches(summoner) {
      const payload = {
        id: summoner.id,
        startIndex: summoner.startIndex + 10,
        endIndex: summoner.endIndex + 10,
      };
      this.updateSummoner(payload, summoner.id);
    },
    checkForSummonerByName(name) {
      let exists = false;
      for (let i = 0; i < this.summoners.length; i += 1) {
        if (this.summoners[i].name === name) { exists = true; }
      }
      return exists;
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
