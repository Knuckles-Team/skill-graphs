## Inertia
### Add `async` and `sync` Options to `cancelAll` Method
Pull request by
Replacing the deprecated `router.cancel()`, you can now get the same functionality with `router.cancelAll({ async: false })`. Giving you more control over request cancellation means smoother UX under heavy navigation or rapid input.
### [2.x] Add Form Context Support
Pull request by
The new `useFormContext` hook allows child components to know about parent component forms without having to do a bunch of unnecessary prop drilling.
```


 1<!-- Parent.vue -->




 2<template>




 3    <Form action="/users" method="post">




 4        <Input name="name" />




 5    </Form>




 6</template>




 7 



 8<!-- Input.vue -->




 9<script setup>




10import { useFormContext } from "@inertiajs/vue3";




11 



12defineProps({




13    name: {




14        type: String,




15        required: true,




16    },




17});




18 



19const form = useFormContext();




20</script>




21 



22<template>




23    <input type="text" :name="name" />




24 



25    <div v-if="form.errors[name]">




26        {{ form.errors[name] }}




27    </div>




28</template>




<!-- Parent.vue -->
<template>
    <Form action="/users" method="post">
        <Input name="name" />
    </Form>
</template>

<!-- Input.vue -->
<script setup>
import { useFormContext } from "@inertiajs/vue3";

defineProps({
    name: {
        type: String,
        required: true,
    },
});

const form = useFormContext();
</script>

<template>
    <input type="text" :name="name" />

    <div v-if="form.errors[name]">
        {{ form.errors[name] }}
    </div>
</template>

```

### Add `dontRemember()` Method to Form Helper
Pull request by
This gives you a straightforward way to opt out of Inertia's form remembering behavior when it's not desired. This is handy for sensitive forms or one-time flows where you don't want old values sticking around (e.g., password resets, invite flows).
## Inertia
### Support for Flash Data
Pull request by
Unlike regular props, Flash Data isn't persisted in the browser's history state, making it ideal for one-time notifications like toasts. On the frontend, Flash Data is available on `page.flash`. You can also listen for Flash Data using the global `flash` event or the `onFlash` callback.
```


1<template>




2    <div v-if="page.flash.toast" class="toast">




3        {{ page.flash.toast.message }}




4    </div>




5</template>




<template>
    <div v-if="page.flash.toast" class="toast">
        {{ page.flash.toast.message }}
    </div>
</template>

```

```


 1router.on("flash", (event) => {




 2    if (event.detail.flash.toast) {




 3        showToast(event.detail.flash.toast);




 4    }




 5});




 6 



 7router.post("/users", data, {




 8    onFlash: ({ newUserId }) => {




 9        // ...




10    },




11});




router.on("flash", (event) => {
    if (event.detail.flash.toast) {
        showToast(event.detail.flash.toast);
    }
});

router.post("/users", data, {
    onFlash: ({ newUserId }) => {
        // ...
    },
});

```

