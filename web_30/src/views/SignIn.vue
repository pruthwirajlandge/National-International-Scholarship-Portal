<template>
  <v-app>
    <div
      class="bg-body d-flex flex-column justify-center align-center min-vh-100"
    >
      <div class="sign-up-card">
        <div class="sign-up-card-container">
          <div class="text-center mb-10">
            <h3 class="mb-3">Welcome To Scholorship</h3>
            <h5 class="text-sm font-600 grey--text text--darken-4">
              Log in with email & password
            </h5>
          </div>
          <ValidationObserver ref="observer" v-slot="{ invalid }">
            <form @Login.prevent="login">
              <div class="mb-4">
                <ValidationProvider
                  name="E-mail"
                  rules="required|email"
                  v-slot="{ errors }"
                  :bails="true"
                >
                  <v-text-field
                    v-model="email"
                    type="email"
                    :error-messages="errors"
                    required
                    counter
                    placeholder="example@mail.com"
                    outlined
                    dense
                    hide-details="auto"
                    class="mb-4"
                    prepend-icon="mdi-email"
                  ></v-text-field>
                </ValidationProvider>
              </div>
              <div class="mb-4">
                <ValidationProvider
                  name="Password"
                  rules="required|min:8"
                  v-slot="{ errors }"
                  :bails="true"
                >
                  <v-text-field
                    v-model="password"
                    :error-messages="errors"
                    :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                    :type="show1 ? 'text' : 'password'"
                    @click:append="show1 = !show1"
                    required
                    counter
                    placeholder="*********"
                    outlined
                    dense
                    hide-details="auto"
                    class="mb-4"
                    prepend-icon="mdi-lock"
                  ></v-text-field>
                </ValidationProvider>
              </div>
              <p
                v-if="error_response"
                class="text-14 text-center my-3"
                style="color:red;"
              >
                {{ error_response }}
              </p>
              <div class="mb-4">
                <v-btn
                  block
                  color="primary"
                  class="text-capitalize font-600"
                  :disabled="invalid"
                  @click="login"
                >
                  Login
                </v-btn>
                <v-overlay :value="overlay">
                  <v-progress-circular
                    indeterminate
                    size="64"
                  ></v-progress-circular>
                </v-overlay>
              </div>
            </form>
          </ValidationObserver>
        </div>
        <div class="py-4 grey lighten-2">
          <div class="text-center">
            <span class="grey--text text--darken-1"
              >Don't have account?
              <router-link :to="'/sign-up'" class="ms-2 grey--text text--darken-4 font-600">
                Sign Up
              </router-link>
            </span>
          </div>
        </div>
      </div>
    </div>
  </v-app>
</template>

<script>
import Vue from "vue";
import axios from "axios";
import { required, digits, email, max, regex } from "vee-validate/dist/rules";
import { extend, setInteractionMode } from "vee-validate";

setInteractionMode("eager");

extend("digits", {
  ...digits,
  message: "{_field_} needs to be {length} digits. ({_value_})"
});

extend("required", {
  ...required,
  message: "{_field_} can not be empty"
});

extend("max", {
  ...max,
  message: "{_field_} may not be greater than {length} characters"
});

extend("regex", {
  ...regex,
  message: "{_field_} {_value_} does not match {regex}"
});

extend("email", {
  ...email,
  message: "Email must be valid"
});

export default {
  data() {
    return {
      base_url : process.env.VUE_APP_SERVER_URL,
      checkbox: false,
      email: "",
      password: "",
      overlay: false,
      show1: false,
      show2: false,
      error_response: ""
    };
  },
  methods: {
    login() {
      this.overlay = true;
      this.$refs.observer.validate().then(success => {
        if (!success) {
          return;
        }
        axios({
          method: "POST",
          url: this.base_url + "auth/token/login/",
          data: JSON.stringify({
            password: this.password,
            email: this.email
          }),
          headers: {
            "Content-Type": "application/json; charset=UTF-8"
          }
        })
          .then(res => {
            Vue.$cookies.set("token", res.data.auth_token, "28d");
            this.overlay = false;
            this.$router.push("/");
            setTimeout(() => (window.location.reload()), 500);
          })
          .catch(error => {
            this.overlay = false;
            console.log(error);
            if (error.response.status == 400) {
              this.error_response = error.response.data.non_field_errors[0];
            } else {
              this.error_response = error.message;
            }
          });
      });
      if (this.overlay) {
        setTimeout(() => (this.overlay = false), 2000);
      }
    }
  }
};
</script>

<style lang="scss" scoped>
.sign-up-card {
  width: 500px;
  overflow: hidden;
  background-color: #fff;
  border-radius: 8px;
  margin: 2rem auto;
  box-shadow: rgb(3 0 71 / 9%) 0px 8px 45px;
  @media (max-width: 500px) {
    width: 100%;
  }
  .sign-up-card-container {
    padding: 3rem 3.75rem 0px;
    @media (max-width: 500px) {
      padding: 3rem 1rem 0px;
    }
  }
}
</style>
