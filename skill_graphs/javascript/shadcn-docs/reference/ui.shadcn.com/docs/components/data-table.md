Data Table - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Data Table Copy Page Previous Next Powerful table and datagrids built using TanStack Table. Radix UI Base UI Radix UI Columns Status Email Amount success ken99@example.com $316.00 Open menu success Abe45@example.com $242.00 Open menu processing Monserrat44@example.com $837.00 Open menu success Silas22@example.com $874.00 Open menu failed carmella@example.com $721.00 Open menu 0 of 5 row(s) selected. Previous Next
 Introduction #
 Every data table or datagrid I&#x27;ve created has been unique. They all behave differently, have specific sorting and filtering requirements, and work with different data sources.
 It doesn&#x27;t make sense to combine all of these variations into a single component. If we do that, we&#x27;ll lose the flexibility that headless UI provides.
 So instead of a data-table component, I thought it would be more helpful to provide a guide on how to build your own.
 We&#x27;ll start with the basic &lt;Table /&gt; component and build a complex data table from scratch.
 Tip: If you find yourself using the same table in multiple places in your app, you can always extract it into a reusable component.
 Table of Contents #
 This guide will show you how to use TanStack Table and the &lt;Table /&gt; component to build your own custom data table. We&#x27;ll cover the following topics:

 Basic Table
 Row Actions
 Pagination
 Sorting
 Filtering
 Visibility
 Row Selection
 Reusable Components

 Installation #

 Add the &lt;Table /&gt; component to your project:

 pnpm npm yarn bun pnpm dlx shadcn@latest add table Copy

 Add tanstack/react-table dependency:

 pnpm npm yarn bun pnpm add @tanstack/react-table Copy
 Prerequisites #
 We are going to build a table to show recent payments. Here&#x27;s what our data looks like:
 Copy type Payment = {
 id : string
 amount : number
 status : &quot;pending&quot; | &quot;processing&quot; | &quot;success&quot; | &quot;failed&quot;
 email : string
 }

 export const payments : Payment [] = [
 {
 id: &quot;728ed52f&quot; ,
 amount: 100 ,
 status: &quot;pending&quot; ,
 email: &quot;m@example.com&quot; ,
 },
 {
 id: &quot;489e1d42&quot; ,
 amount: 125 ,
 status: &quot;processing&quot; ,
 email: &quot;example@gmail.com&quot; ,
 },
 // ...
 ]
 Project Structure #
 Start by creating the following file structure:
 Copy app
 └── payments
 ├── columns.tsx
 ├── data-table.tsx
 └── page.tsx
 I&#x27;m using a Next.js example here but this works for any other React framework.

 columns.tsx (client component) will contain our column definitions.
 data-table.tsx (client component) will contain our &lt;DataTable /&gt; component.
 page.tsx (server component) is where we&#x27;ll fetch data and render our table.

 Basic Table #
 Let&#x27;s start by building a basic table.
 Column Definitions # First, we&#x27;ll define our columns. app/payments/columns.tsx Copy &quot;use client&quot;

 import { ColumnDef } from &quot;@tanstack/react-table&quot;

 // This type is used to define the shape of our data.
 // You can use a Zod schema here if you want.
 export type Payment = {
 id : string
 amount : number
 status : &quot;pending&quot; | &quot;processing&quot; | &quot;success&quot; | &quot;failed&quot;
 email : string
 }

 export const columns : ColumnDef &lt; Payment &gt;[] = [
 {
 accessorKey: &quot;status&quot; ,
 header: &quot;Status&quot; ,
 },
 {
 accessorKey: &quot;email&quot; ,
 header: &quot;Email&quot; ,
 },
 {
 accessorKey: &quot;amount&quot; ,
 header: &quot;Amount&quot; ,
 },
 ] Note: Columns are where you define the core of what your table
