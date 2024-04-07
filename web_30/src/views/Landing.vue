<template>
  <v-app>
      <navigation />
      <home />
  </v-app>
</template>

<script>
import navigation from "@/views/landingComponents/Navigation";
import home from "@/views/landingComponents/Home";

export default {
    components: {
        navigation,
        home
    },
    
}
</script>

<style>

</style>