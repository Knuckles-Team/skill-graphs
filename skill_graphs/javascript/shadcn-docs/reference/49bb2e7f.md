React Hook Form - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json React Hook Form Copy Page Previous Next Build forms in React using React Hook Form and Zod. In this guide, we will take a look at building forms with React Hook Form. We&#x27;ll cover building forms with the &lt;Field /&gt; component, adding schema validation using Zod, error handling, accessibility, and more.
 Demo #
 We are going to build the following form. It has a simple text input and a textarea. On submit, we&#x27;ll validate the form data and display any errors.
 Note: For the purpose of this demo, we have intentionally disabled browser
validation to show how schema validation and form errors work in React Hook
Form. It is recommended to add basic browser validation in your production
code.
 Bug Report Help us improve by reporting bugs you encounter. Bug Title Description 0 /100 characters Include steps to reproduce, expected behavior, and what actually happened. Reset Submit Copy "use client"

 import * as React from "react" View Code
 Approach #
 This form leverages React Hook Form for performant, flexible form handling. We&#x27;ll build our form using the &lt;Field /&gt; component, which gives you complete flexibility over the markup and styling .

 Uses React Hook Form&#x27;s useForm hook for form state management.
 &lt;Controller /&gt; component for controlled inputs.
 &lt;Field /&gt; components for building accessible forms.
 Client-side validation using Zod with zodResolver .

 Anatomy #
 Here&#x27;s a basic example of a form using the &lt;Controller /&gt; component from React Hook Form and the &lt;Field /&gt; component.
 Copy &lt; Controller
 name = &quot;title&quot;
 control = { form.control }
 render = { ({ field , fieldState }) =&gt; (
 &lt; Field data-invalid = { fieldState.invalid } &gt;
 &lt; FieldLabel htmlFor = { field.name } &gt;Bug Title&lt;/ FieldLabel &gt;
 &lt; Input
 { ... field }
 id = { field.name }
 aria-invalid = { fieldState.invalid }
 placeholder = &quot;Login button not working on mobile&quot;
 autoComplete = &quot;off&quot;
 /&gt;
 &lt; FieldDescription &gt;
 Provide a concise title for your bug report.
 &lt;/ FieldDescription &gt;
 { fieldState.invalid &amp;&amp; &lt; FieldError errors = { [fieldState.error] } /&gt; }
 &lt;/ Field &gt;
 ) }
 /&gt;
 Form #
 Create a form schema #
 We&#x27;ll start by defining the shape of our form using a Zod schema.
 Note: This example uses zod v3 for schema validation, but you can
