##  [Open Graph Images](https://vercel.com/docs/getting-started-with-vercel#open-graph-images)[](https://vercel.com/docs/getting-started-with-vercel#open-graph-images)
Dynamic social card images allow you to create a unique image for pages of your site. This is great for sharing links on the web through social platforms or text messages.
To generate dynamic social card images for Nuxt projects, you can use [Server-side rendering(SSR)](https://vercel.com/docs/getting-started-with-vercel#server-side-rendering-ssr) function.
The following example demonstrates using Open Graph (OG) image generation with
  1. Create a new OG template


components/OgImage/Template.vue
TypeScript
TypeScript JavaScript Bash
```
<script setup lang="ts">
  withDefaults(defineProps<{
    title?: string
  }>(), {
    title: 'title',
  })
</script>
<template>
  <div class="h-full w-full flex items-start justify-start border border-blue-500 border-12 bg-gray-50">
    <div class="flex items-start justify-start h-full">
      <div class="flex flex-col justify-between w-full h-full">
        <h1 class="text-[80px] p-20 font-black text-left">
          {{ title }}
        </h1>
        <p class="text-2xl pb-10 px-20 font-bold mb-0">
          acme.com
        </p>
      </div>
    </div>
  </div>
</template>
```

  1. Use that OG image in your pages. Props passed get used in your open graph images.


pages/index.vue
TypeScript
TypeScript JavaScript Bash
```
<script lang="ts" setup>
defineOgImageComponent('Template', {
  title: 'Is this thing on?'
})
</script>
```

To see your generated image, run your project and use Nuxt DevTools. Or you can visit the image at its URL `/__og-image__/image/og.png`.
