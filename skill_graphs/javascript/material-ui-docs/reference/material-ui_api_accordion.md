[Skip to content](https://mui.com/material-ui/api/accordion/#main-content)[Skip to content](https://mui.com/material-ui/api/accordion/#main-content)
[](https://mui.com/)
Search…`Ctrl+K`3
# Accordion API
API reference docs for the React Accordion component. Learn about the props, CSS, and other APIs of this exported module.
## [Demos](https://mui.com/material-ui/api/accordion/#demos)
For examples and details on the usage of this React component, visit the component demo pages:
  * [Accordion](https://mui.com/material-ui/react-accordion/)


## [Import](https://mui.com/material-ui/api/accordion/#import)
Copy(or Ctrl + C)
```
import Accordion from '@mui/material/Accordion';
// or
import { Accordion } from '@mui/material';
```

Learn about the difference by [reading this guide on minimizing bundle size](https://mui.com/material-ui/guides/minimizing-bundle-size/).
## [Props](https://mui.com/material-ui/api/accordion/#props)
View:table
Props of the [Paper](https://mui.com/material-ui/api/paper/) component are also available.
Name | Type | Default | Description
---|---|---|---
children* | node | - | The content of the component.
classes | object | - |  Override or extend the styles applied to the component. See [CSS classes API](https://mui.com/material-ui/api/accordion/#classes) below for more details.
defaultExpanded | bool | false | If `true`, expands the accordion by default.
disabled | bool | false | If `true`, the component is disabled.
disableGutters | bool | false | If `true`, it removes the margin between two expanded accordion items and prevents the increased height when expanded.
expanded | bool | - | If `true`, expands the accordion, otherwise collapses it. Setting this prop enables control over the accordion.
onChange | func | - |  Callback fired when the expand/collapse state is changed. Signature:`function(event: React.SyntheticEvent, expanded: boolean) => void`
  * `event` The event source of the callback. **Warning** : This is a generic event not a change event.
  * `expanded` The `expanded` state of the accordion.


slotProps | { heading?: func
| object, region?: func
| object, root?: func
| object, transition?: func
| object } | {} | The props used for each slot inside.
slots | { heading?: elementType, region?: elementType, root?: elementType, transition?: elementType } | {} | The components used for each slot inside.
sx | Array<func
| object
| bool>
| func
| object | - |  The system prop that allows defining system overrides as well as additional CSS styles. See the [`sx` page](https://mui.com/system/getting-started/the-sx-prop/) for more details.
TransitionComponent | elementType | - |  The component used for the transition. [Follow this guide](https://mui.com/material-ui/transitions/#transitioncomponent-prop) to learn more about the requirements for this component. **Deprecated** －Use `slots.transition` instead. This prop will be removed in a future major release. See [Migrating from deprecated APIs](https://mui.com/material-ui/migration/migrating-from-deprecated-apis/) for more details.
TransitionProps | object | - |  Props applied to the transition element. By default, the element is based on this  **Deprecated** －Use `slotProps.transition` instead. This prop will be removed in a future major release. See [Migrating from deprecated APIs](https://mui.com/material-ui/migration/migrating-from-deprecated-apis/) for more details.
The `ref` is forwarded to the root element.
### [Inheritance](https://mui.com/material-ui/api/accordion/#inheritance)
While not explicitly documented above, the props of the [Paper](https://mui.com/material-ui/api/paper/) component are also available in Accordion. You can take advantage of this to [target nested components](https://mui.com/material-ui/guides/api/#spread).
### [Theme default props](https://mui.com/material-ui/api/accordion/#theme-default-props)
You can use `MuiAccordion` to change the default props of this component [with the theme](https://mui.com/material-ui/customization/theme-components/#theme-default-props).
## [Slots](https://mui.com/material-ui/api/accordion/#slots)
View:table
Slot name | Class name | Default component | Description
---|---|---|---
root | .MuiAccordion-root | `Paper` | The component that renders the root.
heading | .MuiAccordion-heading | `'h3'` | The component that renders the heading.
transition |  | `Collapse` | The component that renders the transition. [Follow this guide](https://mui.com/material-ui/transitions/#transitioncomponent-prop) to learn more about the requirements for this component.
region | .MuiAccordion-region | `'div'` | The component that renders the region.
## [CSS classes](https://mui.com/material-ui/api/accordion/#classes)
View:table
These class names are useful for styling with CSS. They are applied to the component's slots when specific states are triggered.
Class name | Rule name | Description
---|---|---
.Mui-disabled |  | State class applied to the root element if `disabled={true}`.
.Mui-expanded |  | State class applied to the root element if `expanded={true}`.
.MuiAccordion-gutters | gutters | Styles applied to the root element unless `disableGutters={true}`.
.MuiAccordion-rounded | rounded | Styles applied to the root element unless `square={true}`.


You can override the style of the component using one of these customization options:
  * With a [global class name](https://mui.com/material-ui/integrations/interoperability/#global-css).
  * With a rule name as part of the component's [`styleOverrides` property](https://mui.com/material-ui/customization/theme-components/#theme-style-overrides) in a custom theme.


## [Source code](https://mui.com/material-ui/api/accordion/#source-code)
If you did not find the information in this page, consider having a look at the
Was this page helpful?
* * *
[](https://mui.com/material-ui/react-timeline/)[AccordionActions](https://mui.com/material-ui/api/accordion-actions/)
* * *
[](https://mui.com/)
•
[Blog ](https://mui.com/blog/)
•
[Store ](https://mui.com/store/)
[](https://mui.com/r/discord/ "Discord")[](https://mui.com/feed/blog/rss.xml "RSS Feed")
Contents
  * [Demos](https://mui.com/material-ui/api/accordion/#demos)
  * [Import](https://mui.com/material-ui/api/accordion/#import)
  * [Props](https://mui.com/material-ui/api/accordion/#props)
    * [children](https://mui.com/material-ui/api/accordion/#accordion-prop-children)
    * [classes](https://mui.com/material-ui/api/accordion/#accordion-prop-classes)
    * [defaultExpanded](https://mui.com/material-ui/api/accordion/#accordion-prop-defaultExpanded)
    * [disabled](https://mui.com/material-ui/api/accordion/#accordion-prop-disabled)
    * [disableGutters](https://mui.com/material-ui/api/accordion/#accordion-prop-disableGutters)
    * [expanded](https://mui.com/material-ui/api/accordion/#accordion-prop-expanded)
    * [onChange](https://mui.com/material-ui/api/accordion/#accordion-prop-onChange)
    * [slotProps](https://mui.com/material-ui/api/accordion/#accordion-prop-slotProps)
    * [slots](https://mui.com/material-ui/api/accordion/#accordion-prop-slots)
    * [sx](https://mui.com/material-ui/api/accordion/#accordion-prop-sx)
    * [TransitionComponent](https://mui.com/material-ui/api/accordion/#accordion-prop-TransitionComponent)
    * [TransitionProps](https://mui.com/material-ui/api/accordion/#accordion-prop-TransitionProps)
  * [Slots](https://mui.com/material-ui/api/accordion/#slots)
    * [root](https://mui.com/material-ui/api/accordion/#Accordion-css-MuiAccordion-root)
    * [heading](https://mui.com/material-ui/api/accordion/#Accordion-css-MuiAccordion-heading)
    * [transition](https://mui.com/material-ui/api/accordion/#Accordion-css-transition)
    * [region](https://mui.com/material-ui/api/accordion/#Accordion-css-MuiAccordion-region)
  * [CSS classes](https://mui.com/material-ui/api/accordion/#classes)
    * [disabled](https://mui.com/material-ui/api/accordion/#accordion-classes-Mui-disabled)
    * [expanded](https://mui.com/material-ui/api/accordion/#accordion-classes-Mui-expanded)
    * [gutters](https://mui.com/material-ui/api/accordion/#accordion-classes-MuiAccordion-gutters)
    * [rounded](https://mui.com/material-ui/api/accordion/#accordion-classes-MuiAccordion-rounded)
  * [Source code](https://mui.com/material-ui/api/accordion/#source-code)


[Become a Diamond sponsor](https://mui.com/material-ui/discover-more/backers/#diamond-sponsors)
###### Cookie Preferences
We use cookies to understand site usage and improve our content. This includes third-party analytics.
Allow analyticsEssential only
[](https://mui.com/)
Material UIv7.3.9
  * [](https://mui.com/material-ui/getting-started/)
  * [](https://mui.com/material-ui/all-components/)
  * [](https://mui.com/material-ui/api/accordion/)
    * [Accordion](https://mui.com/material-ui/api/accordion/)
    * [AccordionActions](https://mui.com/material-ui/api/accordion-actions/)
    * [AccordionDetails](https://mui.com/material-ui/api/accordion-details/)
    * [AccordionSummary](https://mui.com/material-ui/api/accordion-summary/)
    * [Alert](https://mui.com/material-ui/api/alert/)
    * [AlertTitle](https://mui.com/material-ui/api/alert-title/)
    * [AppBar](https://mui.com/material-ui/api/app-bar/)
    * [Autocomplete](https://mui.com/material-ui/api/autocomplete/)
    * [Avatar](https://mui.com/material-ui/api/avatar/)
    * [AvatarGroup](https://mui.com/material-ui/api/avatar-group/)
    * [Backdrop](https://mui.com/material-ui/api/backdrop/)
    * [Badge](https://mui.com/material-ui/api/badge/)
    * [BottomNavigation](https://mui.com/material-ui/api/bottom-navigation/)
    * [BottomNavigationAction](https://mui.com/material-ui/api/bottom-navigation-action/)
    * [Box](https://mui.com/material-ui/api/box/)
    * [Breadcrumbs](https://mui.com/material-ui/api/breadcrumbs/)
    * [Button](https://mui.com/material-ui/api/button/)
    * [ButtonBase](https://mui.com/material-ui/api/button-base/)
    * [ButtonGroup](https://mui.com/material-ui/api/button-group/)
    * [Card](https://mui.com/material-ui/api/card/)
    * [CardActionArea](https://mui.com/material-ui/api/card-action-area/)
    * [CardActions](https://mui.com/material-ui/api/card-actions/)
    * [CardContent](https://mui.com/material-ui/api/card-content/)
    * [CardHeader](https://mui.com/material-ui/api/card-header/)
    * [CardMedia](https://mui.com/material-ui/api/card-media/)
    * [Checkbox](https://mui.com/material-ui/api/checkbox/)
    * [Chip](https://mui.com/material-ui/api/chip/)
    * [CircularProgress](https://mui.com/material-ui/api/circular-progress/)
    * [ClickAwayListener](https://mui.com/material-ui/api/click-away-listener/)
    * [Collapse](https://mui.com/material-ui/api/collapse/)
    * [Container](https://mui.com/material-ui/api/container/)
    * [CssBaseline](https://mui.com/material-ui/api/css-baseline/)
    * [Dialog](https://mui.com/material-ui/api/dialog/)
    * [DialogActions](https://mui.com/material-ui/api/dialog-actions/)
    * [DialogContent](https://mui.com/material-ui/api/dialog-content/)
    * [DialogContentText](https://mui.com/material-ui/api/dialog-content-text/)
    * [DialogTitle](https://mui.com/material-ui/api/dialog-title/)
    * [Divider](https://mui.com/material-ui/api/divider/)
    * [Drawer](https://mui.com/material-ui/api/drawer/)
    * [Fab](https://mui.com/material-ui/api/fab/)
    * [Fade](https://mui.com/material-ui/api/fade/)
    * [FilledInput](https://mui.com/material-ui/api/filled-input/)
    * [FormControl](https://mui.com/material-ui/api/form-control/)
    * [FormControlLabel](https://mui.com/material-ui/api/form-control-label/)
    * [FormGroup](https://mui.com/material-ui/api/form-group/)
    * [FormHelperText](https://mui.com/material-ui/api/form-helper-text/)
    * [FormLabel](https://mui.com/material-ui/api/form-label/)
    * [GlobalStyles](https://mui.com/material-ui/api/global-styles/)
    * [Grid](https://mui.com/material-ui/api/grid/)
    * [GridLegacy](https://mui.com/material-ui/api/grid-legacy/)
    * [Grow](https://mui.com/material-ui/api/grow/)
    * [Icon](https://mui.com/material-ui/api/icon/)
    * [IconButton](https://mui.com/material-ui/api/icon-button/)
    * [ImageList](https://mui.com/material-ui/api/image-list/)
    * [ImageListItem](https://mui.com/material-ui/api/image-list-item/)
    * [ImageListItemBar](https://mui.com/material-ui/api/image-list-item-bar/)
    * [InitColorSchemeScript](https://mui.com/material-ui/api/init-color-scheme-script/)
    * [Input](https://mui.com/material-ui/api/input/)
    * [InputAdornment](https://mui.com/material-ui/api/input-adornment/)
    * [InputBase](https://mui.com/material-ui/api/input-base/)
    * [InputLabel](https://mui.com/material-ui/api/input-label/)
    * [LinearProgress](https://mui.com/material-ui/api/linear-progress/)
    * [Link](https://mui.com/material-ui/api/link/)
    * [List](https://mui.com/material-ui/api/list/)
    * [ListItem](https://mui.com/material-ui/api/list-item/)
    * [ListItemAvatar](https://mui.com/material-ui/api/list-item-avatar/)
    * [ListItemButton](https://mui.com/material-ui/api/list-item-button/)
    * [ListItemIcon](https://mui.com/material-ui/api/list-item-icon/)
    * [ListItemSecondaryAction](https://mui.com/material-ui/api/list-item-secondary-action/)
    * [ListItemText](https://mui.com/material-ui/api/list-item-text/)
    * [ListSubheader](https://mui.com/material-ui/api/list-subheader/)
    * [Masonry](https://mui.com/material-ui/api/masonry/)
    * [Menu](https://mui.com/material-ui/api/menu/)
    * [MenuItem](https://mui.com/material-ui/api/menu-item/)
    * [MenuList](https://mui.com/material-ui/api/menu-list/)
    * [MobileStepper](https://mui.com/material-ui/api/mobile-stepper/)
    * [Modal](https://mui.com/material-ui/api/modal/)
    * [NativeSelect](https://mui.com/material-ui/api/native-select/)
    * [NoSsr](https://mui.com/material-ui/api/no-ssr/)
    * [OutlinedInput](https://mui.com/material-ui/api/outlined-input/)
    * [Pagination](https://mui.com/material-ui/api/pagination/)
    * [PaginationItem](https://mui.com/material-ui/api/pagination-item/)
    * [Paper](https://mui.com/material-ui/api/paper/)
    * [PigmentContainer](https://mui.com/material-ui/api/pigment-container/)
    * [PigmentGrid](https://mui.com/material-ui/api/pigment-grid/)
    * [PigmentStack](https://mui.com/material-ui/api/pigment-stack/)
    * [Popover](https://mui.com/material-ui/api/popover/)
    * [Popper](https://mui.com/material-ui/api/popper/)
    * [Portal](https://mui.com/material-ui/api/portal/)
    * [Radio](https://mui.com/material-ui/api/radio/)
    * [RadioGroup](https://mui.com/material-ui/api/radio-group/)
    * [Rating](https://mui.com/material-ui/api/rating/)
    * [ScopedCssBaseline](https://mui.com/material-ui/api/scoped-css-baseline/)
    * [Select](https://mui.com/material-ui/api/select/)
    * [Skeleton](https://mui.com/material-ui/api/skeleton/)
    * [Slide](https://mui.com/material-ui/api/slide/)
    * [Slider](https://mui.com/material-ui/api/slider/)
    * [Snackbar](https://mui.com/material-ui/api/snackbar/)
    * [SnackbarContent](https://mui.com/material-ui/api/snackbar-content/)
    * [SpeedDial](https://mui.com/material-ui/api/speed-dial/)
    * [SpeedDialAction](https://mui.com/material-ui/api/speed-dial-action/)
    * [SpeedDialIcon](https://mui.com/material-ui/api/speed-dial-icon/)
    * [Stack](https://mui.com/material-ui/api/stack/)
    * [Step](https://mui.com/material-ui/api/step/)
    * [StepButton](https://mui.com/material-ui/api/step-button/)
    * [StepConnector](https://mui.com/material-ui/api/step-connector/)
    * [StepContent](https://mui.com/material-ui/api/step-content/)
    * [StepIcon](https://mui.com/material-ui/api/step-icon/)
    * [StepLabel](https://mui.com/material-ui/api/step-label/)
    * [Stepper](https://mui.com/material-ui/api/stepper/)
    * [SvgIcon](https://mui.com/material-ui/api/svg-icon/)
    * [SwipeableDrawer](https://mui.com/material-ui/api/swipeable-drawer/)
    * [Switch](https://mui.com/material-ui/api/switch/)
    * [Tab](https://mui.com/material-ui/api/tab/)
    * [TabContext](https://mui.com/material-ui/api/tab-context/)
    * [Table](https://mui.com/material-ui/api/table/)
    * [TableBody](https://mui.com/material-ui/api/table-body/)
    * [TableCell](https://mui.com/material-ui/api/table-cell/)
    * [TableContainer](https://mui.com/material-ui/api/table-container/)
    * [TableFooter](https://mui.com/material-ui/api/table-footer/)
    * [TableHead](https://mui.com/material-ui/api/table-head/)
    * [TablePagination](https://mui.com/material-ui/api/table-pagination/)
    * [TablePaginationActions](https://mui.com/material-ui/api/table-pagination-actions/)
    * [TableRow](https://mui.com/material-ui/api/table-row/)
    * [TableSortLabel](https://mui.com/material-ui/api/table-sort-label/)
    * [TabList](https://mui.com/material-ui/api/tab-list/)
    * [TabPanel](https://mui.com/material-ui/api/tab-panel/)
    * [Tabs](https://mui.com/material-ui/api/tabs/)
    * [TabScrollButton](https://mui.com/material-ui/api/tab-scroll-button/)
    * [TextareaAutosize](https://mui.com/material-ui/api/textarea-autosize/)
    * [TextField](https://mui.com/material-ui/api/text-field/)
    * [Timeline](https://mui.com/material-ui/api/timeline/)
    * [TimelineConnector](https://mui.com/material-ui/api/timeline-connector/)
    * [TimelineContent](https://mui.com/material-ui/api/timeline-content/)
    * [TimelineDot](https://mui.com/material-ui/api/timeline-dot/)
    * [TimelineItem](https://mui.com/material-ui/api/timeline-item/)
    * [TimelineOppositeContent](https://mui.com/material-ui/api/timeline-opposite-content/)
    * [TimelineSeparator](https://mui.com/material-ui/api/timeline-separator/)
    * [ToggleButton](https://mui.com/material-ui/api/toggle-button/)
    * [ToggleButtonGroup](https://mui.com/material-ui/api/toggle-button-group/)
    * [Toolbar](https://mui.com/material-ui/api/toolbar/)
    * [Tooltip](https://mui.com/material-ui/api/tooltip/)
    * [Typography](https://mui.com/material-ui/api/typography/)
    * [Zoom](https://mui.com/material-ui/api/zoom/)
  * [](https://mui.com/material-ui/customization/how-to-customize/)
  * [](https://mui.com/material-ui/guides/building-extensible-themes/)
  * [](https://mui.com/material-ui/integrations/tailwindcss/tailwindcss-v4/)
  * [](https://mui.com/material-ui/experimental-api/classname-generator/)
  * [](https://mui.com/material-ui/migration/upgrade-to-grid-v2/)
  * [](https://mui.com/material-ui/discover-more/showcase/)
  * [](https://mui.com/material-ui/design-resources/material-ui-for-figma/)
  * [](https://mui.com/store/%3Futm_source=docs&utm_medium=referral&utm_campaign=sidenav/)
