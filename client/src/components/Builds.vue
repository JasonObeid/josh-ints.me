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
                @input="search_text()"
                v-model="text"
                type="text"
                placeholder="Search by Name"
              ></b-form-input>
               <div class="container-fluid">
                <div class="row">
                  <div class="col-md-6 pad-15-ver"
                  v-for="champion in all_champions" :key="champion.name">
                    <div class="card-inner">
                      <img class="card-img" :src="champion.imageURL">
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

const localhost = '/api';
// const localhost = 'http://localhost:5000';

export default {
  data() {
    return {
      allChampions: [],
      champions: [],
      top: [],
      jungle: [],
      mid: [],
      bot: [],
      support: [],
      intSortCount: 0,
      dateSortCount: 0,
      searchText: '',
    };
  },
  methods: {
    search_text() {
      this.champions = this.allChampions.filter((champion) => {
        if (champion.name.toLowerCase()
          .indexOf(this.searchText.toLowerCase()) !== '-1') {
          return champion;
        }
        return null;
      });
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
  },
};
</script>
