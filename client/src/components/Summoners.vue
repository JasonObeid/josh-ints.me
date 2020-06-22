<style scoped>
img.champIcon {
  border-radius: 50%;
}
.flex-container
{
  vertical-align:middle;
  align-items:center;
  text-align:center;
  white-space: nowrap;
  padding: 1%;
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
</style>

<template>
  <div class="flex-container">
    <div class="head">
      <a><alert :message=message v-if="showMessage"></alert></a>
      <b-spinner small v-if="showRefresh" class="align-middle"></b-spinner>
    </div>
     <ul class="nav nav-tabs" width='90%'>
      <li class="nav-item" v-for="(summoner, index) in summoners"
      :key="index" :title="summoner.name">
        <button class="nav-link" @click.prevent="setActive(summoner.name)"
        :class="{ active: isActive(summoner.name) }">
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
        <button type="button" class="btn btn-warning btn-sm" id="refresh" @click='getSummoners()'>
          Refresh
        </button>
      </li>
    </ul>
    <div class="tab-content py-3 flex-container" id="myTabContent">
      <div v-for="summoner in summoners" :key="summoner.id"
      class="tab-pane fade" :class="{ 'active show': isActive(summoner.name) }" :id=(summoner.name)>
        <table class="table" id="summonerTable">
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
                <td>
                  <a class="champName">{{ match.championInfo.champName }}</a>
                  <br>
                  <img :src="match.championInfo.champImgPath"
                  :alt="match.championInfo.champName" class="champIcon">
                </td>
                <td>
                  <tr>
                    <td>
                      <img :src="match.spells.spell1.imgPath"
                      :alt="match.spells.spell1.name">
                    </td>
                    <td>
                      <img :src="match.spells.spell2.imgPath"
                      :alt="match.spells.spell2.name">
                    </td>
                  </tr>
                  <tr>
                    <td>
                      <img :src="match.runes.primaryBranch.keystone.imgPath"
                      :alt="match.runes.primaryBranch.keystone.name">
                    </td>
                    <td>
                      <img :src="match.runes.secondaryBranch.imgPath"
                      :alt="match.runes.secondaryBranch.name" height="25px" width="auto">
                    </td>
                  </tr>
                </td>
                <td>
                  <div v-if="match.items.count < 3">
                    <tr>
                      <td v-for="(item, index) in match.items.itemsList
                      .slice(0,match.items.count)" :key="index">
                        <img :src="item.imgPath" :alt="item.name">
                      </td>
                      <td rowspan="2" class="trinket">
                        <img :src="match.items.trinket.imgPath"
                        :alt="match.items.trinket.name">
                      </td>
                    </tr>
                    <tr>
                    </tr>
                  </div>
                  <div v-else>
                    <tr>
                      <td v-for="(item, index) in match.items.itemsList.slice(0,3)"
                      :key="index">
                        <img :src="item.imgPath" :alt="item.name">
                      </td>
                      <td rowspan="2" class="trinket">
                        <img :src="match.items.trinket.imgPath"
                        :alt="match.items.trinket.name">
                      </td>
                    </tr>
                    <tr>
                      <td v-for="(item, index) in match.items.itemsList.slice(3)"
                      :key="index">
                        <img :src="item.imgPath" :alt="item.name">
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
                    <img :src="player.champImgPath" width="20px" height="auto"
                    :alt="player.champName">
                    <a v-if="player.participantId === match.teamInfo.blueTeamTankIndex &&
                    player.participantId === match.teamInfo.blueTeamDPSIndex"
                    v-b-tooltip.hover noninteractive title="Carried">
                       <b-button size='sm' @click=addTeammate(player.summonerName)
                        variant="carry">
                         {{ player.summonerName }}
                       </b-button>
                    </a>
                    <a v-else-if="player.participantId === match.teamInfo.blueTeamDPSIndex"
                    v-b-tooltip.hover noninteractive title="Team damage btw">
                       <b-button size='sm' @click=addTeammate(player.summonerName)
                        variant="damage">
                         {{ player.summonerName }}
                       </b-button>
                    </a>
                    <a v-else-if="player.participantId === match.teamInfo.blueTeamTankIndex "
                    v-b-tooltip.hover noninteractive title="Team tank btw">
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
                    v-b-tooltip.hover noninteractive title="Carried">
                       <b-button size='sm' @click=addTeammate(player.summonerName)
                        variant="carry">
                         {{ player.summonerName }}
                       </b-button>
                    </a>
                    <a v-else-if="player.participantId === match.teamInfo.redTeamDPSIndex"
                     v-b-tooltip.hover noninteractive title="Team damage btw">
                       <b-button size='sm' @click=addTeammate(player.summonerName)
                        variant="damage">
                         {{ player.summonerName }}
                       </b-button>
                    </a>
                    <a v-else-if="player.participantId === match.teamInfo.redTeamTankIndex "
                     v-b-tooltip.hover noninteractive title="Team tank btw">
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
                    <img :src="player.champImgPath" width="20px" height="auto"
                    :alt="player.champName">
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
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

// const localhost = '/api';
const localhost = 'http://localhost:5000';

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
    isActive(menuItem) {
      return this.activeItem === menuItem;
    },
    setActive(menuItem) {
      this.activeItem = menuItem;
    },
    winLoss(game) {
      if (game === true) {
        return 'Win';
      }
      return 'Loss';
    },
    getSummoners(run = '1') {
      const path = `${localhost}/summoners`;
      // console.log(this.summoners[0]);
      if (run === 'goTab0') {
        axios.get(path)
          .then((res) => {
            this.message = res.data.message;
            this.summoners = res.data.summoners;
            this.setActive(this.summoners[0].name);
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });
      } else if (run === 'goTabSummoner') {
        axios.get(path)
          .then((res) => {
            this.message = res.data.message;
            this.summoners = res.data.summoners;
            const len = this.summoners.length;
            this.setActive(this.summoners[len - 1].name);
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });
      } else {
        axios.get(path)
          .then((res) => {
            console.log(res.data.summoners);
            console.log(res.data.message);
            this.message = res.data.message;
            this.summoners = res.data.summoners;
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });
      }
    },
    addSummoner(payload) {
      console.log(payload);
      const path = `${localhost}/summoners`;
      this.message = 'Fetching...';
      this.showRefresh = true;
      this.showMessage = true;
      axios.post(path, payload)
        .then(() => {
          console.log(payload);
          this.getSummoners(payload.code);
          this.showMessage = true;
          this.showRefresh = false;
          this.isActive(payload.name);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getSummoners();
        });
    },
    initForm() {
      this.addSummonerForm.name = '';
      this.editForm.name = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addSummonerModal.hide();
      const payload = {
        name: this.addSummonerForm.name,
        code: 'goTabSummoner',
      };
      this.addSummoner(payload);
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
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editSummonerModal.hide();
      const payload = {
        name: this.editForm.name,
      };
      this.updateSummoner(payload, this.editForm.id);
    },
    updateSummoner(payload, summonerID) {
      const path = `${localhost}/summoners/${summonerID}`;
      this.message = 'Fetching...';
      this.showRefresh = true;
      this.showMessage = true;
      axios.put(path, payload)
        .then(() => {
          this.getSummoners();
          this.message = 'Summoner updated!';
          this.showMessage = true;
          this.showRefresh = false;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getSummoners();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editSummonerModal.hide();
      this.initForm();
      this.getSummoners();
    },
    removeSummoner(summonerID) {
      const path = `${localhost}/summoners/${summonerID}`;
      axios.delete(path)
        .then(() => {
          this.getSummoners('goTab0');
          this.message = 'Summoner removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getSummoners();
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
  },
  created() {
    this.getSummoners('goTab0');
  },
};
</script>
