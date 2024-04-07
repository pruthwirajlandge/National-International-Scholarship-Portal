<template>
  <div>
      <p class="text-sm grey--text text--darken-2 px-5 pt-6">DASHBOARD</p>
        <router-link to="/" class="dashboard-nav-link px-4">
            <div class="d-flex align-center">
                <img v-svg-inline class="icon mr-2" src="@/assets/images/icons/home.svg" />
                <span>Home</span>
            </div>
        </router-link>
        
        <p class="text-sm grey--text text--darken-2 px-5 pt-6">ADMIN SETTINGS</p>
        <a href="http://192.168.0.50:8000/admin/" target="_blank" class="dashboard-nav-link px-4">
            <div class="d-flex align-center">
                <img v-svg-inline class="icon mr-2" src="@/assets/images/icons/user.svg" />
                <span>Admin</span>
            </div>
        </a>
  </div>
</template>

<script>

</script>

<style lang="scss">
    .dashboard-nav-link {
        color: rgb(125, 135, 156) !important;
        text-decoration: none;
        align-items: center;
        display: flex;
        justify-content: space-between;
        border-left: 4px solid #fff;
        margin-bottom: 20px;
        svg {
            width: 20px;
        }
        &.router-link-exact-active {
            color: #D23F57 !important;
            border-left: 4px solid #D23F57;
        }
        &:hover {
            color: #D23F57 !important;
            border-left: 4px solid #D23F57;
        }
    }
</style>