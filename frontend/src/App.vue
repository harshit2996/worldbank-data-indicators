<template>
  <v-app>
    <v-app-bar app color="white" flat>
      <v-container fill-height>
        <img
          src="./assets/Logo-Emptor.svg"
          height="100%"
          class="align-self-center"
          contain
          alt=""
        />
      </v-container>
      <v-spacer></v-spacer>
      <v-toolbar-items>
        <v-col align-self="center">
          <v-btn
            v-if="$vuetify.theme.dark"
            color="deep-orange"
            @click="$vuetify.theme.dark = !$vuetify.theme.dark"
            icon
            ><v-icon>mdi-white-balance-sunny</v-icon></v-btn
          >
          <v-btn
            v-if="!$vuetify.theme.dark"
            color="blue"
            @click="$vuetify.theme.dark = !$vuetify.theme.dark"
            icon
            ><v-icon>mdi-moon-waxing-crescent</v-icon></v-btn
          >
        </v-col>
      </v-toolbar-items>
    </v-app-bar>

    <v-main>
      <v-container fill-height justify-center class="flex-column">
        <v-col class="shrink">
          <v-col class="d-flex shrink py-0 justify-space-between">
            <Indicators :currentIndicator.sync="currentItem"></Indicators>
          </v-col>
        </v-col>
        <v-col class="flex-1">
          <v-container fill-height justify-center>
            <v-data-table
              class="col-12 pa-0 elevation-2 dt"
              :headers="headers"
              :items="data"
              :search="search"
              fixed-header
              :hide-default-header="currentItem.Indicators === 'Indicators'"
              @click:row="onRowSelect"
            >
              <template v-slot:top>
                <v-toolbar
                  flat
                  rounded
                  color="pink lighten-1"
                  class="justify-space-between align-items-center"
                >
                  <v-col class="justify-center">
                    <v-toolbar-title class="white--text">{{
                      title
                    }}</v-toolbar-title>
                  </v-col>

                  <v-row class="justify-center">
                    <v-col class="flex-col flex-grow-1">
                      <v-select
                        v-if="title !== 'Indicators'"
                        v-model="selectedCols"
                        :items="columns"
                        :label="label"
                        multiple
                        @input="updateHeaders"
                        hide-details
                        color="yellow"
                        outlined
                        :menu-props="{ offsetY: true }"
                      >
                        <template
                          v-slot:selection="{ item, index }"
                          class="d-flex flex-shrink-1"
                        >
                          <v-chip
                            v-if="index < 5"
                            close
                            @click:close="removeCol(index)"
                          >
                            <span>{{ item }}</span>
                          </v-chip>
                          <span v-if="index === 5" class="yellow--text caption">
                            (+{{ selectedCols.length - 5 }} others)
                          </span>
                        </template>
                      </v-select>
                    </v-col>
                  </v-row>

                  <v-col v-if="title !== 'Indicators'" class="px-0 text-end">
                    <v-btn @click="reset"
                      ><v-icon>mdi-keyboard-backspace</v-icon
                      ><span> Back</span></v-btn
                    >
                  </v-col>
                </v-toolbar>
                <v-container>
                  <v-text-field
                    v-model="search"
                    outlined
                    dense
                    append-icon="mdi-magnify"
                    label="Search"
                    hide-details
                  ></v-text-field>
                </v-container>
              </template>
            </v-data-table>
            <EditItem
              v-if="dialog"
              :dialog.sync="dialog"
              :rowData.sync="editData"
              :indicator.sync="currentItem.route" 
              :message.sync="errMsg"
            ></EditItem>
            <ErrorComponent :trigger.sync="snackbar" :message.sync="errMsg"></ErrorComponent>
          </v-container>
        </v-col>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import Indicators from "./components/indicators";
import EditItem from "./components/edit";
import ErrorComponent from './components/errormessage'
import axios from "axios";

export default {
  name: "App",

  components: {
    Indicators,
    EditItem,
    ErrorComponent
  },

  data: () => ({
    data: [],
    editData: [],
    headers: [],
    columns: [],
    indicators: [],
    label: "",
    search: "",
    selectedCols: [],
    fixedHeaders: [],
    title: "",
    dialog: false,
    currentItem: [],
    errMsg:"",
    snackbar:false
  }),

  mounted() {
    this.reset();
  },

  watch: {
    currentItem(v) {
      this.onRowSelect(v);
    },

    errMsg(){
      this.snackbar=true
    }

  },

  methods: {
    onRowSelect(item) {
      if (item.Indicators) {
        if (item.Indicators !== "Indicators") {
          this.currentItem = item;
          this.rowSelect(item);
        }
      } else {
        this.editRow(item);
      }
    },

    rowSelect(item) {
      this.selectedCols = [];
      axios
        .get("http://localhost:8000/display_data/" + item.route)
        .then((res) => {
          let headerFields = Object.keys(res.data[0]);
          let temp = [];
          let strFields = [];

          headerFields = headerFields.filter((element) => {
            if (isNaN(element)) {
              strFields.push(element);
            } else {
              return element;
            }
          });
          this.columns = headerFields;
          strFields.forEach((key, index) => {
            temp.push({
              text: key,
              value: key,
              class: "red lighten-2 divider title",
              width: "200px",
              divider: true,
              cellClass: index < 5 ? "custom" : "",
            });
          });
          this.fixedheaders = temp;
          this.headers = temp;
          this.data = res.data;
          this.label = "Select Years";
          this.title = item.Indicators;
        })
        .catch((err) => {
          console.log(err.response.data)
          this.errMsg = err.response.data.message
        });
    },

    editRow(item) {
      this.editData = item;
      this.dialog = true;
    },

    updateHeaders() {
      let temp = [];
      this.selectedCols.sort();
      this.selectedCols.forEach((key, index) => {
        temp.push({
          text: key,
          value: key,
          class: "red lighten-2 divider title",
          width: "200px",
          divider: true,
          cellClass: index < 5 ? "custom" : "",
          isSelectable: false,
        });
      });
      this.headers = this.fixedheaders.concat(temp);
      this.label = "Select Years";
    },

    removeCol(index) {
      this.selectedCols.splice(index, 1);
      this.updateHeaders();
    },

    reset() {
      this.currentItem = { Indicators: "Indicators" };
      axios
        .get("http://localhost:8000/display_data/")
        .then((res) => {
          this.data = res.data;
          this.indicators = res.data;
          let headerFields = Object.keys(res.data[0]);
          this.columns = headerFields.Indicators;
          let temp = [];
          temp.push({
            text: headerFields[0],
            value: headerFields[0],
            class: "red lighten-2 divider title",
            width: "200px",
          });
          this.headers = temp;
          this.title = headerFields[0];
        })
        .catch((err) => {
          console.log(err.response.data)
          this.errMsg = err.response.data.message
          this.snackbar = true
        });
    },
  },
};
</script>

<style lang="scss">
.dt {
  tbody {
    tr:hover {
      cursor: pointer;
    }
  }
}
</style>
