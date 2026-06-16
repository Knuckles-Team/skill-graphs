TanStack Form - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json TanStack Form Copy Page Previous Next Build forms in React using TanStack Form and Zod. This guide explores how to build forms using TanStack Form. You&#x27;ll learn to create forms with the &lt;Field /&gt; component, implement schema validation with Zod, handle errors, and ensure accessibility.
 Demo #
 We&#x27;ll start by building the following form. It has a simple text input and a textarea. On submit, we&#x27;ll validate the form data and display any errors.
 Note: For the purpose of this demo, we have intentionally disabled browser
validation to show how schema validation and form errors work in TanStack
Form. It is recommended to add basic browser validation in your production
code.
 Bug Report Help us improve by reporting bugs you encounter. Bug Title Description 0 /100 characters Include steps to reproduce, expected behavior, and what actually happened. Reset Submit Copy "use client"

 import * as React from "react" View Code
 Approach #
 This form leverages TanStack Form for powerful, headless form handling. We&#x27;ll build our form using the &lt;Field /&gt; component, which gives you complete flexibility over the markup and styling .

 Uses TanStack Form&#x27;s useForm hook for form state management.
 form.Field component with render prop pattern for controlled inputs.
 &lt;Field /&gt; components for building accessible forms.
 Client-side validation using Zod.
 Real-time validation feedback.

 Anatomy #
 Here&#x27;s a basic example of a form using TanStack Form with the &lt;Field /&gt; component.
 Copy &lt; form
 onSubmit = { ( e ) =&gt; {
 e. preventDefault ()
 form. handleSubmit ()
 } }
 &gt;
 &lt; FieldGroup &gt;
 &lt; form.Field
 name = &quot;title&quot;
 children = { ( field ) =&gt; {
 const isInvalid =
 field.state.meta.isTouched &amp;&amp; ! field.state.meta.isValid
 return (
 &lt; Field data-invalid = { isInvalid } &gt;
 &lt; FieldLabel htmlFor = { field.name } &gt;Bug Title&lt;/ FieldLabel &gt;
 &lt; Input
 id = { field.name }
 name = { field.name }
 value = { field.state.value }
 onBlur = { field.handleBlur }
 onChange = { ( e ) =&gt; field. handleChange (e.target.value) }
 aria-invalid = { isInvalid }
 placeholder = &quot;Login button not working on mobile&quot;
 autoComplete = &quot;off&quot;
 /&gt;
 &lt; FieldDescription &gt;
 Provide a concise title for your bug report.
 &lt;/ FieldDescription &gt;
 { isInvalid &amp;&amp; &lt; FieldError errors = { field.state.meta.errors } /&gt; }
 &lt;/ Field &gt;
 )
 } }
 /&gt;
 &lt;/ FieldGroup &gt;
 &lt; Button type = &quot;submit&quot; &gt;Submit&lt;/ Button &gt;
 &lt;/ form &gt;
 Form #
 Create a schema #
 We&#x27;ll start by defining the shape of our form using a Zod schema.
 Note: This example uses zod v3 for schema validation. TanStack Form
