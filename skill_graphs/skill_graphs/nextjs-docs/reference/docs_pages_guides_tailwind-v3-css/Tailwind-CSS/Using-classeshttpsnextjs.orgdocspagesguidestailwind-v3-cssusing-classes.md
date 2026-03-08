## Using classes[](https://nextjs.org/docs/pages/guides/tailwind-v3-css#using-classes)
After installing Tailwind CSS and adding the global styles, you can use Tailwind's utility classes in your application.
pages/index.tsx
TypeScript
JavaScript TypeScript
```
export default function Page() {
  return <h1 className="text-3xl font-bold underline">Hello, Next.js!</h1>
}
```
