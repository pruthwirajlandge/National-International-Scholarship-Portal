import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import vuetify from "@/plugins/vuetify";
import { store } from "./store/store";
import "./plugins";
import "@/assets/scss/_global.scss";
import VueSvgInlinePlugin from "vue-svg-inline-plugin";
import "vue-svg-inline-plugin/src/polyfills";
import VueSlickCarousel from 'vue-slick-carousel'
import 'vue-slick-carousel/dist/vue-slick-carousel.css'
import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'
import VueApexCharts from 'vue-apexcharts'
import {
  ValidationProvider,
  ValidationObserver
} from "vee-validate/dist/vee-validate.full.esm";
import VueCookies from "vue-cookies";
import CKEditor from '@ckeditor/ckeditor5-vue2';

Vue.config.productionTip = false;
Vue.use(VueCookies);
Vue.component("ValidationProvider", ValidationProvider);
Vue.component("ValidationObserver", ValidationObserver);
Vue.use(VueSvgInlinePlugin);
Vue.component(VueSlickCarousel);
Vue.component("VueSlickCarousel", VueSlickCarousel);
Vue.use(VueApexCharts);
Vue.component('apexchart', VueApexCharts);
Vue.use(CKEditor);

VueSvgInlinePlugin.install(Vue, {
	attributes: {
		data: [ "src" ],
		remove: [ "alt" ]
	}
});

new Vue({
  router,
  vuetify,
  store,
  render: h => h(App)
}).$mount("#app");