integrates seamlessly with Zod and other Standard Schema validation libraries
through its validators API.
 form.tsx Copy import * as z from &quot;zod&quot;

 const formSchema = z. object ({
 title: z
 . string ()
 . min ( 5 , &quot;Bug title must be at least 5 characters.&quot; )
 . max ( 32 , &quot;Bug title must be at most 32 characters.&quot; ),
 description: z
 . string ()
 . min ( 20 , &quot;Description must be at least 20 characters.&quot; )
 . max ( 100 , &quot;Description must be at most 100 characters.&quot; ),
 })
 Set up the form #
 Use the useForm hook from TanStack Form to create your form instance with Zod validation.
 form.tsx Copy import { useForm } from &quot;@tanstack/react-form&quot;
 import { toast } from &quot;sonner&quot;
 import * as z from &quot;zod&quot;

 const formSchema = z. object ({
 // ...
 })

 export function BugReportForm () {
 const form = useForm ({
 defaultValues: {
 title: &quot;&quot; ,
 description: &quot;&quot; ,
 },
 validators: {
 onSubmit: formSchema,
 },
 onSubmit : async ({ value }) =&gt; {
 toast. success ( &quot;Form submitted successfully&quot; )
 },
 })

 return (
 &lt; form
 onSubmit = { ( e ) =&gt; {
 e. preventDefault ()
 form. handleSubmit ()
 } }
 &gt;
 { /* ... */ }
 &lt;/ form &gt;
 )
 }
 We are using onSubmit to validate the form data here. TanStack Form supports other validation modes, which you can read about in the documentation .
 Build the form #
 We can now build the form using the form.Field component from TanStack Form and the &lt;Field /&gt; component.
 Expand form.tsx Copy "use client"

 import * as React from "react"
 import { useForm } from "@tanstack/react-form"
 import { toast } from "sonner"
 import * as z from "zod"

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

 const formSchema = z. object ({
 title: z
 . string ()
 . min ( 5 , "Bug title must be at least 5 characters." )
 . max ( 32 , "Bug title must be at most 32 characters." ),
 description: z
 . string ()
 . min ( 20 , "Description must be at least 20 characters." )
 . max ( 100 , "Description must be at most 100 characters." ),
 })

 export function BugReportForm () {
 const form = useForm ({
 defaultValues: {
 title: "" ,
 description: "" ,
 },
 validators: {
 onSubmit: formSchema,
 },
 onSubmit : async ({ value }) => {
 toast ( "You submitted the following values:" , {
 description : (
 &#x3C; pre className = "mt-2 w-[320px] overflow-x-auto rounded-md bg-code p-4 text-code-foreground" >
 &#x3C; code >{ JSON . stringify (value, null , 2 )}&#x3C;/ code >
 &#x3C;/ pre >
 ),
 position: "bottom-right" ,
 classNames: {
 content: "flex flex-col gap-2" ,
 },
 style: {
 "--border-radius" : "calc(var(--radius) + 4px)" ,
 } as React . CSSProperties ,
 })
 },
 })

 return (
 &#x3C; Card className = "w-full sm:max-w-md" >
 &#x3C; CardHeader >
 &#x3C; CardTitle >Bug Report&#x3C;/ CardTitle >
 &#x3C; CardDescription >
 Help us improve by reporting bugs you encounter.
 &#x3C;/ CardDescription >
 &#x3C;/ CardHeader >
 &#x3C; CardContent >
 &#x3C; form
 id = "bug-report-form"
 onSubmit = {( e ) => {
 e. preventDefault ()
 form. handleSubmit ()
 }}
 >
 &#x3C; FieldGroup >
 &#x3C; form.Field
 name = "title"
 children = {( field ) => {
 const isInvalid =
 field.state.meta.isTouched &#x26;&#x26; ! field.state.meta.isValid
 return (
 &#x3C; Field data-invalid = {isInvalid}>
 &#x3C; FieldLabel htmlFor = {field.name}>Bug Title&#x3C;/ FieldLabel >
 &#x3C; Input
 id = {field.name}
 name = {field.name}
 value = {field.state.value}
 onBlur = {field.handleBlur}
 onChange = {( e ) => field. handleChange (e.target.value)}
 aria-invalid = {isInvalid}
 placeholder = "Login button not working on mobile"
 autoComplete = "off"
 />
 {isInvalid &#x26;&#x26; (
 &#x3C; FieldError errors = {field.state.meta.errors} />
 )}
 &#x3C;/ Field >
 )
 }}
 />
 &#x3C; form.Field
 name = "description"
 children = {( field ) => {
 const isInvalid =
 field.state.meta.isTouched &#x26;&#x26; ! field.state.meta.isValid
 return (
 &#x3C; Field data-invalid = {isInvalid}>
 &#x3C; FieldLabel htmlFor = {field.name}>Description&#x3C;/ FieldLabel >
 &#x3C; InputGroup >
 &#x3C; InputGroupTextarea
 id = {field.name}
 name = {field.name}
 value = {field.state.value}
 onBlur = {field.handleBlur}
 onChange = {( e ) => field. handleChange (e.target.value)}
 placeholder = "I'm having an issue with the login button on mobile."
 rows = { 6 }
 className = "min-h-24 resize-none"
 aria-invalid = {isInvalid}
 />
 &#x3C; InputGroupAddon align = "block-end" >
 &#x3C; InputGroupText className = "tabular-nums" >
 {field.state.value. length }/100 characters
 &#x3C;/ InputGroupText >
 &#x3C;/ InputGroupAddon >
 &#x3C;/ InputGroup >
 &#x3C; FieldDescription >
 Include steps to reproduce, expected behavior, and what
 actually happened.
 &#x3C;/ FieldDescription >
 {isInvalid &#x26;&#x26; (
 &#x3C; FieldError errors = {field.state.meta.errors} />
 )}
 &#x3C;/ Field >
 )
 }}
 />
 &#x3C;/ FieldGroup >
 &#x3C;/ form >
 &#x3C;/ CardContent >
 &#x3C; CardFooter >
 &#x3C; Field orientation = "horizontal" >
 &#x3C; Button type = "button" variant = "outline" onClick = {() => form. reset ()}>
 Reset
 &#x3C;/ Button >
 &#x3C; Button type = "submit" form = "bug-report-form" >
 Submit
 &#x3C;/ Button >
 &#x3C;/ Field >
 &#x3C;/ CardFooter >
 &#x3C;/ Card >
 )
 }
 Expand
 Done #
 That&#x27;s it. You now have a fully accessible form with client-side validation.
 When you submit the form, the onSubmit function will be called with the validated form data. If the form data is invalid, TanStack Form will display the errors next to each field.
 Validation #
 Client-side Validation #
 TanStack Form validates your form data using the Zod schema. Validation happens in real-time as the user types.
 form.tsx Copy import { useForm } from &quot;@tanstack/react-form&quot;

 const formSchema = z. object ({
 // ...
 })

 export function BugReportForm () {
 const form = useForm ({
 defaultValues: {
 title: &quot;&quot; ,
 description: &quot;&quot; ,
 },
 validators: {
 onSubmit: formSchema,
 },
 onSubmit : async ({ value }) =&gt; {
 console. log (value)
 },
 })

 return &lt; form onSubmit = { /* ... */ } &gt; { /* ... */ } &lt;/ form &gt;
 }
 Validation Modes #
 TanStack Form supports different validation strategies through the validators option:
 Mode Description &quot;onChange&quot; Validation triggers on every change. &quot;onBlur&quot; Validation triggers on blur. &quot;onSubmit&quot; Validation triggers on submit.
 form.tsx Copy const form = useForm ({
 defaultValues: {
 title: &quot;&quot; ,
 description: &quot;&quot; ,
 },
 validators: {
 onSubmit: formSchema,
 onChange: formSchema,
 onBlur: formSchema,
 },
 })
 Displaying Errors #
 Display errors next to the field using &lt;FieldError /&gt; . For styling and accessibility:

 Add the data-invalid prop to the &lt;Field /&gt; component.
 Add the aria-invalid prop to the form control such as &lt;Input /&gt; , &lt;SelectTrigger /&gt; , &lt;Checkbox /&gt; , etc.

 form.tsx Copy &lt; form.Field
 name = &quot;email&quot;
 children = { ( field ) =&gt; {
 const isInvalid = field.state.meta.isTouched &amp;&amp; ! field.state.meta.isValid

 return (
 &lt; Field data-invalid = { isInvalid } &gt;
 &lt; FieldLabel htmlFor = { field.name } &gt;Email&lt;/ FieldLabel &gt;
 &lt; Input
 id = { field.name }
 name = { field.name }
 value = { field.state.value }
 onBlur = { field.handleBlur }
 onChange = { ( e ) =&gt; field. handleChange (e.target.value) }
 type = &quot;email&quot;
 aria-invalid = { isInvalid }
 /&gt;
 { isInvalid &amp;&amp; &lt; FieldError errors = { field.state.meta.errors } /&gt; }
 &lt;/ Field &gt;
 )
 } }
 /&gt;
 Working with Different Field Types #
 Input #

 For input fields, use field.state.value and field.handleChange on the &lt;Input /&gt; component.
 To show errors, add the aria-invalid prop to the &lt;Input /&gt; component and the data-invalid prop to the &lt;Field /&gt; component.

 Profile Settings Update your profile information below. Username This is your public display name. Must be between 3 and 10 characters. Must only contain letters, numbers, and underscores. Reset Save Copy "use client"

 import { useForm } from "@tanstack/react-form" View Code
 form.tsx Copy &lt; form.Field
 name = &quot;username&quot;
 children = { ( field ) =&gt; {
 const isInvalid = field.state.meta.isTouched &amp;&amp; ! field.state.meta.isValid
 return (
 &lt; Field data-invalid = { isInvalid } &gt;
 &lt; FieldLabel htmlFor = &quot;form-tanstack-input-username&quot; &gt;Username&lt;/ FieldLabel &gt;
 &lt; Input
 id = &quot;form-tanstack-input-username&quot;
 name = { field.name }
 value = { field.state.value }
 onBlur = { field.handleBlur }
 onChange = { ( e ) =&gt; field. handleChange (e.target.value) }
 aria-invalid = { isInvalid }
 placeholder = &quot;shadcn&quot;
 autoComplete = &quot;username&quot;
 /&gt;
 &lt; FieldDescription &gt;
 This is your public display name. Must be between 3 and 10 characters.
 Must only contain letters, numbers, and underscores.
 &lt;/ FieldDescription &gt;
 { isInvalid &amp;&amp; &lt; FieldError errors = { field.state.meta.errors } /&gt; }
 &lt;/ Field &gt;
 )
 } }
 /&gt;
 Textarea #

 For textarea fields, use field.state.value and field.handleChange on the &lt;Textarea /&gt; component.
 To show errors, add the aria-invalid prop to the &lt;Textarea /&gt; component and the data-invalid prop to the &lt;Field /&gt; component.

 Personalization Customize your experience by telling us more about yourself. More about you Tell us more about yourself. This will be used to help us personalize your experience. Reset Save Copy "use client"

 import { useForm } from "@tanstack/react-form" View Code
 form.tsx Copy &lt; form.Field
 name = &quot;about&quot;
 children = { ( field ) =&gt; {
 const isInvalid = field.state.meta.isTouched &amp;&amp; ! field.state.meta.isValid
 return (
 &lt; Field data-invalid = { isInvalid } &gt;
 &lt; FieldLabel htmlFor = &quot;form-tanstack-textarea-about&quot; &gt;
 More about you
 &lt;/ FieldLabel &gt;
 &lt; Textarea
 id = &quot;form-tanstack-textarea-about&quot;
 name = { field.name }
 value = { field.state.value }
 onBlur = { field.handleBlur }
 onChange = { ( e ) =&gt; field. handleChange (e.target.value) }
 aria-invalid = { isInvalid }
 placeholder = &quot;I&#x27;m a software engineer...&quot;
 className = &quot;min-h-[120px]&quot;
 /&gt;
 &lt; FieldDescription &gt;
 Tell us more about yourself. This will be used to help us personalize
 your experience.
 &lt;/ FieldDescription &gt;
 { isInvalid &amp;&amp; &lt; FieldError errors = { field.state.meta.errors } /&gt; }
 &lt;/ Field &gt;
 )
 } }
 /&gt;
 Select #

 For select components, use field.state.value and field.handleChange on the &lt;Select /&gt; component.
 To show errors, add the aria-invalid prop to the &lt;SelectTrigger /&gt; component and the data-invalid prop to the &lt;Field /&gt; component.

 Language Preferences Select your preferred spoken language. Spoken Language For best results, select the language you speak. Select Reset Save Copy "use client"

 import { useForm } from "@tanstack/react-form" View Code
 form.tsx Copy &lt; form.Field
 name = &quot;language&quot;
 children = { ( field ) =&gt; {
 const isInvalid = field.state.meta.isTouched &amp;&amp; ! field.state.meta.isValid
 return (
 &lt; Field orientation = &quot;responsive&quot; data-invalid = { isInvalid } &gt;
 &lt; FieldContent &gt;
 &lt; FieldLabel htmlFor = &quot;form-tanstack-select-language&quot; &gt;
 Spoken Language
 &lt;/ FieldLabel &gt;
 &lt; FieldDescription &gt;
 For best results, select the language you speak.
 &lt;/ FieldDescription &gt;
 { isInvalid &amp;&amp; &lt; FieldError errors = { field.state.meta.errors } /&gt; }
 &lt;/ FieldContent &gt;
 &lt; Select
 name = { field.name }
 value = { field.state.value }
 onValueChange = { field.handleChange }
 &gt;
 &lt; SelectTrigger
 id = &quot;form-tanstack-select-language&quot;
 aria-invalid = { isInvalid }
 className = &quot;min-w-[120px]&quot;
 &gt;
 &lt; SelectValue placeholder = &quot;Select&quot; /&gt;
 &lt;/ SelectTrigger &gt;
 &lt; SelectContent position = &quot;item-aligned&quot; &gt;
 &lt; SelectItem value = &quot;auto&quot; &gt;Auto&lt;/ SelectItem &gt;
 &lt; SelectItem value = &quot;en&quot; &gt;English&lt;/ SelectItem &gt;
 &lt;/ SelectContent &gt;
 &lt;/ Select &gt;
 &lt;/ Field &gt;
 )
 } }
 /&gt;
 Checkbox #

 For checkbox, use field.state.value and field.handleChange on the &lt;Checkbox /&gt; component.
 To show errors, add the aria-invalid prop to the &lt;Checkbox /&gt; component and the data-invalid prop to the &lt;Field /&gt; component.
 For checkbox arrays, use mode=&quot;array&quot; on the &lt;form.Field /&gt; component and TanStack Form&#x27;s array helpers.
 Remember to add data-slot=&quot;checkbox-group&quot; to the &lt;FieldGroup /&gt; component for proper styling and spacing.

 Notifications Manage your notification preferences. Responses Get notified for requests that take time, like research or image generation. Push notifications Tasks Get notified when tasks you&#x27;ve created have updates. Push notifications Email notifications Reset Save Copy "use client"

 import { useForm } from "@tanstack/react-form" View Code
 form.tsx Copy &lt; form.Field
 name = &quot;tasks&quot;
 mode = &quot;array&quot;
 children = { ( field ) =&gt; {
 const isInvalid = field.state.meta.isTouched &amp;&amp; ! field.state.meta.isValid
 return (
 &lt; FieldSet &gt;
 &lt; FieldLegend variant = &quot;label&quot; &gt;Tasks&lt;/ FieldLegend &gt;
 &lt; FieldDescription &gt;
 Get notified when tasks you &amp;apos; ve created have updates.
 &lt;/ FieldDescription &gt;
 &lt; FieldGroup data-slot = &quot;checkbox-group&quot; &gt;
 { tasks. map (( task ) =&gt; (
 &lt; Field
 key = { task.id }
 orientation = &quot;horizontal&quot;
 data-invalid = { isInvalid }
 &gt;
 &lt; Checkbox
 id = { `form-tanstack-checkbox-${ task . id }` }
 name = { field.name }
 aria-invalid = { isInvalid }
 checked = { field.state.value. includes (task.id) }
 onCheckedChange = { ( checked ) =&gt; {
 if (checked) {
 field. pushValue (task.id)
 } else {
 const index = field.state.value. indexOf (task.id)
 if (index &gt; - 1 ) {
 field. removeValue (index)
 }
 }
 } }
 /&gt;
 &lt; FieldLabel
 htmlFor = { `form-tanstack-checkbox-${ task . id }` }
 className = &quot;font-normal&quot;
 &gt;
 { task.label }
 &lt;/ FieldLabel &gt;
 &lt;/ Field &gt;
 )) }
 &lt;/ FieldGroup &gt;
 { isInvalid &amp;&amp; &lt; FieldError errors = { field.state.meta.errors } /&gt; }
 &lt;/ FieldSet &gt;
 )
 } }
 /&gt;
 Radio Group #

 For radio groups, use field.state.value and field.handleChange on the &lt;RadioGroup /&gt; component.
 To show errors, add the aria-invalid prop to the &lt;RadioGroupItem /&gt; component and the data-invalid prop to the &lt;Field /&gt; component.

 Subscription Plan See pricing and features for each plan. Plan You can upgrade or downgrade your plan at any time. Starter (100K tokens/month) For everyday use with basic features. Pro (1M tokens/month) For advanced AI usage with more features. Enterprise (Unlimited tokens) For large teams and heavy usage. Reset Save Copy "use client"

 import { useForm } from "@tanstack/react-form" View Code
 form.tsx Copy &lt; form.Field
 name = &quot;plan&quot;
 children = { ( field ) =&gt; {
 const isInvalid = field.state.meta.isTouched &amp;&amp; ! field.state.meta.isValid
 return (
 &lt; FieldSet &gt;
 &lt; FieldLegend &gt;Plan&lt;/ FieldLegend &gt;
 &lt; FieldDescription &gt;
 You can upgrade or downgrade your plan at any time.
 &lt;/ FieldDescription &gt;
 &lt; RadioGroup
 name = { field.name }
 value = { field.state.value }
 onValueChange = { field.handleChange }
 &gt;
 { plans. map (( plan ) =&gt; (
 &lt; FieldLabel
 key = { plan.id }
 htmlFor = { `form-tanstack-radiogroup-${ plan . id }` }
 &gt;
 &lt; Field orientation = &quot;horizontal&quot; data-invalid = { isInvalid } &gt;
 &lt; FieldContent &gt;
 &lt; FieldTitle &gt; { plan.title } &lt;/ FieldTitle &gt;
 &lt; FieldDescription &gt; { plan.description } &lt;/ FieldDescription &gt;
 &lt;/ FieldContent &gt;
 &lt; RadioGroupItem
 value = { plan.id }
 id = { `form-tanstack-radiogroup-${ plan . id }` }
 aria-invalid = { isInvalid }
 /&gt;
 &lt;/ Field &gt;
 &lt;/ FieldLabel &gt;
 )) }
 &lt;/ RadioGroup &gt;
 { isInvalid &amp;&amp; &lt; FieldError errors = { field.state.meta.errors } /&gt; }
 &lt;/ FieldSet &gt;
 )
 } }
 /&gt;
 Switch #

 For switches, use field.state.value and field.handleChange on the &lt;Switch /&gt; component.
 To show errors, add the aria-invalid prop to the &lt;Switch /&gt; component and the data-invalid prop to the &lt;Field /&gt; component.

 Security Settings Manage your account security preferences. Multi-factor authentication Enable multi-factor authentication to secure your account. Reset Save Copy "use client"

 import { useForm } from "@tanstack/react-form" View Code
 form.tsx Copy &lt; form.Field
 name = &quot;twoFactor&quot;
 children = { ( field ) =&gt; {
 const isInvalid = field.state.meta.isTouched &amp;&amp; ! field.state.meta.isValid
 return (
 &lt; Field orientation = &quot;horizontal&quot; data-invalid = { isInvalid } &gt;
 &lt; FieldContent &gt;
 &lt; FieldLabel htmlFor = &quot;form-tanstack-switch-twoFactor&quot; &gt;
 Multi-factor authentication
 &lt;/ FieldLabel &gt;
 &lt; FieldDescription &gt;
 Enable multi-factor authentication to secure your account.
 &lt;/ FieldDescription &gt;
 { isInvalid &amp;&amp; &lt; FieldError errors = { field.state.meta.errors } /&gt; }
 &lt;/ FieldContent &gt;
 &lt; Switch
 id = &quot;form-tanstack-switch-twoFactor&quot;
 name = { field.name }
 checked = { field.state.value }
 onCheckedChange = { field.handleChange }
 aria-invalid = { isInvalid }
 /&gt;
 &lt;/ Field &gt;
 )
 } }
 /&gt;
 Complex Forms #
 Here is an example of a more complex form with multiple fields and validation.
 Subscription Plan Choose your subscription plan. Basic For individuals and small teams Pro For businesses with higher demands Billing Period Choose how often you want to be billed. Add-ons Select additional features you&#x27;d like to include. Analytics Advanced analytics and reporting Backup Automated daily backups Priority Support 24/7 premium customer support Email Notifications Receive email updates about your subscription Save Preferences Copy "use client"

 import * as React from "react" View Code
 Resetting the Form #
 Use form.reset() to reset the form to its default values.
 Copy &lt; Button type = &quot;button&quot; variant = &quot;outline&quot; onClick = { () =&gt; form. reset () } &gt;
 Reset
 &lt;/ Button &gt;
 Array Fields #
 TanStack Form provides powerful array field management with mode=&quot;array&quot; . This allows you to dynamically add, remove, and update array items with full validation support.
 Contact Emails Manage your contact email addresses. Email Addresses Add up to 5 email addresses where we can contact you. Add Email Address Reset Save Copy "use client"

 import * as React from "react" View Code
 This example demonstrates managing multiple email addresses with array fields. Users can add up to 5 email addresses, remove individual addresses, and each address is validated independently.
 Array Field Structure #
 Use mode=&quot;array&quot; on the parent field to enable array field management.
 form.tsx Copy &lt; form.Field
 name = &quot;emails&quot;
 mode = &quot;array&quot;
 children = { ( field ) =&gt; {
 return (
 &lt; FieldSet &gt;
 &lt; FieldLegend variant = &quot;label&quot; &gt;Email Addresses&lt;/ FieldLegend &gt;
 &lt; FieldDescription &gt;
 Add up to 5 email addresses where we can contact you.
 &lt;/ FieldDescription &gt;
 &lt; FieldGroup &gt;
 { field.state.value. map (( _ , index ) =&gt; (
 // Nested field for each array item
 )) }
 &lt;/ FieldGroup &gt;
 &lt;/ FieldSet &gt;
 )
 } }
 /&gt;
 Nested Fields #
 Access individual array items using bracket notation: fieldName[index].propertyName . This example uses InputGroup to display the remove button inline with the input.
 form.tsx Copy &lt; form.Field
 name = { `emails[${ index }].address` }
 children = { ( subField ) =&gt; {
 const isSubFieldInvalid =
 subField.state.meta.isTouched &amp;&amp; ! subField.state.meta.isValid
 return (
 &lt; Field orientation = &quot;horizontal&quot; data-invalid = { isSubFieldInvalid } &gt;
 &lt; FieldContent &gt;
 &lt; InputGroup &gt;
 &lt; InputGroupInput
 id = { `form-tanstack-array-email-${ index }` }
 name = { subField.name }
 value = { subField.state.value }
 onBlur = { subField.handleBlur }
 onChange = { ( e ) =&gt; subField. handleChange (e.target.value) }
 aria-invalid = { isSubFieldInvalid }
 placeholder = &quot;name@example.com&quot;
 type = &quot;email&quot;
 /&gt;
 { field.state.value. length &gt; 1 &amp;&amp; (
 &lt; InputGroupAddon align = &quot;inline-end&quot; &gt;
 &lt; InputGroupButton
 type = &quot;button&quot;
 variant = &quot;ghost&quot;
 size = &quot;icon-xs&quot;
 onClick = { () =&gt; field. removeValue (index) }
 aria-label = { `Remove email ${ index + 1 }` }
 &gt;
 &lt; XIcon /&gt;
 &lt;/ InputGroupButton &gt;
 &lt;/ InputGroupAddon &gt;
 ) }
 &lt;/ InputGroup &gt;
 { isSubFieldInvalid &amp;&amp; (
 &lt; FieldError errors = { subField.state.meta.errors } /&gt;
 ) }
 &lt;/ FieldContent &gt;
 &lt;/ Field &gt;
 )
 } }
 /&gt;
 Adding Items #
 Use field.pushValue(item) to add items to an array field. You can disable the button when the array reaches its maximum length.
 form.tsx Copy &lt; Button
 type = &quot;button&quot;
 variant = &quot;outline&quot;
 size = &quot;sm&quot;
 onClick = { () =&gt; field. pushValue ({ address: &quot;&quot; }) }
 disabled = { field.state.value. length &gt;= 5 }
 &gt;
 Add Email Address
 &lt;/ Button &gt;
 Removing Items #
 Use field.removeValue(index) to remove items from an array field. You can conditionally show the remove button only when there&#x27;s more than one item.
 form.tsx Copy {
 field.state.value. length &gt; 1 &amp;&amp; (
 &lt; InputGroupButton
 onClick = { () =&gt; field. removeValue (index) }
 aria-label = { `Remove email ${ index + 1 }` }
 &gt;
 &lt; XIcon /&gt;
 &lt;/ InputGroupButton &gt;
 )
 }
 Array Validation #
 Validate array fields using Zod&#x27;s array methods.
 form.tsx Copy const formSchema = z. object ({
 emails: z
 . array (
 z. object ({
 address: z. string (). email ( &quot;Enter a valid email address.&quot; ),
 })
 )
 . min ( 1 , &quot;Add at least one email address.&quot; )
 . max ( 5 , &quot;You can add up to 5 email addresses.&quot; ),
 }) React Hook Form Formisch On This Page Demo Approach Anatomy Form Create a schema Set up the form Build the form Done Validation Client-side Validation Validation Modes Displaying Errors Working with Different Field Types Input Textarea Select Checkbox Radio Group Switch Complex Forms Resetting the Form Array Fields Array Field Structure Nested Fields Adding Items Removing Items Array Validation Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
