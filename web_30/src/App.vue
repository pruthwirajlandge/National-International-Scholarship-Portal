<template>
  <v-app>
    <v-main class="main-content bg-body">
      <v-fade-transition mode="out-in">
        <div id="loading-wrapper" v-if="isLoading">
          <div id="loading-text">
            <v-img
              width="200"
              src="@/assets/logo.png"
              alt="Scholorship Logo"
            ></v-img>
          </div>
          <div id="loading-content"></div>
        </div>
        <router-view />
      </v-fade-transition>
    </v-main>
  </v-app>
</template>

<script>
import Vue from "vue";
export default {
  name: "App",

  data() {
    return {
      token: Vue.$cookies.get("token"),
      has_token: Vue.$cookies.isKey("token"),
      email: "",
      password: "",
      dialog: false,
      overlay: true,
      error_response: true,
      show1: false,
      show2: false,
      isLoading: true,
    };
  },
  mounted() {
    this.onDetectScreen();
    if (this.has_token) {
      this.$store.dispatch("getUsers");
    }
    this.onLoad();
  },
  methods: {
    onDetectScreen() {
      if (
        navigator.userAgent.match(/Android/i) ||
        navigator.userAgent.match(/webOS/i) ||
        navigator.userAgent.match(/iPhone/i) ||
        navigator.userAgent.match(/iPad/i) ||
        navigator.userAgent.match(/iPod/i) ||
        navigator.userAgent.match(/BlackBerry/i) ||
        navigator.userAgent.match(/Windows Phone/i) ||
        window.orientation <= 0
      ) {
        if (!this.has_token) {
          this.$router.push("/sign-in");
        }
      }
    },
    onLoad() {
      setTimeout(() => (this.isLoading = false), 2000);
    },
  },
};
</script>

<style lang="scss">
#loading-wrapper {
  position: fixed;
  width: 100%;
  height: 100%;
  left: 0;
  top: 0;
}

#loading-text {
  display: block;
  position: absolute;
  top: 50%;
  left: 50%;
  color: rgb(20, 121, 60);
  width: 120px;
  height: 50px;
  margin: -60px 0 0 -55px;
  text-align: center;
  font-family: "PT Sans Narrow", sans-serif;
  font-size: 20px;
}

#loading-content {
  display: block;
  position: relative;
  left: 50%;
  top: 50%;
  width: 170px;
  height: 170px;
  margin: -85px 0 0 -85px;
  border: 3px solid #f00;
}

#loading-content {
  border: 3px solid transparent;
  border-top-color: rgb(121, 61, 185);
  border-bottom-color: rgb(121, 61, 185);
  border-radius: 50%;
  -webkit-animation: loader 2s linear infinite;
  -moz-animation: loader 2s linear infinite;
  -o-animation: loader 2s linear infinite;
  animation: loader 2s linear infinite;
}

@keyframes loader {
  0% {
    -webkit-transform: rotate(0deg);
    -ms-transform: rotate(0deg);
    transform: rotate(0deg);
  }

  100% {
    -webkit-transform: rotate(360deg);
    -ms-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
</style>
