<template>
  <v-container class="py-6">
    <v-row>
      <v-col cols="12">
        <div class="box-wrapper" v-for="user in users" :key="user.id">
          <div class="box-overlay" :class="{ open: isSidebar }" @click="isSidebar = !isSidebar"></div>
          <div class="box-sidebar pb-3 shadow-sm" :class="{ open: isSidebar }">
            <DashbordSidebar />
          </div>
          <div class="box-content">
            <div class="d-flex justify-end pa-2 d-block d-md-none">
              <v-btn icon @click="isSidebar = !isSidebar">
                <v-icon dark> mdi-format-list-bulleted-square </v-icon>
              </v-btn>
            </div>
            <div class="box-container">
              <div class="d-flex justify-space-between flex-wrap mb-5">
                <div class="d-flex align-center">
                  <v-avatar tile size="25" class="me-3">
                    <img src="@/assets/images/icons/user_filled.svg" alt="" />
                  </v-avatar>
                  <h2 class="mb-0">My Profile</h2>
                </div>
                <v-btn outlined color="primary" class="text-capitalize font-600" @click="dialog = true">
                  Change Password
                </v-btn>
              </div>

              <v-row>
                <v-col cols="12" md="12" lg="12">
                  <base-card>
                    <div class="pa-5">
                      <div class="d-flex justify-space-between align-center flex-wrap">
                        <div class="d-flex align-center">
                          <v-avatar color="brown" size="64" class="me-4">
                            <!-- <span class="white--text text-h4">{{
                              user.initial_profile
                            }}</span> -->
                            <v-img width="50" :src="storage_url + user.profile_picture"></v-img>
                          </v-avatar>
                          <div>
                            <h4 class="font-600">{{ user.full_name }}</h4>
                            <p class="mb-0 grey--text text--darken-1">
                              {{ user.short_name }}
                            </p>
                          </div>
                        </div>
                      </div>
                    </div>
                  </base-card>
                </v-col>
                <v-col cols="12">
                  <base-card>
                    <div class="pa-4 d-flex justify-space-between flex-wrap">
                      <div class="mx-2 my-2">
                        <p class="text-sm grey--text text--darken-1 mb-1">
                          First Name
                        </p>
                        <span>{{ user.first_name }}</span>
                      </div>
                      <div class="mx-2 my-2">
                        <p class="text-sm grey--text text--darken-1 mb-1">
                          Last Name
                        </p>
                        <span>{{ user.last_name }}</span>
                      </div>
                      <div class="mx-2 my-2">
                        <p class="text-sm grey--text text--darken-1 mb-1">
                          Email
                        </p>
                        <span>{{ user.email }}</span>
                      </div>
                      <div class="mx-2 my-2">
                        <p class="text-sm grey--text text--darken-1 mb-1">
                          Phone Number
                        </p>
                        <span>{{ user.phone_number }}</span>
                      </div>
                      <div class="mx-2 my-2">
                        <p class="text-sm grey--text text--darken-1 mb-1">
                          Address
                        </p>
                        <span>{{ user.address }}</span>
                      </div>
                    </div>
                  </base-card>
                </v-col>
              </v-row>
            </div>
          </div>
        </div>
      </v-col>
    </v-row>
    <div>
      <v-dialog v-model="dialog" width="500">
        <base-card>
          <div class="px-3 px-md-10 py-8">
            <h3 class="mb-2 text-center">Welcome To Scholorship</h3>
            <h5 class="font-600 grey--text text--darken-3 text-sm mb-9 text-center">
              Change Password
            </h5>
            <ValidationObserver ref="observer" v-slot="{ invalid }">
              <form @changePassword.prevent="changePassword">
                <ValidationProvider name="New-Password" vid="new_password"
                  rules="required|min:8|confirmed:confirm_password" v-slot="{ errors }" :bails="true">
                  <v-text-field v-model="new_password" :error-messages="errors"
                    :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'" :type="show2 ? 'text' : 'password'"
                    @click:append="show2 = !show2" required counter placeholder="*********" outlined dense
                    hide-details="auto" class="mb-4" prepend-icon="mdi-lock" />
                </ValidationProvider>

                <ValidationProvider name="Confirm-Password" vid="confirm_password" rules="required|min:8"
                  v-slot="{ errors }" :bails="true">
                  <v-text-field v-model="confirm_password" :error-messages="errors"
                    :append-icon="show3 ? 'mdi-eye' : 'mdi-eye-off'" :type="show3 ? 'text' : 'password'"
                    @click:append="show3 = !show3" required counter placeholder="*********" outlined dense
                    hide-details="auto" class="mb-4" prepend-icon="mdi-lock" />
                </ValidationProvider>
                <v-btn block @click="changePassword" color="primary" class="text-capitalize font-600"
                  :disabled="invalid">Change Password</v-btn>
              </form>
            </ValidationObserver>
            <p v-if="error_response" class="text-14 text-center my-3" style="color: red">
              {{ error_response }}
            </p>
          </div>
          <v-overlay :value="overlay">
            <v-progress-circular indeterminate size="64"></v-progress-circular>
          </v-overlay>
        </base-card>
      </v-dialog>
    </div>
    <div>
      <v-row justify="center">
        <v-dialog v-model="confirmation_dialog" persistent max-width="290">
          <v-card>
            <v-card-title class="text-h5">
              Change Password
            </v-card-title>
            <v-card-text>Password has been changed successfully!</v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="green darken-1" text @click="redirect">
                Okay
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-row>
    </div>
  </v-container>
