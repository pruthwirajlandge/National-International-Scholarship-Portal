<template>
  <div class="header-landing">
    <v-navigation-drawer v-model="drawer" app temporary>
      <v-list>
        <v-list-item>
          <v-list-item-avatar>
            <img v-svg-inline class="mr-2" src="@/assets/images/logo.svg" alt="" />
          </v-list-item-avatar>
        </v-list-item>
      </v-list>

      <v-divider />

      <v-list dense>
        <v-list-item v-for="([text, link], i) in items" :key="i" link @click="$vuetify.goTo(link)">
          <v-list-item-content>
            <v-list-item-title class="subtitile-1">{{
      text
    }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-container>
      <v-app-bar app :flat="flat" elevation="0" class="px-15 header-landing-appbar" :class="{ expand: flat }">
        <v-toolbar-title>
          <h1 class="text-capitalize primary--text">Scholorship</h1>
        </v-toolbar-title>
        <v-spacer />
        <v-col cols="12" md="5">
          <div class="search-bar d-flex p-relative">
            <v-text-field v-model="searchedText" placeholder="Searching For" filled rounded hide-details dense
              prepend-inner-icon="mdi-magnify"></v-text-field>
            <v-btn color="primary" class="text-capitalize search-bar-dropdown px-10 font-600" @click="searchResult">
              Search
            </v-btn>
          </div>
        </v-col>
        <v-spacer />
        <v-app-bar-nav-icon @click.stop="drawer = !drawer" class="mr-4" v-if="isXs" />
        <div v-else>
          <v-btn text @click="$vuetify.goTo('#about')">
            <span class="mr-2 text-capitalize grey--text text--darken-3">About</span>
          </v-btn>
          <v-btn text @click="$vuetify.goTo('#features')">
            <span class="mr-2 text-capitalize grey--text text--darken-3">Features</span>
          </v-btn>
        </div>
        <div>
          <v-dialog v-if="!token" v-model="dialog" width="500">
            <template v-slot:activator="{ on, attrs }">
              <v-btn elevation="0" fab small class="mr-3" color="grey lighten-2" v-bind="attrs" v-on="on">
                <v-icon>mdi-account</v-icon>
              </v-btn>
            </template>
            <base-card>
              <div class="px-3 px-md-10 py-8">
                <h3 class="mb-2 text-center">Welcome To Scholorship</h3>
                <h5 class="font-600 grey--text text--darken-3 text-sm mb-9 text-center">
                  Log in with email & password
                </h5>
                <ValidationObserver ref="observer" v-slot="{ invalid }">
                  <form @Login.prevent="login">
                    <ValidationProvider name="E-mail" rules="required|email" v-slot="{ errors }" :bails="true">
                      <v-text-field v-model="email" type="email" :error-messages="errors" required counter outlined
                        dense hide-details="auto" placeholder="example@mail.com" class="mb-4"
                        prepend-icon="mdi-email"></v-text-field>
                    </ValidationProvider>
                    <ValidationProvider name="Password" rules="required|min:8" v-slot="{ errors }" :bails="true">
                      <v-text-field v-model="password" :error-messages="errors"
                        :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'" :type="show1 ? 'text' : 'password'"
                        @click:append="show1 = !show1" required counter outlined dense hide-details="auto"
                        placeholder="Example@123" class="mb-4" prepend-icon="mdi-lock" />
                    </ValidationProvider>
                    <v-btn block @click="login" color="primary" class="text-capitalize font-600"
                      :disabled="invalid">Login</v-btn>
                  </form>
                </ValidationObserver>
                <div class="text-14 text-center my-3">
                  Don't have account?
                  <router-link to="/sign-up" class="grey--text text--darken-4 font-600">Sign Up</router-link>
                </div>
                <p v-if="error_response" class="text-14 text-center my-3" style="color: red">
                  {{ error_response }}
                </p>
              </div>
              <v-overlay :value="overlay">
                <v-progress-circular indeterminate size="64"></v-progress-circular>
              </v-overlay>
              <div class="py-4 grey lighten-2">
                <div class="text-center">
                  <span class="grey--text text--darken-1">Forgot Your Password
                    <router-link to="/" class="ms-2 grey--text text--darken-4 font-600">Reset It</router-link>
                  </span>
                </div>
              </div>
            </base-card>
          </v-dialog>
          <v-menu bottom min-width="200px" rounded offset-y v-for="user in users" :key="user.id">
            <template v-slot:activator="{ on }">
              <v-btn icon x-large v-on="on">
                <v-avatar color="brown" size="40">
                  <v-img width="50" :src="storage_url + user.profile_picture"></v-img>
                </v-avatar>
              </v-btn>
            </template>
            <v-card>
              <v-list-item-content class="justify-center">
                <div class="mx-auto text-center">
                  <v-avatar color="brown">
                    <v-img width="50" :src="storage_url + user.profile_picture"></v-img>
                  </v-avatar>
                  <h4>{{ user.first_name }} {{ user.last_name }}</h4>
                  <p class="text-caption mt-1">
                    {{ user.email }}
                  </p>
                  <v-divider class="my-3"></v-divider>
                  <v-btn depressed rounded text to="/profile">
                    View Profile
                  </v-btn>
                  <v-divider class="my-3"></v-divider>
                  <v-btn depressed rounded text @click="logout"> Logout </v-btn>
                </div>
              </v-list-item-content>
            </v-card>
          </v-menu>
        </div>
      </v-app-bar>

      <section id="home" class="p-relative pt-100">
        <v-row class="text-center">
          <v-col cols="12">
            <h1 class="font-weight-bold secondary--text text--darken-1">
              This is
              <span class="primary--text text-30 font-weight-bold">
                Scholorship
              </span>
            </h1>
            <h4 class="font-600 primary--text mb-2">
              Now National/International Scholorships in your finger tips
            </h4>
          </v-col>
          <v-col col="12"> </v-col>
        </v-row>
      </section>
      <v-container>
        <v-row class="landing-features p-relative justify-center">
          <v-col cols="6" class="text-center">
            <base-card class="shadow">
              <div class="pa-16">
                <ValidationObserver ref="observer" v-slot="{ invalid }">
                  <form @filterResult.prevent="filterResult">
                    <ValidationProvider name="Income" v-slot="{ errors }" :bails="true">
                      <v-text-field v-model="income_filter" type="text" :error-messages="errors" required counter
                        outlined dense hide-details="auto" placeholder="Filter by Income" class="mb-4"
                        prepend-icon="mdi-cash-multiple"></v-text-field>
                    </ValidationProvider>
                    <ValidationProvider name="Caste" v-slot="{ errors }" :bails="true">
                      <v-select v-model="caste_filter" :items="caste_item" :error-messages="errors" required counter
                        outlined dense hide-details="auto" placeholder="Filter by Caste" class="mb-4"
                        prepend-icon="mdi-account-group"></v-select>
                    </ValidationProvider>
                    <ValidationProvider name="Region" v-slot="{ errors }" :bails="true">
                      <v-text-field v-model="region_filter" type="text" :error-messages="errors" required counter
                        outlined dense hide-details="auto" placeholder="Filter by Region" class="mb-4"
                        prepend-icon="mdi-map-marker"></v-text-field>
                    </ValidationProvider>
                    <ValidationProvider name="Education" v-slot="{ errors }" :bails="true">
                      <v-select v-model="education_filter" :items="education_item" :error-messages="errors" required
                        counter outlined dense hide-details="auto" placeholder="Filter by Education" class="mb-4"
                        prepend-icon="mdi-school"></v-select>
                    </ValidationProvider>
                    <v-row class="justify-center">
                      <v-col cols="6">
                        <v-btn block @click="filterResult" color="primary" class="text-capitalize font-600"
                          :disabled="invalid">Search</v-btn>
                      </v-col>
                    </v-row>
                  </form>
                </ValidationObserver>
              </div>
            </base-card>
          </v-col>
        </v-row>
      </v-container>
    </v-container>
    <v-dialog v-model="explore_scholorship_list" width="1200">
      <base-card>
        <div class="px-3 px-md-10 py-8">
          <h3 class="mb-2 text-center">Welcome To Scholorship</h3>
          <h5 class="font-600 grey--text text--darken-3 text-sm mb-9 text-center">
            Now National/International Scholorships in your finger tips
          </h5>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-simple-table>
                  <template v-slot:default>
                    <thead>
                      <tr>
                        <th class="text-left"> Scheme Name </th>
                        <th class="text-left"> Department Name </th>
                        <th class="text-left"> Last Date </th>
                        <th class="text-left"> Income Criteria </th>
                        <th class="text-left"> Caste Criteria </th>
                        <th class="text-left"> Region Criteria </th>
                        <th class="text-left"> Education Criteria </th>
                        <th class="text-left"> View In-detail </th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="(item, index) in result_data" :key="item.id">
                        <td>{{ item.scheme_name }}</td>
                        <td>{{ item.department_name }}</td>
                        <td>{{ item.last_date }}</td>
                        <td>{{ item.income_criteria }}</td>
                        <td>{{ item.caste_criteria }}</td>
                        <td>{{ item.region_criteria }}</td>
                        <td>{{ item.education_criteria }}</td>
                        <td>
                          <v-btn icon small @click="getScheme(item.id)"> <v-icon>mdi-open-in-new</v-icon> </v-btn>
                        </td>
                      </tr>
                    </tbody>
                  </template>
                </v-simple-table>
              </v-col>
              <v-col cols="6">
                <v-btn block @click="explore_scholorship_list = false" color="primary"
                  class="text-capitalize font-600">Close</v-btn>
              </v-col>
            </v-row>
          </v-container>
        </div>
        <v-overlay :value="overlay">
          <v-progress-circular indeterminate size="64"></v-progress-circular>
        </v-overlay>
      </base-card>
    </v-dialog>
    <v-dialog v-model="explore_scholorship_detail" width="1200">
      <base-card>
        <div class="px-3 px-md-10 py-8">
          <h3 class="mb-2 text-center">Welcome To Scholorship</h3>
          <h5 class="font-600 grey--text text--darken-3 text-sm mb-9 text-center">
            Now National/International Scholorships in your finger tips
          </h5>
          <v-container>

            <div class="px-3 px-md-10 py-8" v-for="item in scheme_data">
              <v-row>
                <v-col cols="12">
                  <h3 class="mb-2 text-center">{{ item.scheme_name }}</h3>
                  <h5 class="font-600 grey--text text--darken-3 text-sm mb-9 text-center">
                    {{ item.department_name }}
                  </h5>
                  <h4 class="text-center"> Overview: </h4>
                  <p class="font-500 grey--text text--darken-4 mx-12 text-justify">
                    <ckeditor :editor="editor" v-model="item.scheme_overview" :config="editorConfig" tag-name="textarea"
                      disabled></ckeditor>
                  </p>
                  <h4 class="text-center"> Benifit: </h4>
                  <p class="font-500 grey--text text--darken-4 mx-12 text-justify">
                    <ckeditor :editor="editor" v-model="item.scheme_benefits" tag-name="textarea" disabled></ckeditor>
                    <!-- {{ item.scheme_benefits }} -->
                  </p>
                  <h4 class="text-center"> Eligibility: </h4>
                  <p class="font-500 grey--text text--darken-4 mx-12 text-justify">
                    <ckeditor :editor="editor" v-model="item.scheme_eligibility" tag-name="textarea" disabled>
                    </ckeditor>
                    <!-- {{ item.scheme_eligibility }} -->
                  </p>
                  <h4 class="text-center"> Documents Needed: </h4>
                  <p class="font-500 grey--text text--darken-4 mx-12 text-justify">
                    <ckeditor :editor="editor" v-model="item.scheme_documents" tag-name="textarea" disabled></ckeditor>
                    <!-- {{ item.scheme_documents }} -->
                  </p>
                </v-col>
                <v-col cols="6">
                  <a :href="item.scheme_link">
                    <v-btn block color="primary" class="text-capitalize font-600">Apply</v-btn>
                  </a>
                </v-col>
                <v-col cols="6">
                  <v-btn block @click="explore_scholorship_detail = false" color="primary"
                    class="text-capitalize font-600">Close</v-btn>
                </v-col>
              </v-row>
            </div>

          </v-container>
        </div>
        <v-overlay :value="overlay">
          <v-progress-circular indeterminate size="64"></v-progress-circular>
        </v-overlay>
      </base-card>
    </v-dialog>
  </div>
</template>

<script>
import axios from "axios";
import Vue from "vue";
import { required, digits, email, max, regex } from "vee-validate/dist/rules";
import { extend, setInteractionMode } from "vee-validate";
import { mapGetters } from "vuex";
import Model from "@/components/module/Model.vue";
import ShowLogs from "@/components/module/ShowLogs.vue";
import ClassicEditor from '@ckeditor/ckeditor5-build-classic';

setInteractionMode("eager");

extend("digits", {
  ...digits,
  message: "{_field_} needs to be {length} digits. ({_value_})",
});

extend("required", {
  ...required,
  message: "{_field_} can not be empty",
});

extend("max", {
  ...max,
  message: "{_field_} may not be greater than {length} characters",
});

extend("regex", {
  ...regex,
  message: "{_field_} {_value_} does not match {regex}",
});

extend("email", {
  ...email,
  message: "Email must be valid",
});

export default {
  components: {
    Model,
    ShowLogs,
  },
  data: () => ({
    storage_url: process.env.VUE_APP_STORAGE_URL,
    explore_scholorship_list: false,
    explore_scholorship_detail: false,
    searchedText: "",
    income_filter: "",
    caste_filter: "",
    region_filter: "",
    education_filter: "",
    caste_item: ['Open', 'Obc', 'Sbc', 'SC', 'NT', 'VJNT', 'Navbouddha'],
    education_item: ['SSC', 'HSC', 'Diploma', 'Under Graduate', 'Graduate', 'Post Graduate', 'Doctorate'],
    result_data: null,
    scheme_data: [],
    counter: 0,
    email: "",
    password: "",
    overlay: false,
    show1: false,
    show2: false,
    error_response: "",
    dialog: false,
    token: Vue.$cookies.get("token"),
    user_name: Vue.$cookies.get("user_name"),
    role: Vue.$cookies.get("role"),
    base_url: process.env.VUE_APP_SERVER_URL,
    drawer: null,
    isXs: false,
    items: [
      ["About", "#about"],
      ["Features", "#features"],
      ["Technology", "#technology"],
    ],
    expert_dialog: false,
    report_dialog: false,
    votes: null,
    editor: ClassicEditor,
    editorConfig: {
      toolbar: {
        items: [
          'heading',
          '|',
          'bold',
          'italic',
          '|',
          'bulletedList',
          'numberedList',
          '|',
          'insertTable',
          '|',
          'imageUpload',
          '|',
          'undo',
          'redo'
        ]
      },
      // image: {
      //   toolbar: [
      //     'imageStyle:full',
      //     'imageStyle:side',
      //     '|',
      //     'imageTextAlternative'
      //   ]
      // },
      // table: {
      //   contentToolbar: [ 'tableColumn', 'tableRow', 'mergeTableCells' ]
      // },
      language: 'en'
    }
  }),
  props: {
    color: String,
    flat: Boolean,
  },
  methods: {
    onResize() {
      this.isXs = window.innerWidth < 850;
    },
    login() {
      this.overlay = true;
      this.$refs.observer.validate().then((success) => {
        if (!success) {
          return;
        }
        axios({
          method: "POST",
          url: process.env.VUE_APP_SERVER_URL + "auth/token/login/",
          data: JSON.stringify({
            password: this.password,
            email: this.email,
          }),
          headers: {
            "Content-Type": "application/json; charset=UTF-8",
          },
        })
          .then((res) => {
            this.overlay = false;
            Vue.$cookies.set("token", res.data.auth_token, "28d");
            window.location.reload();
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
    logout() {
      Vue.$cookies.remove("token");
      window.location.reload();
    },

    filterResult() {
      this.overlay = true;
      axios({
        method: "GET",
        url: this.base_url + "scheme/?scheme_name=&department_name=&last_date=&income_criteria=" + this.income_filter +
          "&caste_criteria=" + this.caste_filter + "&region_criteria=" + this.region_filter +
          "&education_criteria=" + this.education_filter,
        data: JSON.stringify({}),
        headers: {
          "Content-Type": "application/json; charset=UTF-8",
          Authorization: `token ${this.token}`,
        },
      })
        .then((res) => {
          this.overlay = false;
          // alert(res.data);
          this.result_data = res.data;
          this.explore_scholorship_list = true;
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
      if (this.overlay) {
        setTimeout(() => (this.overlay = false), 2000);
      }
    },

    searchResult() {
      this.overlay = true;
      axios({
        method: "GET",
        url: this.base_url + "scheme/?search=" + this.searchedText,
        data: JSON.stringify({}),
        headers: {
          "Content-Type": "application/json; charset=UTF-8",
          Authorization: `token ${this.token}`,
        },
      })
        .then((res) => {
          this.overlay = false;
          // alert(res.data);
          this.result_data = res.data;
          this.explore_scholorship_list = true;
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
      if (this.overlay) {
        setTimeout(() => (this.overlay = false), 2000);
      }
    },

    getScheme(id) {
      this.overlay = true;
      this.scheme_data = []
      axios({
        method: "GET",
        url: this.base_url + "scheme/" + id + "/",
        data: JSON.stringify({}),
        headers: {
          "Content-Type": "application/json; charset=UTF-8",
          Authorization: `token ${this.token}`,
        },
      })
        .then((res) => {
          this.overlay = false;
          this.scheme_data.push(res.data);
          console.log(this.scheme_data);
          this.explore_scholorship_detail = true;
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
      if (this.overlay) {
        setTimeout(() => (this.overlay = false), 2000);
      }
    },
  },

  computed: {
    ...mapGetters(["users"]),
  },

  watch: {
    isXs(value) {
      if (!value) {
        if (this.drawer) {
          this.drawer = false;
        }
      }
    },
  },
  mounted() {
    this.onResize();
    window.addEventListener("resize", this.onResize, { passive: true });
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
</style>
