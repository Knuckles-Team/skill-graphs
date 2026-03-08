[Skip to content](https://mui.com/material-ui/guides/building-extensible-themes/#main-content)
[](https://mui.com/)
Search…`Ctrl+K`3
# Building extensible themes
Learn how to build extensible themes with Material UI.
![ads via Carbon](https://cnv.event.prod.bidr.io/log/cnv?tag_id=3503&buzz_key=dsp&value=&account_id=79&order=\[ORDER\]&ord=\[CACHEBUSTER\])![ads via Carbon](https://segment.prod.bidr.io/associate-segment?buzz_key=dsp&segment_key=dsp-19102)![ads via Carbon](https://secure.adnxs.com/px?id=1777282&t=2)![ads via Carbon](https://secure.adnxs.com/seg?add=37012073&t=2)![ads via Carbon](https://insight.adsrvr.org/track/pxl/?adv=t3k9qrj&ct=0:djrfa1z&fmt=3&orderid=&v=)![ads via Carbon](https://ad.double-click.net/ddm/activity/src=15643656;type=sales;cat=408690;qty=1;cost=\[Revenue\];dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;npa=;gdpr=$;gdpr_consent=$;ord=\[OrderID\])![ads via Carbon](https://sp.analytics.yahoo.com/spp.pl?a=10000&.yp=10207075&he=&hph=&gv=\[ORDER_VALUE\]&orderId=\[ORDER_ID\]&ec=\[EVENT_CATEGORY\]&ea=fire&el=\[EVENT_LABEL\])
## [Introduction](https://mui.com/material-ui/guides/building-extensible-themes/#introduction)
This guide describes recommendations for building a brand-specific theme with Material UI that can be easily extended and customized across multiple apps that consume it.
## [Branded theme](https://mui.com/material-ui/guides/building-extensible-themes/#branded-theme)
This is the source of truth for the brand-specific theme. It represents the brand's visual identity through colors, typography, spacing, and more.
In general, it's recommended to export tokens, components, and the branded theme from a file, as shown here:
brandedTheme.ts
```
import { createTheme } from '@mui/material/styles';
import type { ThemeOptions } from '@mui/material/styles';

export const brandedTokens: ThemeOptions = {
  palette: {
    primary: {
      main: '#000000',
    },
    secondary: {
      main: 'rgb(229, 229, 234)',
    },
  },
  shape: {
    borderRadius: 4,
  },
  typography: {
    fontFamily:
      'var(--font-primary, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif)',
  },
};

export const brandedComponents: ThemeOptions['components'] = {
  MuiButton: {
    defaultProps: {
      disableElevation: true,
    },
    styleOverrides: {
      root: {
        minWidth: 'unset',
        textTransform: 'capitalize',
        '&:hover': {
          textDecoration: 'underline',
        },
      },
    },
  },
};

const brandedTheme = createTheme({
  ...brandedTokens,
  components: brandedComponents,
});

export default brandedTheme;

```
CopyCopied(or Ctrl + C)
For a more optimized approach, you can split the branded components into multiple files. This way, consumers of the theme can choose to import only what they need at the application level.
brandedButtons.ts
```
import type { ThemeOptions } from "@mui/material/styles";

export const buttonTheme: ThemeOptions["components"] = {
  MuiButtonBase: {},
  MuiButton: {},
  MuiIconButton: {},
};

```
CopyCopied(or Ctrl + C)
brandedTheme.ts
```
import { buttonTheme } from './brandedButtons';
// import other branded components as needed

export const brandedTokens: ThemeOptions = {}

export default createTheme({
  ...brandedTokens,
  components: {
    ...buttonTheme,
    // other branded components
  },
});

```
CopyCopied(or Ctrl + C)
## [Application theme](https://mui.com/material-ui/guides/building-extensible-themes/#application-theme)
Consumers of the branded theme may choose to use it directly in their applications, or extend it to better suit their specific use cases. Using the branded button as an example, a consumer could customize its hover styles as shown below:
appTheme.ts
```
import { createTheme } from '@mui/material/styles';
import { brandedTokens, brandedComponents } from './brandedTheme'; // or from an npm package.

const appTheme = createTheme({
  ...brandedTokens,
  palette: {
    ...brandedTokens.palette,
    primary: {
      main: '#1976d2',
    },
  },
  components: {
    ...brandedComponents,
    MuiButton: {
      styleOverrides: {
        root: [
          // Use array syntax to preserve the branded theme styles.
          brandedComponents?.MuiButton?.styleOverrides?.root,
          {
            '&:hover': {
              transform: 'translateY(-2px)',
            },
          },
        ],
      },
    },
  },
});

```
CopyCopied(or Ctrl + C)
### [Merging branded theme](https://mui.com/material-ui/guides/building-extensible-themes/#merging-branded-theme)
When merging the branded theme with the application theme, it's recommended to use the object spread syntax for tokens like palette, typography, and shape.
For components, use the array syntax to ensure that the [variants](https://mui.com/material-ui/customization/theme-components/#variants), states, and pseudo-class styles from the branded theme are preserved.
We don't recommend JavaScript functions or any utilities to do a deep merge between the branded and the application theme.
Doing so will introduce performance overhead on the first render of the application. The impact depends on the size of the themes.
## [Full example](https://mui.com/material-ui/guides/building-extensible-themes/#full-example)
Branded ButtonApp ButtonApp 2 Button
JSTS
Collapse code
Copy(or Ctrl + C)
```
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import { ThemeProvider, createTheme, type ThemeOptions } from '@mui/material/styles';

/**
 * Branded theme: you might want to export this as a separate file
 */
const brandedTokens: ThemeOptions = {
  palette: {
    primary: {
      main: '#000000',
    },
    secondary: {
      main: 'rgb(229, 229, 234)',
    },
  },
  shape: {
    borderRadius: 4,
  },
  typography: {
    fontFamily:
      'var(--font-primary, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif)',
  },
  shadows: [
    'none',
    '0 1px 2px 0 rgb(0 0 0 / 0.05)',
    '0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1)',
    '0 2px 4px 0 rgb(0 0 0 / 0.06)',
    '0 2px 4px -1px rgb(0 0 0 / 0.06), 0 1px 2px -1px rgb(0 0 0 / 0.04)',
    '0 3px 5px -1px rgb(0 0 0 / 0.07), 0 1px 3px -1px rgb(0 0 0 / 0.05)',
    '0 4px 6px -1px rgb(0 0 0 / 0.07), 0 2px 4px -1px rgb(0 0 0 / 0.05)',
    '0 5px 8px -2px rgb(0 0 0 / 0.08), 0 2px 4px -1px rgb(0 0 0 / 0.05)',
    '0 6px 10px -2px rgb(0 0 0 / 0.08), 0 3px 5px -2px rgb(0 0 0 / 0.06)',
    '0 8px 12px -3px rgb(0 0 0 / 0.09), 0 3px 6px -2px rgb(0 0 0 / 0.06)',
    '0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 7px -3px rgb(0 0 0 / 0.07)',
    '0 12px 18px -4px rgb(0 0 0 / 0.11), 0 5px 9px -3px rgb(0 0 0 / 0.08)',
    '0 15px 22px -4px rgb(0 0 0 / 0.12), 0 6px 11px -4px rgb(0 0 0 / 0.09)',
    '0 18px 28px -5px rgb(0 0 0 / 0.13), 0 7px 13px -4px rgb(0 0 0 / 0.1)',
    '0 22px 34px -6px rgb(0 0 0 / 0.14), 0 8px 16px -5px rgb(0 0 0 / 0.11)',
    '0 26px 40px -7px rgb(0 0 0 / 0.15), 0 10px 19px -5px rgb(0 0 0 / 0.12)',
    '0 31px 47px -8px rgb(0 0 0 / 0.16), 0 12px 23px -6px rgb(0 0 0 / 0.13)',
    '0 36px 54px -9px rgb(0 0 0 / 0.17), 0 14px 27px -7px rgb(0 0 0 / 0.14)',
    '0 42px 62px -10px rgb(0 0 0 / 0.18), 0 16px 31px -8px rgb(0 0 0 / 0.15)',
    '0 48px 70px -11px rgb(0 0 0 / 0.2), 0 18px 36px -9px rgb(0 0 0 / 0.16)',
    '0 54px 78px -12px rgb(0 0 0 / 0.21), 0 20px 41px -10px rgb(0 0 0 / 0.17)',
    '0 60px 86px -13px rgb(0 0 0 / 0.22), 0 23px 46px -11px rgb(0 0 0 / 0.18)',
    '0 66px 94px -14px rgb(0 0 0 / 0.23), 0 26px 52px -12px rgb(0 0 0 / 0.19)',
    '0 72px 102px -15px rgb(0 0 0 / 0.24), 0 29px 58px -13px rgb(0 0 0 / 0.2)',
    '0 58px 82px -11px rgb(0 0 0 / 0.26), 0 21px 40px -11px rgb(0 0 0 / 0.22)',
  ],
};

const brandedComponents: ThemeOptions['components'] = {
  MuiButton: {
    defaultProps: {
      disableElevation: true,
    },
    styleOverrides: {
      root: ({ theme }) => ({
        minWidth: 'unset',
        textTransform: 'capitalize',
        fontSize: '1rem',
        '&:hover': {
          textDecoration: 'underline',
        },
        [theme.breakpoints.up('md')]: {
          fontSize: '0.875rem',
        },
      }),
    },
  },
};

const brandedTheme = createTheme({
  ...brandedTokens,
  components: brandedComponents,
});

/**
 * Application theme
 */
const appTheme = createTheme({
  ...brandedTokens,
  palette: {
    ...brandedTokens.palette,
    primary: {
      main: '#1976d2',
    },
  },
  components: {
    ...brandedComponents,
    MuiButton: {
      styleOverrides: {
        root: [
          brandedComponents?.MuiButton?.styleOverrides?.root,
          {
            transition: 'transform 0.2s ease-in-out',
            '&:hover': {
              transform: 'translateY(-2px)',
            },
          },
        ],
      },
    },
  },
});

function App1() {
  return (
    <ThemeProvider theme={appTheme}>
      <Button>App Button</Button>
    </ThemeProvider>
  );
}

const appTheme2 = createTheme({
  ...brandedTokens,
  palette: {
    ...brandedTokens.palette,
    primary: {
      main: '#ffa726',
    },
  },
  components: {
    ...brandedComponents,
    MuiButton: {
      defaultProps: {
        ...brandedComponents?.MuiButton?.defaultProps,
        variant: 'outlined',
      },
      styleOverrides: {
        root: [
          brandedComponents?.MuiButton?.styleOverrides?.root,
          ({ theme }) => ({
            color: theme.palette.primary.dark,
          }),
        ],
      },
    },
  },
});

function App2() {
  return (
    <ThemeProvider theme={appTheme2}>
      <Button>App 2 Button</Button>
    </ThemeProvider>
  );
}

export default function ExtensibleThemes() {
  return (
    <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
      <ThemeProvider theme={brandedTheme}>
        <Button>Branded Button</Button>
      </ThemeProvider>
      <App1 />
      <App2 />
    </Box>
  );
}

```
import Box from '@mui/material/Box'; import Button from '@mui/material/Button'; import { ThemeProvider, createTheme, type ThemeOptions } from '@mui/material/styles'; /** * Branded theme: you might want to export this as a separate file */ const brandedTokens: ThemeOptions = { palette: { primary: { main: '#000000', }, secondary: { main: 'rgb(229, 229, 234)', }, }, shape: { borderRadius: 4, }, typography: { fontFamily: 'var(--font-primary, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif)', }, shadows: [ 'none', '0 1px 2px 0 rgb(0 0 0 / 0.05)', '0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1)', '0 2px 4px 0 rgb(0 0 0 / 0.06)', '0 2px 4px -1px rgb(0 0 0 / 0.06), 0 1px 2px -1px rgb(0 0 0 / 0.04)', '0 3px 5px -1px rgb(0 0 0 / 0.07), 0 1px 3px -1px rgb(0 0 0 / 0.05)', '0 4px 6px -1px rgb(0 0 0 / 0.07), 0 2px 4px -1px rgb(0 0 0 / 0.05)', '0 5px 8px -2px rgb(0 0 0 / 0.08), 0 2px 4px -1px rgb(0 0 0 / 0.05)', '0 6px 10px -2px rgb(0 0 0 / 0.08), 0 3px 5px -2px rgb(0 0 0 / 0.06)', '0 8px 12px -3px rgb(0 0 0 / 0.09), 0 3px 6px -2px rgb(0 0 0 / 0.06)', '0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 7px -3px rgb(0 0 0 / 0.07)', '0 12px 18px -4px rgb(0 0 0 / 0.11), 0 5px 9px -3px rgb(0 0 0 / 0.08)', '0 15px 22px -4px rgb(0 0 0 / 0.12), 0 6px 11px -4px rgb(0 0 0 / 0.09)', '0 18px 28px -5px rgb(0 0 0 / 0.13), 0 7px 13px -4px rgb(0 0 0 / 0.1)', '0 22px 34px -6px rgb(0 0 0 / 0.14), 0 8px 16px -5px rgb(0 0 0 / 0.11)', '0 26px 40px -7px rgb(0 0 0 / 0.15), 0 10px 19px -5px rgb(0 0 0 / 0.12)', '0 31px 47px -8px rgb(0 0 0 / 0.16), 0 12px 23px -6px rgb(0 0 0 / 0.13)', '0 36px 54px -9px rgb(0 0 0 / 0.17), 0 14px 27px -7px rgb(0 0 0 / 0.14)', '0 42px 62px -10px rgb(0 0 0 / 0.18), 0 16px 31px -8px rgb(0 0 0 / 0.15)', '0 48px 70px -11px rgb(0 0 0 / 0.2), 0 18px 36px -9px rgb(0 0 0 / 0.16)', '0 54px 78px -12px rgb(0 0 0 / 0.21), 0 20px 41px -10px rgb(0 0 0 / 0.17)', '0 60px 86px -13px rgb(0 0 0 / 0.22), 0 23px 46px -11px rgb(0 0 0 / 0.18)', '0 66px 94px -14px rgb(0 0 0 / 0.23), 0 26px 52px -12px rgb(0 0 0 / 0.19)', '0 72px 102px -15px rgb(0 0 0 / 0.24), 0 29px 58px -13px rgb(0 0 0 / 0.2)', '0 58px 82px -11px rgb(0 0 0 / 0.26), 0 21px 40px -11px rgb(0 0 0 / 0.22)', ], }; const brandedComponents: ThemeOptions['components'] = { MuiButton: { defaultProps: { disableElevation: true, }, styleOverrides: { root: ({ theme }) => ({ minWidth: 'unset', textTransform: 'capitalize', fontSize: '1rem', '&:hover': { textDecoration: 'underline', }, [theme.breakpoints.up('md')]: { fontSize: '0.875rem', }, }), }, }, }; const brandedTheme = createTheme({ ...brandedTokens, components: brandedComponents, }); /** * Application theme */ const appTheme = createTheme({ ...brandedTokens, palette: { ...brandedTokens.palette, primary: { main: '#1976d2', }, }, components: { ...brandedComponents, MuiButton: { styleOverrides: { root: [ brandedComponents?.MuiButton?.styleOverrides?.root, { transition: 'transform 0.2s ease-in-out', '&:hover': { transform: 'translateY(-2px)', }, }, ], }, }, }, }); function App1() { return ( <ThemeProvider theme={appTheme}> <Button>App Button</Button> </ThemeProvider> ); } const appTheme2 = createTheme({ ...brandedTokens, palette: { ...brandedTokens.palette, primary: { main: '#ffa726', }, }, components: { ...brandedComponents, MuiButton: { defaultProps: { ...brandedComponents?.MuiButton?.defaultProps, variant: 'outlined', }, styleOverrides: { root: [ brandedComponents?.MuiButton?.styleOverrides?.root, ({ theme }) => ({ color: theme.palette.primary.dark, }), ], }, }, }, }); function App2() { return ( <ThemeProvider theme={appTheme2}> <Button>App 2 Button</Button> </ThemeProvider> ); } export default function ExtensibleThemes() { return ( <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}> <ThemeProvider theme={brandedTheme}> <Button>Branded Button</Button> </ThemeProvider> <App1 /> <App2 /> </Box> ); }
Press `Enter` to start editing
Was this page helpful?
* * *
[](https://mui.com/material-ui/customization/css-layers/)[Minimizing bundle size](https://mui.com/material-ui/guides/minimizing-bundle-size/)
* * *
[](https://mui.com/)
•
[Blog ](https://mui.com/blog/)
•
[Store ](https://mui.com/store/)
[](https://mui.com/r/discord/ "Discord")[](https://mui.com/feed/blog/rss.xml "RSS Feed")
Contents
  * [Introduction](https://mui.com/material-ui/guides/building-extensible-themes/#introduction)
  * [Branded theme](https://mui.com/material-ui/guides/building-extensible-themes/#branded-theme)
  * [Application theme](https://mui.com/material-ui/guides/building-extensible-themes/#application-theme)
    * [Merging branded theme](https://mui.com/material-ui/guides/building-extensible-themes/#merging-branded-theme)
  * [Full example](https://mui.com/material-ui/guides/building-extensible-themes/#full-example)


[Become a Diamond sponsor](https://mui.com/material-ui/discover-more/backers/#diamond-sponsors)
###### Cookie Preferences
We use cookies to understand site usage and improve our content. This includes third-party analytics.
Allow analyticsEssential only
[](https://mui.com/)
Material UIv7.3.9
  * [](https://mui.com/material-ui/getting-started/)
  * [](https://mui.com/material-ui/all-components/)
  * [](https://mui.com/material-ui/api/accordion/)
  * [](https://mui.com/material-ui/customization/how-to-customize/)
  * [](https://mui.com/material-ui/guides/building-extensible-themes/)
    * [Building extensible themes](https://mui.com/material-ui/guides/building-extensible-themes/)
    * [Minimizing bundle size](https://mui.com/material-ui/guides/minimizing-bundle-size/)
    * [Server rendering](https://mui.com/material-ui/guides/server-rendering/)
    * [Responsive UI](https://mui.com/material-ui/guides/responsive-ui/)
    * [Testing](https://mui.com/material-ui/guides/testing/)
    * [Localization](https://mui.com/material-ui/guides/localization/)
    * [API design approach](https://mui.com/material-ui/guides/api/)
    * [TypeScript](https://mui.com/material-ui/guides/typescript/)
    * [Composition](https://mui.com/material-ui/guides/composition/)
    * [Content Security Policy](https://mui.com/material-ui/guides/content-security-policy/)
  * [](https://mui.com/material-ui/integrations/tailwindcss/tailwindcss-v4/)
  * [](https://mui.com/material-ui/experimental-api/classname-generator/)
  * [](https://mui.com/material-ui/migration/upgrade-to-grid-v2/)
  * [](https://mui.com/material-ui/discover-more/showcase/)
  * [](https://mui.com/material-ui/design-resources/material-ui-for-figma/)
  * [](https://mui.com/store/%3Futm_source=docs&utm_medium=referral&utm_campaign=sidenav/)
