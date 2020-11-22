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
div.teams
{
  padding-top: 2%;
  padding-bottom: 2%;
}
.alert
{
  margin: .25rem 1.25rem;
}
.champName
{
  color: #212529;
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
.btn-damage
{
  background-color: #ffc4c9;
}
.btn-tank
{
  background-color: #e0f3ff;
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
  background-color: #c2f0c2ad;
}
.loss
{
  background-color: #ff9999a8;
}
.table td
{
  vertical-align: middle;
}
.summonerTab
{
  margin-left: 5%;
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
</style>

<template>
<transition name="fade" mode="out-in">
  <div class="flex-container">
    <div class="head">
      <a><alert :message=message v-if="showMessage"></alert></a>
    </div>
     <ul class="nav nav-tabs" width='90%' style="padding-left: 1%;">
      <li class="nav-item" v-for="(summoner, index) in summoners"
      :key="index" :title="summoner.name">
        <button class="nav-link" @click.prevent="setActiveTab(summoner.name)"
        :class="{ active: isActiveTab(summoner.name) }">
          <a>{{ summoner.name }} | </a>
          <a>{{ summoner.rank }}</a>
          <b-button size='sm' @click=onDeleteSummoner(summoner)
          variant="outline-danger" class="summonerTab">
            x
          </b-button>
        </button>
      </li>
      <li class="nav-item">
        <a class="nav-link">
          <b-button variant="outline-primary" size='sm' v-b-modal.summoner-modal>
            +
          </b-button>
        </a>
      </li>
      <li class="nav-item ml-auto">
        <button type="button" class="btn btn-warning btn-sm"
        id="refresh" @click='refreshSummoners()'>
          Refresh
          <b-spinner small v-if="showRefresh" class="align-middle"></b-spinner>
        </button>
      </li>
    </ul>
    <div class="tab-content py-3 flex-container" id="myTabContent">
      <div v-for="summoner in summoners" :key="summoner.id"
      class="tab-pane fade" :id=(summoner.name)
      :class="{ 'active show': isActiveTab(summoner.name) }">
        <table class="table table-borderless table-striped border" id="summonerTable">
          <tbody>
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
              <tr v-for="(match, index) in summoner.matchInfo" :key="index">
                <td><router-link
                :to="{ name: 'Home',
                params: { champName: match.championInfo.champName.toLowerCase() } }">
                  <a class="champName">{{ match.championInfo.champName }}</a>
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
                        <img class="dropShadow" :src="item.imgPath" :alt="item.name"
                        v-b-tooltip.hover = "{ variant: 'secondary' }" :title="item.name">
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
                        <img class="dropShadow" :src="item.imgPath" :alt="item.name"
                        v-b-tooltip.hover = "{ variant: 'secondary' }" :title="item.name">
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
                <td v-if="match.stats.win == true" class="win">
                  <p>{{ winLoss(match.stats.win) + ': ' }}</p>
                  <a>{{ match.gameInfo.queue}}</a>
                </td>
                <td v-else class="loss">
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
                  <div class="teams" v-for="(player, index) in match.teamInfo.blue" :key="index">
                    <router-link :to="{ name: 'Home',
                    params: { champName: player.champName.toLowerCase() } }">
                      <img class="smallChampIcon"
                      :src="player.champImgPath" width="20px" height="auto"
                      :alt="player.champName">
                    </router-link>
                    <a v-if="player.participantId === match.teamInfo.blueTeamTankIndex &&
                    player.participantId === match.teamInfo.blueTeamDPSIndex"
                    v-b-tooltip.hover.left = "{ variant: 'secondary' }" title="Carried">
                      <b-button size='sm' @click=addTeammate(player.summonerName)
                        variant="carry">
                        {{ player.summonerName }}
                      </b-button>
                    </a>
                    <a v-else-if="player.participantId === match.teamInfo.blueTeamDPSIndex"
                    v-b-tooltip.hover.left = "{ variant: 'secondary' }" title="Team dmg">
                      <b-button size='sm' @click=addTeammate(player.summonerName)
                        variant="damage">
                        {{ player.summonerName }}
                      </b-button>
                    </a>
                    <a v-else-if="player.participantId === match.teamInfo.blueTeamTankIndex "
                    v-b-tooltip.hover.left = "{ variant: 'secondary' }" title="Team tank">
                      <b-button size='sm' @click=addTeammate(player.summonerName)
                        variant="tank">
                        {{ player.summonerName }}
                      </b-button>
                    </a>
                    <a v-else>
                      <b-button size='sm' @click=addTeammate(player.summonerName)
                        variant="light">
                        {{ player.summonerName }}
                      </b-button>
                    </a>
                  </div>
                </td>
                <td class='redTeam'>
                  <div class="teams" v-for="(player, index) in match.teamInfo.red" :key="index">
                    <a v-if="player.participantId === match.teamInfo.redTeamTankIndex &&
                    player.participantId === match.teamInfo.redTeamDPSIndex"
                    v-b-tooltip.right.hover = "{ variant: 'secondary' }" title="Carried">
                      <b-button size='sm' @click=addTeammate(player.summonerName)
                        variant="carry">
                        {{ player.summonerName }}
                      </b-button>
                    </a>
                    <a v-else-if="player.participantId === match.teamInfo.redTeamDPSIndex"
                    v-b-tooltip.right.hover = "{ variant: 'secondary' }" title="Team dmg">
                      <b-button size='sm' @click=addTeammate(player.summonerName)
                        variant="damage">
                        {{ player.summonerName }}
                      </b-button>
                    </a>
                    <a v-else-if="player.participantId === match.teamInfo.redTeamTankIndex "
                    v-b-tooltip.right.hover = "{ variant: 'secondary' }" title="Team tank">
                      <b-button size='sm' @click=addTeammate(player.summonerName)
                        variant="tank">
                        {{ player.summonerName }}
                      </b-button>
                    </a>
                    <a v-else>
                      <b-button size='sm' @click=addTeammate(player.summonerName)
                        variant="light">
                        {{ player.summonerName }}
                      </b-button>
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
                  <button
                    type="button"
                    class="btn btn-info btn-block"
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
    <b-modal ref="addSummonerModal"
            id="summoner-modal"
            title="Add a new summoner"
            hide-footer
            @shown="focusInput()">
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-name-group"
                      label="Summoner:"
                      label-for="form-name-input">
            <b-form-input id="form-name-input"
                          ref="addSummoner"
                          type="text"
                          v-model="addSummonerForm.name"
                          required
                          autofocus
                          placeholder="Enter summoner name">
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
import Alert from './Alert.vue';

