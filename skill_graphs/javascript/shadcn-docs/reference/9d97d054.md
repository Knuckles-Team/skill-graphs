Next.js - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Next.js Copy Page Previous Next Build forms in React using useActionState and Server Actions. In this guide, we will take a look at building forms with Next.js using useActionState and Server Actions. We&#x27;ll cover building forms, validation, pending states, accessibility, and more.
 Demo #
 We are going to build the following form with a simple text input and a textarea. On submit, we&#x27;ll use a server action to validate the form data and update the form state.
 Bug Report Help us improve by reporting bugs you encounter. Bug Title Description 0 /100 characters Include steps to reproduce, expected behavior, and what actually happened. Submit Copy "use client"

 import * as React from "react" View Code
 Note: The examples on this page intentionally disable browser validation
to show how schema validation and form errors work in server actions.
 Approach #
 This form leverages Next.js and React&#x27;s built-in capabilities for form handling. We&#x27;ll build our form using the &lt;Field /&gt; component, which gives you complete flexibility over the markup and styling .

 Uses Next.js &lt;Form /&gt; component for navigation and progressive enhancement.
 &lt;Field /&gt; components for building accessible forms.
 useActionState for managing form state and errors.
 Handles loading states with the pending prop.
 Server Actions for handling form submissions.
 Server-side validation using Zod.

 Anatomy #
 Here&#x27;s a basic example of a form using the &lt;Field /&gt; component.
 Copy &lt; Form action = { formAction } &gt;
 &lt; FieldGroup &gt;
 &lt; Field data-invalid = { !! formState.errors?.title?. length } &gt;
 &lt; FieldLabel htmlFor = &quot;title&quot; &gt;Bug Title&lt;/ FieldLabel &gt;
 &lt; Input
 id = &quot;title&quot;
 name = &quot;title&quot;
 defaultValue = { formState.values.title }
 disabled = { pending }
 aria-invalid = { !! formState.errors?.title?. length }
 placeholder = &quot;Login button not working on mobile&quot;
 autoComplete = &quot;off&quot;
 /&gt;
 &lt; FieldDescription &gt;
 Provide a concise title for your bug report.
 &lt;/ FieldDescription &gt;
 { formState.errors?.title &amp;&amp; (
 &lt; FieldError &gt; { formState.errors.title[ 0 ] } &lt;/ FieldError &gt;
 ) }
 &lt;/ Field &gt;
 &lt;/ FieldGroup &gt;
 &lt; Button type = &quot;submit&quot; &gt;Submit&lt;/ Button &gt;
 &lt;/ Form &gt;
 Usage #
 Create a form schema #
 We&#x27;ll start by defining the shape of our form using a Zod schema in a schema.ts file.
 Note: This example uses zod v3 for schema validation, but you can
