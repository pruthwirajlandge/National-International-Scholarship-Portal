<template>
  <v-card>
    <v-card-title>
      <span class="text-h5">Devices Connected in the Network</span>
    </v-card-title>
    <v-card-text>
      <v-container>
        <v-row>
          <v-col cols="12">
            <v-simple-table>
              <template v-slot:default>
                <thead>
                  <tr>
                    <th class="text-left">Device Type</th>
                    <th class="text-left">Device IP</th>
                    <th class="text-left">Device MAC</th>
                    <th class="text-left">User</th>
                    <th class="text-left">Current Device Status</th>
                    <th class="text-left">Uptime Since</th>
                    <th class="text-left">Last Access</th>
                    <th class="text-left">Os Type</th>
                    <th class="text-left">Network Traffic</th>
                    <th class="text-left">Access Control</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(item, index) in data" :key="item.id">
                    <td>{{ item.device_type }}</td>
                    <td>{{ item.device_ip }}</td>
                    <td>{{ item.device_mac }}</td>
                    <td>{{ item.user }}</td>
                    <td>
                      <div v-if="!item.has_access">
                        Not Connected
                      </div>
                      <div v-else>
                        Connected
                      </div>
                    </td>
                    <td>{{ item.uptime_since }}</td>
                    <td>{{ item.last_access }}</td>
                    <td>{{ item.os_type }}</td>
                    <td>
                      <v-btn icon small @click="explore_traffic=true"> <v-icon>mdi-open-in-new</v-icon> </v-btn>
                    </td>
                    <td v-if="!item.has_access">
                      <v-btn fab small class="green" @click="controlStatus(item.id)"> <v-icon>mdi-wifi</v-icon> </v-btn>
                    </td>
                    <td v-if="item.has_access">
                      <v-btn fab small class="red" @click="controlStatus(item.id)"> <v-icon>mdi-wifi-off</v-icon>
                      </v-btn>
                    </td>
                  </tr>
                </tbody>
              </template>
            </v-simple-table>
          </v-col>
        </v-row>

        <v-dialog v-model="explore_traffic" width="900">
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-simple-table>
                  <template v-slot:default>
                    <thead>
                      <tr>
                        <th class="text-left">Source IP</th>
                        <th class="text-left">Destination IP</th>
                        <th class="text-left">Protocol</th>
                        <th class="text-left">Domain</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="(item, index) in traffic" :key="item.id">
                        <td>{{ item.src_ip }}</td>
                        <td>{{ item.dst_ip }}</td>
                        <td>{{ item.protocol }}</td>
                        <td>{{ item.domain }}</td>
                      </tr>
                    </tbody>
                  </template>
                </v-simple-table>
              </v-col>
              <v-col cols="6">
                  <v-btn block @click="explore_traffic = false" color="primary"
                    class="text-capitalize font-600">Close</v-btn>
                </v-col>
            </v-row>
          </v-container>
        </v-dialog>
      </v-container>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="blue darken-1" text @click="$emit('closeDialog')">
        Close
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import axios from "axios";
import Vue from "vue";

export default {
  data: () => ({
    type: "",
    data: [],
    traffic: [],
    explore_traffic: false,
    error_message: null,
    overlay: false,
    token: Vue.$cookies.get("token"),
    user_name: Vue.$cookies.get("user_name"),
    base_url: process.env.VUE_APP_SERVER_URL,
  }),

  methods: {
    controlStatus(id) {
      console.log(id);
      this.overlay = true;
      axios({
        method: "PATCH",
        url: process.env.VUE_APP_SERVER_URL + "nac/" + id + "/",
        data: {},
        headers: {
          "Content-Type": "application/json; charset=UTF-8",
          Authorization: `token ${this.token}`,
        },
      })
        .then((res) => {
          this.data = res.data;
          console.log(this.data);
          this.overlay = false;
          window.location.reload();
        })
        .catch((error) => {
          this.overlay = false;
          console.log(error);
          if (error.response.status == 400) {
            this.error_response = error.response.data.msg;
          } else {
            this.error_response = error.message;
          }
          console.log(error);
        });
    },
    getDevices() {
      this.overlay = true;
      axios({
        method: "GET",
        url: process.env.VUE_APP_SERVER_URL + "nac/",
        data: {},
        headers: {
          "Content-Type": "application/json; charset=UTF-8",
          Authorization: `token ${this.token}`,
        },
      })
        .then((res) => {
          this.data = res.data;
          console.log(this.data);
          this.overlay = false;
        })
        .catch((error) => {
          this.overlay = false;
          console.log(error);
          if (error.response.status == 400) {
            this.error_response = error.response.data.msg;
          } else {
            this.error_response = error.message;
          }
          console.log(error);
        });
    },

    getTraffic() {
      this.overlay = true;
      axios({
        method: "GET",
        url: process.env.VUE_APP_SERVER_URL + "traffic/",
        data: {},
        headers: {
          "Content-Type": "application/json; charset=UTF-8",
          Authorization: `token ${this.token}`,
        },
      })
        .then((res) => {
          this.traffic = res.data;
          this.overlay = false;
        })
        .catch((error) => {
          this.overlay = false;
          console.log(error);
          if (error.response.status == 400) {
            this.error_response = error.response.data.msg;
          } else {
            this.error_response = error.message;
          }
          console.log(error);
        });
    },
  },

  mounted() {
    this.getDevices();
    this.getTraffic();
  },
};
</script>

<style lang="scss" scoped>
.v-toolbar {
  transition: 0.6s;
}

.pt-100 {
  padding-top: 100px;
}

.expand {
  height: 80px !important;
  padding-top: 10px;
}

.header-landing {
  background-image: url("../../assets/images/landing/landing-bg-2.svg");
  background-size: cover;
  margin-bottom: 100px;
}

.landing-button-wrapper {
  margin-bottom: 100px;
}

.landing-figma-button {
  left: 50%;
  transform: translateX(-50%);
  bottom: -25px;
}

.header-landing-appbar {
  background-color: transparent !important;

  &.v-app-bar--is-scrolled {
    background-color: #fff !important;
    box-shadow: rgb(43 52 69 / 10%) 0px 4px 16px !important;
  }
}

.wrapper {
  position: relative;
}
</style>
