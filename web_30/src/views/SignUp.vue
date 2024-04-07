<template>
  <v-app>
    <div class="bg-body d-flex flex-column justify-center align-center min-vh-100">
      <div class="sign-up-card">
        <div class="sign-up-card-container">
          <div class="text-center mb-10">
            <h3 class="mb-3">Create Your Account</h3>
            <h5 class="text-sm font-600 grey--text text--darken-4">
              Please fill all forms to continued
            </h5>
          </div>
          <ValidationObserver ref="observer" v-slot="{ invalid }">
            <form @Login.prevent="login">
              <div class="mb-4">
                <p class="text-14 mb-1">Full Name</p>
                <v-row>
                  <v-col cols="6">
                    <ValidationProvider name="First Name" rules="required|max:30" v-slot="{ errors }" :bails="true">
                      <v-text-field v-model="first_name" type="text" :error-messages="errors" required
                        placeholder="First Name" outlined dense hide-details="auto"></v-text-field>
                    </ValidationProvider>
                  </v-col>
                  <v-col cols="6">
                    <ValidationProvider name="Last Name" rules="required|max:30" v-slot="{ errors }" :bails="true">
                      <v-text-field v-model="last_name" type="text" :error-messages="errors" required
                        placeholder="Last Name" outlined dense hide-details="auto"></v-text-field>
                    </ValidationProvider>
                  </v-col>
                </v-row>
              </div>
              <div class="mb-4">
                <p class="text-14 mb-1">Email</p>
                <ValidationProvider name="E-mail" rules="required|email" v-slot="{ errors }" :bails="true">
                  <v-text-field v-model="email" type="email" :error-messages="errors" required
                    placeholder="example@mail.com" outlined dense hide-details="auto"></v-text-field>
                </ValidationProvider>
              </div>
              <div class="mb-4">
                <p class="text-14 mb-1">Password</p>
                <ValidationProvider name="password" rules="required|min:8" v-slot="{ errors }" :bails="true">
                  <v-text-field v-model="password" :error-messages="errors"
                    :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'" :type="show1 ? 'text' : 'password'"
                    @click:append="show1 = !show1" required placeholder="*********" outlined dense
                    hide-details="auto"></v-text-field>
                </ValidationProvider>
              </div>
              <div class="mb-4">
                <p class="text-14 mb-1">Confirm Password</p>
                <ValidationProvider name="confirm" rules="required|confirmed:password" v-slot="{ errors }"
                  :bails="true">
                  <v-text-field v-model="confirmation" :error-messages="errors"
                    :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'" :type="show2 ? 'text' : 'password'"
                    @click:append="show2 = !show2" required placeholder="*********" outlined dense
                    hide-details="auto"></v-text-field>
                </ValidationProvider>
              </div>
              <div class="mb-4">
                <p class="text-14 mb-1">Phone Number</p>
                <ValidationProvider name="Phone Numebr" rules="required|digits:10" v-slot="{ errors }" :bails="true">
                  <v-text-field v-model="phone" :error-messages="errors" required placeholder="9123456789" outlined
                    dense hide-details="auto"></v-text-field>
                </ValidationProvider>
              </div>
              <div class="mb-4">
                <p class="text-14 mb-1">Address</p>
                <ValidationProvider name="Address" rules="required" v-slot="{ errors }" :bails="true">
                  <v-text-field v-model="address" type="Address" :error-messages="errors" required
                    placeholder="A1, Street Address" outlined dense hide-details="auto"></v-text-field>
                </ValidationProvider>
              </div>
              <div class="mb-4">
                <p class="text-14 mb-1">Profile Picture</p>
                <ValidationProvider name="Profile Picture" rules="required" v-slot="{ errors }" :bails="true">
                  <v-file-input v-model="profile_picture" accept="image/png, image/jpeg, image/bmp, image/jpg"
                    :error-messages="errors" placeholder="Pick a Profile Picture" outlined small-chips
                    truncate-length="1"></v-file-input>
                </ValidationProvider>
              </div>
              <div class="mb-4">
                <ValidationProvider name="Terms & Condtion" rules="required" v-slot="{ errors }" :bails="true">
                  <v-checkbox v-model="checkbox" :error-messages="errors" value="1" type="checkbox" required>
                    <template v-slot:label>
                      <div>
                        By signing up, you agree to

                        <v-tooltip bottom>
                          <template v-slot:activator="{ on }">
                            <a target="_blank" href="#" @click.stop v-on="on">
                              Terms & Condtion
                            </a>
                          </template>
                          Opens in new window
                        </v-tooltip>
                      </div>
                    </template>
                  </v-checkbox>
                </ValidationProvider>
              </div>
              <p v-if="error_response" class="text-14 text-center my-3" style="color:red;">
                {{ error_response }}
              </p>
              <div class="mb-4">
                <v-btn block color="primary" class="text-capitalize font-600" :disabled="invalid" @click="signup">
                  Create Account
                </v-btn>
              </div>
            </form>
          </ValidationObserver>
        </div>
        <div class="py-4 grey lighten-2">
          <div class="text-center">
            <span class="grey--text text--darken-1">Already Have Account ?
              <a href="/sign-in" class="ms-2 grey--text text--darken-4 font-600">Log in</a>
            </span>
          </div>
        </div>
      </div>
      <div>
        <v-row justify="center">
          <v-dialog v-model="confirmation_dialog" persistent max-width="290">
            <v-card>
              <v-card-title class="text-h5">
                User Created Successfully!
              </v-card-title>
              <v-card-text>By clicking Okay button you'll be redirected to the Login page.
                Thanks for joining with us!</v-card-text>
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
    </div>
  </v-app>
</template>

<script>
import axios from "axios";
import {
  required,
  digits,
  email,
  max,
  regex,
  confirmed
} from "vee-validate/dist/rules";
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

extend("confirmed", {
  ...confirmed,
  message: "The password does not match"
});

export default {
  data() {
    return {
      checkbox: false,
      base_url: process.env.VUE_APP_SERVER_URL,
      first_name: null,
      last_name: null,
      phone: null,
      email: null,
      password: null,
      confirmation: null,
      address: null,
      profile_picture: [],
      overlay: false,
      loading: false,
      show1: false,
      show2: false,
      error_response: null,
      confirmation_dialog: false,
    };
  },

  methods: {
    redirect() {
      this.confirmation_dialog = false;
      this.$router.push("/sign-in");
    },
    save(date) {
      this.$refs.menu.save(date);
    },

    signup() {
      this.overlay = true;
      this.$refs.observer.validate().then(success => {
        if (!success) {
          return;
        }

        axios({
          method: "POST",
          url: this.base_url + "create-profile/",
          data: {
            email: this.email,
            first_name: this.first_name,
            last_name: this.last_name,
            password: this.password,
            re_password: this.confirmation,
            phone_number: this.phone,
            address: this.address,
            profile_picture: this.profile_picture,
          },
          headers: {
            "Content-Type": "multipart/form-data",
          }
        })
          .then(res => {
            this.confirmation_dialog = true;
            this.overlay = false;
          })
          .catch(error => {
            this.overlay = false;
            console.log(error);
            if (error.response.status == 400) {
              this.error_response = error.response.data;
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