const localhost = '/api';
// const localhost = 'http://localhost:5000/api';
export default {
  data() {
    return {
      summoners: [],
      addSummonerForm: {
        name: '',
      },
      message: '',
      showMessage: false,
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
  components: {
    alert: Alert,
  },
  methods: {
    focusInput() {
      this.$refs.addSummoner.focus();
    },
    addTeammate(summonerID) {
      const payload = {
        name: summonerID,
        code: 'goTabSummoner',
      };
      this.addSummoner(payload);
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
            this.message = res.data.message;
            this.summoners = res.data.summoners;
            const len = this.summoners.length;
            this.setActiveTab(this.summoners[len - 1].name);
          })
          .catch((error) => {
            console.error(error);
          });
      } else {
        axios.get(path)
          .then((res) => {
            this.message = res.data.message;
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
      this.message = 'Fetching...';
      this.showRefresh = true;
      this.showMessage = true;
      axios.put(path)
        .then((res) => {
          console.log(res);
          this.message = res.data.message;
          this.summoners = res.data.summoners;
          this.setActiveTab(this.summoners[0].name);
        })
        .catch((error) => {
          console.error(error);
        });
      this.showRefresh = false;
    },
    addSummoner(payload) {
      const path = `${localhost}/summoners`;
      this.message = 'Fetching...';
      this.showRefresh = true;
      this.showMessage = true;
      this.summoners.push({ name: payload.name });
      this.setActiveTab(payload.name);
      axios.put(path, payload)
        .then((res) => {
          const len = this.summoners.length;
          this.summoners[len - 1] = res.data.summoners;
          this.showMessage = false;
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
      const found = this.checkForSummoner(name);
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
    editSummoner(summoner) {
      this.editForm = summoner;
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editSummonerModal.hide();
      this.initForm();
      this.getSummoners();
    },
    removeSummoner(summonerID) {
      const path = `${localhost}/summoners/${summonerID}`;
      this.showRefresh = true;
      axios.delete(path)
        .then(() => {
          this.message = 'Summoner removed!';
          this.showMessage = true;
          for (let i = 0; i < this.summoners.length; i += 1) {
            if (this.summoners[i].id === summonerID) {
              this.summoners.pop(i);
            }
          }
          this.showRefresh = false;
          this.showMessage = false;
          this.setActiveTab(this.summoners[0].name);
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
    checkForSummoner(name) {
      let exists = false;
      for (let i = 0; i < this.summoners.length; i += 1) {
        if (this.summoners[i].name === name) { exists = true; }
      }
      return exists;
    },
  },
  created() {
    this.getSummoners('goTab0');
  },
};
</script>