will look like. They define the data that will be displayed, how it will be
formatted, sorted and filtered. &lt;DataTable /&gt; component # Next, we&#x27;ll create a &lt;DataTable /&gt; component to render our table. app/payments/data-table.tsx Copy &quot;use client&quot;

 import {
 ColumnDef,
 flexRender,
 getCoreRowModel,
 useReactTable,
 } from &quot;@tanstack/react-table&quot;

 import {
 Table,
 TableBody,
 TableCell,
 TableHead,
 TableHeader,
 TableRow,
 } from &quot;@/components/ui/table&quot;

 interface DataTableProps &lt; TData , TValue &gt; {
 columns : ColumnDef &lt; TData , TValue &gt;[]
 data : TData []
 }

 export function DataTable &lt; TData , TValue &gt;({
 columns ,
 data ,
 } : DataTableProps &lt; TData , TValue &gt;) {
 const table = useReactTable ({
 data,
 columns,
 getCoreRowModel: getCoreRowModel (),
 })

 return (
 &lt; div className = &quot;overflow-hidden rounded-md border&quot; &gt;
 &lt; Table &gt;
 &lt; TableHeader &gt;
 { table. getHeaderGroups (). map (( headerGroup ) =&gt; (
 &lt; TableRow key = { headerGroup.id } &gt;
 { headerGroup.headers. map (( header ) =&gt; {
 return (
 &lt; TableHead key = { header.id } &gt;
 { header.isPlaceholder
 ? null
 : flexRender (
 header.column.columnDef.header,
 header. getContext ()
 ) }
 &lt;/ TableHead &gt;
 )
 }) }
 &lt;/ TableRow &gt;
 )) }
 &lt;/ TableHeader &gt;
 &lt; TableBody &gt;
 { table. getRowModel ().rows?. length ? (
 table. getRowModel ().rows. map (( row ) =&gt; (
 &lt; TableRow
 key = { row.id }
 data-state = { row. getIsSelected () &amp;&amp; &quot;selected&quot; }
 &gt;
 { row. getVisibleCells (). map (( cell ) =&gt; (
 &lt; TableCell key = { cell.id } &gt;
 { flexRender (cell.column.columnDef.cell, cell. getContext ()) }
 &lt;/ TableCell &gt;
 )) }
 &lt;/ TableRow &gt;
 ))
 ) : (
 &lt; TableRow &gt;
 &lt; TableCell colSpan = { columns. length } className = &quot;h-24 text-center&quot; &gt;
 No results.
 &lt;/ TableCell &gt;
 &lt;/ TableRow &gt;
 ) }
 &lt;/ TableBody &gt;
 &lt;/ Table &gt;
 &lt;/ div &gt;
 )
 } Tip : If you find yourself using &lt;DataTable /&gt; in multiple places, this is the component you could make reusable by extracting it to components/ui/data-table.tsx . &lt;DataTable columns={columns} data={data} /&gt; Render the table # Finally, we&#x27;ll render our table in our page component. app/payments/page.tsx Copy import { columns, Payment } from &quot;./columns&quot;
 import { DataTable } from &quot;./data-table&quot;

 async function getData () : Promise &lt; Payment []&gt; {
 // Fetch data from your API here.
 return [
 {
 id: &quot;728ed52f&quot; ,
 amount: 100 ,
 status: &quot;pending&quot; ,
 email: &quot;m@example.com&quot; ,
 },
 // ...
 ]
 }

 export default async function DemoPage () {
 const data = await getData ()

 return (
 &lt; div className = &quot;container mx-auto py-10&quot; &gt;
 &lt; DataTable columns = { columns } data = { data } /&gt;
 &lt;/ div &gt;
 )
 }
 Cell Formatting #
 Let&#x27;s format the amount cell to display the dollar amount. We&#x27;ll also align the cell to the right.
 Update columns definition # Update the header and cell definitions for amount as follows: app/payments/columns.tsx Copy export const columns : ColumnDef &lt; Payment &gt;[] = [
 {
 accessorKey: &quot;amount&quot; ,
 header : () =&gt; &lt; div className = &quot;text-right&quot; &gt;Amount&lt;/ div &gt;,
 cell : ({ row }) =&gt; {
 const amount = parseFloat (row. getValue ( &quot;amount&quot; ))
 const formatted = new Intl. NumberFormat ( &quot;en-US&quot; , {
 style: &quot;currency&quot; ,
 currency: &quot;USD&quot; ,
 }). format (amount)

 return &lt; div className = &quot;text-right font-medium&quot; &gt; { formatted } &lt;/ div &gt;
 },
 },
 ] You can use the same approach to format other cells and headers.
 Row Actions #
 Let&#x27;s add row actions to our table. We&#x27;ll use a &lt;DropdownMenu /&gt; component for this.
 Update columns definition # Update our columns definition to add a new actions column. The actions cell returns a &lt;DropdownMenu /&gt; component. app/payments/columns.tsx Copy &quot;use client&quot;

 import { ColumnDef } from &quot;@tanstack/react-table&quot;
 import { MoreHorizontal } from &quot;lucide-react&quot;

 import { Button } from &quot;@/components/ui/button&quot;
 import {
 DropdownMenu,
 DropdownMenuContent,
 DropdownMenuItem,
 DropdownMenuLabel,
 DropdownMenuSeparator,
 DropdownMenuTrigger,
 } from &quot;@/components/ui/dropdown-menu&quot;

 export const columns : ColumnDef &lt; Payment &gt;[] = [
 // ...
 {
 id: &quot;actions&quot; ,
 cell : ({ row }) =&gt; {
 const payment = row.original

 return (
 &lt; DropdownMenu &gt;
 &lt; DropdownMenuTrigger asChild &gt;
 &lt; Button variant = &quot;ghost&quot; className = &quot;h-8 w-8 p-0&quot; &gt;
 &lt; span className = &quot;sr-only&quot; &gt;Open menu&lt;/ span &gt;
 &lt; MoreHorizontal className = &quot;h-4 w-4&quot; /&gt;
 &lt;/ Button &gt;
 &lt;/ DropdownMenuTrigger &gt;
 &lt; DropdownMenuContent align = &quot;end&quot; &gt;
 &lt; DropdownMenuLabel &gt;Actions&lt;/ DropdownMenuLabel &gt;
 &lt; DropdownMenuItem
 onClick = { () =&gt; navigator.clipboard. writeText (payment.id) }
 &gt;
 Copy payment ID
 &lt;/ DropdownMenuItem &gt;
 &lt; DropdownMenuSeparator /&gt;
 &lt; DropdownMenuItem &gt;View customer&lt;/ DropdownMenuItem &gt;
 &lt; DropdownMenuItem &gt;View payment details&lt;/ DropdownMenuItem &gt;
 &lt;/ DropdownMenuContent &gt;
 &lt;/ DropdownMenu &gt;
 )
 },
 },
 // ...
 ] You can access the row data using row.original in the cell function. Use this to handle actions for your row eg. use the id to make a DELETE call to your API.
 Pagination #
 Next, we&#x27;ll add pagination to our table.
 Update &lt;DataTable&gt; # app/payments/data-table.tsx Copy import {
 ColumnDef,
 flexRender,
 getCoreRowModel,
 getPaginationRowModel,
 useReactTable,
 } from &quot;@tanstack/react-table&quot;

 export function DataTable &lt; TData , TValue &gt;({
 columns ,
 data ,
 } : DataTableProps &lt; TData , TValue &gt;) {
 const table = useReactTable ({
 data,
 columns,
 getCoreRowModel: getCoreRowModel (),
 getPaginationRowModel: getPaginationRowModel (),
 })

 // ...
 } This will automatically paginate your rows into pages of 10. See the pagination docs for more information on customizing page size and implementing manual pagination. Add pagination controls # We can add pagination controls to our table using the &lt;Button /&gt; component and the table.previousPage() , table.nextPage() API methods. app/payments/data-table.tsx Copy import { Button } from &quot;@/components/ui/button&quot;

 export function DataTable &lt; TData , TValue &gt;({
 columns ,
 data ,
 } : DataTableProps &lt; TData , TValue &gt;) {
 const table = useReactTable ({
 data,
 columns,
 getCoreRowModel: getCoreRowModel (),
 getPaginationRowModel: getPaginationRowModel (),
 })

 return (
 &lt; div &gt;
 &lt; div className = &quot;overflow-hidden rounded-md border&quot; &gt;
 &lt; Table &gt;
 { // .... }
 &lt;/ Table &gt;
 &lt;/ div &gt;
 &lt; div className = &quot;flex items-center justify-end space-x-2 py-4&quot; &gt;
 &lt; Button
 variant = &quot;outline&quot;
 size = &quot;sm&quot;
 onClick = { () =&gt; table. previousPage () }
 disabled = { ! table. getCanPreviousPage () }
 &gt;
 Previous
 &lt;/ Button &gt;
 &lt; Button
 variant = &quot;outline&quot;
 size = &quot;sm&quot;
 onClick = { () =&gt; table. nextPage () }
 disabled = { ! table. getCanNextPage () }
 &gt;
 Next
 &lt;/ Button &gt;
 &lt;/ div &gt;
 &lt;/ div &gt;
 )
 } See Reusable Components section for a more advanced pagination component.
 Sorting #
 Let&#x27;s make the email column sortable.
 Update &lt;DataTable&gt; # app/payments/data-table.tsx Copy &quot;use client&quot;

 import * as React from &quot;react&quot;
 import {
 ColumnDef,
 SortingState,
 flexRender,
 getCoreRowModel,
 getPaginationRowModel,
 getSortedRowModel,
 useReactTable,
 } from &quot;@tanstack/react-table&quot;

 export function DataTable &lt; TData , TValue &gt;({
 columns ,
 data ,
 } : DataTableProps &lt; TData , TValue &gt;) {
 const [ sorting , setSorting ] = React. useState &lt; SortingState &gt;([])

 const table = useReactTable ({
 data,
 columns,
 getCoreRowModel: getCoreRowModel (),
 getPaginationRowModel: getPaginationRowModel (),
 onSortingChange: setSorting,
 getSortedRowModel: getSortedRowModel (),
 state: {
 sorting,
 },
 })

 return (
 &lt; div &gt;
 &lt; div className = &quot;overflow-hidden rounded-md border&quot; &gt;
 &lt; Table &gt; { ... } &lt;/ Table &gt;
 &lt;/ div &gt;
 &lt;/ div &gt;
 )
 } Make header cell sortable # We can now update the email header cell to add sorting controls. app/payments/columns.tsx Copy &quot;use client&quot;

 import { ColumnDef } from &quot;@tanstack/react-table&quot;
 import { ArrowUpDown } from &quot;lucide-react&quot;

 export const columns : ColumnDef &lt; Payment &gt;[] = [
 {
 accessorKey: &quot;email&quot; ,
 header : ({ column }) =&gt; {
 return (
 &lt; Button
 variant = &quot;ghost&quot;
 onClick = { () =&gt; column. toggleSorting (column. getIsSorted () === &quot;asc&quot; ) }
 &gt;
 Email
 &lt; ArrowUpDown className = &quot;ml-2 h-4 w-4&quot; /&gt;
 &lt;/ Button &gt;
 )
 },
 },
 ] This will automatically sort the table (asc and desc) when the user toggles on the header cell.
 Filtering #
 Let&#x27;s add a search input to filter emails in our table.
 Update &lt;DataTable&gt; # app/payments/data-table.tsx Copy &quot;use client&quot;

 import * as React from &quot;react&quot;
 import {
 ColumnDef,
 ColumnFiltersState,
 SortingState,
 flexRender,
 getCoreRowModel,
 getFilteredRowModel,
 getPaginationRowModel,
 getSortedRowModel,
 useReactTable,
 } from &quot;@tanstack/react-table&quot;

 import { Button } from &quot;@/components/ui/button&quot;
 import { Input } from &quot;@/components/ui/input&quot;

 export function DataTable &lt; TData , TValue &gt;({
 columns ,
 data ,
 } : DataTableProps &lt; TData , TValue &gt;) {
 const [ sorting , setSorting ] = React. useState &lt; SortingState &gt;([])
 const [ columnFilters , setColumnFilters ] = React. useState &lt; ColumnFiltersState &gt;(
 []
 )

 const table = useReactTable ({
 data,
 columns,
 onSortingChange: setSorting,
 getCoreRowModel: getCoreRowModel (),
 getPaginationRowModel: getPaginationRowModel (),
 getSortedRowModel: getSortedRowModel (),
 onColumnFiltersChange: setColumnFilters,
 getFilteredRowModel: getFilteredRowModel (),
 state: {
 sorting,
 columnFilters,
 },
 })

 return (
 &lt; div &gt;
 &lt; div className = &quot;flex items-center py-4&quot; &gt;
 &lt; Input
 placeholder = &quot;Filter emails...&quot;
 value = { (table. getColumn ( &quot;email&quot; )?. getFilterValue () as string ) ?? &quot;&quot; }
 onChange = { ( event ) =&gt;
 table. getColumn ( &quot;email&quot; )?. setFilterValue (event.target.value)
 }
 className = &quot;max-w-sm&quot;
 /&gt;
 &lt;/ div &gt;
 &lt; div className = &quot;overflow-hidden rounded-md border&quot; &gt;
 &lt; Table &gt; { ... } &lt;/ Table &gt;
 &lt;/ div &gt;
 &lt;/ div &gt;
 )
 } Filtering is now enabled for the email column. You can add filters to other columns as well. See the filtering docs for more information on customizing filters.
 Visibility #
 Adding column visibility is fairly simple using @tanstack/react-table visibility API.
 Update &lt;DataTable&gt; # app/payments/data-table.tsx Copy &quot;use client&quot;

 import * as React from &quot;react&quot;
 import {
 ColumnDef,
 ColumnFiltersState,
 SortingState,
 VisibilityState,
 flexRender,
 getCoreRowModel,
 getFilteredRowModel,
 getPaginationRowModel,
 getSortedRowModel,
 useReactTable,
 } from &quot;@tanstack/react-table&quot;

 import { Button } from &quot;@/components/ui/button&quot;
 import {
 DropdownMenu,
 DropdownMenuCheckboxItem,
 DropdownMenuContent,
 DropdownMenuTrigger,
 } from &quot;@/components/ui/dropdown-menu&quot;

 export function DataTable &lt; TData , TValue &gt;({
 columns ,
 data ,
 } : DataTableProps &lt; TData , TValue &gt;) {
 const [ sorting , setSorting ] = React. useState &lt; SortingState &gt;([])
 const [ columnFilters , setColumnFilters ] = React. useState &lt; ColumnFiltersState &gt;(
 []
 )
 const [ columnVisibility , setColumnVisibility ] =
 React. useState &lt; VisibilityState &gt;({})

 const table = useReactTable ({
 data,
 columns,
 onSortingChange: setSorting,
 onColumnFiltersChange: setColumnFilters,
 getCoreRowModel: getCoreRowModel (),
 getPaginationRowModel: getPaginationRowModel (),
 getSortedRowModel: getSortedRowModel (),
 getFilteredRowModel: getFilteredRowModel (),
 onColumnVisibilityChange: setColumnVisibility,
 state: {
 sorting,
 columnFilters,
 columnVisibility,
 },
 })

 return (
 &lt; div &gt;
 &lt; div className = &quot;flex items-center py-4&quot; &gt;
 &lt; Input
 placeholder = &quot;Filter emails...&quot;
 value = { table. getColumn ( &quot;email&quot; )?. getFilterValue () as string }
 onChange = { ( event ) =&gt;
 table. getColumn ( &quot;email&quot; )?. setFilterValue (event.target.value)
 }
 className = &quot;max-w-sm&quot;
 /&gt;
 &lt; DropdownMenu &gt;
 &lt; DropdownMenuTrigger asChild &gt;
 &lt; Button variant = &quot;outline&quot; className = &quot;ml-auto&quot; &gt;
 Columns
 &lt;/ Button &gt;
 &lt;/ DropdownMenuTrigger &gt;
 &lt; DropdownMenuContent align = &quot;end&quot; &gt;
 { table
 . getAllColumns ()
 . filter (
 ( column ) =&gt; column. getCanHide ()
 )
 . map (( column ) =&gt; {
 return (
 &lt; DropdownMenuCheckboxItem
 key = { column.id }
 className = &quot;capitalize&quot;
 checked = { column. getIsVisible () }
 onCheckedChange = { ( value ) =&gt;
 column. toggleVisibility ( !! value)
 }
 &gt;
 { column.id }
 &lt;/ DropdownMenuCheckboxItem &gt;
 )
 }) }
 &lt;/ DropdownMenuContent &gt;
 &lt;/ DropdownMenu &gt;
 &lt;/ div &gt;
 &lt; div className = &quot;overflow-hidden rounded-md border&quot; &gt;
 &lt; Table &gt; { ... } &lt;/ Table &gt;
 &lt;/ div &gt;
 &lt;/ div &gt;
 )
 } This adds a dropdown menu that you can use to toggle column visibility.
 Row Selection #
 Next, we&#x27;re going to add row selection to our table.
 Update column definitions # app/payments/columns.tsx Copy &quot;use client&quot;

 import { ColumnDef } from &quot;@tanstack/react-table&quot;

 import { Badge } from &quot;@/components/ui/badge&quot;
 import { Checkbox } from &quot;@/components/ui/checkbox&quot;

 export const columns : ColumnDef &lt; Payment &gt;[] = [
 {
 id: &quot;select&quot; ,
 header : ({ table }) =&gt; (
 &lt; Checkbox
 checked = {
 table. getIsAllPageRowsSelected () ||
 (table. getIsSomePageRowsSelected () &amp;&amp; &quot;indeterminate&quot; )
 }
 onCheckedChange = { ( value ) =&gt; table. toggleAllPageRowsSelected ( !! value) }
 aria-label = &quot;Select all&quot;
 /&gt;
 ),
 cell : ({ row }) =&gt; (
 &lt; Checkbox
 checked = { row. getIsSelected () }
 onCheckedChange = { ( value ) =&gt; row. toggleSelected ( !! value) }
 aria-label = &quot;Select row&quot;
 /&gt;
 ),
 enableSorting: false ,
 enableHiding: false ,
 },
 ] Update &lt;DataTable&gt; # app/payments/data-table.tsx Copy export function DataTable &lt; TData , TValue &gt;({
 columns ,
 data ,
 } : DataTableProps &lt; TData , TValue &gt;) {
 const [ sorting , setSorting ] = React. useState &lt; SortingState &gt;([])
 const [ columnFilters , setColumnFilters ] = React. useState &lt; ColumnFiltersState &gt;(
 []
 )
 const [ columnVisibility , setColumnVisibility ] =
 React. useState &lt; VisibilityState &gt;({})
 const [ rowSelection , setRowSelection ] = React. useState ({})

 const table = useReactTable ({
 data,
 columns,
 onSortingChange: setSorting,
 onColumnFiltersChange: setColumnFilters,
 getCoreRowModel: getCoreRowModel (),
 getPaginationRowModel: getPaginationRowModel (),
 getSortedRowModel: getSortedRowModel (),
 getFilteredRowModel: getFilteredRowModel (),
 onColumnVisibilityChange: setColumnVisibility,
 onRowSelectionChange: setRowSelection,
 state: {
 sorting,
 columnFilters,
 columnVisibility,
 rowSelection,
 },
 })

 return (
 &lt; div &gt;
 &lt; div className = &quot;overflow-hidden rounded-md border&quot; &gt;
 &lt; Table /&gt;
 &lt;/ div &gt;
 &lt;/ div &gt;
 )
 } This adds a checkbox to each row and a checkbox in the header to select all rows. Show selected rows # You can show the number of selected rows using the table.getFilteredSelectedRowModel() API. Copy &lt; div className = &quot;flex-1 text-sm text-muted-foreground&quot; &gt;
 { table. getFilteredSelectedRowModel ().rows. length } of { &quot; &quot; }
 { table. getFilteredRowModel ().rows. length } row(s) selected.
 &lt;/ div &gt;
 Reusable Components #
 Here are some components you can use to build your data tables. This is from the Tasks demo.
 Column header #
 Make any column header sortable and hideable.
 Expand components/data-table-column-header.tsx Copy import { type Column } from "@tanstack/react-table"
 import { ArrowDown, ArrowUp, ChevronsUpDown, EyeOff } from "lucide-react"

 import { cn } from "@/lib/utils"
 import { Button } from "@/components/ui/button"
 import {
 DropdownMenu,
 DropdownMenuContent,
 DropdownMenuItem,
 DropdownMenuSeparator,
 DropdownMenuTrigger,
 } from "@/components/ui/dropdown-menu"

 interface DataTableColumnHeaderProps &#x3C; TData , TValue >
 extends React . HTMLAttributes &#x3C; HTMLDivElement > {
 column : Column &#x3C; TData , TValue >
 title : string
 }

 export function DataTableColumnHeader &#x3C; TData , TValue >({
 column ,
 title ,
 className ,
 } : DataTableColumnHeaderProps &#x3C; TData , TValue >) {
 if ( ! column. getCanSort ()) {
 return &#x3C; div className = { cn (className)}>{title}&#x3C;/ div >
 }

 return (
 &#x3C; div className = { cn ( "flex items-center gap-2" , className)}>
 &#x3C; DropdownMenu >
 &#x3C; DropdownMenuTrigger asChild >
 &#x3C; Button
 variant = "ghost"
 size = "sm"
 className = "-ml-3 h-8 data-[state=open]:bg-accent"
 >
 &#x3C; span >{title}&#x3C;/ span >
 {column. getIsSorted () === "desc" ? (
 &#x3C; ArrowDown />
 ) : column. getIsSorted () === "asc" ? (
 &#x3C; ArrowUp />
 ) : (
 &#x3C; ChevronsUpDown />
 )}
 &#x3C;/ Button >
 &#x3C;/ DropdownMenuTrigger >
 &#x3C; DropdownMenuContent align = "start" >
 &#x3C; DropdownMenuItem onClick = {() => column. toggleSorting ( false )}>
 &#x3C; ArrowUp />
 Asc
 &#x3C;/ DropdownMenuItem >
 &#x3C; DropdownMenuItem onClick = {() => column. toggleSorting ( true )}>
 &#x3C; ArrowDown />
 Desc
 &#x3C;/ DropdownMenuItem >
 &#x3C; DropdownMenuSeparator />
 &#x3C; DropdownMenuItem onClick = {() => column. toggleVisibility ( false )}>
 &#x3C; EyeOff />
 Hide
 &#x3C;/ DropdownMenuItem >
 &#x3C;/ DropdownMenuContent >
 &#x3C;/ DropdownMenu >
 &#x3C;/ div >
 )
 }
 Expand
 Copy export const columns = [
 {
 accessorKey: &quot;email&quot; ,
 header : ({ column }) =&gt; (
 &lt; DataTableColumnHeader column = { column } title = &quot;Email&quot; /&gt;
 ),
 },
 ]
 Pagination #
 Add pagination controls to your table including page size and selection count.
 Expand Copy import { type Table } from "@tanstack/react-table"
 import {
 ChevronLeft,
 ChevronRight,
 ChevronsLeft,
 ChevronsRight,
 } from "lucide-react"

 import { Button } from "@/registry/new-york-v4/ui/button"
 import {
 Select,
 SelectContent,
 SelectItem,
 SelectTrigger,
 SelectValue,
 } from "@/registry/new-york-v4/ui/select"

 interface DataTablePaginationProps &#x3C; TData > {
 table : Table &#x3C; TData >
 }

 export function DataTablePagination &#x3C; TData >({
 table ,
 } : DataTablePaginationProps &#x3C; TData >) {
 return (
 &#x3C; div className = "flex items-center justify-between px-2" >
 &#x3C; div className = "flex-1 text-sm text-muted-foreground" >
 {table. getFilteredSelectedRowModel ().rows. length } of{ " " }
 {table. getFilteredRowModel ().rows. length } row(s) selected.
 &#x3C;/ div >
 &#x3C; div className = "flex items-center space-x-6 lg:space-x-8" >
 &#x3C; div className = "flex items-center space-x-2" >
 &#x3C; p className = "text-sm font-medium" >Rows per page&#x3C;/ p >
 &#x3C; Select
 value = { `${ table . getState (). pagination . pageSize }` }
 onValueChange = {( value ) => {
 table. setPageSize ( Number (value))
 }}
 >
 &#x3C; SelectTrigger className = "h-8 w-[70px]" >
 &#x3C; SelectValue placeholder = {table. getState ().pagination.pageSize} />
 &#x3C;/ SelectTrigger >
 &#x3C; SelectContent side = "top" >
 {[ 10 , 20 , 25 , 30 , 40 , 50 ]. map (( pageSize ) => (
 &#x3C; SelectItem key = {pageSize} value = { `${ pageSize }` }>
 {pageSize}
 &#x3C;/ SelectItem >
 ))}
 &#x3C;/ SelectContent >
 &#x3C;/ Select >
 &#x3C;/ div >
 &#x3C; div className = "flex w-[100px] items-center justify-center text-sm font-medium" >
 Page {table. getState ().pagination.pageIndex + 1 } of{ " " }
 {table. getPageCount ()}
 &#x3C;/ div >
 &#x3C; div className = "flex items-center space-x-2" >
 &#x3C; Button
 variant = "outline"
 size = "icon"
 className = "hidden size-8 lg:flex"
 onClick = {() => table. setPageIndex ( 0 )}
 disabled = { ! table. getCanPreviousPage ()}
 >
 &#x3C; span className = "sr-only" >Go to first page&#x3C;/ span >
 &#x3C; ChevronsLeft />
 &#x3C;/ Button >
 &#x3C; Button
 variant = "outline"
 size = "icon"
 className = "size-8"
 onClick = {() => table. previousPage ()}
 disabled = { ! table. getCanPreviousPage ()}
 >
 &#x3C; span className = "sr-only" >Go to previous page&#x3C;/ span >
 &#x3C; ChevronLeft />
 &#x3C;/ Button >
 &#x3C; Button
 variant = "outline"
 size = "icon"
 className = "size-8"
 onClick = {() => table. nextPage ()}
 disabled = { ! table. getCanNextPage ()}
 >
 &#x3C; span className = "sr-only" >Go to next page&#x3C;/ span >
 &#x3C; ChevronRight />
 &#x3C;/ Button >
 &#x3C; Button
 variant = "outline"
 size = "icon"
 className = "hidden size-8 lg:flex"
 onClick = {() => table. setPageIndex (table. getPageCount () - 1 )}
 disabled = { ! table. getCanNextPage ()}
 >
 &#x3C; span className = "sr-only" >Go to last page&#x3C;/ span >
 &#x3C; ChevronsRight />
 &#x3C;/ Button >
 &#x3C;/ div >
 &#x3C;/ div >
 &#x3C;/ div >
 )
 }
 Expand
 Copy &lt; DataTablePagination table = { table } /&gt;
 Column toggle #
 A component to toggle column visibility.
 Expand Copy "use client"

 import { type Table } from "@tanstack/react-table"
 import { Settings2 } from "lucide-react"

 import { Button } from "@/registry/new-york-v4/ui/button"
 import {
 DropdownMenu,
 DropdownMenuCheckboxItem,
 DropdownMenuContent,
 DropdownMenuLabel,
 DropdownMenuSeparator,
 DropdownMenuTrigger,
 } from "@/registry/new-york-v4/ui/dropdown-menu"

 export function DataTableViewOptions &#x3C; TData >({
 table ,
 } : {
 table : Table &#x3C; TData >
 }) {
 return (
 &#x3C; DropdownMenu >
 &#x3C; DropdownMenuTrigger asChild >
 &#x3C; Button
 variant = "outline"
 size = "sm"
 className = "ml-auto hidden h-8 lg:flex"
 >
 &#x3C; Settings2 />
 View
 &#x3C;/ Button >
 &#x3C;/ DropdownMenuTrigger >
 &#x3C; DropdownMenuContent align = "end" className = "w-[150px]" >
 &#x3C; DropdownMenuLabel >Toggle columns&#x3C;/ DropdownMenuLabel >
 &#x3C; DropdownMenuSeparator />
 {table
 . getAllColumns ()
 . filter (
 ( column ) =>
 typeof column.accessorFn !== "undefined" &#x26;&#x26; column. getCanHide ()
 )
 . map (( column ) => {
 return (
 &#x3C; DropdownMenuCheckboxItem
 key = {column.id}
 className = "capitalize"
 checked = {column. getIsVisible ()}
 onCheckedChange = {( value ) => column. toggleVisibility ( !! value)}
 >
 {column.id}
 &#x3C;/ DropdownMenuCheckboxItem >
 )
 })}
 &#x3C;/ DropdownMenuContent >
 &#x3C;/ DropdownMenu >
 )
 }
 Expand
 Copy &lt; DataTableViewOptions table = { table } /&gt;
 RTL #
 To enable RTL support in shadcn/ui, see the RTL configuration guide .
 Arabic (العربية) ▼ Toggle الأعمدة الحالة البريد الإلكتروني المبلغ ناجح ken99@example.com ‏٣١٦٫٠٠ US$ فتح القائمة ناجح Abe45@example.com ‏٢٤٢٫٠٠ US$ فتح القائمة قيد المعالجة Monserrat44@example.com ‏٨٣٧٫٠٠ US$ فتح القائمة ناجح Silas22@example.com ‏٨٧٤٫٠٠ US$ فتح القائمة فشل carmella@example.com ‏٧٢١٫٠٠ US$ فتح القائمة 0 من 5 صف(وف) محدد. السابق التالي Context Menu Date Picker On This Page Introduction Table of Contents Installation Prerequisites Project Structure Basic Table Column Definitions &lt;DataTable /&gt; component Render the table Cell Formatting Update columns definition Row Actions Update columns definition Pagination Update &lt;DataTable&gt; Add pagination controls Sorting Update &lt;DataTable&gt; Make header cell sortable Filtering Update &lt;DataTable&gt; Visibility Update &lt;DataTable&gt; Row Selection Update column definitions Update &lt;DataTable&gt; Show selected rows Reusable Components Column header Pagination Column toggle RTL Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
