} from 'react';
import {Video} from './Video';
import videos from './data';

function Item() {
  return (
    <ViewTransition
      enter={{
        'add-video-back': 'slide-in-back',
        'add-video-forward': 'slide-in-forward',
      }}
      exit={{
        'remove-video-back': 'slide-in-forward',
        'remove-video-forward': 'slide-in-back',
      }}>
      <Video video={videos[0]} />
    </ViewTransition>
  );
}

export default function Component() {
  const [showItem, setShowItem] = useState(false);
  return (
    <>
      <div className="button-container">
        <button
          onClick={() => {
            startTransition(() => {
              if (showItem) {
                addTransitionType('remove-video-back');
              } else {
                addTransitionType('add-video-back');
              }
              setShowItem((prev) => !prev);
            });
          }}>
          ⬅️
        </button>
        <button
          onClick={() => {
            startTransition(() => {
              if (showItem) {
                addTransitionType('remove-video-forward');
              } else {
                addTransitionType('add-video-forward');
              }
              setShowItem((prev) => !prev);
            });
          }}>
          ➡️
        </button>
      </div>
      {showItem ? <Item /> : null}
    </>
  );
}
```

```js src/data.js hidden
export default [
  {
    id: '1',
    title: 'First video',
    description: 'Video description',
    image: 'blue',
  },
];
```

```css
::view-transition-old(.slide-in-back) {
  animation-name: slideOutRight;
  animation-duration: 500ms;
  animation-timing-function: ease-in-out;
}

::view-transition-new(.slide-in-back) {
  animation-name: slideInRight;
  animation-duration: 500ms;
  animation-timing-function: ease-in-out;
}

::view-transition-old(.slide-out-back) {
  animation-name: slideOutLeft;
  animation-duration: 500ms;
  animation-timing-function: ease-in-out;
}

::view-transition-new(.slide-out-back) {
  animation-name: slideInLeft;
  animation-duration: 500ms;
  animation-timing-function: ease-in-out;
}

::view-transition-old(.slide-in-forward) {
  animation-name: slideOutLeft;
  animation-duration: 500ms;
  animation-timing-function: ease-in-out;
}

::view-transition-new(.slide-in-forward) {
  animation-name: slideInLeft;
  animation-duration: 500ms;
  animation-timing-function: ease-in-out;
}

::view-transition-old(.slide-out-forward) {
  animation-name: slideOutRight;
  animation-duration: 500ms;
  animation-timing-function: ease-in-out;
}

::view-transition-new(.slide-out-forward) {
  animation-name: slideInRight;
  animation-duration: 500ms;
  animation-timing-function: ease-in-out;
}

@keyframes slideOutLeft {
  from {
    transform: translateX(0);
    opacity: 1;
  }
  to {
    transform: translateX(-100%);
    opacity: 0;
  }
}