### First-Party Support for Precognition
Pull requests by @pascalbaljet:
[Laravel Precognition](https://laravel.com/docs/precognition) is now baked directly into the `useForm` hook and the `Form` component; there is no need to install additional libraries. Live validation has never been easier.
```


 1<template>




 2    <Form action="/users" method="post" #default="{ errors, invalid, validate, validating }">




 3        <div>




 4            <input name="name" @change="validate('name')" />




 5            <p v-if="invalid('name')">{{ errors.name }}</p>




 6        </div>




 7 



 8        <div>




 9            <input name="email" @change="validate('email')" />




10            <p v-if="invalid('email')">{{ errors.email }}</p>




11        </div>




12 



13        <p v-if="validating">Validating...</p>




14    </Form>




15</template>




<template>
    <Form action="/users" method="post" #default="{ errors, invalid, validate, validating }">
        <div>
            <input name="name" @change="validate('name')" />
            <p v-if="invalid('name')">{{ errors.name }}</p>
        </div>

        <div>
            <input name="email" @change="validate('email')" />
            <p v-if="invalid('email')">{{ errors.email }}</p>
        </div>

        <p v-if="validating">Validating...</p>
    </Form>
</template>

```

### Optimize Page Data Size and Parsing
Pull request by
Opt-in support was added for loading the initial Inertia page data from a `<script type="application/json">` element instead of the `body` tag. This results in a greatly reduced initial page data size, faster parsing, and makes the initial page data a breeze to inspect with your browser's dev tools.
You can opt in to this behavior as follows:
```


1createInertiaApp({




2    // ...




3    defaults: {




4        future: {




5            useScriptElementForInitialPage: true,




6        },




7    },




8});




createInertiaApp({
    // ...
    defaults: {
        future: {
            useScriptElementForInitialPage: true,
        },
    },
});

```

### Support for `once()` Props
Pull request by
Some data rarely changes, is expensive to compute, or is simply large. Rather than including this data in every response, `once` props are remembered by the client and reused on subsequent pages that include the same prop.
```


1return Inertia::render('Billing', [




2    'plans' => Inertia::once(fn () => Plan::all()),




3]);




return Inertia::render('Billing', [
    'plans' => Inertia::once(fn () => Plan::all()),
]);

```

## Inertia
![Inertia Website Share Image](https://laravel.com/images/changelog/2025-11/inertia-refresh.png)
The Inertia
Inertia finally has the website it deserves, showing off all of its power and flexibility as the best way to create a SPA with the backend and frontend of your choice.
Furthermore,
## Inertia
### Configure Global Defaults and Update During Runtime
Pull request by
Inertia now supports setting `createInertiaApp()` method:
```


 1createInertiaApp({




 2    // resolve, setup, etc.




 3    defaults: {




 4        form: {




 5            recentlySuccessfulDuration: 5_000,




 6        },




 7        prefetch: {




 8            cacheFor: 60_000,




 9        },




10        visitOptions: (href: string, options: VisitOptions) => {




11            return { headers: { ...options.headers, "X-Foo": "Bar" } };




12        },




13    },




14});




createInertiaApp({
    // resolve, setup, etc.
    defaults: {
        form: {
            recentlySuccessfulDuration: 5_000,
        },
        prefetch: {
            cacheFor: 60_000,
        },
        visitOptions: (href: string, options: VisitOptions) => {
            return { headers: { ...options.headers, "X-Foo": "Bar" } };
        },
    },
});

```

Each adapter now also exports a `config` instance to update any values at runtime:
```


1import { config } from "@inertiajs/vue3";




2 



3config.set("form.recentlySuccessfulDuration", 1000);




import { config } from "@inertiajs/vue3";

config.set("form.recentlySuccessfulDuration", 1000);

```

### Support for Type-Hinting Shared Page Props
Pull request by
`usePage()` now supports a global type definition file, allowing you to type-hint shared page props:
```


 1// resources/js/types/globals.d.ts




 2 



 3declare module "@inertiajs/core" {




 4    export interface InertiaConfig {




 5        sharedPageProps: {




 6            auth: { user: { id: number; name: string } | null };




 7            flash: { success?: string; error?: string };




 8        };




 9    }




10}




// resources/js/types/globals.d.ts

declare module "@inertiajs/core" {
    export interface InertiaConfig {
        sharedPageProps: {
            auth: { user: { id: number; name: string } | null };
            flash: { success?: string; error?: string };
        };
    }
}

```

Shared page props are now automatically type-hinted throughout the app when you use `usePage()`:
```


1const page = usePage();




2const successMessage = page.props.flash.success;




const page = usePage();
const successMessage = page.props.flash.success;

```

## Inertia
### Introduction of the `<InfiniteScroll>` Component
Pull request by
```


1<template>




2    <InfiniteScroll data="users">




3        <div v-for="user in users.data" :key="user.id">{{ user.name }}</div>




4    </InfiniteScroll>




5</template>




<template>
    <InfiniteScroll data="users">
        <div v-for="user in users.data" :key="user.id">{{ user.name }}</div>
    </InfiniteScroll>
</template>

```

A new `<InfiniteScroll>` component was introduced for React, Vue, and Svelte that allows you to easily create infinite scroll interfaces by wrapping your items in the new component.
### Support for Merging Nested Prop Paths
Pull request by
A new middle ground was added between `Inertia::merge()` and `Inertia::deepMerge()` so you can have fine-grained control over what should be merged.
The front-end will replace the entire object, except the `data` array. The new items will be appended to the existing items:
```


1Inertia::merge(User::paginate())->append('data');




Inertia::merge(User::paginate())->append('data');

```

There's also `prepend()`, and you can also combine multiple calls:
```


1Inertia::merge($complexObject)




2    ->append('users', matchOn: 'username')




3    ->prepend('messages.data');




Inertia::merge($complexObject)
    ->append('users', matchOn: 'username')
    ->prepend('messages.data');

```

Then there's a new `Inertia::scroll()` function which you can pass paginated resources:
```


1Inertia::scroll(User::paginate());




Inertia::scroll(User::paginate());

```

### Progress Indicator API
Pull request by
```


 1import { progress } from "@inertiajs/vue3";




 2 



 3progress.start(); // Begin progress animation




 4progress.set(0.25); // Set to 25% complete




 5progress.finish(); // Complete and fade out




 6progress.reset(); // Reset to start




 7progress.remove(); // Complete and remove from DOM




 8progress.hide(); // Hide progress bar




 9progress.reveal(); // Show progress bar




10 



11progress.isStarted(); // Returns boolean




12progress.getStatus(); // Returns current percentage or null




import { progress } from "@inertiajs/vue3";

progress.start(); // Begin progress animation
progress.set(0.25); // Set to 25% complete
progress.finish(); // Complete and fade out
progress.reset(); // Reset to start
progress.remove(); // Complete and remove from DOM
progress.hide(); // Hide progress bar
progress.reveal(); // Show progress bar

progress.isStarted(); // Returns boolean
progress.getStatus(); // Returns current percentage or null

```

The internal methods used to drive the
## Inertia
### Introduction of the `Form` Component
Pull request by
```


 1<script setup>




 2import { Form } from "@inertiajs/vue3";




 3</script>




 4 



 5<template>




 6    <Form action="/users" method="post">




 7        <input type="text" name="name" />




 8        <input type="email" name="email" />




 9        <button type="submit">Create User</button>




10    </Form>




11</template>




<script setup>
import { Form } from "@inertiajs/vue3";
</script>

<template>
    <Form action="/users" method="post">
        <input type="text" name="name" />
        <input type="email" name="email" />
        <button type="submit">Create User</button>
    </Form>
</template>

```

A new `<Form>` component that behaves much like a classic HTML form and simply allows Inertia to intercept the network call on form submission. This new component greatly reduces the boilerplate needed to create a form with Inertia.
### Support for Passing Wayfinder Objects to Router Methods
Pull request by
```


 1import UserController from "@/actions/App/Http/Controllers/UserController";




 2 



 3// Regular visits




 4router.visit(UserController.store());




 5 



 6// Prefetching




 7router.prefetch(UserController.index());




 8router.getPrefetching(UserController.index());




 9router.getCached(UserController.index());




10router.flush(UserController.index());




import UserController from "@/actions/App/Http/Controllers/UserController";

// Regular visits
router.visit(UserController.store());

// Prefetching
router.prefetch(UserController.index());
router.getPrefetching(UserController.index());
router.getCached(UserController.index());
router.flush(UserController.index());

```

Adds support for passing Wayfinder-like objects into router methods instead of specifying the URL and method manually.
### Tag-Based Cache Invalidation for Prefetch Requests
Pull request by
```


 1// Specify cache tags via the Link component




 2<Link href="/users/1" prefetch="hover" :tags="['user', 'profile']">




 3    View Profile




 4</Link>




 5 



 6// Or via prefetch method on the route




 7router.prefetch(




 8  '/users',




 9  { method: 'get', data: { page: 2 } },




10  { cacheFor: '1m', tags: ['users'] }




11)




12 



13// Flushes all cache entries tagged with 'user'




14router.flushByTags(['user'])




15 



16// Flushes entries tagged with 'user' OR 'product'




17router.flushByTags(['user', 'product'])




18 



19// Flush via visit




20router.visit('/users', {




21  invalidate: ['user']




22})




23 



24// Flush via useForm helper




25form.post('/users', { invalidate: ['users'] })




// Specify cache tags via the Link component
<Link href="/users/1" prefetch="hover" :tags="['user', 'profile']">
    View Profile
</Link>

// Or via prefetch method on the route
router.prefetch(
  '/users',
  { method: 'get', data: { page: 2 } },
  { cacheFor: '1m', tags: ['users'] }
)

// Flushes all cache entries tagged with 'user'
router.flushByTags(['user'])

// Flushes entries tagged with 'user' OR 'product'
router.flushByTags(['user', 'product'])

// Flush via visit
router.visit('/users', {
  invalidate: ['user']
})

// Flush via useForm helper
form.post('/users', { invalidate: ['users'] })

```

Introduces tag-based cache invalidation for prefetch requests. This enables better control over the prefetch cache without having to flush everything.
### Support for Passing Custom Component to `as` Prop of `Link` Component
Pull request by
```


1<Link as={CustomButton} method="post" href="/user" data={{ test: "data" }}>




2    Custom Component with Data




3</Link>




<Link as={CustomButton} method="post" href="/user" data={{ test: "data" }}>
    Custom Component with Data
</Link>

```

The Inertia `Link` component now supports custom components instead of just HTML tags such as `a` or `button`.
## Inertia
### Reset Form State and Clear Errors with a Single Method
Pull request by
```


1const form = useForm({ name: "", email: "" });




2 



3// Instead of:




4form.reset();




5form.clearErrors();




6 



7// You can now:




8form.resetAndClearErrors();




const form = useForm({ name: "", email: "" });

// Instead of:
form.reset();
form.clearErrors();

// You can now:
form.resetAndClearErrors();

```

You can now concisely reset all fields and errors in one go, bringing your form back to square one.
### Prevent Minifying JavaScript Builds and Test Apps
Pull request by
Inertia no longer distributes minified builds, aligning it with the strategy of other popular libraries. This makes debugging more straightforward and allows for local patching if the need arises.
## Inertia
### Allow `deepMerge` on Custom Properties
Pull request by
When implementing infinite scrolling with Inertia or other paginated data merges, you can now specify a key (`matchOn`) to do a deep merge, matching items by ID and replacing or appending as appropriate. This provides greater flexibility, prevents duplicated entries, and keeps your client-side data consistent.
```


1Inertia::render('Users/Index', [




2    'users' => Inertia::deepMerge($users)->matchOn('data.id'),




3]);




Inertia::render('Users/Index', [
    'users' => Inertia::deepMerge($users)->matchOn('data.id'),
]);

```

### Prevent Duplicate Render in React
Pull request by
We fixed a React-specific issue in `<StrictMode>` where the initial Inertia page would render twice. Now you get a single, clean first render without flicker, improving perceived performance.
Get started with the
[ ](https://laravel.com/rss/oss-changelog)
  * [ February 2026 ](https://laravel.com/docs/changelog#log-2026-02)
  * [ January 2026 ](https://laravel.com/docs/changelog#log-2026-01)
  * [ December 2025 ](https://laravel.com/docs/changelog#log-2025-12)
  * [ November 2025 ](https://laravel.com/docs/changelog#log-2025-11)
  * [ October 2025 ](https://laravel.com/docs/changelog#log-2025-10)
  * [ September 2025 ](https://laravel.com/docs/changelog#log-2025-09)
  * [ August 2025 ](https://laravel.com/docs/changelog#log-2025-08)
  * [ July 2025 ](https://laravel.com/docs/changelog#log-2025-07)
  * [ June 2025 ](https://laravel.com/docs/changelog#log-2025-06)


[ ![Laravel Forge](https://laravel.com/images/ads/forge-logo.svg) Server management made simple for any PHP app Learn more  ](https://forge.laravel.com)
[ ![Laravel Cloud](https://laravel.com/images/ads/cloud-logo.svg) The fastest way to deploy and scale Laravel apps Learn more  ](https://cloud.laravel.com)
[ ![Laravel Nightwatch](https://laravel.com/images/ads/nightwatch-logo.svg) First-class monitoring and deep insights for Laravel apps Learn more  ](https://nightwatch.laravel.com)
[ ![Laravel Boost](https://laravel.com/images/ads/boost-logo.svg) Supercharge your AI development with essential context Learn more  ](https://laravel.com/ai/boost)
Laravel is the most productive way to
build, deploy, and monitor software.
  * © 2026 Laravel
  * [ Legal ](https://laravel.com/legal)
  * [ Status ](https://status.laravel.com/)


####  Products
  * [ Cloud ](https://cloud.laravel.com)
  * [ Forge ](https://forge.laravel.com)
  * [ Nightwatch ](https://nightwatch.laravel.com)
  * [ Vapor ](https://vapor.laravel.com)
  * [ Nova ](https://nova.laravel.com)


####  Packages
  * [ Cashier ](https://laravel.com/docs/cashier)
  * [ Dusk ](https://laravel.com/docs/dusk)
  * [ Horizon ](https://laravel.com/docs/horizon)
  * [ Octane ](https://laravel.com/docs/octane)
  * [ Scout ](https://laravel.com/docs/scout)
  * [ Pennant ](https://laravel.com/docs/pennant)
  * [ Pint ](https://laravel.com/docs/pint)
  * [ Sail ](https://laravel.com/docs/sail)
  * [ Sanctum ](https://laravel.com/docs/sanctum)
  * [ Socialite ](https://laravel.com/docs/socialite)
  * [ Telescope ](https://laravel.com/docs/telescope)
  * [ Pulse ](https://laravel.com/docs/pulse)
  * [ Reverb ](https://laravel.com/docs/reverb)
  * [ Echo ](https://laravel.com/docs/broadcasting)


####  Resources
  * [ Documentation ](https://laravel.com/docs)
  * [ Starter Kits ](https://laravel.com/starter-kits)
  * [ Release Notes ](https://laravel.com/docs/releases)
  * [ Blog ](https://laravel.com/blog)
  * [ Community ](https://laravel.com/community)
  * [ Learn ](https://laravel.com/learn)
  * [ Careers ](https://laravel.com/careers)
  * [ Trust ](https://trust.laravel.com)


####  Partners
  *   * [Vehikl](https://partners.laravel.com/partners/vehikl)
  * [Active Logic](https://partners.laravel.com/partners/active-logic)
  * [Jump24](https://partners.laravel.com/partners/jump24)
  * [Kirschbaum](https://partners.laravel.com/partners/kirschbaum)
  * [byte5](https://partners.laravel.com/partners/byte5)
  * [Tighten](https://partners.laravel.com/partners/tighten)
  * [Curotec](https://partners.laravel.com/partners/curotec)
  * [Redberry](https://partners.laravel.com/partners/redberry)
  * [ More Partners ](https://partners.laravel.com)
