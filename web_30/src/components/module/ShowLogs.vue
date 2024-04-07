<template>
  <v-card color="#eeeeee">
    <v-toolbar dark color="primary">
      <v-btn icon dark @click="$emit('closeDialog')">
        <v-icon>mdi-close</v-icon>
      </v-btn>
      <v-toolbar-title>Scholorship</v-toolbar-title>
    </v-toolbar>
    <v-container>
      <v-row class="landing-features p-relative">
        <v-col cols="6" class="text-center">
          <base-card class="shadow">
            <OsLog />
            <h3>Operating Systems</h3>
          </base-card>
        </v-col>
        <v-col cols="6" class="text-center">
          <base-card class="shadow">
            <AccessLog />
            <h3>Total Device Access</h3>
          </base-card>
        </v-col>
        <v-col cols="6" class="text-center">
          <base-card class="shadow">
            <DevicesLog />
            <h3>Devices by Types</h3>
          </base-card>
        </v-col>
        <v-col cols="6" class="text-center">
          <base-card class="shadow">
            <SessionLog />
            <h3>Sessions of Devices</h3>
          </base-card>
        </v-col>
      </v-row>
    </v-container>

    <v-card-title class="d-flex flex-column text-center align-center justify-center">
      <span class="text-h5 mx-16 mt-16">Devices Connected in the Network</span>
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
                    <th class="text-left">Connected With</th>
                    <th class="text-left">Current Device Status</th>
                    <th class="text-left">Uptime Since</th>
                    <th class="text-left">Last Access</th>
                    <th class="text-left">Os Type</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(item, index) in data" :key="item.id">
                    <td>{{ item.device_type }}</td>
                    <td>{{ item.device_ip }}</td>
                    <td>{{ item.device_mac }}</td>
                    <td>{{ item.associate_device }}</td>
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
                    <!-- <td v-if="!item.has_access">
                      <v-btn class="secondary" @click="controlStatus(item.id)"> Allow </v-btn>
                    </td>
                    <td v-if="item.has_access">
                      <v-btn class="secondary" @click="controlStatus(item.id)"> Block </v-btn>
                    </td> -->
                  </tr>
                </tbody>
              </template>
            </v-simple-table>
          </v-col>
        </v-row>
      </v-container>
    </v-card-text>
    <v-card-actions>
    </v-card-actions>
  </v-card>
</template>

<script>
import Vue from "vue";
import axios from "axios";
import OsLog from './OsLog.vue'
import AccessLog from './AccessLog.vue'
import DevicesLog from './DevicesLog.vue'
import SessionLog from './SessionLog.vue'

export default {
  components: {
    OsLog,
    AccessLog,
    DevicesLog,
    SessionLog
  },
  data: () => ({
    token: Vue.$cookies.get("token"),
    loaded: false,
    data: null,
  }),

  mounted() {
        this.Get();
    },

    methods: {
        Get() {
            axios({
                method: "GET",
                url: "http://127.0.0.1:8000/device/",
                data: JSON.stringify({}),
                headers: {
                    "Content-Type": "application/json; charset=UTF-8",
                    Authorization: `token ${this.token}`,
                },
            })
                .then((res) => {
                    this.data = res.data;
                    this.loaded = true;
                })
                .catch((error) => {
                    console.log(error);
                    this.errored = true;
                });
        },
    },
};
</script>

<style></style>