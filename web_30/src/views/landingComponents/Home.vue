<template>
  <div>
    <!-- About us  -->
    <section id="about" class="p-relative pt-100 mx-12 mb-15">
      <v-row class="text-center mx-12">
        <v-col cols="12" v-for="(n, index) in about" :key="index">
          <h2 class="text-40 secondary--text font-weight-black mb-5">
            About Project
          </h2>
          <p class="font-500 grey--text text--darken-4 mx-12 text-justify">
            {{ n.para }}
          </p>
        </v-col>
      </v-row>
    </section>

    <!-- features  -->
    <section id="features" class="mb-15">
      <v-container>
        <v-row>
          <v-col cols="12" class="text-center mb-15">
            <h1 class="secondary--text text-40 font-weight-bold">
              Project Features
            </h1>
          </v-col>
        </v-row>
        <v-row class="landing-features p-relative">
          <v-col
            cols="12"
            md="4"
            lg="3"
            class="text-center"
            v-for="(n, index) in powerfulFeatures"
            :key="index"
          >
            <base-card class="shadow">
              <div class="py-14">
                <v-avatar class="mb-6" size="64" tile>
                  <img v-svg-inline class="icon" :src="n.img" alt="" />
                </v-avatar>
                <h4>{{ n.name }}</h4>
              </div>
            </base-card>
          </v-col>
        </v-row>
      </v-container>
    </section>
    
    <footer class="py-8">
      <v-container>
        <div class="d-flex justify-space-between flex-wrap">
          <p class="py-1">
            Developed with
            <v-icon small color="primary" class="mx-1">mdi-cards-heart</v-icon>
            & Care by Scholorship
          </p>
          <div class="d-flex py-1 flex-wrap">
            <a
              href="https://www.facebook.com/UILibOfficial"
              target=""
              class="text-decoration-none me-2"
            >
              <v-icon color="secondary">mdi-facebook</v-icon>
            </a>
            <a
              href="https://twitter.com/uilibofficial"
              target=""
              class="text-decoration-none me-2"
            >
              <v-icon color="secondary">mdi-twitter</v-icon>
            </a>
            <a
              href="https://www.youtube.com/channel/UCsIyD-TSO1wQFz-n2Y4i3Rg"
              target=""
              class="text-decoration-none me-2"
            >
              <v-icon color="secondary">mdi-youtube</v-icon>
            </a>
            <a
              href="https://www.linkedin.com/company/ui-lib/"
              target=""
              class="text-decoration-none me-2"
            >
              <v-icon color="secondary">mdi-linkedin</v-icon>
            </a>
          </div>
        </div>
      </v-container>
    </footer>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tab: null,

      powerfulFeatures: [
        {
          img: require("@/assets/images/icons/multivendor.svg"),
          name: "National/International Scholarship",
        },
        {
          img: require("@/assets/images/icons/code.svg"),
          name: "All Scholarship is on your figer tips",
        },
        {
          img: require("@/assets/images/icons/optimization.svg"),
          name: "Detailed category wise results",
        },
        {
          img: require("@/assets/images/icons/optimization.svg"),
          name: "Saves your time and energy",
        },
      ],
      technology: [
        {
          img: require("@/assets/images/logos/vue.svg"),
          name: "Vue.js (Javascript based Frontend Framework)",
        },
        {
          img: require("@/assets/images/logos/vuetify.svg"),
          name: "Django (Python based Backend Framework)",
        },
        {
          img: require("@/assets/images/logos/sql-database.svg"),
          name: "SQL Database",
        },
        // {
        //   img: require("@/assets/images/logos/openai.svg"),
        //   name: "OpenAI",
        // },
      ],
      about: [
        {
          para: `
          The scholarship platform project aims to revolutionize the way students connect with funding opportunities for 
          their education. By leveraging advanced technology and intuitive user interfaces, the platform offers 
          a comprehensive database of scholarships from various sources, including institutions, organizations, and private donors. 
          Through smart algorithms and personalized recommendation systems, it matches students with scholarships that align 
          with their academic achievements, interests, and financial needs. The platform streamlines the application process, 
          providing guidance and resources to help students craft compelling applications. Additionally, it facilitates communication 
          between applicants and scholarship providers, fostering a transparent and efficient exchange of information. 
          With its user-centric design and commitment to accessibility, the scholarship platform project seeks to empower 
          students worldwide to pursue their educational aspirations without the burden of financial constraints.
          `,
        },
      ],
    };
  },
};
</script>

<style lang="scss" scoped>
#hero {
  margin-top: 64px;
}
.landing-features {
  z-index: 1;
  &::after {
    content: " ";
    position: absolute;
    height: 100px;
    width: 200px;
    background: rgb(227, 233, 239);
    z-index: -1;
    bottom: 0;

    left: 60px;
    border-bottom-right-radius: 300px;
    border-bottom-left-radius: 300px;
    margin-left: -100px;
    margin-bottom: -50px;
  }
  &::before {
    content: " ";
    position: absolute;
    height: 100px;
    width: 200px;
    background: rgb(227, 233, 239);
    z-index: -1;
    top: -65px;
    transform: rotate(180deg);
    right: 0;
    border-bottom-right-radius: 300px;
    border-bottom-left-radius: 300px;
    margin-right: 0px;
  }
}

.section-pricing {
  background-image: url("../../assets/images/landing/bonik.svg");
  background-position: center;
  background-repeat: no-repeat;
  background-size: contain;
  background-color: rgb(246, 249, 252);
}
.landing-card {
  &:hover {
  }
  .landing-card-body {
    box-shadow: none;
    cursor: unset;
    padding: 10% 10% 0px;
    background-color: rgb(243, 245, 249);
    border: 1px solid rgb(227, 233, 239);
    border-radius: 8px;
    position: relative;
    margin-bottom: 1.5rem;
    &:hover {
      .landing-card-overlay {
        opacity: 1;
      }
    }
    .landing-card-overlay {
      position: absolute;
      background-color: rgba(0, 0, 0, 0.54);
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      border-radius: 8px;
      opacity: 0;
      transition: opacity 250ms ease-in-out 0s;
    }
  }
}

// section-demos
.section-demos {
  background-image: url("../../assets/images/landing/landing-bg-2.svg");
  background-repeat: no-repeat;
  background-position: top center;
  background-size: contain;
}

.pricing-card {
  background-color: rgb(255, 255, 255);
  box-shadow: rgb(43 52 69 / 10%) 0px 4px 16px;
  border-radius: 8px;
  padding: 3rem 1rem 2rem;
  margin: 1.325rem;
  min-width: 270px;
  p {
    max-width: 216px;
    margin: 0 auto;
  }
}
</style>
