Calendar - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Calendar Copy Page Previous Next A calendar component that allows users to select a date or a range of dates. Radix UI Base UI Radix UI Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec Jun 1926 1927 1928 1929 1930 1931 1932 1933 1934 1935 1936 1937 1938 1939 1940 1941 1942 1943 1944 1945 1946 1947 1948 1949 1950 1951 1952 1953 1954 1955 1956 1957 1958 1959 1960 1961 1962 1963 1964 1965 1966 1967 1968 1969 1970 1971 1972 1973 1974 1975 1976 1977 1978 1979 1980 1981 1982 1983 1984 1985 1986 1987 1988 1989 1990 1991 1992 1993 1994 1995 1996 1997 1998 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026 2026 June 2026 Su Mo Tu We Th Fr Sa 31 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 1 2 3 4 Copy "use client"

 import * as React from "react" View Code
 Installation #
 Command Manual pnpm npm yarn bun pnpm dlx shadcn@latest add calendar Copy
 Usage #
 Copy import { Calendar } from &quot;@/components/ui/calendar&quot;
 Copy const [ date , setDate ] = React. useState &lt; Date | undefined &gt;( new Date ())

 return (
 &lt; Calendar
 mode = &quot;single&quot;
 selected = { date }
 onSelect = { setDate }
 className = &quot;rounded-lg border&quot;
 /&gt;
 )
 See the React DayPicker documentation for more information.
 About #
 The Calendar component is built on top of React DayPicker .
 Date Picker #
 You can use the &lt;Calendar&gt; component to build a date picker. See the Date Picker page for more information.
 Persian / Hijri / Jalali Calendar #
 To use the Persian calendar, edit components/ui/calendar.tsx and replace react-day-picker with react-day-picker/persian .
 Copy - import { DayPicker } from &quot;react-day-picker&quot;
 + import { DayPicker } from &quot;react-day-picker/persian&quot;
 خرداد ۱۴۰۴ ش ۱ش ۲ش ۳ش ۴ش ۵ش ج ۲۷ ۲۸ ۲۹ ۳۰ ۳۱ ۱ ۲ ۳ ۴ ۵ ۶ ۷ ۸ ۹ ۱۰ ۱۱ ۱۲ ۱۳ ۱۴ ۱۵ ۱۶ ۱۷ ۱۸ ۱۹ ۲۰ ۲۱ ۲۲ ۲۳ ۲۴ ۲۵ ۲۶ ۲۷ ۲۸ ۲۹ ۳۰ ۳۱ ۱ ۲ ۳ ۴ ۵ ۶ Copy "use client"

 import * as React from "react" View Code
 Selected Date (With TimeZone) #
 The Calendar component accepts a timeZone prop to ensure dates are displayed and selected in the user&#x27;s local timezone.
 Copy export function CalendarWithTimezone () {
 const [ date , setDate ] = React. useState &lt; Date | undefined &gt;( undefined )
 const [ timeZone , setTimeZone ] = React. useState &lt; string | undefined &gt;( undefined )

 React. useEffect (() =&gt; {
 setTimeZone (Intl. DateTimeFormat (). resolvedOptions ().timeZone)
 }, [])

 return (
 &lt; Calendar
 mode = &quot;single&quot;
 selected = { date }
 onSelect = { setDate }
 timeZone = { timeZone }
 /&gt;
 )
 }
 Note: If you notice a selected date offset (for example, selecting the 20th highlights the 19th), make sure the timeZone prop is set to the user&#x27;s local timezone.
 Why client-side? The timezone is detected using Intl.DateTimeFormat().resolvedOptions().timeZone inside a useEffect to ensure compatibility with server-side rendering. Detecting the timezone during render would cause hydration mismatches, as the server and client may be in different timezones.
 Examples #
 Basic #
 A basic calendar component. We used className=&quot;rounded-lg border&quot; to style the calendar.
 June 2026 Su Mo Tu We Th Fr Sa 31 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 1 2 3 4 Copy "use client"

 import { Calendar } from "@/components/ui/calendar" View Code
 Range Calendar #
 Use the mode=&quot;range&quot; prop to enable range selection.
 January 2026 Su Mo Tu We Th Fr Sa 28 29 30 31 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 February 2026 Su Mo Tu We Th Fr Sa 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 Copy "use client"

 import * as React from "react" View Code
 Month and Year Selector #
 Use captionLayout=&quot;dropdown&quot; to show month and year dropdowns.
 Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec Jun 1926 1927 1928 1929 1930 1931 1932 1933 1934 1935 1936 1937 1938 1939 1940 1941 1942 1943 1944 1945 1946 1947 1948 1949 1950 1951 1952 1953 1954 1955 1956 1957 1958 1959 1960 1961 1962 1963 1964 1965 1966 1967 1968 1969 1970 1971 1972 1973 1974 1975 1976 1977 1978 1979 1980 1981 1982 1983 1984 1985 1986 1987 1988 1989 1990 1991 1992 1993 1994 1995 1996 1997 1998 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026 2026 June 2026 Su Mo Tu We Th Fr Sa 31 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 1 2 3 4 Copy "use client"

 import { Calendar } from "@/components/ui/calendar" View Code
 Presets #
 June 2026 Su Mo Tu We Th Fr Sa 31 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 1 2 3 4 5 6 7 8 9 10 11 Today Tomorrow In 3 days In a week In 2 weeks Copy "use client"

 import * as React from "react" View Code
 Date and Time Picker #
 June 2026 Su Mo Tu We Th Fr Sa 31 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 1 2 3 4 Start Time End Time Copy "use client"

 import * as React from "react" View Code
 Booked dates #
 February 2026 Su Mo Tu We Th Fr Sa 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 Copy "use client"

 import * as React from "react" View Code
 Custom Cell Size #
 January February March April May June July August September October November December December 1926 1927 1928 1929 1930 1931 1932 1933 1934 1935 1936 1937 1938 1939 1940 1941 1942 1943 1944 1945 1946 1947 1948 1949 1950 1951 1952 1953 1954 1955 1956 1957 1958 1959 1960 1961 1962 1963 1964 1965 1966 1967 1968 1969 1970 1971 1972 1973 1974 1975 1976 1977 1978 1979 1980 1981 1982 1983 1984 1985 1986 1987 1988 1989 1990 1991 1992 1993 1994 1995 1996 1997 1998 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026 2026 December 2026 Su Mo Tu We Th Fr Sa 29 30 1 $100 2 $100 3 $100 4 $100 5 $120 6 $120 7 $100 8 $100 9 $100 10 $100 11 $100 12 $120 13 $120 14 $100 15 $100 16 $100 17 $100 18 $100 19 $120 20 $120 21 $100 22 $100 23 $100 24 $100 25 $100 26 $120 27 $120 28 $100 29 $100 30 $100 31 $100 Copy "use client"

 import * as React from "react" View Code
 You can customize the size of calendar cells using the --cell-size CSS variable. You can also make it responsive by using breakpoint-specific values:
 Copy &lt; Calendar
 mode = &quot;single&quot;
 selected = { date }
 onSelect = { setDate }
 className = &quot;rounded-lg border [--cell-size:--spacing(11)] md:[--cell-size:--spacing(12)]&quot;
 /&gt;
 Or use fixed values:
 Copy &lt; Calendar
 mode = &quot;single&quot;
 selected = { date }
 onSelect = { setDate }
 className = &quot;rounded-lg border [--cell-size:2.75rem] md:[--cell-size:3rem]&quot;
 /&gt;
 Week Numbers #
 Use showWeekNumber to show week numbers.
 February 2026 Su Mo Tu We Th Fr Sa 06 1 2 3 4 5 6 7 07 8 9 10 11 12 13 14 08 15 16 17 18 19 20 21 09 22 23 24 25 26 27 28 Copy "use client"

 import * as React from "react" View Code
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 See also the Hijri Guide for enabling the Persian / Hijri / Jalali calendar.
 Arabic (العربية) ▼ Toggle يناير فبراير مارس أبريل مايو يونيو يوليو أغسطس سبتمبر أكتوبر نوفمبر ديسمبر يونيو 1926 1927 1928 1929 1930 1931 1932 1933 1934 1935 1936 1937 1938 1939 1940 1941 1942 1943 1944 1945 1946 1947 1948 1949 1950 1951 1952 1953 1954 1955 1956 1957 1958 1959 1960 1961 1962 1963 1964 1965 1966 1967 1968 1969 1970 1971 1972 1973 1974 1975 1976 1977 1978 1979 1980 1981 1982 1983 1984 1985 1986 1987 1988 1989 1990 1991 1992 1993 1994 1995 1996 1997 1998 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026 2026 يونيو 2026 أحد اثنين ثلاثاء أربعاء خميس جمعة سبت 31 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 1 2 3 4 Copy "use client"

 import * as React from "react" View Code
 When using RTL, import the locale from react-day-picker/locale and pass both the locale and dir props to the Calendar component:
 Copy import { arSA } from &quot;react-day-picker/locale&quot;

 ; &lt; Calendar
 mode = &quot;single&quot;
 selected = {date}
 onSelect = {setDate}
 locale = {arSA}
 dir = &quot;rtl&quot;
 /&gt;
 API Reference #
 See the React DayPicker documentation for more information on the Calendar component.
 Changelog #
 RTL Support #
 If you&#x27;re upgrading from a previous version of the Calendar component, you&#x27;ll need to apply the following updates to add locale support:
 Import the Locale type. Add Locale to your imports from react-day-picker : Copy import {
 DayPicker,
 getDefaultClassNames,
 type DayButton,
 + type Locale,
 } from &quot;react-day-picker&quot; Add locale prop to the Calendar component. Add the locale prop to the component&#x27;s props: Copy function Calendar({
 className,
 classNames,
 showOutsideDays = true,
 captionLayout = &quot;label&quot;,
 buttonVariant = &quot;ghost&quot;,
 + locale,
 formatters,
 components,
 ...props
 }: React.ComponentProps&lt;typeof DayPicker&gt; &amp; {
 buttonVariant?: React.ComponentProps&lt;typeof Button&gt;[&quot;variant&quot;]
 }) { Pass locale to DayPicker. Pass the locale prop to the DayPicker component: Copy &lt;DayPicker
 showOutsideDays={showOutsideDays}
 className={cn(...)}
 captionLayout={captionLayout}
 + locale={locale}
 formatters={{
 formatMonthDropdown: (date) =&gt;
 - date.toLocaleString(&quot;default&quot;, { month: &quot;short&quot; }),
 + date.toLocaleString(locale?.code, { month: &quot;short&quot; }),
 ...formatters,
 }} Update CalendarDayButton to accept locale. Update the CalendarDayButton component signature and pass locale : Copy function CalendarDayButton({
 className,
 day,
 modifiers,
 + locale,
 ...props
 - }: React.ComponentProps&lt;typeof DayButton&gt;) {
 + }: React.ComponentProps&lt;typeof DayButton&gt; &amp; { locale?: Partial&lt;Locale&gt; }) { Update date formatting in CalendarDayButton. Use locale?.code in the date formatting: Copy &lt;Button
 variant=&quot;ghost&quot;
 size=&quot;icon&quot;
 - data-day={day.date.toLocaleDateString()}
 + data-day={day.date.toLocaleDateString(locale?.code)}
 ...
 /&gt; Pass locale to DayButton component. Update the DayButton component usage to pass the locale prop: Copy components={{
 ...
 - DayButton: CalendarDayButton,
 + DayButton: ({ ...props }) =&gt; (
 + &lt;CalendarDayButton locale={locale} {...props} /&gt;
 + ),
 ...
 }} Update RTL-aware CSS classes. Replace directional classes with logical properties for better RTL support: Copy // In the day classNames:
 - [&amp;:last-child[data-selected=true]_button]:rounded-r-(--cell-radius)
 + [&amp;:last-child[data-selected=true]_button]:rounded-e-(--cell-radius)
 - [&amp;:nth-child(2)[data-selected=true]_button]:rounded-l-(--cell-radius)
 + [&amp;:nth-child(2)[data-selected=true]_button]:rounded-s-(--cell-radius)
 - [&amp;:first-child[data-selected=true]_button]:rounded-l-(--cell-radius)
 + [&amp;:first-child[data-selected=true]_button]:rounded-s-(--cell-radius)

 // In range_start classNames:
 - rounded-l-(--cell-radius) ... after:right-0
 + rounded-s-(--cell-radius) ... after:end-0

 // In range_end classNames:
 - rounded-r-(--cell-radius) ... after:left-0
 + rounded-e-(--cell-radius) ... after:start-0

 // In CalendarDayButton className:
 - data-[range-end=true]:rounded-r-(--cell-radius)
 + data-[range-end=true]:rounded-e-(--cell-radius)
 - data-[range-start=true]:rounded-l-(--cell-radius)
 + data-[range-start=true]:rounded-s-(--cell-radius)
 After applying these changes, you can use the locale prop to provide locale-specific formatting:
 Copy import { enUS } from &quot;react-day-picker/locale&quot;

 ; &lt; Calendar mode = &quot;single&quot; selected = {date} onSelect = {setDate} locale = {enUS} /&gt; Button Group Card On This Page Installation Usage About Date Picker Persian / Hijri / Jalali Calendar Selected Date (With TimeZone) Examples Basic Range Calendar Month and Year Selector Presets Date and Time Picker Booked dates Custom Cell Size Week Numbers RTL API Reference Changelog RTL Support Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