replace it with any other schema validation library. Make sure your schema
library conforms to the Standard Schema specification.
 schema.ts Copy import { z } from &quot;zod&quot;

 export const formSchema = z. object ({
 title: z
 . string ()
 . min ( 5 , &quot;Bug title must be at least 5 characters.&quot; )
 . max ( 32 , &quot;Bug title must be at most 32 characters.&quot; ),
 description: z
 . string ()
 . min ( 20 , &quot;Description must be at least 20 characters.&quot; )
 . max ( 100 , &quot;Description must be at most 100 characters.&quot; ),
 })
 Define the form state type #
 Next, we&#x27;ll create a type for our form state that includes values, errors, and success status. This will be used to type the form state on the client and server.
 schema.ts Copy import { z } from &quot;zod&quot;

 export type FormState = {
 values ?: z . infer &lt; typeof formSchema&gt;
 errors : null | Partial &lt; Record &lt; keyof z . infer &lt; typeof formSchema&gt;, string []&gt;&gt;
 success : boolean
 }
 Important: We define the schema and the FormState type in a separate file so we can import them into both the client and server components.
 Create the Server Action #
 A server action is a function that runs on the server and can be called from the client. We&#x27;ll use it to validate the form data and update the form state.
 Expand actions.ts Copy "use server"

 import { formSchema, type FormState } from "./form-next-demo-schema"

 export async function demoFormAction (
 _prevState : FormState ,
 formData : FormData
 ) {
 const values = {
 title: formData. get ( "title" ) as string ,
 description: formData. get ( "description" ) as string ,
 }

 const result = formSchema. safeParse (values)

 if ( ! result.success) {
 return {
 values,
 success: false ,
 errors: result.error. flatten ().fieldErrors,
 }
 }

 // Do something with the values.
 // Call your database or API here.

 return {
 values: {
 title: "" ,
 description: "" ,
 },
 errors: null ,
 success: true ,
 }
 }
 Expand
 Note: We&#x27;re returning values for error cases. This is because we want to keep the user submitted values in the form state. For success cases, we&#x27;re returning empty values to reset the form.
 Build the form #
 We can now build the form using the &lt;Field /&gt; component. We&#x27;ll use the useActionState hook to manage the form state, server action, and pending state.
 Expand form.tsx Copy "use client"

 import * as React from "react"
 import Form from "next/form"
 import { toast } from "sonner"

 import { Button } from "@/components/ui/button"
 import {
 Card,
 CardContent,
 CardDescription,
 CardFooter,
 CardHeader,
 CardTitle,
 } from "@/components/ui/card"
 import {
 Field,
 FieldDescription,
 FieldError,
 FieldGroup,
 FieldLabel,
 } from "@/components/ui/field"
 import { Input } from "@/components/ui/input"
 import {
 InputGroup,
 InputGroupAddon,
 InputGroupText,
 InputGroupTextarea,
 } from "@/components/ui/input-group"
 import { Spinner } from "@/components/ui/spinner"

 import { demoFormAction } from "./form-next-demo-action"
 import { type FormState } from "./form-next-demo-schema"

 export function FormNextDemo () {
 const [ formState , formAction , pending ] = React.useActionState &#x3C;
 FormState,
 FormData
 > (demoFormAction, {
 values: {
 title: "" ,
 description: "" ,
 },
 errors: null ,
 success: false ,
 })
 const [ descriptionLength , setDescriptionLength ] = React. useState ( 0 )

 React. useEffect (() => {
 if (formState.success) {
 toast ( "Thank you for your feedback" , {
 description: "We'll review your report and get back to you soon." ,
 })
 }
 }, [formState.success])

 React. useEffect (() => {
 setDescriptionLength (formState.values.description. length )
 }, [formState.values.description])

 return (
 &#x3C; Card className = "w-full max-w-md" >
 &#x3C; CardHeader >
 &#x3C; CardTitle >Bug Report&#x3C;/ CardTitle >
 &#x3C; CardDescription >
 Help us improve by reporting bugs you encounter.
 &#x3C;/ CardDescription >
 &#x3C;/ CardHeader >
 &#x3C; CardContent >
 &#x3C; Form action = {formAction} id = "bug-report-form" >
 &#x3C; FieldGroup >
 &#x3C; Field data-invalid = { !! formState.errors?.title?. length }>
 &#x3C; FieldLabel htmlFor = "title" >Bug Title&#x3C;/ FieldLabel >
 &#x3C; Input
 id = "title"
 name = "title"
 defaultValue = {formState.values.title}
 disabled = {pending}
 aria-invalid = { !! formState.errors?.title?. length }
 placeholder = "Login button not working on mobile"
 autoComplete = "off"
 />
 {formState.errors?.title &#x26;&#x26; (
 &#x3C; FieldError >{formState.errors.title[ 0 ]}&#x3C;/ FieldError >
 )}
 &#x3C;/ Field >
 &#x3C; Field data-invalid = { !! formState.errors?.description?. length }>
 &#x3C; FieldLabel htmlFor = "description" >Description&#x3C;/ FieldLabel >
 &#x3C; InputGroup >
 &#x3C; InputGroupTextarea
 id = "description"
 name = "description"
 defaultValue = {formState.values.description}
 placeholder = "I'm having an issue with the login button on mobile."
 rows = { 6 }
 className = "min-h-24 resize-none"
 disabled = {pending}
 aria-invalid = { !! formState.errors?.description?. length }
 onChange = {( e ) => setDescriptionLength (e.target.value. length )}
 />
 &#x3C; InputGroupAddon align = "block-end" >
 &#x3C; InputGroupText className = "tabular-nums" >
 {descriptionLength}/100 characters
 &#x3C;/ InputGroupText >
 &#x3C;/ InputGroupAddon >
 &#x3C;/ InputGroup >
 &#x3C; FieldDescription >
 Include steps to reproduce, expected behavior, and what actually
 happened.
 &#x3C;/ FieldDescription >
 {formState.errors?.description &#x26;&#x26; (
 &#x3C; FieldError >{formState.errors.description[ 0 ]}&#x3C;/ FieldError >
 )}
 &#x3C;/ Field >
 &#x3C;/ FieldGroup >
 &#x3C;/ Form >
 &#x3C;/ CardContent >
 &#x3C; CardFooter >
 &#x3C; Field orientation = "horizontal" >
 &#x3C; Button type = "submit" disabled = {pending} form = "bug-report-form" >
 {pending &#x26;&#x26; &#x3C; Spinner />}
 Submit
 &#x3C;/ Button >
 &#x3C;/ Field >
 &#x3C;/ CardFooter >
 &#x3C;/ Card >
 )
 }
 Expand
 Done #
 That&#x27;s it. You now have a fully accessible form with client and server-side validation.
 When you submit the form, the formAction function will be called on the server. The server action will validate the form data and update the form state.
 If the form data is invalid, the server action will return the errors to the client. If the form data is valid, the server action will return the success status and update the form state.
 Pending States #
 Use the pending prop from useActionState to show loading indicators and disable form inputs.
 Copy &quot;use client&quot;

 import * as React from &quot;react&quot;
 import Form from &quot;next/form&quot;

 import { Spinner } from &quot;@/components/ui/spinner&quot;

 import { bugReportFormAction } from &quot;./actions&quot;

 export function BugReportForm () {
 const [ formState , formAction , pending ] = React. useActionState (
 bugReportFormAction,
 {
 errors: null ,
 success: false ,
 }
 )

 return (
 &lt; Form action = { formAction } &gt;
 &lt; FieldGroup &gt;
 &lt; Field data-disabled = { pending } &gt;
 &lt; FieldLabel htmlFor = &quot;name&quot; &gt;Name&lt;/ FieldLabel &gt;
 &lt; Input id = &quot;name&quot; name = &quot;name&quot; disabled = { pending } /&gt;
 &lt;/ Field &gt;
 &lt; Field &gt;
 &lt; Button type = &quot;submit&quot; disabled = { pending } &gt;
 { pending &amp;&amp; &lt; Spinner /&gt; } Submit
 &lt;/ Button &gt;
 &lt;/ Field &gt;
 &lt;/ FieldGroup &gt;
 &lt;/ Form &gt;
 )
 }
 Disabled States #
 Submit Button #
 To disable the submit button, use the pending prop on the button&#x27;s disabled prop.
 Copy &lt; Button type = &quot;submit&quot; disabled = { pending } &gt;
 { pending &amp;&amp; &lt; Spinner /&gt; } Submit
 &lt;/ Button &gt;
 Field #
 To apply a disabled state and styling to a &lt;Field /&gt; component, use the data-disabled prop on the &lt;Field /&gt; component.
 Copy &lt; Field data-disabled = { pending } &gt;
 &lt; FieldLabel htmlFor = &quot;name&quot; &gt;Name&lt;/ FieldLabel &gt;
 &lt; Input id = &quot;name&quot; name = &quot;name&quot; disabled = { pending } /&gt;
 &lt;/ Field &gt;
 Validation #
 Server-side Validation #
 Use safeParse() on your schema in your server action to validate the form data.
 actions.ts Copy &quot;use server&quot;

 export async function bugReportFormAction (
 _prevState : FormState ,
 formData : FormData
 ) {
 const values = {
 title: formData. get ( &quot;title&quot; ) as string ,
 description: formData. get ( &quot;description&quot; ) as string ,
 }

 const result = formSchema. safeParse (values)

 if ( ! result.success) {
 return {
 values,
 success: false ,
 errors: result.error. flatten ().fieldErrors,
 }
 }

 return {
 errors: null ,
 success: true ,
 }
 }
 Business Logic Validation #
 You can add additional custom validation logic in your server action.
 Make sure to return the values on validation errors. This is to ensure that the form state maintains the user&#x27;s input.
 actions.ts Copy &quot;use server&quot;

 export async function bugReportFormAction (
 _prevState : FormState ,
 formData : FormData
 ) {
 const values = {
 title: formData. get ( &quot;title&quot; ) as string ,
 description: formData. get ( &quot;description&quot; ) as string ,
 }

 const result = formSchema. safeParse (values)

 if ( ! result.success) {
 return {
 values,
 success: false ,
 errors: result.error. flatten ().fieldErrors,
 }
 }

 // Check if email already exists in database.
 const existingUser = await db.user. findUnique ({
 where: { email: result.data.email },
 })

 if (existingUser) {
 return {
 values,
 success: false ,
 errors: {
 email: [ &quot;This email is already registered&quot; ],
 },
 }
 }

 return {
 errors: null ,
 success: true ,
 }
 }
 Displaying Errors #
 Display errors next to the field using &lt;FieldError /&gt; . Make sure to add the data-invalid prop to the &lt;Field /&gt; component and aria-invalid prop to the input.
 Copy &lt; Field data-invalid = { !! formState.errors?.email?. length } &gt;
 &lt; FieldLabel htmlFor = &quot;email&quot; &gt;Email&lt;/ FieldLabel &gt;
 &lt; Input
 id = &quot;email&quot;
 name = &quot;email&quot;
 type = &quot;email&quot;
 aria-invalid = { !! formState.errors?.email?. length }
 /&gt;
 { formState.errors?.email &amp;&amp; (
 &lt; FieldError &gt; { formState.errors.email[ 0 ] } &lt;/ FieldError &gt;
 ) }
 &lt;/ Field &gt;
 Resetting the Form #
 When you submit a form with a server action, React will automatically reset the form state to the initial values.
 Reset on Success #
 To reset the form on success, you can omit the values from the server action and React will automatically reset the form state to the initial values. This is standard React behavior.
 actions.ts Copy export async function demoFormAction (
 _prevState : FormState ,
 formData : FormData
 ) {
 const values = {
 title: formData. get ( &quot;title&quot; ) as string ,
 description: formData. get ( &quot;description&quot; ) as string ,
 }

 // Validation.
 if ( ! result.success) {
 return {
 values,
 success: false ,
 errors: result.error. flatten ().fieldErrors,
 }
 }

 // Business logic.
 callYourDatabaseOrAPI (values)

 // Omit the values on success to reset the form state.
 return {
 errors: null ,
 success: true ,
 }
 }
 Preserve on Validation Errors #
 To prevent the form from being reset on failure, you can return the values in the server action. This is to ensure that the form state maintains the user&#x27;s input.
 actions.ts Copy export async function demoFormAction (
 _prevState : FormState ,
 formData : FormData
 ) {
 const values = {
 title: formData. get ( &quot;title&quot; ) as string ,
 description: formData. get ( &quot;description&quot; ) as string ,
 }

 // Validation.
 if ( ! result.success) {
 return {
 // Return the values on validation errors.
 values,
 success: false ,
 errors: result.error. flatten ().fieldErrors,
 }
 }
 }
 Complex Forms #
 Here is an example of a more complex form with multiple fields and validation.
 Subscription Plan Choose your subscription plan. Basic For individuals and small teams Pro For businesses with higher demands Billing Period Choose how often you want to be billed. Add-ons Select additional features you&#x27;d like to include. Analytics Advanced analytics and reporting Backup Automated daily backups Priority Support 24/7 premium customer support Email Notifications Receive email updates about your subscription Save Preferences
 Schema #
 Expand schema.ts Copy import { z } from "zod"

 export const formSchema = z. object ({
 plan: z
 . string ({
 required_error: "Please select a subscription plan" ,
 })
 . min ( 1 , "Please select a subscription plan" )
 . refine (( value ) => value === "basic" || value === "pro" , {
 message: "Invalid plan selection. Please choose Basic or Pro" ,
 }),
 billingPeriod: z
 . string ({
 required_error: "Please select a billing period" ,
 })
 . min ( 1 , "Please select a billing period" ),
 addons: z
 . array (z. string ())
 . min ( 1 , "Please select at least one add-on" )
 . max ( 3 , "You can select up to 3 add-ons" )
 . refine (
 ( value ) => value. every (( addon ) => addons. some (( a ) => a.id === addon)),
 {
 message: "You selected an invalid add-on" ,
 }
 ),
 emailNotifications: z. boolean (),
 })

 export type FormState = {
 values : z . infer &#x3C; typeof formSchema>
 errors : null | Partial &#x3C; Record &#x3C; keyof z . infer &#x3C; typeof formSchema>, string []>>
 success : boolean
 }

 export const addons = [
 {
 id: "analytics" ,
 title: "Analytics" ,
 description: "Advanced analytics and reporting" ,
 },
 {
 id: "backup" ,
 title: "Backup" ,
 description: "Automated daily backups" ,
 },
 {
 id: "support" ,
 title: "Priority Support" ,
 description: "24/7 premium customer support" ,
 },
 ] as const
 Expand
 Form #
 Expand form.tsx Copy "use client"

 import * as React from "react"
 import Form from "next/form"
 import { toast } from "sonner"

 import { Button } from "@/components/ui/button"
 import { Card, CardContent, CardFooter } from "@/components/ui/card"
 import { Checkbox } from "@/components/ui/checkbox"
 import {
 Field,
 FieldContent,
 FieldDescription,
 FieldError,
 FieldGroup,
 FieldLabel,
 FieldLegend,
 FieldSeparator,
 FieldSet,
 FieldTitle,
 } from "@/components/ui/field"
 import {
 RadioGroup,
 RadioGroupItem,
 } from "@/components/ui/radio-group"
 import {
 Select,
 SelectContent,
 SelectItem,
 SelectTrigger,
 SelectValue,
 } from "@/components/ui/select"
 import { Spinner } from "@/components/ui/spinner"
 import { Switch } from "@/components/ui/switch"

 import { complexFormAction } from "./form-next-complex-action"
 import { addons, type FormState } from "./form-next-complex-schema"

 export function FormNextComplex () {
 const [ formState , formAction , pending ] = React.useActionState &#x3C;
 FormState,
 FormData
 > (complexFormAction, {
 values: {
 plan: "basic" ,
 billingPeriod: "monthly" ,
 addons: [],
 emailNotifications: false ,
 },
 errors: null ,
 success: false ,
 })

 React. useEffect (() => {
 if (formState.success) {
 toast. success ( "Preferences saved" , {
 description: "Your subscription plan has been updated." ,
 })
 }
 }, [formState.success])

 return (
 &#x3C; Card className = "w-full max-w-sm" >
 &#x3C; CardContent >
 &#x3C; Form action = {formAction} id = "subscription-form" >
 &#x3C; FieldGroup >
 &#x3C; FieldSet data-invalid = { !! formState.errors?.plan?. length }>
 &#x3C; FieldLegend >Subscription Plan&#x3C;/ FieldLegend >
 &#x3C; FieldDescription >
 Choose your subscription plan.
 &#x3C;/ FieldDescription >
 &#x3C; RadioGroup
 name = "plan"
 defaultValue = {formState.values.plan}
 disabled = {pending}
 aria-invalid = { !! formState.errors?.plan?. length }
 >
 &#x3C; FieldLabel htmlFor = "basic" >
 &#x3C; Field orientation = "horizontal" >
 &#x3C; FieldContent >
 &#x3C; FieldTitle >Basic&#x3C;/ FieldTitle >
 &#x3C; FieldDescription >
 For individuals and small teams
 &#x3C;/ FieldDescription >
 &#x3C;/ FieldContent >
 &#x3C; RadioGroupItem value = "basic" id = "basic" />
 &#x3C;/ Field >
 &#x3C;/ FieldLabel >
 &#x3C; FieldLabel htmlFor = "pro" >
 &#x3C; Field orientation = "horizontal" >
 &#x3C; FieldContent >
 &#x3C; FieldTitle >Pro&#x3C;/ FieldTitle >
 &#x3C; FieldDescription >
 For businesses with higher demands
 &#x3C;/ FieldDescription >
 &#x3C;/ FieldContent >
 &#x3C; RadioGroupItem value = "pro" id = "pro" />
 &#x3C;/ Field >
 &#x3C;/ FieldLabel >
 &#x3C;/ RadioGroup >
 {formState.errors?.plan &#x26;&#x26; (
 &#x3C; FieldError >{formState.errors.plan[ 0 ]}&#x3C;/ FieldError >
 )}
 &#x3C;/ FieldSet >
 &#x3C; FieldSeparator />
 &#x3C; Field data-invalid = { !! formState.errors?.billingPeriod?. length }>
 &#x3C; FieldLabel htmlFor = "billingPeriod" >Billing Period&#x3C;/ FieldLabel >
 &#x3C; Select
 name = "billingPeriod"
 defaultValue = {formState.values.billingPeriod}
 disabled = {pending}
 aria-invalid = { !! formState.errors?.billingPeriod?. length }
 >
 &#x3C; SelectTrigger id = "billingPeriod" >
 &#x3C; SelectValue placeholder = "Select" />
 &#x3C;/ SelectTrigger >
 &#x3C; SelectContent >
 &#x3C; SelectItem value = "monthly" >Monthly&#x3C;/ SelectItem >
 &#x3C; SelectItem value = "yearly" >Yearly&#x3C;/ SelectItem >
 &#x3C;/ SelectContent >
 &#x3C;/ Select >
 &#x3C; FieldDescription >
 Choose how often you want to be billed.
 &#x3C;/ FieldDescription >
 {formState.errors?.billingPeriod &#x26;&#x26; (
 &#x3C; FieldError >{formState.errors.billingPeriod[ 0 ]}&#x3C;/ FieldError >
 )}
 &#x3C;/ Field >
 &#x3C; FieldSeparator />
 &#x3C; FieldSet >
 &#x3C; FieldLegend >Add-ons&#x3C;/ FieldLegend >
 &#x3C; FieldDescription >
 Select additional features you &#x26;apos; d like to include.
 &#x3C;/ FieldDescription >
 &#x3C; FieldGroup data-slot = "checkbox-group" >
 {addons. map (( addon ) => (
 &#x3C; Field
 key = {addon.id}
 orientation = "horizontal"
 data-invalid = { !! formState.errors?.addons?. length }
 >
 &#x3C; Checkbox
 id = {addon.id}
 name = "addons"
 value = {addon.id}
 defaultChecked = {formState.values.addons. includes (
 addon.id
 )}
 disabled = {pending}
 aria-invalid = { !! formState.errors?.addons?. length }
 />
 &#x3C; FieldContent >
 &#x3C; FieldLabel htmlFor = {addon.id}>{addon.title}&#x3C;/ FieldLabel >
 &#x3C; FieldDescription >{addon.description}&#x3C;/ FieldDescription >
 &#x3C;/ FieldContent >
 &#x3C;/ Field >
 ))}
 &#x3C;/ FieldGroup >
 {formState.errors?.addons &#x26;&#x26; (
 &#x3C; FieldError >{formState.errors.addons[ 0 ]}&#x3C;/ FieldError >
 )}
 &#x3C;/ FieldSet >
 &#x3C; FieldSeparator />
 &#x3C; Field orientation = "horizontal" >
 &#x3C; FieldContent >
 &#x3C; FieldLabel htmlFor = "emailNotifications" >
 Email Notifications
 &#x3C;/ FieldLabel >
 &#x3C; FieldDescription >
 Receive email updates about your subscription
 &#x3C;/ FieldDescription >
 &#x3C;/ FieldContent >
 &#x3C; Switch
 id = "emailNotifications"
 name = "emailNotifications"
 defaultChecked = {formState.values.emailNotifications}
 disabled = {pending}
 aria-invalid = { !! formState.errors?.emailNotifications?. length }
 />
 &#x3C;/ Field >
 &#x3C;/ FieldGroup >
 &#x3C;/ Form >
 &#x3C;/ CardContent >
 &#x3C; CardFooter >
 &#x3C; Field orientation = "horizontal" className = "justify-end" >
 &#x3C; Button type = "submit" disabled = {pending} form = "subscription-form" >
 {pending &#x26;&#x26; &#x3C; Spinner />}
 Save Preferences
 &#x3C;/ Button >
 &#x3C;/ Field >
 &#x3C;/ CardFooter >
 &#x3C;/ Card >
 )
 }
 Expand
 Server Action #
 Expand actions.ts Copy "use server"

 import { formSchema, type FormState } from "./form-next-complex-schema"

 export async function complexFormAction (
 _prevState : FormState ,
 formData : FormData
 ) {
 // Sleep for 1 second
 await new Promise (( resolve ) => setTimeout (resolve, 1000 ))

 const values = {
 plan: formData. get ( "plan" ) as FormState [ "values" ][ "plan" ],
 billingPeriod: formData. get ( "billingPeriod" ) as string ,
 addons: formData. getAll ( "addons" ) as string [],
 emailNotifications: formData. get ( "emailNotifications" ) === "on" ,
 }

 const result = formSchema. safeParse (values)

 if ( ! result.success) {
 return {
 values,
 success: false ,
 errors: result.error. flatten ().fieldErrors,
 }
 }

 // Do something with the values.
 // Call your database or API here.

 return {
 values,
 errors: null ,
 success: true ,
 }
 }
 Expand June 2026 - GitHub Registries Gatsby On This Page Demo Approach Anatomy Usage Create a form schema Define the form state type Create the Server Action Build the form Done Pending States Disabled States Submit Button Field Validation Server-side Validation Business Logic Validation Displaying Errors Resetting the Form Reset on Success Preserve on Validation Errors Complex Forms Schema Form Server Action Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