replace it with any other Standard Schema validation library supported by
React Hook Form.
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
 Next, we&#x27;ll use the useForm hook from React Hook Form to create our form instance. We&#x27;ll also add the Zod resolver to validate the form data.
 form.tsx Copy import { zodResolver } from &quot;@hookform/resolvers/zod&quot;
 import { useForm } from &quot;react-hook-form&quot;
 import * as z from &quot;zod&quot;

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

 export function BugReportForm () {
 const form = useForm &lt; z . infer &lt; typeof formSchema&gt;&gt;({
 resolver: zodResolver (formSchema),
 defaultValues: {
 title: &quot;&quot; ,
 description: &quot;&quot; ,
 },
 })

 function onSubmit ( data : z . infer &lt; typeof formSchema&gt;) {
 // Do something with the form values.
 console. log (data)
 }

 return (
 &lt; form onSubmit = { form. handleSubmit (onSubmit) } &gt;
 { /* ... */ }
 { /* Build the form here */ }
 { /* ... */ }
 &lt;/ form &gt;
 )
 }
 Build the form #
 We can now build the form using the &lt;Controller /&gt; component from React Hook Form and the &lt;Field /&gt; component.
 Expand form.tsx Copy "use client"

 import * as React from "react"
 import { zodResolver } from "@hookform/resolvers/zod"
 import { Controller, useForm } from "react-hook-form"
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
 const form = useForm &#x3C; z . infer &#x3C; typeof formSchema>>({
 resolver: zodResolver (formSchema),
 defaultValues: {
 title: "" ,
 description: "" ,
 },
 })

 function onSubmit ( data : z . infer &#x3C; typeof formSchema>) {
 toast ( "You submitted the following values:" , {
 description : (
 &#x3C; pre className = "mt-2 w-[320px] overflow-x-auto rounded-md bg-code p-4 text-code-foreground" >
 &#x3C; code >{ JSON . stringify (data, null , 2 )}&#x3C;/ code >
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
 }

 return (
 &#x3C; Card className = "w-full sm:max-w-md" >
 &#x3C; CardHeader >
 &#x3C; CardTitle >Bug Report&#x3C;/ CardTitle >
 &#x3C; CardDescription >
 Help us improve by reporting bugs you encounter.
 &#x3C;/ CardDescription >
 &#x3C;/ CardHeader >
 &#x3C; CardContent >
 &#x3C; form id = "form-rhf-demo" onSubmit = {form. handleSubmit (onSubmit)}>
 &#x3C; FieldGroup >
 &#x3C; Controller
 name = "title"
 control = {form.control}
 render = {({ field , fieldState }) => (
 &#x3C; Field data-invalid = {fieldState.invalid}>
 &#x3C; FieldLabel htmlFor = "form-rhf-demo-title" >
 Bug Title
 &#x3C;/ FieldLabel >
 &#x3C; Input
 { ... field}
 id = "form-rhf-demo-title"
 aria-invalid = {fieldState.invalid}
 placeholder = "Login button not working on mobile"
 autoComplete = "off"
 />
 {fieldState.invalid &#x26;&#x26; (
 &#x3C; FieldError errors = {[fieldState.error]} />
 )}
 &#x3C;/ Field >
 )}
 />
 &#x3C; Controller
 name = "description"
 control = {form.control}
 render = {({ field , fieldState }) => (
 &#x3C; Field data-invalid = {fieldState.invalid}>
 &#x3C; FieldLabel htmlFor = "form-rhf-demo-description" >
 Description
 &#x3C;/ FieldLabel >
 &#x3C; InputGroup >
 &#x3C; InputGroupTextarea
 { ... field}
 id = "form-rhf-demo-description"
 placeholder = "I'm having an issue with the login button on mobile."
 rows = { 6 }
 className = "min-h-24 resize-none"
 aria-invalid = {fieldState.invalid}
 />
 &#x3C; InputGroupAddon align = "block-end" >
 &#x3C; InputGroupText className = "tabular-nums" >
 {field.value. length }/100 characters
 &#x3C;/ InputGroupText >
 &#x3C;/ InputGroupAddon >
 &#x3C;/ InputGroup >
 &#x3C; FieldDescription >
 Include steps to reproduce, expected behavior, and what
 actually happened.
 &#x3C;/ FieldDescription >
 {fieldState.invalid &#x26;&#x26; (
 &#x3C; FieldError errors = {[fieldState.error]} />
 )}
 &#x3C;/ Field >
 )}
 />
 &#x3C;/ FieldGroup >
 &#x3C;/ form >
 &#x3C;/ CardContent >
 &#x3C; CardFooter >
 &#x3C; Field orientation = "horizontal" >
 &#x3C; Button type = "button" variant = "outline" onClick = {() => form. reset ()}>
 Reset
 &#x3C;/ Button >
 &#x3C; Button type = "submit" form = "form-rhf-demo" >
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
 When you submit the form, the onSubmit function will be called with the validated form data. If the form data is invalid, React Hook Form will display the errors next to each field.
 Validation #
 Client-side Validation #
 React Hook Form validates your form data using the Zod schema. Define a schema and pass it to the resolver option of the useForm hook.
 example-form.tsx Copy import { zodResolver } from &quot;@hookform/resolvers/zod&quot;
 import { useForm } from &quot;react-hook-form&quot;
 import * as z from &quot;zod&quot;

 const formSchema = z. object ({
 title: z. string (),
 description: z. string (). optional (),
 })

 export function ExampleForm () {
 const form = useForm &lt; z . infer &lt; typeof formSchema&gt;&gt;({
 resolver: zodResolver (formSchema),
 defaultValues: {
 title: &quot;&quot; ,
 description: &quot;&quot; ,
 },
 })
 }
 Validation Modes #
 React Hook Form supports different validation modes.
 form.tsx Copy const form = useForm &lt; z . infer &lt; typeof formSchema&gt;&gt;({
 resolver: zodResolver (formSchema),
 mode: &quot;onChange&quot; ,
 })
 Mode Description &quot;onChange&quot; Validation triggers on every change. &quot;onBlur&quot; Validation triggers on blur. &quot;onSubmit&quot; Validation triggers on submit (default). &quot;onTouched&quot; Validation triggers on first blur, then on every change. &quot;all&quot; Validation triggers on blur and change.
 Displaying Errors #
 Display errors next to the field using &lt;FieldError /&gt; . For styling and accessibility:

 Add the data-invalid prop to the &lt;Field /&gt; component.
 Add the aria-invalid prop to the form control such as &lt;Input /&gt; , &lt;SelectTrigger /&gt; , &lt;Checkbox /&gt; , etc.

 form.tsx Copy &lt; Controller
 name = &quot;email&quot;
 control = { form.control }
 render = { ({ field , fieldState }) =&gt; (
 &lt; Field data-invalid = { fieldState.invalid } &gt;
 &lt; FieldLabel htmlFor = { field.name } &gt;Email&lt;/ FieldLabel &gt;
 &lt; Input
 { ... field }
 id = { field.name }
 type = &quot;email&quot;
 aria-invalid = { fieldState.invalid }
 /&gt;
 { fieldState.invalid &amp;&amp; &lt; FieldError errors = { [fieldState.error] } /&gt; }
 &lt;/ Field &gt;
 ) }
 /&gt;
 Working with Different Field Types #
 Input #

 For input fields, spread the field object onto the &lt;Input /&gt; component.
 To show errors, add the aria-invalid prop to the &lt;Input /&gt; component and the data-invalid prop to the &lt;Field /&gt; component.

 Profile Settings Update your profile information below. Username This is your public display name. Must be between 3 and 10 characters. Must only contain letters, numbers, and underscores. Reset Save Copy "use client"

 import { zodResolver } from "@hookform/resolvers/zod" View Code
 For simple text inputs, spread the field object onto the input.
 form.tsx Copy &lt; Controller
 name = &quot;name&quot;
 control = { form.control }
 render = { ({ field , fieldState }) =&gt; (
 &lt; Field data-invalid = { fieldState.invalid } &gt;
 &lt; FieldLabel htmlFor = { field.name } &gt;Name&lt;/ FieldLabel &gt;
 &lt; Input { ... field } id = { field.name } aria-invalid = { fieldState.invalid } /&gt;
 { fieldState.invalid &amp;&amp; &lt; FieldError errors = { [fieldState.error] } /&gt; }
 &lt;/ Field &gt;
 ) }
 /&gt;
 Textarea #

 For textarea fields, spread the field object onto the &lt;Textarea /&gt; component.
 To show errors, add the aria-invalid prop to the &lt;Textarea /&gt; component and the data-invalid prop to the &lt;Field /&gt; component.

 Personalization Customize your experience by telling us more about yourself. More about you Tell us more about yourself. This will be used to help us personalize your experience. Reset Save Copy "use client"

 import * as React from "react" View Code
 For textarea fields, spread the field object onto the textarea.
 form.tsx Copy &lt; Controller
 name = &quot;about&quot;
 control = { form.control }
 render = { ({ field , fieldState }) =&gt; (
 &lt; Field data-invalid = { fieldState.invalid } &gt;
 &lt; FieldLabel htmlFor = &quot;form-rhf-textarea-about&quot; &gt;More about you&lt;/ FieldLabel &gt;
 &lt; Textarea
 { ... field }
 id = &quot;form-rhf-textarea-about&quot;
 aria-invalid = { fieldState.invalid }
 placeholder = &quot;I&#x27;m a software engineer...&quot;
 className = &quot;min-h-[120px]&quot;
 /&gt;
 &lt; FieldDescription &gt;
 Tell us more about yourself. This will be used to help us personalize
 your experience.
 &lt;/ FieldDescription &gt;
 { fieldState.invalid &amp;&amp; &lt; FieldError errors = { [fieldState.error] } /&gt; }
 &lt;/ Field &gt;
 ) }
 /&gt;
 Select #

 For select components, use field.value and field.onChange on the &lt;Select /&gt; component.
 To show errors, add the aria-invalid prop to the &lt;SelectTrigger /&gt; component and the data-invalid prop to the &lt;Field /&gt; component.

 Language Preferences Select your preferred spoken language. Spoken Language For best results, select the language you speak. Select Reset Save Copy "use client"

 import * as React from "react" View Code
 form.tsx Copy &lt; Controller
 name = &quot;language&quot;
 control = { form.control }
 render = { ({ field , fieldState }) =&gt; (
 &lt; Field orientation = &quot;responsive&quot; data-invalid = { fieldState.invalid } &gt;
 &lt; FieldContent &gt;
 &lt; FieldLabel htmlFor = &quot;form-rhf-select-language&quot; &gt;
 Spoken Language
 &lt;/ FieldLabel &gt;
 &lt; FieldDescription &gt;
 For best results, select the language you speak.
 &lt;/ FieldDescription &gt;
 { fieldState.invalid &amp;&amp; &lt; FieldError errors = { [fieldState.error] } /&gt; }
 &lt;/ FieldContent &gt;
 &lt; Select
 name = { field.name }
 value = { field.value }
 onValueChange = { field.onChange }
 &gt;
 &lt; SelectTrigger
 id = &quot;form-rhf-select-language&quot;
 aria-invalid = { fieldState.invalid }
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
 ) }
 /&gt;
 Checkbox #

 For checkbox arrays, use field.value and field.onChange with array manipulation.
 To show errors, add the aria-invalid prop to the &lt;Checkbox /&gt; component and the data-invalid prop to the &lt;Field /&gt; component.
 Remember to add data-slot=&quot;checkbox-group&quot; to the &lt;FieldGroup /&gt; component for proper styling and spacing.

 Notifications Manage your notification preferences. Responses Get notified for requests that take time, like research or image generation. Push notifications Tasks Get notified when tasks you&#x27;ve created have updates. Push notifications Email notifications Reset Save Copy "use client"

 import * as React from "react" View Code
 form.tsx Copy &lt; Controller
 name = &quot;tasks&quot;
 control = { form.control }
 render = { ({ field , fieldState }) =&gt; (
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
 data-invalid = { fieldState.invalid }
 &gt;
 &lt; Checkbox
 id = { `form-rhf-checkbox-${ task . id }` }
 name = { field.name }
 aria-invalid = { fieldState.invalid }
 checked = { field.value. includes (task.id) }
 onCheckedChange = { ( checked ) =&gt; {
 const newValue = checked
 ? [ ... field.value, task.id]
 : field.value. filter (( value ) =&gt; value !== task.id)
 field. onChange (newValue)
 } }
 /&gt;
 &lt; FieldLabel
 htmlFor = { `form-rhf-checkbox-${ task . id }` }
 className = &quot;font-normal&quot;
 &gt;
 { task.label }
 &lt;/ FieldLabel &gt;
 &lt;/ Field &gt;
 )) }
 &lt;/ FieldGroup &gt;
 { fieldState.invalid &amp;&amp; &lt; FieldError errors = { [fieldState.error] } /&gt; }
 &lt;/ FieldSet &gt;
 ) }
 /&gt;
 Radio Group #

 For radio groups, use field.value and field.onChange on the &lt;RadioGroup /&gt; component.
 To show errors, add the aria-invalid prop to the &lt;RadioGroupItem /&gt; component and the data-invalid prop to the &lt;Field /&gt; component.

 Subscription Plan See pricing and features for each plan. Plan You can upgrade or downgrade your plan at any time. Starter (100K tokens/month) For everyday use with basic features. Pro (1M tokens/month) For advanced AI usage with more features. Enterprise (Unlimited tokens) For large teams and heavy usage. Reset Save Copy "use client"

 import * as React from "react" View Code
 form.tsx Copy &lt; Controller
 name = &quot;plan&quot;
 control = { form.control }
 render = { ({ field , fieldState }) =&gt; (
 &lt; FieldSet &gt;
 &lt; FieldLegend &gt;Plan&lt;/ FieldLegend &gt;
 &lt; FieldDescription &gt;
 You can upgrade or downgrade your plan at any time.
 &lt;/ FieldDescription &gt;
 &lt; RadioGroup
 name = { field.name }
 value = { field.value }
 onValueChange = { field.onChange }
 &gt;
 { plans. map (( plan ) =&gt; (
 &lt; FieldLabel key = { plan.id } htmlFor = { `form-rhf-radiogroup-${ plan . id }` } &gt;
 &lt; Field orientation = &quot;horizontal&quot; data-invalid = { fieldState.invalid } &gt;
 &lt; FieldContent &gt;
 &lt; FieldTitle &gt; { plan.title } &lt;/ FieldTitle &gt;
 &lt; FieldDescription &gt; { plan.description } &lt;/ FieldDescription &gt;
 &lt;/ FieldContent &gt;
 &lt; RadioGroupItem
 value = { plan.id }
 id = { `form-rhf-radiogroup-${ plan . id }` }
 aria-invalid = { fieldState.invalid }
 /&gt;
 &lt;/ Field &gt;
 &lt;/ FieldLabel &gt;
 )) }
 &lt;/ RadioGroup &gt;
 { fieldState.invalid &amp;&amp; &lt; FieldError errors = { [fieldState.error] } /&gt; }
 &lt;/ FieldSet &gt;
 ) }
 /&gt;
 Switch #

 For switches, use field.value and field.onChange on the &lt;Switch /&gt; component.
 To show errors, add the aria-invalid prop to the &lt;Switch /&gt; component and the data-invalid prop to the &lt;Field /&gt; component.

 Security Settings Manage your account security preferences. Multi-factor authentication Enable multi-factor authentication to secure your account. Reset Save Copy "use client"

 import * as React from "react" View Code
 form.tsx Copy &lt; Controller
 name = &quot;twoFactor&quot;
 control = { form.control }
 render = { ({ field , fieldState }) =&gt; (
 &lt; Field orientation = &quot;horizontal&quot; data-invalid = { fieldState.invalid } &gt;
 &lt; FieldContent &gt;
 &lt; FieldLabel htmlFor = &quot;form-rhf-switch-twoFactor&quot; &gt;
 Multi-factor authentication
 &lt;/ FieldLabel &gt;
 &lt; FieldDescription &gt;
 Enable multi-factor authentication to secure your account.
 &lt;/ FieldDescription &gt;
 { fieldState.invalid &amp;&amp; &lt; FieldError errors = { [fieldState.error] } /&gt; }
 &lt;/ FieldContent &gt;
 &lt; Switch
 id = &quot;form-rhf-switch-twoFactor&quot;
 name = { field.name }
 checked = { field.value }
 onCheckedChange = { field.onChange }
 aria-invalid = { fieldState.invalid }
 /&gt;
 &lt;/ Field &gt;
 ) }
 /&gt;
 Complex Forms #
 Here is an example of a more complex form with multiple fields and validation.
 You&#x27;re almost there! Choose your subscription plan and billing period. Subscription Plan Choose your subscription plan. Basic For individuals and small teams Pro For businesses with higher demands Billing Period Select Choose how often you want to be billed. Add-ons Select additional features you&#x27;d like to include. Analytics Advanced analytics and reporting Backup Automated daily backups Priority Support 24/7 premium customer support Email Notifications Receive email updates about your subscription Save Preferences Reset Copy "use client"

 import * as React from "react" View Code
 Resetting the Form #
 Use form.reset() to reset the form to its default values.
 Copy &lt; Button type = &quot;button&quot; variant = &quot;outline&quot; onClick = { () =&gt; form. reset () } &gt;
 Reset
 &lt;/ Button &gt;
 Array Fields #
 React Hook Form provides a useFieldArray hook for managing dynamic array fields. This is useful when you need to add or remove fields dynamically.
 Contact Emails Manage your contact email addresses. Email Addresses Add up to 5 email addresses where we can contact you. Add Email Address Reset Save Copy "use client"

 import * as React from "react" View Code
 Using useFieldArray #
 Use the useFieldArray hook to manage array fields. It provides fields , append , and remove methods.
 form.tsx Copy import { useFieldArray, useForm } from &quot;react-hook-form&quot;

 export function ExampleForm () {
 const form = useForm ({
 // ... form config
 })

 const { fields , append , remove } = useFieldArray ({
 control: form.control,
 name: &quot;emails&quot; ,
 })
 }
 Array Field Structure #
 Wrap your array fields in a &lt;FieldSet /&gt; with a &lt;FieldLegend /&gt; and &lt;FieldDescription /&gt; .
 form.tsx Copy &lt; FieldSet className = &quot;gap-4&quot; &gt;
 &lt; FieldLegend variant = &quot;label&quot; &gt;Email Addresses&lt;/ FieldLegend &gt;
 &lt; FieldDescription &gt;
 Add up to 5 email addresses where we can contact you.
 &lt;/ FieldDescription &gt;
 &lt; FieldGroup className = &quot;gap-4&quot; &gt; { /* Array items go here */ } &lt;/ FieldGroup &gt;
 &lt;/ FieldSet &gt;
 Controller Pattern for Array Items #
 Map over the fields array and use &lt;Controller /&gt; for each item. Make sure to use field.id as the key .
 form.tsx Copy {
 fields. map (( field , index ) =&gt; (
 &lt; Controller
 key = { field.id }
 name = { `emails.${ index }.address` }
 control = { form.control }
 render = { ({ field : controllerField , fieldState }) =&gt; (
 &lt; Field orientation = &quot;horizontal&quot; data-invalid = { fieldState.invalid } &gt;
 &lt; FieldContent &gt;
 &lt; InputGroup &gt;
 &lt; InputGroupInput
 { ... controllerField }
 id = { `form-rhf-array-email-${ index }` }
 aria-invalid = { fieldState.invalid }
 placeholder = &quot;name@example.com&quot;
 type = &quot;email&quot;
 autoComplete = &quot;email&quot;
 /&gt;
 { /* Remove button */ }
 &lt;/ InputGroup &gt;
 { fieldState.invalid &amp;&amp; &lt; FieldError errors = { [fieldState.error] } /&gt; }
 &lt;/ FieldContent &gt;
 &lt;/ Field &gt;
 ) }
 /&gt;
 ))
 }
 Adding Items #
 Use the append method to add new items to the array.
 form.tsx Copy &lt; Button
 type = &quot;button&quot;
 variant = &quot;outline&quot;
 size = &quot;sm&quot;
 onClick = { () =&gt; append ({ address: &quot;&quot; }) }
 disabled = { fields. length &gt;= 5 }
 &gt;
 Add Email Address
 &lt;/ Button &gt;
 Removing Items #
 Use the remove method to remove items from the array. Add the remove button conditionally.
 form.tsx Copy {
 fields. length &gt; 1 &amp;&amp; (
 &lt; InputGroupAddon align = &quot;inline-end&quot; &gt;
 &lt; InputGroupButton
 type = &quot;button&quot;
 variant = &quot;ghost&quot;
 size = &quot;icon-xs&quot;
 onClick = { () =&gt; remove (index) }
 aria-label = { `Remove email ${ index + 1 }` }
 &gt;
 &lt; XIcon /&gt;
 &lt;/ InputGroupButton &gt;
 &lt;/ InputGroupAddon &gt;
 )
 }
 Array Validation #
 Use Zod&#x27;s array method to validate array fields.
 form.tsx Copy const formSchema = z. object ({
 emails: z
 . array (
 z. object ({
 address: z. string (). email ( &quot;Enter a valid email address.&quot; ),
 })
 )
 . min ( 1 , &quot;Add at least one email address.&quot; )
 . max ( 5 , &quot;You can add up to 5 email addresses.&quot; ),
 }) Forms TanStack Form On This Page Demo Approach Anatomy Form Create a form schema Set up the form Build the form Done Validation Client-side Validation Validation Modes Displaying Errors Working with Different Field Types Input Textarea Select Checkbox Radio Group Switch Complex Forms Resetting the Form Array Fields Using useFieldArray Array Field Structure Controller Pattern for Array Items Adding Items Removing Items Array Validation Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