</template>

<script>
import { mapGetters } from "vuex";
import Vue from "vue";
import axios from "axios";
import DashbordSidebar from "@/components/base/DashboardSidebar";
import { required, min, confirmed } from "vee-validate/dist/rules";
import { extend, setInteractionMode } from "vee-validate";

setInteractionMode("eager");

extend("required", {
  ...required,
  message: "{_field_} can not be empty",
});

extend("min", {
  ...min,
  message: "{_field_} may not be less than {length} characters",
});

extend("confirmed", {
  ...confirmed,
  params: ["target"],
  validate(value, { target }) {
    return value === target;
  },
  message: "The {_field_} does not match the {target}",
});

export default {
  components: {
    DashbordSidebar,
  },
  data() {
    return {
      storage_url: process.env.VUE_APP_STORAGE_URL,
      new_password: null,
      confirm_password: null,
      show1: false,
      show2: false,
      show3: false,
      error_response: "",
      dialog: false,
      confirmation_dialog: false,
      isSidebar: false,
      overlay: false,
      token: Vue.$cookies.get("token"),
    };
  },
  computed: {
    ...mapGetters(["users"]),
  },
  methods: {
    redirect() {
      this.confirmation_dialog = false;
      Vue.$cookies.remove("token");
      this.$router.push("/sign-in");
    },
    changePassword() {
      this.overlay = true;
      this.$refs.observer.validate().then((success) => {
        if (!success) {
          return;
        }
        axios({
          method: "POST",
          url: process.env.VUE_APP_SERVER_URL + "auth/users/set_password/",
          data: JSON.stringify({
            new_password: this.new_password,
            current_password: this.confirm_password,
          }),
          headers: {
            "Content-Type": "application/json; charset=UTF-8",
            "Authorization": `token ${this.token}`,
          },
        })
          .then((res) => {
            this.overlay = false;
            this.confirmation_dialog = true;
          })
          .catch((error) => {
            this.overlay = false;
            console.log(error);
            if (error.response.status == 400) {
              this.error_response = error.response.data.non_field_errors[0];
            } else {
              this.error_response = error.message;
            }
          });
      });
      if (this.overlay == true) {
        setTimeout(() => (this.overlay = false), 2000);
      }
    },
  },
};
</script>
<style lang="scss" scoped>
.main-content {
  padding: 0px 0px 0px !important;
}
</style>
