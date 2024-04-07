// Imports
import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

const router = new Router({
  mode: "history",
  base: process.env.BASE_URL,
  scrollBehavior: (to, from, savedPosition) => {
    if (to.hash) return { selector: to.hash };
    if (savedPosition) return savedPosition;

    return { x: 0, y: 0 };
  },
  routes: [
    {
      path: "/sign-up",
      name: "Sign Up",
      component: () => import("@/views/SignUp.vue")
    },
    {
      path: "/sign-in",
      name: "Sign In",
      component: () => import("@/views/SignIn.vue")
    },
    {
      path: "/",
      name: "Home",
      component: () => import("@/views/Landing.vue")
    },
    {
      path: "/profile",
      name: "Profile",
      component: () => import("@/views/ViewProfile.vue")
    },
  ]
});
router.beforeEach((to, from, next) => {
  
  document.title = `${to.name} - ${process.env.VUE_APP_TITLE}`
  next()
})
export default router;
