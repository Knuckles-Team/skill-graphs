## Possible Ways to Fix It[](https://nextjs.org/docs/messages/no-img-element#possible-ways-to-fix-it)
  1. Use [`next/image`](https://nextjs.org/docs/pages/api-reference/components/image) to improve performance with automatic [Image Optimization](https://nextjs.org/docs/pages/api-reference/components/image).


> **Note** : If deploying to a [managed hosting provider](https://nextjs.org/docs/pages/getting-started/deploying), remember to check provider pricing since optimized images might be charged differently than the original images.
> Common image optimization platform pricing:
> **Note** : If self-hosting, remember to install
pages/index.js
```
import Image from 'next/image'

function Home() {
  return (
    <Image
      src="https://example.com/hero.jpg"
      alt="Landscape picture"
      width={800}
      height={500}
    />
  )
}

export default Home
```

  1. If you would like to use `next/image` features such as blur-up placeholders but disable Image Optimization, you can do so using [unoptimized](https://nextjs.org/docs/pages/api-reference/components/image#unoptimized):


pages/index.js
```
import Image from 'next/image'

const UnoptimizedImage = (props) => {
  return <Image {...props} unoptimized />
}
```

  1. You can also use the `<picture>` element with the nested `<img>` element:


pages/index.js
```
function Home() {
  return (
    <picture>
      <source srcSet="https://example.com/hero.avif" type="image/avif" />
      <source srcSet="https://example.com/hero.webp" type="image/webp" />
      <img
        src="https://example.com/hero.jpg"
        alt="Landscape picture"
        width={800}
        height={500}
      />
    </picture>
  )
}
```

  1. You can use a [custom image loader](https://nextjs.org/docs/pages/api-reference/components/image#loader) to optimize images. Set [loaderFile](https://nextjs.org/docs/pages/api-reference/components/image#loaderfile) to the path of your custom loader.


next.config.js
```
module.exports = {
  images: {
    loader: 'custom',
    loaderFile: './my/image/loader.js',
  },
}
```
