 * [`getModifierState(key)`](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/getModifierState)
 * [`key`](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key)
 * [`keyCode`](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/keyCode)
 * [`locale`](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/locale)
 * [`metaKey`](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/metaKey)
 * [`location`](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/location)
 * [`repeat`](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/repeat)
 * [`shiftKey`](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/shiftKey)
 * [`which`](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/which)

 It also includes the inherited [`UIEvent`](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent) properties:

 * [`detail`](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent/detail)
 * [`view`](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent/view)

---

### `MouseEvent` handler function {/*mouseevent-handler*/}

An event handler type for mouse events.

```js
 console.log('onClick')}
 onMouseEnter={e => console.log('onMouseEnter')}
 onMouseOver={e => console.log('onMouseOver')}
 onMouseDown={e => console.log('onMouseDown')}
 onMouseUp={e => console.log('onMouseUp')}
 onMouseLeave={e => console.log('onMouseLeave')}
/>
```

[See an example.](#handling-mouse-events)

#### Parameters {/*mouseevent-handler-parameters*/}

* `e`: A [React event object](#react-event-object) with these extra [`MouseEvent`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent) properties:
 * [`altKey`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/altKey)
 * [`button`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/button)
 * [`buttons`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/buttons)
 * [`ctrlKey`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/ctrlKey)
 * [`clientX`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/clientX)
 * [`clientY`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/clientY)
 * [`getModifierState(key)`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/getModifierState)
 * [`metaKey`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/metaKey)
 * [`movementX`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/movementX)
 * [`movementY`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/movementY)
 * [`pageX`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/pageX)
 * [`pageY`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/pageY)
 * [`relatedTarget`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/relatedTarget)
 * [`screenX`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/screenX)
 * [`screenY`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/screenY)
 * [`shiftKey`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/shiftKey)

 It also includes the inherited [`UIEvent`](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent) properties:

 * [`detail`](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent/detail)
 * [`view`](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent/view)

---

### `PointerEvent` handler function {/*pointerevent-handler*/}

An event handler type for [pointer events.](https://developer.mozilla.org/en-US/docs/Web/API/Pointer_events)

```js
 console.log('onPointerEnter')}
 onPointerMove={e => console.log('onPointerMove')}
 onPointerDown={e => console.log('onPointerDown')}
 onPointerUp={e => console.log('onPointerUp')}
 onPointerLeave={e => console.log('onPointerLeave')}
/>
```

[See an example.](#handling-pointer-events)

#### Parameters {/*pointerevent-handler-parameters*/}

* `e`: A [React event object](#react-event-object) with these extra [`PointerEvent`](https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent) properties:
 * [`height`](https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent/height)
 * [`isPrimary`](https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent/isPrimary)
 * [`pointerId`](https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent/pointerId)
 * [`pointerType`](https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent/pointerType)
 * [`pressure`](https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent/pressure)
 * [`tangentialPressure`](https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent/tangentialPressure)
 * [`tiltX`](https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent/tiltX)
 * [`tiltY`](https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent/tiltY)
 * [`twist`](https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent/twist)
 * [`width`](https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent/width)

 It also includes the inherited [`MouseEvent`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent) properties:

 * [`altKey`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/altKey)
 * [`button`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/button)
 * [`buttons`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/buttons)
 * [`ctrlKey`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/ctrlKey)
 * [`clientX`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/clientX)
 * [`clientY`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/clientY)
 * [`getModifierState(key)`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/getModifierState)
 * [`metaKey`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/metaKey)
 * [`movementX`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/movementX)
 * [`movementY`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/movementY)
 * [`pageX`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/pageX)
 * [`pageY`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/pageY)
 * [`relatedTarget`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/relatedTarget)
 * [`screenX`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/screenX)
 * [`screenY`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/screenY)
 * [`shiftKey`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/shiftKey)

 It also includes the inherited [`UIEvent`](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent) properties:

 * [`detail`](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent/detail)
 * [`view`](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent/view)

---

### `TouchEvent` handler function {/*touchevent-handler*/}

An event handler type for [touch events.](https://developer.mozilla.org/en-US/docs/Web/API/Touch_events)

```js
 console.log('onTouchStart')}
 onTouchMove={e => console.log('onTouchMove')}
 onTouchEnd={e => console.log('onTouchEnd')}
 onTouchCancel={e => console.log('onTouchCancel')}
/>
```

#### Parameters {/*touchevent-handler-parameters*/}

* `e`: A [React event object](#react-event-object) with these extra [`TouchEvent`](https://developer.mozilla.org/en-US/docs/Web/API/TouchEvent) properties:
 * [`altKey`](https://developer.mozilla.org/en-US/docs/Web/API/TouchEvent/altKey)
 * [`ctrlKey`](https://developer.mozilla.org/en-US/docs/Web/API/TouchEvent/ctrlKey)
 * [`changedTouches`](https://developer.mozilla.org/en-US/docs/Web/API/TouchEvent/changedTouches)
 * [`getModifierState(key)`](https://developer.mozilla.org/en-US/docs/Web/API/TouchEvent/getModifierState)
 * [`metaKey`](https://developer.mozilla.org/en-US/docs/Web/API/TouchEvent/metaKey)
 * [`shiftKey`](https://developer.mozilla.org/en-US/docs/Web/API/TouchEvent/shiftKey)
 * [`touches`](https://developer.mozilla.org/en-US/docs/Web/API/TouchEvent/touches)
 * [`targetTouches`](https://developer.mozilla.org/en-US/docs/Web/API/TouchEvent/targetTouches)

 It also includes the inherited [`UIEvent`](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent) properties:

 * [`detail`](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent/detail)
 * [`view`](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent/view)

---

### `TransitionEvent` handler function {/*transitionevent-handler*/}

An event handler type for the CSS transition events.

```js
 console.log('onTransitionEnd')}
/>
```

#### Parameters {/*transitionevent-handler-parameters*/}

* `e`: A [React event object](#react-event-object) with these extra [`TransitionEvent`](https://developer.mozilla.org/en-US/docs/Web/API/TransitionEvent) properties:
 * [`elapsedTime`](https://developer.mozilla.org/en-US/docs/Web/API/TransitionEvent/elapsedTime)
 * [`propertyName`](https://developer.mozilla.org/en-US/docs/Web/API/TransitionEvent/propertyName)
 * [`pseudoElement`](https://developer.mozilla.org/en-US/docs/Web/API/TransitionEvent/pseudoElement)

---

### `UIEvent` handler function {/*uievent-handler*/}

An event handler type for generic UI events.

```js
 console.log('onScroll')}
/>
```

#### Parameters {/*uievent-handler-parameters*/}

* `e`: A [React event object](#react-event-object) with these extra [`UIEvent`](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent) properties:
 * [`detail`](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent/detail)
 * [`view`](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent/view)

---

### `WheelEvent` handler function {/*wheelevent-handler*/}

An event handler type for the `onWheel` event.

```js
 console.log('onWheel')}
/>
```

#### Parameters {/*wheelevent-handler-parameters*/}

* `e`: A [React event object](#react-event-object) with these extra [`WheelEvent`](https://developer.mozilla.org/en-US/docs/Web/API/WheelEvent) properties:
 * [`deltaMode`](https://developer.mozilla.org/en-US/docs/Web/API/WheelEvent/deltaMode)
 * [`deltaX`](https://developer.mozilla.org/en-US/docs/Web/API/WheelEvent/deltaX)
 * [`deltaY`](https://developer.mozilla.org/en-US/docs/Web/API/WheelEvent/deltaY)
 * [`deltaZ`](https://developer.mozilla.org/en-US/docs/Web/API/WheelEvent/deltaZ)

 It also includes the inherited [`MouseEvent`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent) properties:

 * [`altKey`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/altKey)
 * [`button`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/button)
 * [`buttons`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/buttons)
 * [`ctrlKey`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/ctrlKey)
 * [`clientX`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/clientX)
 * [`clientY`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/clientY)
 * [`getModifierState(key)`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/getModifierState)
 * [`metaKey`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/metaKey)
 * [`movementX`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/movementX)
 * [`movementY`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/movementY)
 * [`pageX`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/pageX)
 * [`pageY`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/pageY)
 * [`relatedTarget`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/relatedTarget)
 * [`screenX`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/screenX)
 * [`screenY`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/screenY)
 * [`shiftKey`](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/shiftKey)

 It also includes the inherited [`UIEvent`](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent) properties:

 * [`detail`](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent/detail)
 * [`view`](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent/view)

---

## Usage {/*usage*/}

### Applying CSS styles {/*applying-css-styles*/}

In React, you specify a CSS class with [`className`.](https://developer.mozilla.org/en-US/docs/Web/API/Element/className) It works like the `class` attribute in HTML:

```js

```

Then you write the CSS rules for it in a separate CSS file:

```css
/* In your CSS */
.avatar {
 border-radius: 50%;
}
```

React does not prescribe how you add CSS files. In the simplest case, you'll add a [` `](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/link) tag to your HTML. If you use a build tool or a framework, consult its documentation to learn how to add a CSS file to your project.

Sometimes, the style values depend on data. Use the `style` attribute to pass some styles dynamically:

```js {3-6}

```

In the above example, `style={{}}` is not a special syntax, but a regular `{}` object inside the `style={ }` [JSX curly braces.](/learn/javascript-in-jsx-with-curly-braces) We recommend only using the `style` attribute when your styles depend on JavaScript variables.

```js src/App.js
import Avatar from './Avatar.js';

const user = {
 name: 'Hedy Lamarr',
 imageUrl: 'https://react.dev/images/docs/scientists/yXOvdOSs.jpg',
 imageSize: 90,
};

export default function App() {
 return ;
}
```

```js src/Avatar.js active
export default function Avatar({ user }) {
 return (

 );
}
```

```css src/styles.css
.avatar {
 border-radius: 50%;
}
```

#### How to apply multiple CSS classes conditionally? {/*how-to-apply-multiple-css-classes-conditionally*/}

To apply CSS classes conditionally, you need to produce the `className` string yourself using JavaScript.

For example, `className={'row ' + (isSelected ? 'selected': '')}` will produce either `className="row"` or `className="row selected"` depending on whether `isSelected` is `true`.

To make this more readable, you can use a tiny helper library like [`classnames`:](https://github.com/JedWatson/classnames)

```js
import cn from 'classnames';

function Row({ isSelected }) {
 return (

 ...

 );
}
```

It is especially convenient if you have multiple conditional classes:

```js
import cn from 'classnames';

function Row({ isSelected, size }) {
 return (

 ...

 );
}
```

---

### Manipulating a DOM node with a ref {/*manipulating-a-dom-node-with-a-ref*/}

Sometimes, you'll need to get the browser DOM node associated with a tag in JSX. For example, if you want to focus an ` ` when a button is clicked, you need to call [`focus()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/focus) on the browser ` ` DOM node.

To obtain the browser DOM node for a tag, [declare a ref](/reference/react/useRef) and pass it as the `ref` attribute to that tag:

```js {7}
import { useRef } from 'react';

export default function Form() {
 const inputRef = useRef(null);
 // ...
 return (

 // ...
```

React will put the DOM node into `inputRef.current` after it's been rendered to the screen.

```js
import { useRef } from 'react';

export default function Form() {
 const inputRef = useRef(null);

 function handleClick() {
 inputRef.current.focus();
 }

 return (
 <>

 Focus the input

 );
}
```

Read more about [manipulating DOM with refs](/learn/manipulating-the-dom-with-refs) and [check out more examples.](/reference/react/useRef#usage)

For more advanced use cases, the `ref` attribute also accepts a [callback function.](#ref-callback)

---

### Dangerously setting the inner HTML {/*dangerously-setting-the-inner-html*/}

You can pass a raw HTML string to an element like so:

```js
const markup = { __html: ' some raw html ' };
return ;
```

**This is dangerous. As with the underlying DOM [`innerHTML`](https://developer.mozilla.org/en-US/docs/Web/API/Element/innerHTML) property, you must exercise extreme caution! Unless the markup is coming from a completely trusted source, it is trivial to introduce an [XSS](https://en.wikipedia.org/wiki/Cross-site_scripting) vulnerability this way.**

For example, if you use a Markdown library that converts Markdown to HTML, you trust that its parser doesn't contain bugs, and the user only sees their own input, you can display the resulting HTML like this:

```js
import { useState } from 'react';
import MarkdownPreview from './MarkdownPreview.js';

export default function MarkdownEditor() {
 const [postContent, setPostContent] = useState('_Hello,_ **Markdown**!');
 return (
 <>

 Enter some markdown:
 setPostContent(e.target.value)}
 />

 );
}
```

```js src/MarkdownPreview.js active
import { Remarkable } from 'remarkable';

const md = new Remarkable();

function renderMarkdownToHTML(markdown) {
 // This is ONLY safe because the output HTML
 // is shown to the same user, and because you
 // trust this Markdown parser to not have bugs.
 const renderedHTML = md.render(markdown);
 return {__html: renderedHTML};
}

export default function MarkdownPreview({ markdown }) {
 const markup = renderMarkdownToHTML(markdown);
 return ;
}
```

```json package.json
{
 "dependencies": {
 "react": "latest",
 "react-dom": "latest",
 "react-scripts": "latest",
 "remarkable": "2.0.1"
 },
 "scripts": {
 "start": "react-scripts start",
 "build": "react-scripts build",
 "test": "react-scripts test --env=jsdom",
 "eject": "react-scripts eject"
 }
}
```

```css
textarea { display: block; margin-top: 5px; margin-bottom: 10px; }
```

The `{__html}` object should be created as close to where the HTML is generated as possible, like the above example does in the `renderMarkdownToHTML` function. This ensures that all raw HTML being used in your code is explicitly marked as such, and that only variables that you expect to contain HTML are passed to `dangerouslySetInnerHTML`. It is not recommended to create the object inline like ` `.

To see why rendering arbitrary HTML is dangerous, replace the code above with this:

```js {1-4,7,8}
const post = {
 // Imagine this content is stored in the database.
 content: ` `
};

export default function MarkdownPreview() {
 // 🔴 SECURITY HOLE: passing untrusted input to dangerouslySetInnerHTML
 const markup = { __html: post.content };
 return ;
}
```

The code embedded in the HTML will run. A hacker could use this security hole to steal user information or to perform actions on their behalf. **Only use `dangerouslySetInnerHTML` with trusted and sanitized data.**

---

### Handling mouse events {/*handling-mouse-events*/}

This example shows some common [mouse events](#mouseevent-handler) and when they fire.

```js
export default function MouseExample() {
 return (
 console.log('onMouseEnter (parent)')}
 onMouseLeave={e => console.log('onMouseLeave (parent)')}
 >
 console.log('onClick (first button)')}
 onMouseDown={e => console.log('onMouseDown (first button)')}
 onMouseEnter={e => console.log('onMouseEnter (first button)')}
 onMouseLeave={e => console.log('onMouseLeave (first button)')}
 onMouseOver={e => console.log('onMouseOver (first button)')}
 onMouseUp={e => console.log('onMouseUp (first button)')}
 >
 First button

 console.log('onClick (second button)')}
 onMouseDown={e => console.log('onMouseDown (second button)')}
 onMouseEnter={e => console.log('onMouseEnter (second button)')}
 onMouseLeave={e => console.log('onMouseLeave (second button)')}
 onMouseOver={e => console.log('onMouseOver (second button)')}
 onMouseUp={e => console.log('onMouseUp (second button)')}
 >
 Second button

 );
}
```

```css
label { display: block; }
input { margin-left: 10px; }
```

---

### Handling pointer events {/*handling-pointer-events*/}

This example shows some common [pointer events](#pointerevent-handler) and when they fire.

```js
export default function PointerExample() {
 return (
 console.log('onPointerEnter (parent)')}
 onPointerLeave={e => console.log('onPointerLeave (parent)')}
 style={{ padding: 20, backgroundColor: '#ddd' }}
 >
 console.log('onPointerDown (first child)')}
 onPointerEnter={e => console.log('onPointerEnter (first child)')}
 onPointerLeave={e => console.log('onPointerLeave (first child)')}
 onPointerMove={e => console.log('onPointerMove (first child)')}
 onPointerUp={e => console.log('onPointerUp (first child)')}
 style={{ padding: 20, backgroundColor: 'lightyellow' }}
 >
 First child

 console.log('onPointerDown (second child)')}
 onPointerEnter={e => console.log('onPointerEnter (second child)')}
 onPointerLeave={e => console.log('onPointerLeave (second child)')}
 onPointerMove={e => console.log('onPointerMove (second child)')}
 onPointerUp={e => console.log('onPointerUp (second child)')}
 style={{ padding: 20, backgroundColor: 'lightblue' }}
 >
 Second child

 );
}
```

```css
label { display: block; }
input { margin-left: 10px; }
```

---

### Handling focus events {/*handling-focus-events*/}

In React, [focus events](#focusevent-handler) bubble. You can use the `currentTarget` and `relatedTarget` to differentiate if the focusing or blurring events originated from outside of the parent element. The example shows how to detect focusing a child, focusing the parent element, and how to detect focus entering or leaving the whole subtree.

```js
export default function FocusExample() {
 return (
 {
 if (e.currentTarget === e.target) {
 console.log('focused parent');
 } else {
 console.log('focused child', e.target.name);
 }
 if (!e.currentTarget.contains(e.relatedTarget)) {
 // Not triggered when swapping focus between children
 console.log('focus entered parent');
 }
 }}
 onBlur={(e) => {
 if (e.currentTarget === e.target) {
 console.log('unfocused parent');
 } else {
 console.log('unfocused child', e.target.name);
 }
 if (!e.currentTarget.contains(e.relatedTarget)) {
 // Not triggered when swapping focus between children
 console.log('focus left parent');
 }
 }}
 >

 First name:

 Last name:

 );
}
```

```css
label { display: block; }
input { margin-left: 10px; }
```

---

### Handling keyboard events {/*handling-keyboard-events*/}

This example shows some common [keyboard events](#keyboardevent-handler) and when they fire.

```js
export default function KeyboardExample() {
 return (

 First name:
 console.log('onKeyDown:', e.key, e.code)}
 onKeyUp={e => console.log('onKeyUp:', e.key, e.code)}
 />

 );
}
```

```css
label { display: block; }
input { margin-left: 10px; }
```

---

## Sitemap

[Overview of all docs pages](/llms.txt)
