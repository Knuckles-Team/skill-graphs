Formisch - shadcn/ui Toggle Menu Menu Home Docs Components Blocks Charts Directory Create Search documentation... Search... 117k Toggle theme New Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Package Imports Theming Dark Mode CLI Monorepo Skills JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Formisch Registry Introduction Getting Started GitHub Registries Registry Directory Examples Namespaces Authentication MCP Server Open in v0 API Reference registry.json registry-item.json Formisch Copy Page Previous Next Build forms in React using Formisch and Valibot. This guide covers building forms with Formisch , the lightweight, schema-first, and fully type-safe form library for React. We&#x27;ll create forms with the &lt;Field /&gt; component, validate them with Valibot schemas, handle errors, and ensure accessibility.
 Demo #
 We&#x27;ll build the following form. It has a simple text input and a textarea. On submit, we&#x27;ll validate the form data and display any errors.
 Note: For the purpose of this demo, we have intentionally disabled browser
validation to show how schema validation and form errors work in Formisch. It
is recommended to add basic browser validation in your production code.
 Bug Report Help us improve by reporting bugs you encounter. Bug Title Description 0 /100 characters Include steps to reproduce, expected behavior, and what actually happened. Reset Submit Copy "use client"

 import * as React from "react" View Code
 Approach #
 This form leverages Formisch for headless, schema-first form handling. We&#x27;ll build our form using the &lt;Field /&gt; component, which gives you complete flexibility over the markup and styling .

 Uses Formisch&#x27;s useForm hook for form state management.
 &lt;Form /&gt; component to wrap the native &lt;form&gt; element with submit handling.
 &lt;Field /&gt; render-prop component for controlled inputs.
 Schema validation using Valibot .
 Type-safe field paths inferred from the schema.

 Form Methods #
 Formisch exposes form operations as top-level functions rather than methods on a form object. Import only what you need:
 Copy import { getInput, insert, reset, submit } from &quot;@formisch/react&quot;
 Every method follows the same signature: the first parameter is always the form store , and the second parameter (if necessary) is always a config object .
 Copy // Read a field value
 const email = getInput (form, { path: [ &quot;email&quot; ] })

 // Reset the form with new initial values
 reset (form, { initialInput: { email: &quot;&quot; , password: &quot;&quot; } })

 // Move an item in a field array
 move (form, { path: [ &quot;items&quot; ], from: 0 , to: 3 })
 This design keeps the API flexible and consistent across all methods. You&#x27;ll see the same (form, config) shape used throughout this guide for reading state ( getInput , getErrors ), writing state ( setInput , setErrors ), form control ( submit , validate , focus ), and array operations ( insert , remove , move , swap , replace ). See the full methods reference for details.
 Anatomy #
 Here&#x27;s a basic example of a form using the &lt;Field /&gt; component from Formisch and the shadcn &lt;Field /&gt; component.
 Copy &lt; Form of = { form } onSubmit = { handleSubmit } &gt;
 &lt; FieldGroup &gt;
 &lt; FormischField of = { form } path = { [ &quot;title&quot; ] } &gt;
 { ( field ) =&gt; (
 &lt; Field data-invalid = { field.errors !== null } &gt;
 &lt; FieldLabel htmlFor = &quot;form-title&quot; &gt;Bug Title&lt;/ FieldLabel &gt;
 &lt; Input
 { ... field.props }
 id = &quot;form-title&quot;
 value = { field.input }
 aria-invalid = { field.errors !== null }
 placeholder = &quot;Login button not working on mobile&quot;
 autoComplete = &quot;off&quot;
 /&gt;
 &lt; FieldDescription &gt;
 Provide a concise title for your bug report.
 &lt;/ FieldDescription &gt;
 { field.errors &amp;&amp; (
 &lt; FieldError errors = { field.errors. map (( message ) =&gt; ({ message })) } /&gt;
 ) }
 &lt;/ Field &gt;
 ) }
 &lt;/ FormischField &gt;
 &lt;/ FieldGroup &gt;
 &lt;/ Form &gt;
 Note: Formisch ships its own Field component. To avoid a name clash with
