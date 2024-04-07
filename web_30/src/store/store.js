import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
    users: null,
  },
  getters: {
    users: (state) => state.users,
  },
  actions: {
    getUsers({ commit, state }) {
      if (Vue.$cookies.isKey("token")) {
        const token = Vue.$cookies.get("token");
        axios({
          method: "GET",
          url: process.env.VUE_APP_SERVER_URL + "my-account/",
          data: JSON.stringify({}),
          headers: {
            "Content-Type": "application/json; charset=UTF-8",
            Authorization: `token ${token}`,
          },
        })
          .then((res) => {
            commit("users", {
              users: res.data,
            });
            Vue.$cookies.set("user_name", res.data[0]['full_name']);
            Vue.$cookies.set("role", res.data[0]['role']);
          })
          .catch((err) => {
            console.error(err);
          });
      }
    },
  },
  mutations: {
    users(state, data) {
      state.users = data.users;
    },
  },
});