@keyframes slideInLeft {
  from {
    transform: translateX(-100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

@keyframes slideOutRight {
  from {
    transform: translateX(0);
    opacity: 1;
  }
  to {
    transform: translateX(100%);
    opacity: 0;
  }
}

@keyframes slideInRight {
  from {
    transform: translateX(100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

@keyframes slideInRight {
  from {
    transform: translateX(100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

#root {
  display: flex;
  flex-direction: column;
  align-items: center;
  min-height: 200px;
}
button {
  border: none;
  border-radius: 50%;
  width: 50px;
  height: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f0f8ff;
  color: white;
  font-size: 20px;
  cursor: pointer;
  transition: background-color 0.3s, border 0.3s;
}
button:hover {
  border: 2px solid #ccc;
  background-color: #e0e8ff;
}
.button-container {
  display: flex;
}
.thumbnail {
  position: relative;
  aspect-ratio: 16 / 9;
  display: flex;
  overflow: hidden;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border-radius: 0.5rem;
  outline-offset: 2px;
  width: 8rem;
  vertical-align: middle;
  background-color: #ffffff;
  background-size: cover;
  user-select: none;
}
.thumbnail.blue {
  background-image: conic-gradient(at top right, #c76a15, #087ea4, #2b3491);
}
.video {
  display: flex;
  flex-direction: row;
  gap: 0.75rem;
  align-items: center;
  margin-top: 1em;
}
.video .link {
  display: flex;
  flex-direction: row;
  flex: 1 1 0;
  gap: 0.125rem;
  outline-offset: 4px;
  cursor: pointer;
}
.video .info {
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-left: 8px;
  gap: 0.125rem;
}
.video .info:hover {
  text-decoration: underline;
}
.video-title {
  font-size: 15px;
  line-height: 1.25;
  font-weight: 700;
  color: #23272f;
}
.video-description {
  color: #5e687e;
  font-size: 13px;
}
```

```json package.json hidden
{
  "dependencies": {
    "react": "canary",
    "react-dom": "canary",
    "react-scripts": "latest"
  }
}
```

</Sandpack>

---

### Animating with JavaScript {/*animating-with-javascript*/}

While [View Transition Classes](#view-transition-class) let you define animations with CSS, sometimes you need imperative control over the animation. The `onEnter`, `onExit`, `onUpdate`, and `onShare` callbacks give you direct access to the view transition pseudo-elements so you can animate them using the [Web Animations API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API).

Each callback receives an `instance` with `.old` and `.new` properties representing the view transition pseudo-elements. You can call `.animate()` on them just like you would on a DOM element:

```js
<ViewTransition
  onEnter={(instance) => {
    const anim = instance.new.animate(
      [
        {transform: 'scale(0.8)'},
        {transform: 'scale(1)'},
      ],
      {duration: 300, easing: 'ease-out'}
    );
    return () => anim.cancel();
  }}>
  <div>...</div>
</ViewTransition>
```

This allows you to combine CSS-driven animations and JavaScript-driven animations.

In the following example, the default cross-fade is handled by CSS, and the slide animations are driven by JavaScript in the `onEnter` and `onExit` animations:

<Sandpack>

```js src/Video.js hidden
function Thumbnail({video, children}) {
  return (
    <div
      aria-hidden="true"
      tabIndex={-1}
      className={`thumbnail ${video.image}`}
    />
  );
}

export function Video({video}) {
  return (
    <div className="video">
      <div className="link">
        <Thumbnail video={video}></Thumbnail>

        <div className="info">
          <div className="video-title">{video.title}</div>
          <div className="video-description">{video.description}</div>
        </div>
      </div>
    </div>
  );
}
```

```js
import {ViewTransition, useState, startTransition} from 'react';
import {Video} from './Video';
import videos from './data';
import {SLIDE_IN, SLIDE_OUT} from './animations';

function Item() {
  return (
    <ViewTransition
      default="none"
      /* CSS driven cross fade defaults */
      enter="auto"
      exit="auto"
      /* JS driven slide animations */
      onEnter={(instance) => {
        const anim = instance.new.animate(
          SLIDE_IN,
          {duration: 500, easing: 'ease-out'}
        );
        return () => anim.cancel();
      }}
      onExit={(instance) => {
        const anim = instance.old.animate(
          SLIDE_OUT,
          {duration: 300, easing: 'ease-in'}
        );
        return () => anim.cancel();
      }}>
      <Video video={videos[0]} />
    </ViewTransition>
  );
}

export default function Component() {
  const [showItem, setShowItem] = useState(false);
  return (
    <>
      <button
        onClick={() => {
          startTransition(() => {
            setShowItem((prev) => !prev);
          });
        }}>
        {showItem ? '➖' : '➕'}
      </button>

      {showItem ? <Item /> : null}
    </>
  );
}
```

```js src/animations.js
export const SLIDE_IN = [
  {transform: 'translateY(20px)'},
  {transform: 'translateY(0)'},
];

export const SLIDE_OUT = [
  {transform: 'translateY(0)'},
  {transform: 'translateY(-20px)'},
];
```

```js src/data.js hidden
export default [
  {
    id: '1',
    title: 'First video',
    description: 'Video description',
    image: 'blue',
  },
];
```

```css
#root {
  display: flex;
  flex-direction: column;
  align-items: center;
  min-height: 200px;
}
button {
  border: none;
  border-radius: 50%;
  width: 50px;
  height: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f0f8ff;
  color: white;
  font-size: 20px;
  cursor: pointer;
  transition: background-color 0.3s, border 0.3s;
}
button:hover {
  border: 2px solid #ccc;
  background-color: #e0e8ff;
}
.thumbnail {
  position: relative;
  aspect-ratio: 16 / 9;
  display: flex;
  overflow: hidden;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border-radius: 0.5rem;
  outline-offset: 2px;
  width: 8rem;
  vertical-align: middle;
  background-color: #ffffff;
  background-size: cover;
  user-select: none;
}
.thumbnail.blue {
  background-image: conic-gradient(at top right, #c76a15, #087ea4, #2b3491);
}
.video {
  display: flex;
  flex-direction: row;
  gap: 0.75rem;
  align-items: center;
  margin-top: 1em;
}
.video .link {
  display: flex;
  flex-direction: row;
  flex: 1 1 0;
  gap: 0.125rem;
  outline-offset: 4px;
  cursor: pointer;
}
.video .info {
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-left: 8px;
  gap: 0.125rem;
}
.video .info:hover {
  text-decoration: underline;
}
.video-title {
  font-size: 15px;
  line-height: 1.25;
  font-weight: 700;
  color: #23272f;
}
.video-description {
  color: #5e687e;
  font-size: 13px;
}

```

```json package.json hidden
{
  "dependencies": {
    "react": "canary",
    "react-dom": "canary",
    "react-scripts": "latest"
  }
}
```

</Sandpack>

<Note>

#### Always clean up View Transition Events {/*always-clean-up-view-transition-events*/}

View Transition Events should always return a cleanup function:

```js {7}
<ViewTransition
  onEnter={(instance) => {
    const anim = instance.new.animate(
      SLIDE_IN,
      {duration: 500, easing: 'ease-out'}
    );
    return () => anim.cancel();
  }}
>
```

This allows the browser to cancel the animation when the View Transition is interrupted.

</Note>

---

### Animating transition types with JavaScript {/*animating-transition-types-with-javascript*/}

You can use `types` passed to `ViewTransition` events to conditionally apply different animations based on how the Transition was triggered.

```js {3}
 <ViewTransition
  onEnter={(instance, types) => {
    const duration = types.includes('fast') ? 150 : 2000;
    const anim = instance.new.animate(
      SLIDE_IN,
      {duration: duration, easing: 'ease-out'}
    );
    return () => anim.cancel();
  }}
>
```

This example calls [`addTransitionType`](/reference/react/addTransitionType) to mark a Transition as "fast" and then adjust the animation duration:

<Sandpack>

```js src/Video.js hidden
function Thumbnail({video, children}) {
  return (
    <div
      aria-hidden="true"
      tabIndex={-1}
      className={`thumbnail ${video.image}`}
    />
  );
}

export function Video({video}) {
  return (
    <div className="video">
      <div className="link">
        <Thumbnail video={video}></Thumbnail>

        <div className="info">
          <div className="video-title">{video.title}</div>
          <div className="video-description">{video.description}</div>
        </div>
      </div>
    </div>
  );
}
```

```js
import {ViewTransition, useState, startTransition, addTransitionType} from 'react';
import {Video} from './Video';
import videos from './data';
import {SLIDE_IN, SLIDE_OUT} from './animations';

function Item() {
  return (
    <ViewTransition
      onEnter={(instance, types) => {
        const duration = types.includes('fast') ? 150 : 2000;
        const anim = instance.new.animate(
          SLIDE_IN,
          {duration: duration, easing: 'ease-out'}
        );
        return () => anim.cancel();
      }}
      onExit={(instance, types) => {
        const duration = types.includes('fast') ? 150 : 500;
        const anim = instance.old.animate(
          SLIDE_OUT,
          {duration: duration, easing: 'ease-in'}
        );
        return () => anim.cancel();
      }}>
      <Video video={videos[0]} />
    </ViewTransition>
  );
}

export default function Component() {
  const [showItem, setShowItem] = useState(false);
  const [isFast, setIsFast] = useState(false);
  return (
    <>
      <div>
        Fast: <input type="checkbox" onChange={() => {setIsFast(f => !f)}} value={isFast}></input>
      </div><br />
      <button
        onClick={() => {
          startTransition(() => {
            if (isFast) {
              addTransitionType('fast');
            }
            setShowItem((prev) => !prev);
          });
        }}>
        {showItem ? '➖' : '➕'}
      </button>

      {showItem ? <Item /> : null}
    </>
  );
}
```

```js src/animations.js
export const SLIDE_IN = [
  {opacity: 0, transform: 'translateY(20px)'},
  {opacity: 1, transform: 'translateY(0)'},
];

export const SLIDE_OUT = [
  {opacity: 1, transform: 'translateY(0)'},
  {opacity: 0, transform: 'translateY(-20px)'},
];
```

```js src/data.js hidden
export default [
  {
    id: '1',
    title: 'First video',
    description: 'Video description',
    image: 'blue',
  },
];
```

```css
#root {
  display: flex;
  flex-direction: column;
  align-items: center;
  min-height: 200px;
}
button {
  border: none;
  border-radius: 50%;
  width: 50px;
  height: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f0f8ff;
  color: white;
  font-size: 20px;
  cursor: pointer;
  transition: background-color 0.3s, border 0.3s;
}
button:hover {
  border: 2px solid #ccc;
  background-color: #e0e8ff;
}
.thumbnail {
  position: relative;
  aspect-ratio: 16 / 9;
  display: flex;
  overflow: hidden;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border-radius: 0.5rem;
  outline-offset: 2px;
  width: 8rem;
  vertical-align: middle;
  background-color: #ffffff;
  background-size: cover;
  user-select: none;
}
.thumbnail.blue {
  background-image: conic-gradient(at top right, #c76a15, #087ea4, #2b3491);
}
.video {
  display: flex;
  flex-direction: row;
  gap: 0.75rem;
  align-items: center;
  margin-top: 1em;
}
.video .link {
  display: flex;
  flex-direction: row;
  flex: 1 1 0;
  gap: 0.125rem;
  outline-offset: 4px;
  cursor: pointer;
}
.video .info {
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-left: 8px;
  gap: 0.125rem;
}
.video .info:hover {
  text-decoration: underline;
}
.video-title {
  font-size: 15px;
  line-height: 1.25;
  font-weight: 700;
  color: #23272f;
}
.video-description {
  color: #5e687e;
  font-size: 13px;
}

```

```json package.json hidden
{
  "dependencies": {
    "react": "canary",
    "react-dom": "canary",
    "react-scripts": "latest"
  }
}
```

</Sandpack>

---

### Building View Transition enabled routers {/*building-view-transition-enabled-routers*/}

React waits for any pending Navigation to finish to ensure that scroll restoration happens within the animation. If the Navigation is blocked on React, your router must unblock in `useLayoutEffect` since `useEffect` would lead to a deadlock.

If a `startTransition` is started from the legacy popstate event, such as during a "back"-navigation then it must finish synchronously to ensure scroll and form restoration works correctly. This is in conflict with running a View Transition animation. Therefore, React will skip animations from popstate and animations won't run for the back button. You can fix this by upgrading your router to use the Navigation API.

---

## Troubleshooting {/*troubleshooting*/}

### My `<ViewTransition>` is not activating {/*my-viewtransition-is-not-activating*/}

`<ViewTransition>` only activates if it is placed before any DOM node:

```js [3, 5]
function Component() {
  return (
    <div>
      <ViewTransition>Hi</ViewTransition>
    </div>
  );
}
```

To fix, ensure that the `<ViewTransition>` comes before any other DOM nodes:

```js [3, 5]
function Component() {
  return (
    <ViewTransition>
      <div>Hi</div>
    </ViewTransition>
  );
}
```

### I'm getting an error "There are two `<ViewTransition name=%s>` components with the same name mounted at the same time." {/*two-viewtransition-with-same-name*/}

This error occurs when two `<ViewTransition>` components with the same `name` are mounted at the same time:

```js [3]
function Item() {
  // 🚩 All items will get the same "name".
  return <ViewTransition name="item">...</ViewTransition>;
}

function ItemList({items}) {
  return (
    <>
      {items.map((item) => (
        <Item key={item.id} />
      ))}
    </>
  );
}
```

This will cause the View Transition to error. In development, React detects this issue to surface it and logs two errors:

<ConsoleBlockMulti>
<ConsoleLogLine level="error">

There are two `<ViewTransition name=%s>` components with the same name mounted at the same time. This is not supported and will cause View Transitions to error. Try to use a more unique name e.g. by using a namespace prefix and adding the id of an item to the name.
{' '}at Item
{' '}at ItemList

</ConsoleLogLine>

<ConsoleLogLine level="error">

The existing `<ViewTransition name=%s>` duplicate has this stack trace.
{' '}at Item
{' '}at ItemList

</ConsoleLogLine>
</ConsoleBlockMulti>

To fix, ensure that there's only one `<ViewTransition>` with the same name mounted at a time in the entire app by ensuring the `name` is unique, or adding an `id` to the name:

```js [3]
function Item({id}) {
  // ✅ All items will get a unique name.
  return <ViewTransition name={`item-${id}`}>...</ViewTransition>;
}

function ItemList({items}) {
  return (
    <>
      {items.map((item) => (
        <Item key={item.id} item={item} />
      ))}
    </>
  );
}
```

---

## Sitemap

[Overview of all docs pages](/llms.txt)