the shadcn Field , the examples below import the Formisch one as
 FormischField and keep the shadcn Field under its original name. In your
own code you can alias either side — just be consistent.
 Form #
 Create a form schema #
 We&#x27;ll start by defining the shape of our form using a Valibot schema. Formisch infers all input and output types directly from this schema.
 form.tsx Copy import * as v from &quot;valibot&quot;

 const FormSchema = v. object ({
 title: v. pipe (
 v. string (),
 v. minLength ( 5 , &quot;Bug title must be at least 5 characters.&quot; ),
 v. maxLength ( 32 , &quot;Bug title must be at most 32 characters.&quot; )
 ),
 description: v. pipe (
 v. string (),
 v. minLength ( 20 , &quot;Description must be at least 20 characters.&quot; ),
 v. maxLength ( 100 , &quot;Description must be at most 100 characters.&quot; )
 ),
 })
 Set up the form #
 Next, we&#x27;ll use the useForm hook from Formisch to create our form instance. The schema is passed directly to useForm — there is no resolver step.
 form.tsx Copy import { Form, Field as FormischField, useForm } from &quot;@formisch/react&quot;
 import type { SubmitHandler } from &quot;@formisch/react&quot;
 import * as v from &quot;valibot&quot;

 const FormSchema = v. object ({
 title: v. pipe (
 v. string (),
 v. minLength ( 5 , &quot;Bug title must be at least 5 characters.&quot; ),
 v. maxLength ( 32 , &quot;Bug title must be at most 32 characters.&quot; )
 ),
 description: v. pipe (
 v. string (),
 v. minLength ( 20 , &quot;Description must be at least 20 characters.&quot; ),
 v. maxLength ( 100 , &quot;Description must be at most 100 characters.&quot; )
 ),
 })

 export function BugReportForm () {
 const form = useForm ({
 schema: FormSchema,
 initialInput: {
 title: &quot;&quot; ,
 description: &quot;&quot; ,
 },
 })

 const handleSubmit : SubmitHandler &lt; typeof FormSchema&gt; = ( output ) =&gt; {
 // Do something with the validated form values.
 console. log (output)
 }

 return (
 &lt; Form of = { form } onSubmit = { handleSubmit } &gt;
 { /* ... */ }
 { /* Build the form here */ }
 { /* ... */ }
 &lt;/ Form &gt;
 )
 }
 The &lt;Form /&gt; component wraps a native &lt;form&gt; element. It calls event.preventDefault() , runs validation, and only invokes onSubmit when the data is valid. The output you receive is fully typed from the schema.
 Build the form #
 We can now build the form using the &lt;Field /&gt; component from Formisch and the shadcn &lt;Field /&gt; component.
 Expand form.tsx Copy "use client"

 import * as React from "react"
 import { Form, Field as FormischField, reset, useForm } from "@formisch/react"
 import type { SubmitHandler } from "@formisch/react"
 import { toast } from "sonner"
 import * as v from "valibot"

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

 const FormSchema = v. object ({
 title: v. pipe (
 v. string (),
 v. minLength ( 5 , "Bug title must be at least 5 characters." ),
 v. maxLength ( 32 , "Bug title must be at most 32 characters." )
 ),
 description: v. pipe (
 v. string (),
 v. minLength ( 20 , "Description must be at least 20 characters." ),
 v. maxLength ( 100 , "Description must be at most 100 characters." )
 ),
 })

 export function BugReportForm () {
 const form = useForm ({
 schema: FormSchema,
 initialInput: {
 title: "" ,
 description: "" ,
 },
 })

 const handleSubmit : SubmitHandler &#x3C; typeof FormSchema> = ( output ) => {
 toast ( "You submitted the following values:" , {
 description : (
 &#x3C; pre className = "mt-2 w-[320px] overflow-x-auto rounded-md bg-code p-4 text-code-foreground" >
 &#x3C; code >{ JSON . stringify (output, null , 2 )}&#x3C;/ code >
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
 &#x3C; Form of = {form} id = "form-formisch-demo" onSubmit = {handleSubmit}>
 &#x3C; FieldGroup >
 &#x3C; FormischField of = {form} path = {[ "title" ]}>
 {( field ) => (
 &#x3C; Field data-invalid = {field.errors !== null }>
 &#x3C; FieldLabel htmlFor = "form-formisch-demo-title" >
 Bug Title
 &#x3C;/ FieldLabel >
 &#x3C; Input
 { ... field.props}
 id = "form-formisch-demo-title"
 value = {field.input ?? "" }
 aria-invalid = {field.errors !== null }
 placeholder = "Login button not working on mobile"
 autoComplete = "off"
 />
 {field.errors &#x26;&#x26; (
 &#x3C; FieldError
 errors = {field.errors. map (( message ) => ({ message }))}
 />
 )}
 &#x3C;/ Field >
 )}
 &#x3C;/ FormischField >
 &#x3C; FormischField of = {form} path = {[ "description" ]}>
 {( field ) => (
 &#x3C; Field data-invalid = {field.errors !== null }>
 &#x3C; FieldLabel htmlFor = "form-formisch-demo-description" >
 Description
 &#x3C;/ FieldLabel >
 &#x3C; InputGroup >
 &#x3C; InputGroupTextarea
 { ... field.props}
 id = "form-formisch-demo-description"
 value = {field.input ?? "" }
 placeholder = "I'm having an issue with the login button on mobile."
 rows = { 6 }
 className = "min-h-24 resize-none"
 aria-invalid = {field.errors !== null }
 />
 &#x3C; InputGroupAddon align = "block-end" >
 &#x3C; InputGroupText className = "tabular-nums" >
 {(field.input ?? "" ). length }/100 characters
 &#x3C;/ InputGroupText >
 &#x3C;/ InputGroupAddon >
 &#x3C;/ InputGroup >
 &#x3C; FieldDescription >
 Include steps to reproduce, expected behavior, and what
 actually happened.
 &#x3C;/ FieldDescription >
 {field.errors &#x26;&#x26; (
 &#x3C; FieldError
 errors = {field.errors. map (( message ) => ({ message }))}
 />
 )}
 &#x3C;/ Field >
 )}
 &#x3C;/ FormischField >
 &#x3C;/ FieldGroup >
 &#x3C;/ Form >
 &#x3C;/ CardContent >
 &#x3C; CardFooter >
 &#x3C; Field orientation = "horizontal" >
 &#x3C; Button type = "button" variant = "outline" onClick = {() => reset (form)}>
 Reset
 &#x3C;/ Button >
 &#x3C; Button type = "submit" form = "form-formisch-demo" >
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
 When you submit the form, the handleSubmit function will be called with the validated form data. If the form data is invalid, Formisch will populate field.errors for each invalid field and the UI will display them.
 Validation #
 Client-side Validation #
 Formisch validates your form data using the Valibot schema you pass to useForm . There is no resolver — the schema is the single source of truth for both runtime validation and static types.
 form.tsx Copy import { useForm } from &quot;@formisch/react&quot;

 const FormSchema = v. object ({
 title: v. string (),
 description: v. optional (v. string ()),
 })

 export function ExampleForm () {
 const form = useForm ({
 schema: FormSchema,
 initialInput: {
 title: &quot;&quot; ,
 description: &quot;&quot; ,
 },
 })
 }
 Validation Modes #
 Formisch separates the first validation from subsequent validations. You configure them with the validate and revalidate options on useForm .
 form.tsx Copy const form = useForm ({
 schema: FormSchema,
 validate: &quot;blur&quot; ,
 revalidate: &quot;input&quot; ,
 })
 Option Value Description validate &quot;submit&quot; Validate on form submission (default). validate &quot;blur&quot; Validate when a field loses focus. validate &quot;input&quot; Validate on every input change. validate &quot;initial&quot; Validate immediately on form creation. revalidate &quot;input&quot; Revalidate on every input change after the first run (default). revalidate &quot;blur&quot; Revalidate on blur after the first run. revalidate &quot;submit&quot; Revalidate only on form submission.
 Displaying Errors #
 Display errors next to the field using &lt;FieldError /&gt; . Formisch returns errors as an array of strings, so map them to the shape &lt;FieldError /&gt; expects. For styling and accessibility:

 Add the data-invalid prop to the &lt;Field /&gt; component.
 Add the aria-invalid prop to the form control such as &lt;Input /&gt; , &lt;SelectTrigger /&gt; , &lt;Checkbox /&gt; , etc.

 form.tsx Copy &lt; FormischField of = { form } path = { [ &quot;email&quot; ] } &gt;
 { ( field ) =&gt; (
 &lt; Field data-invalid = { field.errors !== null } &gt;
 &lt; FieldLabel htmlFor = &quot;form-email&quot; &gt;Email&lt;/ FieldLabel &gt;
 &lt; Input
 { ... field.props }
 id = &quot;form-email&quot;
 value = { field.input }
 type = &quot;email&quot;
 aria-invalid = { field.errors !== null }
 /&gt;
 { field.errors &amp;&amp; (
 &lt; FieldError errors = { field.errors. map (( message ) =&gt; ({ message })) } /&gt;
 ) }
 &lt;/ Field &gt;
 ) }
 &lt;/ FormischField &gt;
 Working with Different Field Types #
 Formisch exposes two ways to bind a field to an element:

 Native HTML elements (like &lt;Input /&gt; and &lt;Textarea /&gt; ) — spread field.props and provide value={field.input} . Formisch wires up name , ref , onChange , onBlur , and onFocus for you.
 Component-library inputs (like Radix-based &lt;Select /&gt; , &lt;Checkbox /&gt; , &lt;RadioGroup /&gt; , &lt;Switch /&gt; ) — read the value from field.input and call field.onChange(value) to update it.

 Input #

 For input fields, spread field.props and provide value={field.input} .
 To show errors, add the aria-invalid prop to the &lt;Input /&gt; component and the data-invalid prop to the &lt;Field /&gt; component.

 Profile Settings Update your profile information below. Username This is your public display name. Must be between 3 and 10 characters. Must only contain letters, numbers, and underscores. Reset Save Copy "use client"

 import * as React from "react" View Code
 form.tsx Copy &lt; FormischField of = { form } path = { [ &quot;username&quot; ] } &gt;
 { ( field ) =&gt; (
 &lt; Field data-invalid = { field.errors !== null } &gt;
 &lt; FieldLabel htmlFor = &quot;form-username&quot; &gt;Username&lt;/ FieldLabel &gt;
 &lt; Input
 { ... field.props }
 id = &quot;form-username&quot;
 value = { field.input }
 aria-invalid = { field.errors !== null }
 /&gt;
 { field.errors &amp;&amp; (
 &lt; FieldError errors = { field.errors. map (( message ) =&gt; ({ message })) } /&gt;
 ) }
 &lt;/ Field &gt;
 ) }
 &lt;/ FormischField &gt;
 Textarea #

 For textarea fields, spread field.props and provide value={field.input} .
 To show errors, add the aria-invalid prop to the &lt;Textarea /&gt; component and the data-invalid prop to the &lt;Field /&gt; component.

 Personalization Customize your experience by telling us more about yourself. More about you Tell us more about yourself. This will be used to help us personalize your experience. Reset Save Copy "use client"

 import * as React from "react" View Code
 form.tsx Copy &lt; FormischField of = { form } path = { [ &quot;about&quot; ] } &gt;
 { ( field ) =&gt; (
 &lt; Field data-invalid = { field.errors !== null } &gt;
 &lt; FieldLabel htmlFor = &quot;form-about&quot; &gt;More about you&lt;/ FieldLabel &gt;
 &lt; Textarea
 { ... field.props }
 id = &quot;form-about&quot;
 value = { field.input }
 aria-invalid = { field.errors !== null }
 placeholder = &quot;I&#x27;m a software engineer...&quot;
 className = &quot;min-h-[120px]&quot;
 /&gt;
 &lt; FieldDescription &gt;
 Tell us more about yourself. This will be used to help us personalize
 your experience.
 &lt;/ FieldDescription &gt;
 { field.errors &amp;&amp; (
 &lt; FieldError errors = { field.errors. map (( message ) =&gt; ({ message })) } /&gt;
 ) }
 &lt;/ Field &gt;
 ) }
 &lt;/ FormischField &gt;
 Select #

 For select components, read field.input and call field.onChange from &lt;Select /&gt; &#x27;s onValueChange .
 To show errors, add the aria-invalid prop to the &lt;SelectTrigger /&gt; component and the data-invalid prop to the &lt;Field /&gt; component.

 Language Preferences Select your preferred spoken language. Spoken Language For best results, select the language you speak. Select Reset Save Copy "use client"

 import * as React from "react" View Code
 form.tsx Copy &lt; FormischField of = { form } path = { [ &quot;language&quot; ] } &gt;
 { ( field ) =&gt; (
 &lt; Field orientation = &quot;responsive&quot; data-invalid = { field.errors !== null } &gt;
 &lt; FieldContent &gt;
 &lt; FieldLabel htmlFor = &quot;form-language&quot; &gt;Spoken Language&lt;/ FieldLabel &gt;
 &lt; FieldDescription &gt;
 For best results, select the language you speak.
 &lt;/ FieldDescription &gt;
 { field.errors &amp;&amp; (
 &lt; FieldError errors = { field.errors. map (( message ) =&gt; ({ message })) } /&gt;
 ) }
 &lt;/ FieldContent &gt;
 &lt; Select value = { field.input } onValueChange = { field.onChange } &gt;
 &lt; SelectTrigger
 id = &quot;form-language&quot;
 aria-invalid = { field.errors !== null }
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
 &lt;/ FormischField &gt;
 Checkbox #

 For checkbox arrays, read field.input and update it from onCheckedChange using field.onChange .
 To show errors, add the aria-invalid prop to the &lt;Checkbox /&gt; component and the data-invalid prop to the &lt;Field /&gt; component.
 Remember to add data-slot=&quot;checkbox-group&quot; to the &lt;FieldGroup /&gt; component for proper styling and spacing.

 Notifications Manage your notification preferences. Responses Get notified for requests that take time, like research or image generation. Push notifications Tasks Get notified when tasks you&#x27;ve created have updates. Push notifications Email notifications Reset Save Copy "use client"

 import * as React from "react" View Code
 form.tsx Copy &lt; FormischField of = { form } path = { [ &quot;tasks&quot; ] } &gt;
 { ( field ) =&gt; (
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
 data-invalid = { field.errors !== null }
 &gt;
 &lt; Checkbox
 id = { `form-checkbox-${ task . id }` }
 aria-invalid = { field.errors !== null }
 checked = { field.input?. includes (task.id) ?? false }
 onCheckedChange = { ( checked ) =&gt; {
 const current = field.input ?? []
 field. onChange (
 checked === true
 ? [ ... current, task.id]
 : current. filter (( value ) =&gt; value !== task.id)
 )
 } }
 /&gt;
 &lt; FieldLabel
 htmlFor = { `form-checkbox-${ task . id }` }
 className = &quot;font-normal&quot;
 &gt;
 { task.label }
 &lt;/ FieldLabel &gt;
 &lt;/ Field &gt;
 )) }
 &lt;/ FieldGroup &gt;
 { field.errors &amp;&amp; (
 &lt; FieldError errors = { field.errors. map (( message ) =&gt; ({ message })) } /&gt;
 ) }
 &lt;/ FieldSet &gt;
 ) }
 &lt;/ FormischField &gt;
 Radio Group #

 For radio groups, read field.input and call field.onChange from onValueChange .
 To show errors, add the aria-invalid prop to the &lt;RadioGroupItem /&gt; component and the data-invalid prop to the &lt;Field /&gt; component.

 Subscription Plan See pricing and features for each plan. Plan You can upgrade or downgrade your plan at any time. Starter (100K tokens/month) For everyday use with basic features. Pro (1M tokens/month) For advanced AI usage with more features. Enterprise (Unlimited tokens) For large teams and heavy usage. Reset Save Copy "use client"

 import * as React from "react" View Code
 form.tsx Copy &lt; FormischField of = { form } path = { [ &quot;plan&quot; ] } &gt;
 { ( field ) =&gt; (
 &lt; FieldSet &gt;
 &lt; FieldLegend &gt;Plan&lt;/ FieldLegend &gt;
 &lt; FieldDescription &gt;
 You can upgrade or downgrade your plan at any time.
 &lt;/ FieldDescription &gt;
 &lt; RadioGroup value = { field.input } onValueChange = { field.onChange } &gt;
 { plans. map (( plan ) =&gt; (
 &lt; FieldLabel key = { plan.id } htmlFor = { `form-radiogroup-${ plan . id }` } &gt;
 &lt; Field
 orientation = &quot;horizontal&quot;
 data-invalid = { field.errors !== null }
 &gt;
 &lt; FieldContent &gt;
 &lt; FieldTitle &gt; { plan.title } &lt;/ FieldTitle &gt;
 &lt; FieldDescription &gt; { plan.description } &lt;/ FieldDescription &gt;
 &lt;/ FieldContent &gt;
 &lt; RadioGroupItem
 value = { plan.id }
 id = { `form-radiogroup-${ plan . id }` }
 aria-invalid = { field.errors !== null }
 /&gt;
 &lt;/ Field &gt;
 &lt;/ FieldLabel &gt;
 )) }
 &lt;/ RadioGroup &gt;
 { field.errors &amp;&amp; (
 &lt; FieldError errors = { field.errors. map (( message ) =&gt; ({ message })) } /&gt;
 ) }
 &lt;/ FieldSet &gt;
 ) }
 &lt;/ FormischField &gt;
 Switch #

 For switches, read field.input and call field.onChange from onCheckedChange .
 To show errors, add the aria-invalid prop to the &lt;Switch /&gt; component and the data-invalid prop to the &lt;Field /&gt; component.

 Security Settings Manage your account security preferences. Multi-factor authentication Enable multi-factor authentication to secure your account. Reset Save Copy "use client"

 import * as React from "react" View Code
 form.tsx Copy &lt; FormischField of = { form } path = { [ &quot;twoFactor&quot; ] } &gt;
 { ( field ) =&gt; (
 &lt; Field orientation = &quot;horizontal&quot; data-invalid = { field.errors !== null } &gt;
 &lt; FieldContent &gt;
 &lt; FieldLabel htmlFor = &quot;form-twoFactor&quot; &gt;
 Multi-factor authentication
 &lt;/ FieldLabel &gt;
 &lt; FieldDescription &gt;
 Enable multi-factor authentication to secure your account.
 &lt;/ FieldDescription &gt;
 { field.errors &amp;&amp; (
 &lt; FieldError errors = { field.errors. map (( message ) =&gt; ({ message })) } /&gt;
 ) }
 &lt;/ FieldContent &gt;
 &lt; Switch
 id = &quot;form-twoFactor&quot;
 checked = { field.input ?? false }
 onCheckedChange = { field.onChange }
 aria-invalid = { field.errors !== null }
 /&gt;
 &lt;/ Field &gt;
 ) }
 &lt;/ FormischField &gt;
 Complex Forms #
 Here is an example of a more complex form with multiple fields and validation.
 You&#x27;re almost there! Choose your subscription plan and billing period. Subscription Plan Choose your subscription plan. Basic For individuals and small teams Pro For businesses with higher demands Billing Period Select Choose how often you want to be billed. Add-ons Select additional features you&#x27;d like to include. Analytics Advanced analytics and reporting Backup Automated daily backups Priority Support 24/7 premium customer support Email Notifications Receive email updates about your subscription Save Preferences Reset Copy "use client"

 import * as React from "react" View Code
 Resetting the Form #
 Formisch exposes a top-level reset function. Pass the form store to reset it to its initial input.
 Copy &lt; Button type = &quot;button&quot; variant = &quot;outline&quot; onClick = { () =&gt; reset (form) } &gt;
 Reset
 &lt;/ Button &gt;
 You can also reset to new initial values, or reset while keeping the user&#x27;s current input:
 Copy // Reset to a fresh set of initial values
 reset (form, { initialInput: { title: &quot;&quot; , description: &quot;&quot; } })

 // Sync the baseline to new server data, but keep the user&#x27;s edits
 reset (form, { initialInput: serverData, keepInput: true })
 Array Fields #
 Formisch provides a &lt;FieldArray /&gt; component and a set of helper functions for managing dynamic array fields. Use it whenever you need to add, remove, or reorder items.
 Contact Emails Manage your contact email addresses. Email Addresses Add up to 5 email addresses where we can contact you. Add Email Address Reset Save Copy "use client"

 import * as React from "react" View Code
 Using FieldArray #
 &lt;FieldArray /&gt; follows the same render-prop pattern as &lt;Field /&gt; . Its items array contains a stable key per item that you should use as the React key .
 form.tsx Copy import {
 Field as FormischField,
 FieldArray,
 insert,
 remove,
 } from &quot;@formisch/react&quot;

 export function ExampleForm () {
 // ... form config

 return (
 &lt; FieldArray of = { form } path = { [ &quot;emails&quot; ] } &gt;
 { ( fieldArray ) =&gt; (
 &lt; FieldGroup className = &quot;gap-4&quot; &gt;
 { fieldArray.items. map (( item , index ) =&gt; (
 &lt; FormischField
 key = { item }
 of = { form }
 path = { [ &quot;emails&quot; , index, &quot;address&quot; ] }
 &gt;
 { ( field ) =&gt; /* ... */ }
 &lt;/ FormischField &gt;
 )) }
 &lt;/ FieldGroup &gt;
 ) }
 &lt;/ FieldArray &gt;
 )
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
 Adding Items #
 Use the insert function to add new items to the array. By default new items are appended to the end. You can also pass an at index to insert at a specific position.
 form.tsx Copy &lt; Button
 type = &quot;button&quot;
 variant = &quot;outline&quot;
 size = &quot;sm&quot;
 onClick = { () =&gt;
 insert (form, { path: [ &quot;emails&quot; ], initialInput: { address: &quot;&quot; } })
 }
 disabled = { fieldArray.items. length &gt;= 5 }
 &gt;
 Add Email Address
 &lt;/ Button &gt;
 Removing Items #
 Use the remove function with an at index to remove items from the array.
 form.tsx Copy import { remove } from &quot;@formisch/react&quot;

 {
 fieldArray.items. length &gt; 1 &amp;&amp; (
 &lt; InputGroupAddon align = &quot;inline-end&quot; &gt;
 &lt; InputGroupButton
 type = &quot;button&quot;
 variant = &quot;ghost&quot;
 size = &quot;icon-xs&quot;
 onClick = { () =&gt; remove (form, { path: [ &quot;emails&quot; ], at: index }) }
 aria-label = { `Remove email ${ index + 1 }` }
 &gt;
 &lt; XIcon /&gt;
 &lt;/ InputGroupButton &gt;
 &lt;/ InputGroupAddon &gt;
 )
 }
 Formisch also exposes move , swap , and replace for reordering and replacing items. They follow the same (form, config) signature.
 Array Validation #
 Use Valibot&#x27;s array and pipeline validators to constrain array fields.
 form.tsx Copy const FormSchema = v. object ({
 emails: v. pipe (
 v. array (
 v. object ({
 address: v. pipe (
 v. string (),
 v. nonEmpty ( &quot;Enter an email address.&quot; ),
 v. email ( &quot;Enter a valid email address.&quot; )
 ),
 })
 ),
 v. minLength ( 1 , &quot;Add at least one email address.&quot; ),
 v. maxLength ( 5 , &quot;You can add up to 5 email addresses.&quot; )
 ),
 }) TanStack Form Installation On This Page Demo Approach Form Methods Anatomy Form Create a form schema Set up the form Build the form Done Validation Client-side Validation Validation Modes Displaying Errors Working with Different Field Types Input Textarea Select Checkbox Radio Group Switch Complex Forms Resetting the Form Array Fields Using FieldArray Array Field Structure Adding Items Removing Items Array Validation Deploy your shadcn/ui app on Vercel Trusted by OpenAI, Sonos, Adobe, and more. Vercel provides tools and infrastructure to deploy apps and features at scale. Deploy Now Deploy to Vercel Built by shadcn at Vercel . The source code is available on GitHub . Get Code
