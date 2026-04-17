## React + Vue Starter Kits
### Migrate `useForm` to New Inertia `Form` Component
Pull request by
```


1import { Form } from "@inertiajs/react";




2 



3export default function Login() {




4    return (




5        <Form action="/login" method="post">




6            {/* Form fields */}




7        </Form>




8    );




9}




import { Form } from "@inertiajs/react";

export default function Login() {
    return (
        <Form action="/login" method="post">
            {/* Form fields */}
        </Form>
    );
}

```

Reduces the boilerplate for all forms in the [starter kits](https://laravel.com/starter-kits) by replacing `useForm` with the new Inertia `Form` component.
### Replace Ziggy With Wayfinder
Pull request by
```


 1import AuthenticatedSessionController from "@/actions/App/Http/Controllers/Auth/AuthenticatedSessionController";




 2import { Form } from "@inertiajs/react";




 3 



 4export default function Login() {




 5    return (




 6        <Form {...AuthenticatedSessionController.store.form()}>




 7            {/* Form fields */}




 8        </Form>




 9    );




10}




import AuthenticatedSessionController from "@/actions/App/Http/Controllers/Auth/AuthenticatedSessionController";
import { Form } from "@inertiajs/react";

export default function Login() {
    return (
        <Form {...AuthenticatedSessionController.store.form()}>
            {/* Form fields */}
        </Form>
    );
}

```

Removes Ziggy from the starter kits and replaces it with the current version of Laravel Wayfinder, bringing end-to-end type safety to your routes.
### 100% Baseline Test Coverage
Pull request by
Adds the missing feature tests so that fresh projects start with 100% test coverage.
