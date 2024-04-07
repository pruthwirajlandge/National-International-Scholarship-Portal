export const themeConfig = {
  disableCustomizer: false,
  rtl: false,
  verticalSidebarMini: false,
  verticalSidebarDrawer: true,
  verticalCompactSidebarDrawer: true,
  verticalSaasSidebarDrawer: true,
  showBreadcrumb: true,

  layout: "VerticalSidebar",
  isLoading: false,

  isDark: false,
  verticalSidebarDrawerColor: "dark",
  appBarColor: "white"
};

export const themePreset = {
  breakpoint: {
    thresholds: {
      xs: 340,
      sm: 540,
      md: 960,
      lg: 1600
    },
    scrollBarWidth: 10
  },
  rtl: false,

  theme: {
    dark: themeConfig.isDark,

    default: "light",
    disable: false,
    options: {
      cspNonce: undefined,
      customProperties: true,
      minifyTheme: undefined,
      themeCache: undefined
    },
    themes: {
      light: {
        primary: "#D23F57",
        secondary: "#0F3460",
        success: "#33D067",
        danger: "#FF5353",
        warning: "#FFCD4E",
        warning: "#FF8A48",
        info: "#5e5ce6",
        dark: "#242939",
        black: "#242939",
        background: "#f2f3f8",
        color: "#0F3460",
        grey: "#AEB4BE",
        accent1: '#84CEEB',
        accent2: '#54B9EA',
        accent3: '#C1C8E4',
        accent4: '#8860D0',
      },
      dark: {
        primary: "#5680E9",
        secondary: "#D83F87",
        success: "#33D067",
        danger: "#FF5353",
        warning: "#FFCD4E",
        info: "#5e5ce6",
        warning: "#FF8A48",
        color: "#fff",
        grey: "#AEB4BE",
        accent1: '#84CEEB',
        accent2: '#54B9EA',
        accent3: '#C1C8E4',
        accent4: '#8860D0',
      }
    }
  }
};
